import sys, re, json
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from inhalt import *
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
        elif k=='ul': o.append('\n'.join('- '+md(i) for i in b[1]))
        elif k=='ol': o.append('\n'.join(f'{n}. '+md(i) for n,i in enumerate(b[1],1)))
        elif k=='box': o.append(f'**{b[1]}:** {b[2]}')
        elif k=='btn': o.append(f'[{b[1]} →]({b[2]})')
        elif k=='src': o.append('Quellen: '+' | '.join(f'[{t}]({u})' for t,u in b[1]))
    return o
base=f'https://www.prozesswurm.de/newsletter/{BILD_ORDNER}/'
o=[f'# Montags-Wurm {DATUM}','Vereinbarte Fassung (neues Layout, angelehnt an den Beispiel-Newsletter). Bilder liegen unter '+base,
'## Fassung A – Webseite und E-Mail (gleicher Text)', f'# {TITEL}', f'### {UNTERTITEL}', md(EINSTIEG[0][1]), f'> **Doktor Kuddelmuddel:** *„{EINSTIEG[1][1]}“*']
for s in ABSCHNITTE:
    o.append(f'## {s["nr"]}. {s["name"]}'); o.append(f'**{s["headline"]}**'); o+=blocks(s['blocks'],base)
o+=['## 7. Zum Schluss: Ein Satz zum Mitnehmen', f'*„{ZITAT["text"]}“*', ZITAT['wer'], ZITAT['reaktion'], SCHLUSS, '**Dein Prozesswurm**', '[← Zur Übersicht aller Ausgaben](https://www.prozesswurm.de/montags-wurm)',
'## Fassung B – LinkedIn-Artikel',
f'**Erste Zeile (ersetzt den Einstieg):** {LI_ERSTE_ZEILE}', f'**Frage vor dem Schlusssatz:** {LI_FRAGE}', 'Sonst gleicher Text wie Fassung A. Titelbild: titel.jpg.',
'### Begleittext für den Beitrag', LI_BEGLEIT, LI_TAGS,
'## Fassung C – Brevo (E-Mail)',
'- Absendername: Prozesswurm', '- Antwortadresse: prozesswurm@gmail.com', f'- Betreff: {BETREFF}', f'- Betreff zum Testen: {BETREFF_ALT}', f'- Vorschautext: {VORSCHAU}',
'- Inhalt: die ganze Ausgabe im neuen Layout (Datei newsletter-brevo.html, mit Bildern, Kuddelmuddel-Kästen, Knöpfen). Ab dieser Ausgabe kommt die ganze Ausgabe per E-Mail, nicht mehr die Kurzfassung.',
'- Fußzeile von Brevo mit Abmeldelink und Impressum muss aktiv sein.',
'## Webseiten-Vorlage',
f'1. Neue Unterseite unter „Montags-Wurm“, Seitenname „{DATUM}“ (Adresse {AUSGABE_URL}).','2. Oben das Titelbild titel.jpg (Originalfiguren), darunter EIN Textfeld mit Fassung A.',
'3. Formatvorlagen der Webseite: Titel, Überschrift, Zwischenüberschrift für 1.–7., sonst Normaler Text.', f'4. Auf der Übersichtsseite oben eintragen: „{DATUM} – {UNTERTITEL}“.',
'## Hinweise zur Prüfung',
'- Sicherheitsbeauftragte: Bundestagsbeschluss Ende März 2026 (Handwerkskammer Halle). Datum des Inkrafttretens nicht gefunden.',
'- 123.000 und 135 Mio. Euro stammen aus dem Konzept des Bundesarbeitsministeriums (Oktober 2025, über dpa). Die Gesamtzahl der Sicherheitsbeauftragten ist uneinheitlich (Oiger 670.000, DHZ 760.000), deshalb nicht genannt.',
'- Datenschutzbeauftragter: nur angekündigt (Föderale Modernisierungsagenda 4.12.2025), Einbringung bis 31.12.2026 geplant, kein Beschluss.',
'- Redwood-Studie: Anbieterstudie, so im Text gekennzeichnet.',
'- Deming-Zitat: Mitschrift eines Seminarteilnehmers 1993, daher „zugeschrieben“.',
'- ARTE-Reportage geprüft am 26.10.2026: 31 Min., verfügbar bis 22.03.2028.',
'- Lied „Wer hat den Hut auf?“ auf Suno geprüft: 3:14, erklärt die 51-Prozent-Regel.',
'- Brevo-Kontakte: keine neuen Anmelde-Mails in Gmail gefunden.']
open('out/doc.md','w').write('\n\n'.join(o)); print(len('\n\n'.join(o)))
