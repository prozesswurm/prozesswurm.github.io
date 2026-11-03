// Angriffstests (Penetrationstest) für Website und Lernwerkstatt – nur gegen die lokale Kopie.
// Aufruf im Hauptordner:  python3 -m http.server 8765  (im Hintergrund), dann  node _bau/sicherheit/angriff.js
// Braucht Playwright (npm i playwright). Ergebnis: Tabelle, Exit-Code 1 bei einem Befund.
// "Hinweis" = bekannte Grenze von GitHub Pages, kein Fehler.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), http = require('http'), os = require('os');
const B = (process.argv[2] || 'http://localhost:8765/').replace(/\/?$/, '/');
const ROOT = process.env.SITE_ROOT || '.';
const EXE = process.env.CHROMIUM && fs.existsSync(process.env.CHROMIUM) ? process.env.CHROMIUM : undefined;
const KEY = 'wurmLernwerkstatt.v2';

// Schadtexte: jeder setzt window.__x, wenn er ausgeführt wird
const PAYLOADS = [
  '"><img src=x onerror="window.__x=1">',
  '<svg onload="window.__x=1">',
  'javascript:window.__x=1',
  "'-(window.__x=1)-'",
  '{{constructor.constructor("window.__x=1")()}}',
  '%3Cimg%20src%3Dx%20onerror%3D%22window.__x%3D1%22%3E',
  '%253Cimg%2520src%253Dx%2520onerror%253Dwindow.__x%253D1%253E',
  '‮evil‬<img src=x onerror=window.__x=1>',
  'A'.repeat(10000),
];
const enc = s => encodeURIComponent(s);

