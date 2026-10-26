import re, sys, html, json
sys.path.insert(0, sys.argv[3] if len(sys.argv) > 3 else '.')
from inhalt import *

IMG_BASE = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "auto" else f"https://prozesswurm.github.io/newsletter/{BILD_ORDNER}/"
OUT = sys.argv[2] if len(sys.argv) > 2 else "out/newsletter-brevo.html"

F = "Helvetica,Arial,sans-serif"
GRUEN = "#2E7D32"; DUNKEL = "#1C241D"; GRAU = "#5A675C"; LILA = "#7A4BB4"; LILA_HELL = "#EEE6F8"; GRUEN_HELL = "#E3EEDD"
P = f"margin:0 0 16px;font-family:{F};font-size:16px;line-height:1.6;color:{DUNKEL};"
LINK = f"color:{GRUEN};text-decoration:underline;"

def links(s):
    return s.replace('<a href=', f'<a style="{LINK}" target="_blank" href=')

def text_of(s): return re.sub(r'<[^>]+>', ' ', s)

def kud(t):
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:6px 0 18px;background:{LILA_HELL};border-radius:10px;border-left:5px solid {LILA};">
<tr><td width="64" valign="top" style="padding:12px 0 12px 12px;"><img src="{IMG_BASE}kuddel.png" width="48" alt="Doktor Kuddelmuddel" style="display:block;width:48px;height:auto;border:0;"></td>
<td valign="top" style="padding:12px 14px 12px 10px;font-family:{F};font-size:15px;line-height:1.5;color:{DUNKEL};"><b>Doktor Kuddelmuddel:</b> <i>„{t}“</i></td></tr></table>'''

def img(f, alt, cap):
    c = f'<div style="margin-top:8px;font-family:{F};font-size:13px;color:{GRAU};font-style:italic;text-align:center;line-height:1.4;">{cap}</div>' if cap else ''
    return f'<div style="margin:6px 0 20px;"><img src="{IMG_BASE}{f}" width="580" alt="{html.escape(alt)}" style="display:block;width:100%;max-width:580px;height:auto;border:0;border-radius:8px;">{c}</div>'

def src(lst):
    s = " | ".join(f'<a style="color:{GRUEN};text-decoration:none;" target="_blank" href="{u}">{t}</a>' for t, u in lst)
    return f'<p style="margin:-4px 0 18px;font-family:{F};font-size:13px;color:{GRAU};">Quellen: {s}</p>'

def btn(t, u):
    # Knopf-Stil B (seit 26.10.2026): gruener Rahmen, rund, ohne Flaeche
    return f'''<table role="presentation" cellpadding="0" cellspacing="0" style="margin:4px 0 22px;"><tr><td style="border:2px solid {GRUEN};border-radius:999px;">
<a href="{u}" target="_blank" style="display:inline-block;padding:9px 20px;font-family:{F};font-size:15px;font-weight:bold;color:{GRUEN};text-decoration:none;">{t} &rarr;</a></td></tr></table>'''

def box(k, t):
    return f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 12px;background:{GRUEN_HELL};border-radius:10px;"><tr><td style="padding:12px 16px;font-family:{F};">
<div style="font-size:12px;font-weight:bold;letter-spacing:1.5px;text-transform:uppercase;color:#3C5A3A;margin-bottom:4px;">{k}</div>
<div style="font-size:16px;line-height:1.5;color:{DUNKEL};">{t}</div></td></tr></table>'''

def block(b):
    k = b[0]
    if k == "p": return f'<p style="{P}">{links(b[1])}</p>'
    if k == "h3": return f'<h3 style="margin:26px 0 10px;font-family:{F};font-size:19px;line-height:1.3;color:{DUNKEL};">{b[1]}</h3>'
    if k == "img": return img(b[1], b[2], b[3])
    if k == "kud": return kud(b[1])
    if k == "src": return src(b[1])
    if k == "btn": return btn(b[1], b[2])
    if k == "box": return box(b[1], b[2])
    if k in ("ul", "ol"):
        items = "".join(f'<li style="margin:0 0 10px;">{links(i)}</li>' for i in b[1])
        return f'<{k} style="margin:0 0 18px;padding-left:22px;font-family:{F};font-size:16px;line-height:1.6;color:{DUNKEL};">{items}</{k}>'
    raise ValueError(k)

