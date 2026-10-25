// Baut aus den Lektionen der App eigene Seiten, damit Google sie findet.
// Aufruf im Hauptordner:  node _bau/lektionsseiten.mjs
// Danach neu veröffentlichen. Immer ausführen, wenn sich Lektionen ändern.
// Ordner, die mit _ beginnen, veröffentlicht GitHub Pages nicht – dieses Skript bleibt also privat.
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const BASE = 'https://prozesswurm.github.io/';
const html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');

const all = JSON.parse(html.match(/const ALL = (\[.*?\]);\n/s)[1]);
const levelsSrc = html.match(/const LEVELS = (\[[\s\S]*?\n\]);\nLEVELS\.forEach/)[1];
const levels = vm.runInNewContext('(' + levelsSrc + ')');
levels.forEach(lv => { if (lv.branches) lv.ids = lv.branches.flatMap(b => b.ids); });
const L = Object.fromEntries(all.map(l => [l.id, l]));

const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const today = new Date().toISOString().slice(0, 10);
const order = levels.flatMap(lv => lv.ids).filter(id => L[id]);
const levelOf = id => levels.find(lv => lv.ids.includes(id));
const branchOf = id => { const lv = levelOf(id); return lv && lv.branches ? lv.branches.find(b => b.ids.includes(id)) : null; };

const css = `
@font-face{font-family:"Atkinson Hyperlegible";src:url(/fonts/atkinson-hyperlegible-latin-400-normal.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"Atkinson Hyperlegible";src:url(/fonts/atkinson-hyperlegible-latin-700-normal.woff2) format("woff2");font-weight:700;font-display:swap}
@font-face{font-family:"Bricolage Grotesque";src:url(/fonts/bricolage-grotesque-latin-800-normal.woff2) format("woff2");font-weight:800;font-display:swap}
:root{--bg:#F2F5F0;--surface:#fff;--fg:#1C241D;--muted:#5A675C;--worm:#2E9A43;--ink:#1D7432;--soft:#DDF1DF;--line:#D3DBCE}
@media (prefers-color-scheme:dark){:root{--bg:#131915;--surface:#1C231E;--fg:#E7EDE5;--muted:#9CAA9E;--worm:#5BC86C;--ink:#86E294;--soft:#1F3A24;--line:#334036}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 "Atkinson Hyperlegible",system-ui,sans-serif}
main{max-width:680px;margin:0 auto;padding:20px 16px 48px}
a{color:var(--ink)}h1,h2{font-family:"Bricolage Grotesque","Trebuchet MS",sans-serif;line-height:1.2}
h1{font-size:30px;margin:8px 0}h2{font-size:21px;margin:28px 0 8px}
.top{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--fg);font-weight:700}
.k{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:700}
.lead{font-size:19px;color:var(--muted)}
.box{background:var(--surface);border-radius:16px;padding:14px 18px;margin:14px 0;border:1px solid var(--line)}
.aha{background:var(--soft);border:0;font-weight:700}
.cta{display:block;text-align:center;background:var(--worm);color:#fff;text-decoration:none;font-weight:700;border-radius:14px;padding:15px;margin:26px 0 10px;font-size:18px}
.nav{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:18px;font-size:15px}
ol{padding-left:22px}li{margin-bottom:6px}
.list a{display:block;padding:6px 0;text-decoration:none}.list small{color:var(--muted)}
footer{max-width:680px;margin:0 auto;padding:0 16px 40px;font-size:14px;color:var(--muted)}`;

// Hat eine Lektion ein eigenes Bild (bilder/<id>.webp), wird es oben gezeigt und als Vorschaubild beim Teilen genutzt.
const picOf = id => fs.existsSync(path.join(ROOT, 'bilder', `${id}.webp`)) ? `bilder/${id}.webp` : null;
const head = (title, desc, url, img) => `<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)}</title><meta name="description" content="${esc(desc)}">
<link rel="canonical" href="${url}"><link rel="icon" href="/favicon-64.png">
<meta property="og:type" content="article"><meta property="og:title" content="${esc(title)}"><meta property="og:description" content="${esc(desc)}">
<meta property="og:url" content="${url}"><meta property="og:image" content="${BASE}${img || 'app-og.jpg'}"><meta property="og:locale" content="de_DE">
<style>${css}</style>
<script data-goatcounter="https://prozesswurm.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</head><body><main>
<a class="top" href="/"><img src="/wurm.png?v=2" width="44" height="40" alt="">Prozesswurm Lernwerkstatt</a>`;

const foot = `</main><footer>Kostenlos von Prozesswurm, ohne Anmeldung und ohne Werbung. Für dich und dein Team frei nutzbar, bitte „Prozesswurm“ als Quelle nennen.<br>
<a href="/lektionen.html">Alle Lektionen</a> · <a href="/hilfe.html">Hilfe</a> · <a href="https://www.prozesswurm.de/">prozesswurm.de</a> · <a href="https://www.prozesswurm.de/datenschutz">Datenschutz</a></footer></body></html>\n`;

fs.mkdirSync(path.join(ROOT, 'lektion'), { recursive: true });
for (const f of fs.readdirSync(path.join(ROOT, 'lektion'))) if (f.endsWith('.html') && !L[f.slice(0, -5)]) fs.unlinkSync(path.join(ROOT, 'lektion', f));

