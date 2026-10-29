#!/usr/bin/env node
/* Baut die Vorschaubilder für LinkedIn, WhatsApp und Co. (1200 × 627 Pixel, JPG).
   LinkedIn zeigt nur JPG, PNG und GIF an, kein WebP, und schneidet Hochformate ab.
   Liste kommt aus _bau/website/vorschau-liste.json (schreibt bauen.py).
   Gebaut wird nur, was neu ist oder sich geändert hat. Alles neu: --alle
   Aufruf im Hauptordner:  node _bau/website/vorschaubilder.js */
"use strict";
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const HAUPT = path.resolve(__dirname, "..", "..");
const LISTE = path.join(__dirname, "vorschau-liste.json");
const STAND = path.join(__dirname, "vorschau-stand.json");
const ZIEL = path.join(HAUPT, "assets", "og");
const VORLAGE = path.join(__dirname, "_vorschau.html");
const VERSION = "3"; // hochzählen, wenn sich die Gestaltung ändert

const liste = JSON.parse(fs.readFileSync(LISTE, "utf8"));
const stand = fs.existsSync(STAND) ? JSON.parse(fs.readFileSync(STAND, "utf8")) : {};
const alle = process.argv.includes("--alle");
fs.mkdirSync(ZIEL, { recursive: true });

const esc = t => String(t).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const hash = x => crypto.createHash("sha1").update(VERSION + JSON.stringify(x)).digest("hex").slice(0, 12);

function groesse(x) {
  const lang = Math.max(...x.titel.split(/\s+/).map(w => w.length));
  const breite = x.bild ? 560 : 1000;
  let g = x.titel.length > 42 ? 54 : x.titel.length > 28 ? 62 : 72;
  return Math.min(g, Math.floor(breite / (0.6 * lang)));
}

function seite(x) {
  const bild = x.bild ? `<figure><img src="../../${esc(x.bild)}" alt=""><span>Mit KI erstellt</span></figure>` : "";
  return `<!doctype html><html lang="de"><head><meta charset="utf-8"><style>
@font-face{font-family:A;src:url(../../assets/fonts/atkinson-hyperlegible-latin-700-normal.woff2)}
@font-face{font-family:B;src:url(../../assets/fonts/bricolage-grotesque-latin-800-normal.woff2)}
*{box-sizing:border-box;margin:0}
body{width:1200px;height:627px;overflow:hidden;background:#F2F5F0;font-family:A,sans-serif;color:#16201A;display:flex;gap:44px;padding:56px 56px 52px 64px;position:relative}
body::after{content:"";position:absolute;left:0;top:0;bottom:0;width:14px;background:#1D7432}
.text{flex:1;display:flex;flex-direction:column;min-width:0}
.marke{display:flex;align-items:center;gap:14px;font:800 34px B,sans-serif}
.marke img{width:64px}
.oben{margin-top:38px;font-size:24px;letter-spacing:.06em;text-transform:uppercase;color:#1D7432}
h1{margin-top:14px;font:800 ${groesse(x)}px/1.04 B,sans-serif;letter-spacing:-.02em}
.url{margin-top:auto;font-size:26px;color:#3E4A42}
figure{position:relative;flex:0 0 ${x.bild ? 430 : 0}px;border-radius:28px;overflow:hidden;box-shadow:0 18px 50px rgba(22,32,26,.18)}
figure img{width:100%;height:100%;object-fit:cover;object-position:28% 50%}
figure span{position:absolute;right:12px;bottom:12px;padding:4px 12px;border-radius:99px;background:rgba(15,20,16,.6);color:#fff;font-size:17px}
</style></head><body><div class="text">
<div class="marke"><img src="../../assets/img/prozesswurm.webp" alt="">Prozesswurm</div>
<p class="oben">${esc(x.oben)}</p><h1>${esc(x.titel)}</h1><p class="url">prozesswurm.de</p></div>${bild}</body></html>`;
}

(async () => {
  const offen = liste.filter(x => alle || stand[x.datei] !== hash(x) || !fs.existsSync(path.join(ZIEL, x.datei + ".jpg")));
  if (!offen.length) { console.log("vorschaubilder: alle aktuell"); return; }
  let chromium;
  try { ({ chromium } = require("playwright")); } catch (e) {
    console.log("vorschaubilder: Playwright fehlt, übersprungen (npm i playwright)"); return;
  }
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 627 } });
  for (const x of offen) {
    fs.writeFileSync(VORLAGE, seite(x));
    await p.goto("file://" + VORLAGE);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(80);
    await p.screenshot({ path: path.join(ZIEL, x.datei + ".jpg"), type: "jpeg", quality: 86 });
    stand[x.datei] = hash(x);
    console.log("vorschaubild:", x.datei + ".jpg");
  }
  await b.close();
  fs.unlinkSync(VORLAGE);
  fs.writeFileSync(STAND, JSON.stringify(stand, null, 1) + "\n");
})();
