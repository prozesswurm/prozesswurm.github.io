// Rendert das Instagram-Karussell aus tpl/instagram.html (ein Bild je <section class=s>) als JPG 1080 x 1350, Qualität 85.
// Aufruf: node _bau/newsletter/instagram.js newsletter/JJJJ-MM-TT/instagram
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const ziel = process.argv[2]; fs.mkdirSync(ziel, { recursive: true });
(async()=>{ const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1080,height:1350}});
  await p.goto('file://'+path.join(__dirname,'tpl','instagram.html')); await p.waitForTimeout(900);
  const s = await p.$$('section.s');
  for (let i=0;i<s.length;i++){ await s[i].screenshot({path: path.join(ziel, String(i+1).padStart(2,'0')+'.jpg'), type:'jpeg', quality:85}); }
  console.log(s.length+' Bilder'); await b.close(); })();
