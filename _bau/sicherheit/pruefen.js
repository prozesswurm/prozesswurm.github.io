// Sicherheitstests der Lernwerkstatt. Aufruf: node _bau/sicherheit/pruefen.js [Basis-URL]
// Standard: http://localhost:8800/ (vorher im Hauptordner: python3 -m http.server 8800)
// Braucht Playwright (npm i playwright). Ergebnis: Tabelle, Exit-Code 1 bei einem Fehlschlag.
const { chromium } = require('playwright');
const fs = require('fs');
const B = process.argv[2] || 'http://localhost:8800/';
const EXE = process.env.CHROMIUM || (fs.existsSync('/opt/pw-browsers/chromium') ? '/opt/pw-browsers/chromium' : undefined);
const PAY = '"><img src=x onerror="window.__x=(window.__x||0)+1"><svg onload="window.__x=(window.__x||0)+1">';
const b64 = o => Buffer.from(JSON.stringify(o)).toString('base64').replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
const KEY = 'wurmLernwerkstatt.v2';
(async () => {
  const br = await chromium.launch(EXE ? { executablePath: EXE } : {});
  const rows = [];
  async function t(name, url, { ls, after, expect = 'sicher' } = {}) {
    const ctx = await br.newContext(); const p = await ctx.newPage(); p.setDefaultTimeout(5000);
    const errs = [], csp = []; let dialog = false;
    p.on('dialog', d => { dialog = true; d.dismiss(); });
    p.on('pageerror', e => errs.push(e.message));
    await p.addInitScript(() => document.addEventListener('securitypolicyviolation', e => { (window.__csp = window.__csp || []).push(e.violatedDirective + ' ' + e.blockedURI); }));
    if (ls) await p.addInitScript(([k, v]) => { try { localStorage.setItem(k, v); } catch (e) {} }, [KEY, ls]);
    await p.goto(B + url, { waitUntil: 'load' }).catch(e => errs.push('Laden: ' + e.message));
    await p.waitForTimeout(800);
    let extra = '';
    if (after) extra = await after(p).catch(e => 'Fehler: ' + e.message) || '';
    await p.waitForTimeout(300);
    const r = await p.evaluate(() => ({ x: window.__x || 0, csp: window.__csp || [], proto: ({}).polluted || null }));
    const bad = r.x > 0 || dialog || r.proto || errs.length || r.csp.length;
    rows.push({ Test: name, Ergebnis: bad || /^FEHLER/.test(extra) ? 'FEHLER' : (expect === 'sicher' ? 'ok' : extra || 'ok'),
      Details: [r.x || dialog ? 'Skript eingeschleust' : '', r.proto ? 'Prototyp verändert' : '', ...errs.slice(0, 2), ...r.csp.slice(0, 2), expect !== 'sicher' ? extra : ''].filter(Boolean).join(' | ') });
    await ctx.close();
  }
  const pages = ['index.html', 'mediathek.html', 'urkunde.html?n=Test&k=A1&d=2026-01-01&c=PW-A1-ABC', 'hilfe.html', 'lektionen.html', 'lektion/b01.html', 'lektion/i11.html'];
  for (const u of pages) await t('Seite lädt ohne Fehler: ' + u.split('?')[0], u);
  // Alle Ansichten der App einmal öffnen (findet Regelverstöße, die erst später auftreten)
  await t('App: alle Ansichten öffnen', 'index.html', { after: async p => {
    for (const sel of ['[data-view]', 'nav a', 'nav button', '[data-badge]']) { for (const el of await p.$$(sel)) { await el.click({ timeout: 800 }).catch(() => {}); await p.waitForTimeout(80); } }
    await p.goto(B + 'index.html#lektion=i11'); await p.waitForTimeout(400); await p.getByText("Los geht's").first().click().catch(() => {});
    await p.goto(B + 'index.html#mediathek'); await p.waitForTimeout(300);
    const play = await p.$('[data-k], .embed, [data-play]'); if (play) await play.click().catch(() => {}); await p.waitForTimeout(500);
  } });
  await t('CSP blockt fremdes Skript (Gegenprobe)', 'index.html', { expect: 'info', after: async p => {
    const v = await p.evaluate(() => new Promise(res => { document.addEventListener('securitypolicyviolation', e => res('blockiert: ' + e.violatedDirective), { once: true }); const s = document.createElement('script'); s.src = 'https://boese.example/x.js'; document.head.appendChild(s); setTimeout(() => res('NICHT blockiert'), 1500); }));
    await p.evaluate(() => { window.__csp = (window.__csp || []).filter(x => !/boese\.example/.test(x)); }); return v; } });
  await t('Mediathek: Lied und Video lassen sich einbetten', 'mediathek.html', { expect: 'info', after: async p => {
    const els = await p.$$('.play'); for (const el of [els[0], els[els.length - 1]].filter(Boolean)) { await el.click().catch(() => {}); }
    await p.waitForTimeout(600); const src = await p.$$eval('iframe', f => f.map(x => new URL(x.src).host)); return 'eingebettet: ' + (src.join(', ') || 'nichts'); } });
  await t('App: Lied und Video lassen sich einbetten', 'index.html#mediathek', { expect: 'info', after: async p => {
    await p.$$eval('details', d => d.forEach(x => x.open = true)); const els = await p.$$('[data-play]');
    for (const el of [els[0], els[els.length - 1]].filter(Boolean)) { await el.click().catch(() => {}); }
    await p.waitForTimeout(600); const src = await p.$$eval('iframe', f => f.map(x => new URL(x.src).host)); return 'eingebettet: ' + ([...new Set(src)].join(', ') || 'nichts'); } });
  // Angriffe über Links
  await t('Urkunde: Schadcode im Namen/Code', 'urkunde.html?n=' + encodeURIComponent(PAY) + '&c=' + encodeURIComponent(PAY) + '&k=' + encodeURIComponent(PAY) + '&d=' + encodeURIComponent(PAY));
  for (const h of ['lektion', 'problem', 'hilfe']) await t(`Link #${h}= mit Schadcode`, `index.html#${h}=` + encodeURIComponent(PAY));
  await t('Team-Link mit Schadcode im Namen', 'index.html#team=b01.b02&name=' + encodeURIComponent(PAY));
  await t('Speicherlink mit Schadcode (Name, Ziel)', 'index.html#p=' + b64({ v: 1, d: { b: 'f' }, k: [], b: {}, n: PAY, g: PAY }), { after: async p => { for (const el of await p.$$('nav a, nav button')) { await el.click({ timeout: 800 }).catch(() => {}); } } });
  await t('Speicherlink mit __proto__', 'index.html#p=' + b64({ v: 1, d: {}, k: [], b: JSON.parse('{"__proto__":{"polluted":"ja"}}') }));
  await t('Speicherlink kaputt', 'index.html#p=%%%%');
  // Manipulierter Browserspeicher
  await t('Browserspeicher mit Schadcode', 'index.html', { ls: JSON.stringify({ done: ['b01'], known: [], notes: { b01: PAY }, badges: { A1: '2026-01-01' }, name: PAY, goal: PAY, team: { n: PAY, ids: ['b01'] } }), after: async p => { for (const el of await p.$$('nav a, nav button, [data-badge]')) { await el.click({ timeout: 800 }).catch(() => {}); } } });
  await t('Browserspeicher kaputt (falsche Typen)', 'index.html', { ls: '{"done":"kaputt","badges":5,"notes":null,"weeks":"x","team":7}' });
  await t('Browserspeicher kein JSON', 'index.html', { ls: 'kein json{' });
  // Urkunde fälschen (zeigt den Ist-Stand, kein Sicherheitsfehler)
  const d = {}; ['b', 'c', 'e', 'g', 'i', 'k', 'l', 'p', 's', 'v'].forEach(x => d[x] = 'ffffff');
  await t('Fälschung: Speicherlink mit allem erledigt + Prüfung + GESAMT', 'index.html#p=' + b64({ v: 1, d, k: [], b: { PRUEFUNG: '260101', GESAMT: '260101' }, n: 'Test' }), { expect: 'info', after: async p => {
    const s = await p.evaluate(k => { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }, KEY);
    return (s && s.exam && s.exam.passed) ? 'FEHLER: Meister-Prüfung per Link übernommen' : `${(s && s.done || []).length} Lektionen übernommen, Meister-Prüfung nicht übernommen`; } });
  // Feedback-Schutz
  await t('Feedback: Fangfeld blockt Spam-Programm', 'index.html', { expect: 'info', after: async p => {
    let sent = false; await p.route('https://docs.google.com/**', r => { sent = true; r.abort(); });
    await p.evaluate(() => { const b = document.querySelector('[data-feedback]'); if (b) b.click(); });
    await p.waitForTimeout(3200); await p.fill('#fbText', 'Spam'); await p.evaluate(() => { const w = document.querySelector('#fbWeb'); if (w) w.value = 'http://spam'; });
    await p.click('#fbSend').catch(() => {}); await p.waitForTimeout(500); return sent ? 'FEHLER: Spam wurde gesendet' : 'Spam nicht gesendet'; } });
  await t('Feedback: echte Nachricht kommt durch', 'index.html', { expect: 'info', after: async p => {
    let sent = false; await p.route('https://docs.google.com/**', r => { sent = true; r.fulfill({ status: 200, body: '' }); });
    await p.evaluate(() => { const b = document.querySelector('[data-feedback]'); if (b) b.click(); });
    await p.waitForTimeout(3200); await p.fill('#fbText', 'Test'); await p.click('#fbSend').catch(() => {}); await p.waitForTimeout(800);
    return sent ? 'gesendet' : 'FEHLER: nicht gesendet'; } });
  await t('Urkunde erzeugen (Bild, LinkedIn-Knopf)', 'index.html', { expect: 'info', ls: JSON.stringify({ done: [], known: [], notes: {}, badges: { A1: '2026-10-01' }, name: 'Erika Muster' }), after: async p => {
    await p.evaluate(() => { const b = document.querySelector('[data-badge="A1"]'); if (b) b.click(); }); await p.waitForTimeout(900);
    const img = await p.$$eval('img', a => a.filter(x => x.src.startsWith('data:image/png')).length); return img ? 'Urkundenbild erzeugt' : 'FEHLER: kein Urkundenbild'; } });
  await t('Meister-Prüfung: keine Lösungen, neuer Versuch erst morgen', 'index.html', { expect: 'info', after: async p => {
    await p.evaluate(k => { const s = JSON.parse(localStorage.getItem(k) || '{}'); s.done = Object.keys(L); localStorage.setItem(k, JSON.stringify(s)); }, KEY);
    await p.reload(); await p.waitForTimeout(700); await p.evaluate(() => openExam()); await p.waitForTimeout(300);
    const next = () => p.locator('#v-lesson button:visible').filter({ hasText: /^(Prüfung starten|Weiter|Auswertung)$/ }).first().click({ timeout: 1500 }).catch(() => {});
    await next();
    for (let i = 0; i < 15; i++) { await p.locator('#v-lesson section.lc:not([hidden]) .opt[data-o="2"]').first().click({ timeout: 1500 }).catch(() => {}); await next(); await p.waitForTimeout(60); }
    await p.waitForTimeout(400);
    const txt = await p.evaluate(() => (document.querySelector('#examResult') || {}).innerText || '');
    const st = await p.evaluate(k => JSON.parse(localStorage.getItem(k)).exam, KEY);
    if (st && st.passed) return 'Test nicht aussagekräftig (zufällig bestanden)';
    if (/Richtig:/.test(txt)) return 'FEHLER: Lösungen werden gezeigt';
    await p.evaluate(() => openExam()); await p.waitForTimeout(300);
    const toast = await p.evaluate(() => document.body.innerText.includes('Neuer Versuch ab morgen'));
    return toast && st && st.lastFail ? 'keine Lösungen gezeigt, zweiter Versuch heute gesperrt' : 'FEHLER: zweiter Versuch nicht gesperrt'; } });
  await t('Urkunde: erst nach Ehrenwort herunterladen', 'index.html', { expect: 'info', ls: JSON.stringify({ done: [], known: [], notes: {}, badges: { A1: '2026-10-01' }, name: 'Erika Muster' }), after: async p => {
    await p.evaluate(() => { const b = document.querySelector('[data-badge="A1"]'); if (b) b.click(); }); await p.waitForTimeout(800);
    let dl = false; p.on('download', () => { dl = true; });
    await p.click('#certDl').catch(() => {}); await p.waitForTimeout(500); const ohne = dl;
    await p.check('#certHonor'); await p.click('#certDl').catch(() => {}); await p.waitForTimeout(800);
    return ohne ? 'FEHLER: Download ohne Bestätigung' : (dl ? 'ohne Bestätigung gesperrt, mit Bestätigung geladen' : 'gesperrt; Download mit Bestätigung nicht erkannt'); } });
  await br.close();
  // Prüfungen am Quelltext
  const root = process.env.SITE_ROOT || '.';
  const htmls = []; (function walk(dir) { for (const f of fs.readdirSync(dir, { withFileTypes: true })) { if (f.name === '.git' || f.name === 'node_modules') continue; const p = dir + '/' + f.name; if (f.isDirectory()) walk(p); else if (p.endsWith('.html')) htmls.push(p); } })(root);
  const noSri = htmls.filter(f => /gc\.zgo\.at\/count/.test(fs.readFileSync(f, 'utf8')) && !/integrity="sha384-/.test(fs.readFileSync(f, 'utf8')));
  rows.push({ Test: 'Zähl-Skript überall mit Prüfsumme', Ergebnis: noSri.length ? 'FEHLER' : 'ok', Details: noSri.slice(0, 3).join(', ') });
  const appPages = htmls.filter(f => /^\.?\/?(index|mediathek|urkunde|hilfe|lektionen)\.html$/.test(f.replace(root + '/', '')) || /\/lektion\//.test(f));
  const noCsp = appPages.filter(f => !/Content-Security-Policy/.test(fs.readFileSync(f, 'utf8')));
  rows.push({ Test: 'Sicherheitsregeln (CSP) auf allen App-Seiten', Ergebnis: noCsp.length ? 'FEHLER' : 'ok', Details: noCsp.slice(0, 3).join(', ') });
  const blank = htmls.filter(f => !/\/newsletter\//.test(f)).flatMap(f => (fs.readFileSync(f, 'utf8').match(/<a [^>]*target="_blank"[^>]*>/g) || []).filter(a => !/noopener/.test(a)).map(() => f));
  rows.push({ Test: 'Links nach außen mit noopener', Ergebnis: blank.length ? 'FEHLER' : 'ok', Details: [...new Set(blank)].slice(0, 3).join(', ') });
  const secret = /(ghp_[0-9A-Za-z]{30,}|github_pat_[0-9A-Za-z_]{30,}|AIza[0-9A-Za-z_-]{30,}|xkeysib-[0-9a-f]{20,}|sk-[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY)/;
  const leaks = htmls.filter(f => secret.test(fs.readFileSync(f, 'utf8')));
  rows.push({ Test: 'Keine Zugangsschlüssel in Seiten', Ergebnis: leaks.length ? 'FEHLER' : 'ok', Details: leaks.join(', ') });
  console.table(rows);
  fs.writeFileSync(process.env.OUT || 'sicherheit-ergebnis.json', JSON.stringify(rows, null, 1));
  process.exit(rows.some(r => r.Ergebnis.startsWith('FEHLER')) ? 1 : 0);
})();