(async () => {
  const br = await chromium.launch(EXE ? { executablePath: EXE } : {});
  const rows = [];
  const add = (Test, Ergebnis, Details = '') => (console.log(Ergebnis.padEnd(8), Test), rows.push({ Test, Ergebnis, Details: String(Details).slice(0, 220) }));

  async function open(url, { ls, after } = {}) {
    const ctx = await br.newContext(); const p = await ctx.newPage(); p.setDefaultTimeout(4000);
    const errs = []; let dialog = false;
    p.on('dialog', d => { dialog = true; d.dismiss().catch(() => {}); });
    p.on('pageerror', e => errs.push(e.message));
    // Fremde Dienste nicht anfragen (Zähler, Google): Anfragen merken und abbrechen
    const outbound = [];
    await ctx.route(u => !u.href.startsWith(B.replace(/\/$/, '')) && !/^(data|blob|about):/.test(u.href), r => { outbound.push(r.request().url() + ' ' + (r.request().postData() || '')); r.abort(); });
    await p.addInitScript(() => document.addEventListener('securitypolicyviolation', e => {
      if (!/gc\.zgo\.at|goatcounter/.test(e.blockedURI)) (window.__csp = window.__csp || []).push(e.violatedDirective + ' ' + e.blockedURI); }));
    if (ls) await p.addInitScript(([k, v]) => { try { localStorage.setItem(k, v); sessionStorage.setItem(k, v); } catch (e) {} }, [KEY, ls]);
    await p.goto(B + url, { waitUntil: 'load' }).catch(e => errs.push('Laden: ' + e.message.split('\n')[0]));
    await p.waitForTimeout(250);
    let extra = '';
    if (after) extra = await after(p).catch(e => 'Fehler: ' + e.message.split('\n')[0]) || '';
    await p.waitForTimeout(100);
    const r = await p.evaluate(() => ({ x: window.__x || 0, csp: window.__csp || [], proto: ({}).polluted || null, href: location.href })).catch(() => ({ x: 0, csp: [], href: p.url() }));
    await ctx.close();
    return { ...r, dialog, errs, extra, outbound };
  }
  const bad = r => r.x || r.dialog || r.proto || r.errs.length || r.csp.length;
  const why = r => [r.x || r.dialog ? 'Skript eingeschleust' : '', r.proto ? 'Prototyp verändert' : '', ...r.errs.slice(0, 1), ...r.csp.slice(0, 1)].filter(Boolean).join(' | ');

  // ---------- a) Schadcode über Adresse (?- und #-Teil) auf allen Website-Seiten ----------
  const sitePages = [];
  (function walk(d) { for (const f of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, f.name), rel = path.relative(ROOT, p);
    if (f.isDirectory()) { if (!/^(\.|_|node_modules$|lernwerkstatt$|newsletter$)/.test(rel)) walk(p); }
    else if (f.name === 'index.html' || (d === ROOT && f.name === '404.html')) {
      const s = fs.readFileSync(p, 'utf8'); if (!/http-equiv="refresh"/.test(s)) sitePages.push(rel.replace(/index\.html$/, ''));
    } } })(ROOT);
  for (const pg of sitePages) {
    let fail = null;
    for (const pl of [PAYLOADS[0], PAYLOADS[1], PAYLOADS[3], PAYLOADS[5]]) {
      const r = await open(`${pg}?q=${enc(pl)}&n=${enc(pl)}#${enc(pl)}`);
      if (bad(r)) { fail = why(r) + ' mit ' + pl.slice(0, 30); break; }
    }
    add('Website: Schadcode in Adresse – /' + pg, fail ? 'FEHLER' : 'ok', fail || '');
  }

  // Website-Suche mit Schadtexten
  { let fail = null;
    for (const pl of PAYLOADS) {
      const r = await open('', { after: async p => {
        await p.click('[data-search-open]'); await p.fill('#suchfeld', pl); await p.waitForTimeout(150);
        await p.fill('#suchfeld', 'prozess ' + pl.slice(0, 50)); await p.waitForTimeout(150); } });
      if (bad(r) || /^Fehler/.test(r.extra)) { fail = why(r) || r.extra; break; }
    }
    add('Website: Suche mit Schadtexten', fail ? 'FEHLER' : 'ok', fail || ''); }

  // ---------- a) Lernwerkstatt: weitere Eingabestellen ----------
  const L = 'lernwerkstatt/';
  const appCases = [
    ['App: #lektion= kodiert/doppelt kodiert', PAYLOADS.slice(5, 7).map(pl => L + 'index.html#lektion=' + pl)],
    ['App: #problem= mit Schadtext', PAYLOADS.slice(0, 5).map(pl => L + 'index.html#problem=' + enc(pl))],
    ['App: #team= mit Schadtext im Namen', PAYLOADS.map(pl => L + 'index.html#team=b01.b02&name=' + enc(pl))],
    ['App: #hilfe= mit Schadtext', PAYLOADS.slice(0, 5).map(pl => L + 'index.html#hilfe=' + enc(pl))],
    ['App: #p= Speicherlink mit Müll', ['#p=' + enc(PAYLOADS[0]), '#p=' + 'A'.repeat(10000), '#p=e30', '#p=bnVsbA'].map(h => L + 'index.html' + h)],
    ['Urkunde: Schadtext, 10.000 Zeichen, Schreibrichtung', PAYLOADS.map(pl => L + `urkunde.html?n=${enc(pl)}&k=${enc(pl)}&d=${enc(pl)}&c=${enc(pl)}`)],
    ['Mediathek: Schadtext in Adresse', PAYLOADS.slice(0, 5).map(pl => L + `mediathek.html?q=${enc(pl)}#${enc(pl)}`)],
  ];
  for (const [name, urls] of appCases) {
    let fail = null;
    for (const u of urls) { const r = await open(u); if (bad(r)) { fail = why(r) + ' bei ' + u.slice(0, 80); break; } }
    add(name, fail ? 'FEHLER' : 'ok', fail || '');
  }
  // Eingabefelder der App
  { let fail = null;
    for (const pl of PAYLOADS) {
      const r = await open(L + 'index.html', { after: async p => {
        for (const sel of ['#q', '#helpQ', '#tbName', '#certName', '#fbText', '#saveCode']) {
          await p.evaluate(([s, v]) => { const el = document.querySelector(s); if (!el) return;
            el.value = v; el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true }));
            el.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', bubbles: true })); }, [sel, pl]);
          await p.waitForTimeout(60);
        } } });
      if (bad(r)) { fail = why(r) + ' mit ' + pl.slice(0, 30); break; }
    }
    add('App: Eingabefelder (Suche, Hilfe, Teamname, Urkundenname, Feedback, Code)', fail ? 'FEHLER' : 'ok', fail || ''); }
  // Browserspeicher mit fremden Feldern und Schadtext
  { const evil = [
      JSON.stringify({ __proto__: { polluted: 1 }, constructor: { prototype: { polluted: 1 } }, name: PAYLOADS[0], done: { [PAYLOADS[1]]: 1 } }),
      '{"done":' + '['.repeat(5000) + ']'.repeat(5000) + '}', '{kaputt', 'null', '"' + PAYLOADS[0] + '"'];
    let fail = null;
    for (const v of evil) { const r = await open(L + 'index.html', { ls: v }); if (bad(r)) { fail = why(r) + ' bei ' + v.slice(0, 40); break; } }
    add('App: Browserspeicher mit __proto__, Schadtext, kaputtem JSON', fail ? 'FEHLER' : 'ok', fail || ''); }

  // Urkunde: Name darf nie nach außen gehen (Zähler, Herkunftsangabe)
  { const NAME = 'Erika Mustermann Geheim';
    const r = await open(L + `urkunde.html?n=${enc(NAME)}&k=A1&d=2026-01-01&c=PW-A1-ABC`, { after: async p => {
      const ref = await p.evaluate(() => { const m = document.querySelector('meta[name="referrer"]'); return m ? m.content : ''; });
      await p.evaluate(b => { const a = document.querySelector('a.cta'); if (a) a.href = b + 'lernwerkstatt/'; }, B);   // live: gleiche Herkunft
      await Promise.all([p.waitForNavigation({ timeout: 4000 }).catch(() => {}), p.click('a.cta')]);
      await p.waitForTimeout(400);
      const docRef = await p.evaluate(() => document.referrer);
      return `Regel: ${ref || 'keine'}; Herkunft auf Folgeseite: ${docRef || '(leer)'}`; } });
    const leak = r.outbound.filter(o => /Erika|Mustermann/.test(decodeURIComponent(o)));
    const refLeak = /Erika|Mustermann/.test(decodeURIComponent(r.extra));
    add('Urkunde: Name geht nicht an Zähler oder Folgeseite', leak.length || refLeak ? 'FEHLER' : 'ok', leak.length ? 'an ' + leak[0].slice(0, 80) : r.extra); }

  // ---------- b) Offene Weiterleitung ----------
  const EVIL = ['//boese.example', 'https://boese.example', '/\\boese.example', '\\\\boese.example', 'javascript:window.__x=1', 'data:text/html,x', '%2F%2Fboese.example'];
  const redirectPages = ['', 'urkunde.html', 'hilfe.html', 'lektionen.html', 'mediathek.html', 'lektion/b01.html', 'start/', 'angebote/', 'über-uns/', 'hören-und-sehen/'];
  { const fails = [];
    const ctx = await br.newContext(); let x = false;
    await ctx.route(u => !u.href.startsWith(B.replace(/\/$/, '')), r => { if (r.request().isNavigationRequest()) x = r.request().url(); r.abort(); });
    const p = await ctx.newPage(); p.setDefaultTimeout(3000);
    for (const pg of redirectPages) for (const ev of EVIL) for (const form of ['#' + ev, '?' + ev, '#lektion=' + ev]) {
      x = false;
      await p.goto(B + pg + form, { waitUntil: 'domcontentloaded' }).catch(() => {}); await p.waitForTimeout(250);
      const now = p.url(); const run = await p.evaluate(() => window.__x || 0).catch(() => 0);
      if (x || run || !now.startsWith(B.replace(/\/$/, ''))) fails.push(`/${pg}${form} -> ${x || now}`);
      await p.goto('about:blank').catch(() => {});
    }
    await ctx.close();
    add('Offene Weiterleitung (Weiche und alle Umzugsseiten)', fails.length ? 'FEHLER' : 'ok', fails.slice(0, 3).join(' ; ') || `${redirectPages.length * EVIL.length * 3} Versuche, alle bleiben auf prozesswurm.de`); }

  // ---------- d) Fremdes Einbetten ----------
  { const srv = http.createServer((q, s) => { s.setHeader('content-type', 'text/html');
      s.end(`<iframe id=f src="${B}" width=800 height=600></iframe><iframe id=g src="${B}lernwerkstatt/" width=800 height=600></iframe>`); }).listen(0);
    const port = srv.address().port; const ctx = await br.newContext(); const p = await ctx.newPage();
    await ctx.route(u => /gc\.zgo\.at|goatcounter|google/.test(u.href), r => r.abort());
    await p.goto(`http://127.0.0.1:${port}/`); await p.waitForTimeout(1500);
    const frames = p.frames().filter(f => f !== p.mainFrame());
    const loaded = []; for (const f of frames) { const t = await f.title().catch(() => ''); if (t) loaded.push(t); }
    const top = p.url().includes(String(port));
    await ctx.close(); srv.close();
    add('Fremdes Einbetten in fremde Seite', 'Hinweis', loaded.length && top ? `lässt sich einbetten (${loaded.length} von 2). GitHub Pages kann den Schutz nicht setzen; Risiko gering, da keine Konten, Eingaben oder Zahlungen.` : 'eingebettet blockiert'); }

  // ---------- e) Zwischenspeicher sw.js ----------
  { const sw = fs.readFileSync(path.join(ROOT, 'sw.js'), 'utf8');
    const probs = [];
    if (!/url\.origin\s*!==\s*self\.location\.origin/.test(sw)) probs.push('fremde Adressen werden nicht ausgeschlossen');
    if (!/caches\.delete/.test(sw)) probs.push('alte Versionen werden nicht gelöscht');
    const nav = sw.split('req.mode === "navigate"')[1] || '';
    const navBlock = nav.split('return;')[0];
    if (!/res\.ok/.test(navBlock)) probs.push('Seiten mit Fehlercode werden gespeichert');
    if (!/url\.search/.test(sw)) probs.push('Adressen mit ?-Teil (z. B. Urkunde mit Namen) werden gespeichert');
    if (!/register\(base \+ "sw\.js"\)/.test(fs.readFileSync(path.join(ROOT, 'assets/js/main.js'), 'utf8'))) probs.push('Bereich nicht prüfbar');
    add('Zwischenspeicher sw.js', probs.length ? 'FEHLER' : 'ok', probs.join('; ')); }

  // ---------- g) Verräterische Dateien im veröffentlichten Teil ----------
  { const bad = []; const re = /(\.(bak|old|orig|swp|map|env|log|sql|zip|tar|gz|7z|pem|key)$|^\.DS_Store$|^sicherheit-ergebnis\.json$|^package(-lock)?\.json$|~$)/i;
    (function walk(d) { for (const f of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, f.name), rel = path.relative(ROOT, p);
      if (/^(\.|_)/.test(f.name) && f.name !== '.well-known') continue;   // Jekyll veröffentlicht diese nicht
      if (f.isDirectory()) { if (f.name !== 'node_modules') walk(p); } else if (re.test(f.name)) bad.push(rel);
    } })(ROOT);
    add('Keine verräterischen Dateien veröffentlicht', bad.length ? 'FEHLER' : 'ok', bad.join(', ')); }

  // ---------- k) security.txt ----------
  { const f = path.join(ROOT, '.well-known/security.txt'); let res = 'FEHLER', det = 'fehlt';
    const cfg = fs.existsSync(path.join(ROOT, '_config.yml')) ? fs.readFileSync(path.join(ROOT, '_config.yml'), 'utf8') : '';
    if (fs.existsSync(f)) { const s = fs.readFileSync(f, 'utf8'); const m = /^Expires:\s*(\S+)/m.exec(s);
      const exp = m ? new Date(m[1]) : null;
      if (!/^Contact:/m.test(s)) det = 'ohne Contact';
      else if (!exp || exp < new Date(Date.now() + 30 * 864e5)) det = 'läuft in unter 30 Tagen ab oder ohne Expires';
      else if (!/\.well-known/.test(cfg)) det = 'wird nicht veröffentlicht (_config.yml ohne include .well-known)';
      else { res = 'ok'; det = 'gültig bis ' + m[1].slice(0, 10); } }
    add('security.txt (Meldestelle für Lücken)', res, det); }

  await br.close();
  console.table(rows);
  fs.writeFileSync(process.env.OUT || path.join(os.tmpdir(), 'angriff-ergebnis.json'), JSON.stringify(rows, null, 1));
  process.exit(rows.some(r => r.Ergebnis.startsWith('FEHLER')) ? 1 : 0);
})();