HR = f'<hr style="border:0;border-top:1px solid #D3DBCE;margin:30px 0;">'

def section(s):
    out = [f'<div style="font-family:{F};font-size:12px;font-weight:bold;letter-spacing:2px;text-transform:uppercase;color:{GRUEN};margin:0 0 6px;">{s["nr"]}. {s["name"]}</div>',
           f'<h2 style="margin:0 0 16px;font-family:{F};font-size:24px;line-height:1.25;color:{DUNKEL};">{s["headline"]}</h2>']
    out += [block(b) for b in s["blocks"]]
    return "\n".join(out)

# Wortzahl
alltext = " ".join(text_of(b[1]) if isinstance(b[1], str) else " ".join(map(text_of, b[1])) if b[0] in ("ul","ol") else "" for s in ABSCHNITTE for b in s["blocks"] if b[0] in ("p","h3","kud","ul","ol"))
alltext += " ".join(text_of(b[1]) for b in EINSTIEG) + " " + " ".join(b[2] for s in ABSCHNITTE for b in s["blocks"] if b[0]=="box")
alltext += " " + ZITAT["text"] + " " + ZITAT["reaktion"] + " " + SCHLUSS
WORDS = len(alltext.split()); WORDS_R = round(WORDS / 50) * 50; MIN = max(1, round(WORDS / 200))

intro = f'''<p style="{P}">{EINSTIEG[0][1]}</p>
{kud(EINSTIEG[1][1])}
<p style="{P}">Diese Ausgabe hat rund <b>{WORDS_R} Wörter</b>, etwa <b>{MIN} Minuten</b> Lesezeit. Heute ist <b>Montag, der {DATUM}</b>, willkommen in der <b>{KW}</b>.</p>
<p style="margin:0;font-family:{F};font-size:15px;line-height:1.6;color:{GRAU};">Du kennst jemanden, der plötzlich Prozesse am Hals hat? Leite ihm diese Mail weiter. Anmelden geht kostenlos über <a style="{LINK}" target="_blank" href="https://www.prozesswurm.de/montags-wurm">prozesswurm.de</a>.</p>'''

inhalt = f'''<div style="font-family:{F};font-size:13px;font-weight:bold;letter-spacing:2px;text-transform:uppercase;color:{GRAU};margin:0 0 4px;">Der Montags-Wurm · {DATUM}</div>
<h1 style="margin:0 0 18px;font-family:{F};font-size:30px;line-height:1.2;color:{DUNKEL};">{UNTERTITEL}</h1>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F7F9F5;border-radius:10px;margin:0 0 28px;"><tr><td style="padding:12px 16px;font-family:{F};font-size:13px;color:{GRAU};">
<b style="color:{DUNKEL};">Heute drin:</b> {HEUTE_DRIN}</td></tr></table>
'''

