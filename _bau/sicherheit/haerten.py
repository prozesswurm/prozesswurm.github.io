#!/usr/bin/env python3
"""Sicherheits-Härtung der Lernwerkstatt. Im Hauptordner des Archivs ausführen:
   python3 _bau/sicherheit/haerten.py
Mehrfach ausführbar: ändert nur, was noch nicht gehärtet ist."""
import pathlib, re, sys
ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'lernwerkstatt')

# 1) Eigenes Zählskript statt GoatCounter-Skript (seit 07.11.2026):
#    /assets/js/zaehlen.js liest nichts aus dem Gerät (kein localStorage, keine Bildschirmgröße).
GC_OLD = re.compile(r'async src="(?://|https://)gc\.zgo\.at/count(?:\.v\d+)?\.js"[^>]*></script>')
GC_NEW = 'async src="/assets/js/zaehlen.js"></script>'

# 2) Sicherheitsregeln für den Browser
CSP = ("default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; "
       "img-src 'self' data: blob: https://www.prozesswurm.de/lernwerkstatt https://prozesswurm.goatcounter.com; font-src 'self'; "
       "connect-src 'self' https://prozesswurm.goatcounter.com; "
       "frame-src https://suno.com https://www.youtube-nocookie.com; media-src 'self'; manifest-src 'self'; "
       "object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests")
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
left = [str(p) for p in ROOT.rglob('*.html') if 'gc.zgo.at' in p.read_text(encoding='utf-8', errors='ignore')]
print('noch mit fremdem Zählskript:', left or 'keine')
