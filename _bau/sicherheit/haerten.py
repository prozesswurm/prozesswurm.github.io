#!/usr/bin/env python3
"""Sicherheits-Härtung der Lernwerkstatt. Im Hauptordner des Archivs ausführen:
   python3 _bau/sicherheit/haerten.py
Mehrfach ausführbar: ändert nur, was noch nicht gehärtet ist."""
import pathlib, re, sys
ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')

# 1) Zähl-Skript mit fester Version und Prüfsumme (https://goatcounter.com/help/countjs-versions)
GC_OLD = re.compile(r'async src="//gc\.zgo\.at/count\.js"></script>')
GC_NEW = ('async src="https://gc.zgo.at/count.v5.js" crossorigin="anonymous" '
          'integrity="sha384-atnOLvQb9t+jTSipvd75X2yginT4PjVbqDdlJAmxMm+wYElFmeR6EmLP5bYeoRVQ"></script>')

# 2) Sicherheitsregeln für den Browser
CSP = ("default-src 'self'; script-src 'self' 'unsafe-inline' https://gc.zgo.at; style-src 'self' 'unsafe-inline'; "
       "img-src 'self' data: blob: https://prozesswurm.github.io https://prozesswurm.goatcounter.com; font-src 'self'; "
       "connect-src 'self' https://prozesswurm.goatcounter.com https://docs.google.com; "
       "frame-src https://suno.com https://www.youtube-nocookie.com; media-src 'self'; manifest-src 'self'; "
       "object-src 'none'; base-uri 'self'; form-action 'self' https://docs.google.com; upgrade-insecure-requests")
CSP_TAG = f'<meta http-equiv="Content-Security-Policy" content="{CSP}">'
CHARSET = re.compile(r'<meta charset="utf-8">', re.I)

pages = ['index.html', 'mediathek.html', 'urkunde.html', 'hilfe.html', 'lektionen.html'] + \
        sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'lektion').glob('*.html'))
changed = []
for rel in pages + ['_bau/lektionsseiten.mjs']:
    f = ROOT / rel
    if not f.exists():
        continue
    s = o = f.read_text(encoding='utf-8')
    s = GC_OLD.sub(GC_NEW, s)
    if 'Content-Security-Policy' in s:          # vorhandene Regel auf den aktuellen Stand bringen
        s = re.sub(r'<meta http-equiv="Content-Security-Policy" content="[^"]*">', CSP_TAG, s)
    else:
        s = CHARSET.sub(lambda m: m.group(0) + CSP_TAG, s, count=1)
    if s != o:
        f.write_text(s, encoding='utf-8'); changed.append(rel)
print(f'{len(changed)} Dateien gehärtet')
left = [str(p) for p in ROOT.rglob('*.html') if 'gc.zgo.at/count.js"' in p.read_text(encoding='utf-8', errors='ignore')]
print('noch ohne Prüfsumme:', left or 'keine')
