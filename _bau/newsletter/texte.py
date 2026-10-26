import sys, re, json
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from inhalt import *

def blocks_html(blocks, linkedin=False):
    out = []
    for b in blocks:
        k = b[0]
        if k == "p": out.append(f"<p>{b[1]}</p>")
        elif k == "h3": out.append(f"<p><b>{b[1]}</b></p>")
        elif k == "kud": out.append(f"<p><b>Doktor Kuddelmuddel:</b> <i>„{b[1]}“</i></p>")
        elif k in ("ul", "ol"): out.append(f"<{k}>" + "".join(f"<li>{i}</li>" for i in b[1]) + f"</{k}>")
        elif k == "box": out.append(f"<p><b>{b[1]}:</b> {b[2]}</p>")
        elif k == "btn": out.append(f'<p><a href="{b[2]}">{b[1]} →</a></p>')
        elif k == "src": out.append("<p>Quellen: " + " | ".join(f'<a href="{u}">{t}</a>' for t, u in b[1]) + "</p>")
    return out

def ausgabe(linkedin=False):
    o = [f"<h1>{TITEL}</h1>", f"<h2>{UNTERTITEL}</h2>"]
    if linkedin:
        o.append(f"<p><b>{LI_ERSTE_ZEILE}</b></p>")
        o.append("<p>Die Bundesregierung will ausmisten. Diese Woche geht es darum, warum ein Titel noch keine Zuständigkeit ist und wie du herausfindest, wer bei euch wirklich den Hut aufhat.</p>")
        o.append(f"<p><b>Doktor Kuddelmuddel:</b> <i>„{EINSTIEG[1][1]}“</i></p>")
    else:
        o.append(f"<p>{EINSTIEG[0][1]}</p>")
        o.append(f"<p><b>Doktor Kuddelmuddel:</b> <i>„{EINSTIEG[1][1]}“</i></p>")
    for s in ABSCHNITTE:
        o.append(f"<h3>{s['nr']}. {s['name']}</h3>" if not linkedin else f"<h2>{s['nr']}. {s['name']}</h2>")
        o.append(f"<p><b>{s['headline']}</b></p>")
        o += blocks_html(s["blocks"], linkedin)
    o.append("<h3>7. Zum Schluss: Ein Satz zum Mitnehmen</h3>" if not linkedin else "<h2>7. Zum Schluss: Ein Satz zum Mitnehmen</h2>")
    o.append(f"<p><i>„{ZITAT['text']}“</i></p><p>{ZITAT['wer']}</p><p>{ZITAT['reaktion']}</p>")
    if linkedin:
        o.append(f"<p><b>Frage an dich:</b> {LI_FRAGE}</p>")
    o.append(f"<p>{SCHLUSS}</p><p><b>Dein Prozesswurm</b></p>")
    if linkedin:
        o.append(f'<p>Den Montags-Wurm gibt es auch per E-Mail: <a href="https://www.prozesswurm.de/montags-wurm">prozesswurm.de/montags-wurm</a></p>')
    else:
        o.append('<p><a href="https://www.prozesswurm.de/montags-wurm">← Zur Übersicht aller Ausgaben</a></p>')
    return "\n".join(o)

open("out/webseite.html", "w").write(ausgabe(False))
open("out/linkedin.html", "w").write(ausgabe(True))
print(len(re.sub('<[^>]+>', ' ', ausgabe(False)).split()))
