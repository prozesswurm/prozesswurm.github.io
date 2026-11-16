// Rendert die Bildvorlagen aus tpl/ nach <ziel>. Aufruf: node bilder.js <ziel-ordner> [name:breite:hoehe ...]
// Ohne Angaben: alle Standardbilder. Playwright ist vorinstalliert (require('playwright')).
const { chromium } = require('playwright'); const path = require('path');
const ziel = process.argv[2] || 'out';
const std = ['kopf:1200:420','hutliste:1200:760','zahlen:1200:640','sehenswert:1200:560','lied:1200:480','lernwerkstatt:1200:860','cover:1600:900'];
const liste = process.argv.length > 3 ? process.argv.slice(3) : std;
(async()=>{ const b = await chromium.launch();
  for (const e of liste){ const [n,w,h] = e.split(':'); const p = await b.newPage({viewport:{width:+w,height:+h}});
    await p.goto('file://'+path.join(__dirname,'tpl',n+'.html')); await p.waitForTimeout(700);
    await p.screenshot({path: path.join(ziel, n==='cover' ? 'titelbild-webseite.jpg' : n+'.jpg'), type:'jpeg', quality:86}); await p.close(); }
  await b.close(); })();