body = [intro, HR, inhalt] + [section(s) + HR for s in ABSCHNITTE]
zitat = f'''<div style="font-family:{F};font-size:12px;font-weight:bold;letter-spacing:2px;text-transform:uppercase;color:{GRUEN};margin:0 0 6px;">7. Zum Schluss: Ein Satz zum Mitnehmen</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:8px 0 14px;"><tr><td style="border-left:5px solid {GRUEN};padding:6px 0 6px 18px;">
<div style="font-family:Georgia,'Times New Roman',serif;font-size:22px;line-height:1.4;font-style:italic;color:{DUNKEL};">„{ZITAT["text"]}“</div>
<div style="margin-top:8px;font-family:{F};font-size:14px;color:{GRAU};">{ZITAT["wer"]}</div></td></tr></table>
<p style="{P}">{ZITAT["reaktion"]}</p>'''
body.append(zitat + HR)
schluss = f'''<p style="{P}">{SCHLUSS.replace("prozesswurm@gmail.com", f'<a style="{LINK}" href="mailto:prozesswurm@gmail.com">prozesswurm@gmail.com</a>')}</p>
<table role="presentation" cellpadding="0" cellspacing="0" style="margin:6px 0 4px;"><tr><td valign="middle" style="padding-right:12px;"><img src="{IMG_BASE}wurm.png" width="56" alt="Der Prozesswurm" style="display:block;width:56px;height:auto;border:0;"></td>
<td valign="middle" style="font-family:{F};font-size:17px;font-weight:bold;color:{DUNKEL};">Dein Prozesswurm</td></tr></table>
{btn("Diese Ausgabe auf prozesswurm.de lesen", AUSGABE_URL)}'''
body.append(schluss)

fuss = f'''<p style="margin:0 0 8px;">Folge dem Prozesswurm:
<a style="color:{DUNKEL};text-decoration:none;" href="https://www.instagram.com/prozesswurm/">Instagram</a> |
<a style="color:{DUNKEL};text-decoration:none;" href="https://www.linkedin.com/company/prozesswurm">LinkedIn</a> |
<a style="color:{DUNKEL};text-decoration:none;" href="https://www.youtube.com/@Prozesswurm">YouTube</a> |
<a style="color:{DUNKEL};text-decoration:none;" href="https://suno.com/@prozesswurm">Suno</a></p>
<p style="margin:0 0 8px;"><a style="color:{DUNKEL};text-decoration:none;" href="{APP}">Lernwerkstatt</a> |
<a style="color:{DUNKEL};text-decoration:none;" href="https://www.prozesswurm.de/montags-wurm">Alle Ausgaben</a> |
<a style="color:{DUNKEL};text-decoration:none;" href="https://www.prozesswurm.de/impressum">Impressum</a> |
<a style="color:{DUNKEL};text-decoration:none;" href="https://www.prozesswurm.de/datenschutz">Datenschutz</a></p>
<p style="margin:0;">© Prozesswurm</p>'''

doc = f'''<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{TITEL}</title>
<style>@media only screen and (max-width:620px){{ .inhalt{{padding:20px 16px !important;}} h1{{font-size:26px !important;}} h2{{font-size:21px !important;}} }}</style></head>
<body style="margin:0;padding:0;background:#F2F5F0;">
<div style="display:none;max-height:0;overflow:hidden;">{VORSCHAU}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F2F5F0;"><tr><td align="center" style="padding:16px 8px;">
<table role="presentation" width="640" cellpadding="0" cellspacing="0" style="width:100%;max-width:640px;background:#ffffff;border:1px solid #D3DBCE;border-radius:12px;overflow:hidden;">
<tr><td><a href="https://www.prozesswurm.de/montags-wurm" target="_blank"><img src="{IMG_BASE}kopf.jpg" width="640" alt="Der Montags-Wurm – Prozessmanagement in einfachen Worten, mit dem Prozesswurm und Doktor Kuddelmuddel" style="display:block;width:100%;max-width:640px;height:auto;border:0;"></a></td></tr>
<tr><td class="inhalt" style="padding:28px 30px;">
{chr(10).join(body)}
</td></tr></table>
<table role="presentation" width="640" cellpadding="0" cellspacing="0" style="width:100%;max-width:640px;"><tr><td style="padding:18px 10px;text-align:center;font-family:{F};font-size:12px;line-height:1.5;color:{GRAU};">
{fuss}
</td></tr></table>
</td></tr></table></body></html>'''
open(OUT, "w").write(doc)
print("Wörter:", WORDS, "->", WORDS_R, MIN, "Min")
