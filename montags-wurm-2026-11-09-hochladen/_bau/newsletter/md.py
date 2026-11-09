import sys, re, json
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from inhalt import *
try: EIGENE_SACHE
except NameError: EIGENE_SACHE = None
try: HINWEISE
except NameError: HINWEISE = []
def md(s):
    s=re.sub(r'<a href="([^"]+)">(.*?)</a>', r'[\2](\1)', s)
    s=s.replace('<b>','**').replace('</b>','**').replace('<i>','*').replace('</i>','*')
    return s
def blocks(bl, base):
    o=[]
    for b in bl:
        k=b[0]
        if k=='p': o.append(md(b[1]))
        elif k=='h3': o.append('### '+b[1])
        elif k=='img': o.append(f'![{b[2]}]({base}{b[1]})' + (f'\n*{b[3]}*' if b[3] else ''))
        elif k=='kud': o.append(f'> **Doktor Kuddelmuddel:** *„{b[1]}“*')
        elif k=='wurm': o.append(f'**Der Prozesswurm:** „{b[1]}“')
        elif k=='ul': o.append('\n'.join('- '+md(i) for i in b[1]))
        elif k=='ol': o.append('\n'.join(f'{n}. '+md(i) for n,i in enumerate(b[1],1)))
        elif k=='box': o.append(f'**{b[1]}:** {b[2]}')
        elif k=='btn': o.append(f'[{b[1]} →]({b[2]})')
        elif k=='src': o.append(('Quelle: ' if len(b[1])==1 else 'Quellen: ')+' | '.join(f'[{t}]({u})' for t,u in b[1]))
    return o
base=f'https://www.prozesswurm.de/newsletter/{BILD_ORDNER}/'
o=[f'# Montags-Wurm {DATUM}','Bilder liegen unter '+base,
'## Fassung A – Webseite und E-Mail (gleicher Text)', f'# {TITEL}', f'### {UNTERTITEL}', md(EINSTIEG[0][1])] + ([f'> **Doktor Kuddelmuddel:** *„{EINSTIEG[1][1]}“*'] if len(EINSTIEG) > 1 else [])
if EIGENE_SACHE:
    o.append('### '+EIGENE_SACHE['titel']); o+=blocks(EIGENE_SACHE['blocks'],base)
for s in ABSCHNITTE:
    o.append(f'## {s["nr"]}. {s["name"]}'); o.append(f'**{s["headline"]}**'); o+=blocks(s['blocks'],base)
o+=['## 7. Zum Schluss: Ein Satz zum Mitnehmen', f'*„{ZITAT["text"]}“*', ZITAT['wer'], ZITAT['reaktion'], SCHLUSS, '**Dein Prozesswurm**', '[← Zur Übersicht aller Ausgaben](https://www.prozesswurm.de/montags-wurm)',
'## Fassung B – LinkedIn-Artikel',
f'**Erste Zeile (ersetzt den Einstieg):** {LI_ERSTE_ZEILE}', f'**Frage vor dem Schlusssatz:** {LI_FRAGE}', 'Sonst gleicher Text wie Fassung A. Titelbild: titel.jpg.',
'### Begleittext für den Beitrag', LI_BEGLEIT, LI_TAGS,
'## Fassung C – Brevo (E-Mail)',
'- Absendername: Prozesswurm', '- Antwortadresse: info@prozesswurm.de', f'- Betreff: {BETREFF}', f'- Betreff zum Testen: {BETREFF_ALT}', f'- Vorschautext: {VORSCHAU}',
'- Inhalt: die ganze Ausgabe im neuen Layout (Datei newsletter-brevo.html, mit Bildern, Kuddelmuddel-Kästen, Knöpfen). Ab dieser Ausgabe kommt die ganze Ausgabe per E-Mail, nicht mehr die Kurzfassung.',
'- Fußzeile von Brevo mit Abmeldelink und Impressum muss aktiv sein.',
'## Webseite',
f'Quelldatei _bau/website/seiten/2x-mw-JJJJ-MM-TT.html, Eintrag oben in _bau/website/daten/ausgaben.json, Adresse {AUSGABE_URL}/. Bauen mit python3 _bau/website/bauen.py.',
'## Hinweise zur Prüfung'] + ['- '+h for h in HINWEISE]
open('out/doc.md','w').write('\n\n'.join(o)); print(len('\n\n'.join(o)))
