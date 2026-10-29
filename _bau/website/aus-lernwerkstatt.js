#!/usr/bin/env node
/* Holt Lektionen, Stufen und Fachbegriffe aus der Lernwerkstatt (lernwerkstatt/index.html)
   und legt sie als Daten für die Website ab:
     _bau/website/daten/lektionen.json  (id, Titel, Kurztext, Minuten, Stufe)
     _bau/website/daten/begriffe.json   (Begriff, Erklärung, Stufe, passende Lektion)
   Aufruf im Hauptordner des Archivs:  node _bau/website/aus-lernwerkstatt.js
   Wird von _bau/website/bauen.py automatisch aufgerufen. */
"use strict";
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const HAUPT = path.resolve(__dirname, "..", "..");
const QUELLE = path.join(HAUPT, "lernwerkstatt", "index.html");
const DATEN = path.join(__dirname, "daten");
const s = fs.readFileSync(QUELLE, "utf8");

/* Liest den Wert hinter "const NAME =" bis zur passenden schließenden Klammer. */
function wert(name) {
  const start = s.indexOf("const " + name + " =");
  if (start < 0) throw new Error("Nicht gefunden: " + name);
  let i = s.indexOf("=", start) + 1;
  while (/\s/.test(s[i])) i++;
  const auf = s[i], zu = auf === "[" ? "]" : "}";
  let tiefe = 0, j = i, str = null;
  for (; j < s.length; j++) {
    const c = s[j];
    if (str) { if (c === "\\") { j++; continue; } if (c === str) str = null; continue; }
    if (c === '"' || c === "'" || c === "`") { str = c; continue; }
    if (c === auf) tiefe++;
    else if (c === zu) { tiefe--; if (tiefe === 0) break; }
  }
  return vm.runInNewContext("(" + s.slice(i, j + 1) + ")");
}

const ALL = wert("ALL");
const LEVELS = wert("LEVELS");
const CARDS = wert("CARDS");
const EXTRA = wert("GLOSS_EXTRA");
const ALIAS = wert("GLOSS_ALIAS");

/* Stufe jeder Lektion */
const stufe = {};
const reihenfolge = [];
LEVELS.forEach(l => {
  const ids = (l.ids || []).concat(...(l.branches || []).map(b => b.ids));
  ids.forEach(id => { if (!stufe[id]) { stufe[id] = l.code; reihenfolge.push(id); } });
});

const lektionen = ALL.filter(l => stufe[l.id]).map(l => ({
  id: l.id, t: l.t, d: l.d, min: l.min, stufe: stufe[l.id]
}));
lektionen.sort((a, b) => reihenfolge.indexOf(a.id) - reihenfolge.indexOf(b.id));

/* Fachbegriffe: passende Lektion = erste Lektion in Lernreihenfolge, in deren Titel,
   Erklärung oder Merksatz der Begriff (oder eine Schreibvariante) vorkommt. */
const text = {};
ALL.forEach(l => { text[l.id] = [l.t, l.d, ...(l.exp || []), l.ex || "", l.aha || "", ...(l.steps || []).map(x => typeof x === "string" ? x : JSON.stringify(x))].join(" "); });
const esc = w => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
function lektionZu(begriff) {
  const woerter = [begriff, ...(ALIAS[begriff] || [])];
  const re = new RegExp("(^|[^0-9A-Za-zÄÖÜäöüß-])(" + woerter.map(esc).join("|") + ")(?:e|en|n|s|es|er)?(?=$|[^0-9A-Za-zÄÖÜäöüß])", "i");
  return reihenfolge.find(id => text[id] && re.test(text[id])) || null;
}
const begriffe = [...CARDS, ...EXTRA]
  .map(c => ({ t: c[1], d: c[2], stufe: c[0], lektion: lektionZu(c[1]) }))
  .filter((x, i, alle) => alle.findIndex(y => y.t === x.t) === i)
  .sort((a, b) => a.t.localeCompare(b.t, "de"));

fs.writeFileSync(path.join(DATEN, "lektionen.json"), JSON.stringify(lektionen, null, 1) + "\n");
fs.writeFileSync(path.join(DATEN, "begriffe.json"), JSON.stringify(begriffe, null, 1) + "\n");
console.log("aus der Lernwerkstatt:", lektionen.length, "Lektionen,", begriffe.length, "Begriffe");