for (const id of order) {
  const l = L[id], lv = levelOf(id), br = branchOf(id);
  const ids = br ? br.ids : lv.ids, pos = ids.indexOf(id), prev = ids[pos - 1], next = ids[pos + 1];
  const where = `${lv.code} · ${br ? 'Vertiefung ' + br.name : lv.name}`;
  const url = `${BASE}lektion/${id}.html`;
  const pic = picOf(id);
  const page = head(`${l.t} – einfach erklärt | Prozesswurm`, l.d, url, pic) + `
${pic ? `<img src="/${pic}?v=1" alt="" width="1200" style="width:100%;height:auto;border-radius:16px;margin:12px 0 4px">` : ''}
<p class="k">${esc(where)} · ${l.min} Minuten</p>
<h1>${esc(l.t)}</h1>
<p class="lead">${esc(l.d)}</p>
${l.exp.map(p => `<p>${esc(p)}</p>`).join('\n')}
${l.steps ? `<ol>${l.steps.map(x => `<li>${esc(x)}</li>`).join('')}</ol>` : ''}
<h2>Beispiel aus dem Alltag</h2><div class="box">${esc(l.ex)}</div>
<div class="box aha">Zum Merken: ${esc(l.aha)}</div>
<h2>Für deinen Alltag</h2><p>${esc(l.task)}</p>
<a class="cta" href="/#lektion=${id}">In der Lernwerkstatt lernen und ${l.quiz.length} Fragen beantworten →</a>
<div class="nav">${prev ? `<a href="${prev}.html">← ${esc(L[prev].t)}</a>` : '<span></span>'}${next ? `<a href="${next}.html">${esc(L[next].t)} →</a>` : ''}</div>
` + foot;
  fs.writeFileSync(path.join(ROOT, 'lektion', `${id}.html`), page);
}

// Übersicht aller Lektionen
const overview = head('Prozessmanagement einfach erklärt: alle Lektionen | Prozesswurm',
  'Alle Lektionen der kostenlosen Prozesswurm Lernwerkstatt von A1 bis C2: Prozesse, Rollen, Prozesslandkarte, Werkzeuge, Lean, Veränderung und KI, einfach erklärt.',
  `${BASE}lektionen.html`) + `
<h1>Prozessmanagement einfach erklärt</h1>
<p class="lead">Alle Lektionen der Prozesswurm Lernwerkstatt zum Nachlesen. Kostenlos und ohne Anmeldung. Mit Quiz, Abzeichen und Fortschritt geht es in der <a href="/">Lernwerkstatt</a>.</p>
${levels.map(lv => `<h2>${lv.code} · ${esc(lv.name)}</h2><p>${esc(lv.sub)}</p>` + (lv.branches
  ? lv.branches.map(b => `<p class="k">Vertiefung ${esc(b.name)}</p><div class="list">${b.ids.map(id => `<a href="lektion/${id}.html">${esc(L[id].t)}<br><small>${esc(L[id].d)}</small></a>`).join('')}</div>`).join('')
  : `<div class="list">${lv.ids.map(id => `<a href="lektion/${id}.html">${esc(L[id].t)}<br><small>${esc(L[id].d)}</small></a>`).join('')}</div>`)).join('\n')}
` + foot;
fs.writeFileSync(path.join(ROOT, 'lektionen.html'), overview);

// Hilfe als eigene Seite (gleiche Inhalte wie in der App, Quelle: const HELP in index.html)
const help = JSON.parse(html.match(/const HELP = (\[.*?\]);\n/s)[1]);
const helpGroups = [...new Set(help.map(h => h.g))];
const slug = g => g.toLowerCase().replace(/[^a-zäöüß]+/g, '-').replace(/^-|-$/g, '');
const helpBody = h => [...(h.a || []).map(p => `<p>${esc(p)}</p>`), h.s ? `<ol>${h.s.map(x => `<li>${esc(x)}</li>`).join('')}</ol>` : '', ...(h.a2 || []).map(p => `<p>${esc(p)}</p>`)].join('\n');
const helpPage = head('Hilfe: So funktioniert die Prozesswurm Lernwerkstatt',
  'Anleitung zur kostenlosen Prozesswurm Lernwerkstatt: erste Schritte, Lektionen, Werkzeuge, Team-Lernpfad, Urkunden, Fortschritt sichern und Datenschutz.',
  `${BASE}hilfe.html`) + `
<h1>Hilfe: So funktioniert die Lernwerkstatt</h1>
<p class="lead">Alle Fragen und Antworten zur Prozesswurm Lernwerkstatt. Zum Nachlesen, Ausdrucken und Weiterschicken, zum Beispiel an dein Team oder deine Kursgruppe.</p>
<div class="box">${helpGroups.map(g => `<a href="#${slug(g)}">${esc(g)}</a>`).join(' · ')}</div>
${helpGroups.map(g => `<h2 id="${slug(g)}">${esc(g)}</h2>\n` + help.filter(h => h.g === g).map(h => `<h3 id="${h.id}" style="font-size:18px;margin:22px 0 6px">${esc(h.q)}</h3>\n${helpBody(h)}`).join('\n')).join('\n')}
<a class="cta" href="/">Zur Lernwerkstatt →</a>
` + foot;
fs.writeFileSync(path.join(ROOT, 'hilfe.html'), helpPage);

// Sitemap und robots.txt
const urls = [BASE, `${BASE}lektionen.html`, `${BASE}hilfe.html`, `${BASE}mediathek.html`, ...order.map(id => `${BASE}lektion/${id}.html`)];
fs.writeFileSync(path.join(ROOT, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(u => `  <url><loc>${u}</loc><lastmod>${today}</lastmod></url>`).join('\n')}
</urlset>
`);
fs.writeFileSync(path.join(ROOT, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${BASE}sitemap.xml\n`);
console.log(`Fertig: ${order.length} Lektionsseiten, Übersicht, Hilfe (${help.length} Fragen), Sitemap mit ${urls.length} Adressen.`);
