#!/usr/bin/env python3
"""Prozesswurm – Seitenbaukasten.

Baut alle Seiten aus werkzeug/seiten/*.html mit gemeinsamer Kopf- und Fußzeile.
Aufruf (im Hauptordner des Archivs):  python3 _bau/website/bauen.py

Jede Quelldatei beginnt mit einer Kopfzeile in diesem Format:
<!--{"pfad": "ueber-uns/", "titel": "Über uns", "beschreibung": "...", "menue": "ueber-uns"}-->

Neue Montags-Wurm-Ausgabe: Datei _bau/website/seiten/2x-mw-JJJJ-MM-TT.html anlegen,
Eintrag oben in _bau/website/daten/ausgaben.json ergänzen, Skript laufen lassen.

Regeln seit 29.10.2026 (bitte einhalten):
- ausgaben.json: jeder Eintrag hat zusätzlich "stichwort" (ein, zwei Wörter, z. B. "Zuständigkeit")
  und "bild" (Titelbild, z. B. "assets/img/mw-JJJJ-MM-TT-titel.webp"). Die neueste Ausgabe erscheint
  damit groß auf der Startseite und auf „Für Teams“, alle Ausgaben mit Bild in der Übersicht.
- Kopfzeile der Ausgabe: "bild" setzen (gleiches Titelbild). Daraus baut das Skript automatisch
  das Vorschaubild für LinkedIn (assets/og/…jpg, 1200 × 627). Dafür braucht es Node und Playwright.
- In jeder Ausgabe direkt vor <p class="signoff"> den Platzhalter {{teilen}} setzen
  (Knöpfe: Auf LinkedIn teilen, Per E-Mail schicken, Link kopieren).
- Abschnitt 6 heißt auf der Website „6. Lied oder Kurzvideo der Woche“.
- Handgriff der Woche als Text (Liste) im Kasten; eine Beispieltabelle als echte HTML-Tabelle
  (class="example-table" in div.table-wrap), nicht als Bild, damit sie vorlesbar ist.
- Lektionen und Fachbegriffe holt das Skript selbst aus lernwerkstatt/index.html
  (aus-lernwerkstatt.js → daten/lektionen.json). Lerninhalte (Lektionen, Begriffe) bleiben in der
  Lernwerkstatt; die Website verlinkt nur dorthin und zeigt sie nicht noch einmal (Wunsch 29.10.2026).
- Platzhalter für Seiten: {{lektionen:b01,b02}} (Lektionskarten), {{lernpfad:Name|b01,b02}}
  (fertiger Team-Lernpfad mit Link), {{neueste_gross}}, {{einstieg}} (Auswahl aus daten/einstieg.json),
  {{feedback}} (Mail-Link für Rückmeldungen). Unbekannte Platzhalter brechen den Bau ab.
"""
import html
import json
import os
import re
import subprocess
import sys

HAUPT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUELLE = os.path.join(HAUPT, "_bau", "website", "seiten")
DATEN = os.path.join(HAUPT, "_bau", "website", "daten")
LERNWERKSTATT = "lernwerkstatt/"  # relativ zum Hauptordner, wird mit Pfad-Vorsilbe versehen
BREVO = ("https://f509acc4.sibforms.com/serve/MUIFAG7E7H_pxKUm92N5L95yq3kpYnnNVdWem9VyMNff-VNoTRBYAzOueDJjIsg2ujVdaPZ4yDhSMb-"
         "tlaIgg_-oOeSC1Ts4J1QHxs3_TwME7mZ5xJWayF2IRWz7kiKvsuT0zZwwbqN3QppFo8W1lraSVY3LeAKGHJrg5ju-T9oqiI7KnEBK0NfMHS_uS35AX1_lW6NGoTZMD-Yu9g==")
DOMAIN = "https://www.prozesswurm.de/"

CSP = ("default-src 'self'; img-src 'self' data: https://prozesswurm.goatcounter.com; style-src 'self'; font-src 'self'; "
       "script-src 'self' 'inline-speculation-rules' https://gc.zgo.at; "
       "connect-src 'self' https://prozesswurm.goatcounter.com; form-action 'none'; "
       "base-uri 'self'; object-src 'none'; upgrade-insecure-requests")

ICON = {
    "suche": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>',
    "menue": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "pfeil": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "instagram": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>',
    "linkedin": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5h6v2M3 13h18"/></svg>',
    "youtube": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9l5 3-5 3z"/></svg>',
    "spotify": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/></svg>',
    "suno": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V6l11-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/></svg>',
    "buch": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5M8 7h7"/></svg>',
    "post": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "ohr": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/></svg>',
    "kette": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg>',
    "team": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 14.5c3 0 5.5 2 5.5 5"/></svg>',
    "zurueck": '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>',
}

KANAELE = [
    ("instagram", "Instagram", "Comics und kurze Clips", "https://www.instagram.com/prozesswurm/"),
    ("linkedin", "LinkedIn", "Montags-Wurm und Praxistipps", "https://www.linkedin.com/company/prozesswurm/"),
    ("youtube", "YouTube", "Lieder und Kurzvideos", "https://www.youtube.com/@Prozesswurm"),
    ("spotify", "Spotify", "Der Podcast", "https://open.spotify.com/show/1HXgfdJge3mqgA1BxTc2V4"),
    ("suno", "Suno", "Alle Lieder", "https://suno.com/@prozesswurm"),
]

MENUE = [
    ("teams", "Für Teams", "fuer-teams/"),
    ("montags-wurm", "Montags-Wurm", "montags-wurm/"),
    ("hoeren", "Hören und sehen", "hoeren-und-sehen/"),
    ("ueber-uns", "Über uns", "ueber-uns/"),
]
STARTTITEL = "Prozesswurm – Prozessmanagement einfach erklärt"
FEEDBACK = ("mailto:prozesswurm@gmail.com?subject=" + "R%C3%BCckmeldung%20zur%20Website"
            + "&body=" + "Das%20gef%C3%A4llt%20mir%3A%0A%0ADas%20fehlt%20mir%3A%0A%0AHier%20hakt%20es%3A%0A")
VORSCHAU = []  # wird beim Bauen gefüllt, daraus entstehen die Vorschaubilder


def e(text):
    return html.escape(text, quote=True)


def vorschau_name(pfad):
    return (pfad.strip("/").replace("/", "-").replace(".html", "") or "start")


def kopf(seite, p):
    titel = seite["titel"]
    voller_titel = STARTTITEL if seite["pfad"] == "" else f"{titel} – Prozesswurm"
    og_datei = vorschau_name(seite["pfad"])
    if seite["pfad"].startswith("montags-wurm/") and seite["pfad"] != "montags-wurm/" and "og_oben" not in seite:
        for a in daten("ausgaben.json"):
            if seite["pfad"] == f'montags-wurm/{a["pfad"]}/':
                seite["og_oben"] = f'Montags-Wurm · {a["datum"]}'

    VORSCHAU.append({"datei": og_datei, "titel": seite.get("og_titel", titel if seite["pfad"] else "Prozessmanagement, endlich verständlich."),
                     "oben": seite.get("og_oben", "Prozessmanagement einfach erklärt"), "bild": seite.get("bild", "assets/img/titel-zukunftsstadt.webp")})
    bild = f"assets/og/{og_datei}.jpg"
    zeilen = [
        "<!doctype html>",
        '<html lang="de">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
        f"<title>{e(voller_titel)}</title>",
        f'<meta name="description" content="{e(seite["beschreibung"])}">',
        f'<meta http-equiv="Content-Security-Policy" content="{CSP}">',
        '<meta name="referrer" content="strict-origin-when-cross-origin">',
        '<meta name="theme-color" content="#1D7432">',
        f'<meta property="og:title" content="{e(voller_titel)}">',
        f'<meta property="og:description" content="{e(seite["beschreibung"])}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:url" content="{DOMAIN}{seite["pfad"]}">',
        f'<meta property="og:image" content="{DOMAIN}{bild}">',
        '<meta property="og:image:type" content="image/jpeg">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="627">',
        f'<meta property="og:image:alt" content="{e(voller_titel)}">',
        '<meta property="og:site_name" content="Prozesswurm">',
        '<meta property="og:locale" content="de_DE">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<link rel="canonical" href="{DOMAIN}{seite["pfad"]}">',
    ]
    if seite.get("verstecken"):
        zeilen.append('<meta name="robots" content="noindex">')
    zeilen += [
        f'<link rel="icon" href="{p}assets/img/favicon-32.png" sizes="32x32" type="image/png">',
        f'<link rel="apple-touch-icon" href="{p}assets/img/favicon-180.png">',
        f'<link rel="preload" href="{p}assets/fonts/bricolage-grotesque-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>',
        f'<link rel="stylesheet" href="{p}assets/css/style.css">',
        f'<script src="{p}assets/js/theme.js"></script>',
    ] + ([f'<script src="{p}assets/js/weiche.js"></script>'] if seite.get("weiche") else []) + [
        f'<script src="{p}assets/js/main.js" defer></script>',
        '<script type="speculationrules">',
        '{"prefetch":[{"where":{"and":[{"href_matches":"/*"},{"not":{"href_matches":"/lernwerkstatt/*"}},{"not":{"href_matches":"/newsletter/*"}}]},"eagerness":"moderate"}]}',
        "</script>",
        '<script data-goatcounter="https://prozesswurm.goatcounter.com/count" async src="https://gc.zgo.at/count.v5.js" crossorigin="anonymous" integrity="sha384-atnOLvQb9t+jTSipvd75X2yginT4PjVbqDdlJAmxMm+wYElFmeR6EmLP5bYeoRVQ"></script>',
        "</head>",
        "<body>",
        '<a class="skip-link" href="#inhalt">Zum Inhalt springen</a>',
    ]
    menue = []
    for schluessel, name, ziel in MENUE:
        aktiv = ' aria-current="page"' if seite.get("menue") == schluessel else ""
        ziel_url = f"{p}{ziel}" if ziel else (p or "./")
        menue.append(f'        <li><a href="{ziel_url}"{aktiv}>{name}</a></li>')
    zeilen.append(f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{p or './'}" aria-label="Prozesswurm, zur Startseite">
      <img src="{p}assets/img/prozesswurm.webp" alt="" width="240" height="218">
      <span>Prozesswurm</span>
    </a>
    <div class="header-tools">
      <button type="button" class="icon-button" data-search-open aria-haspopup="dialog">
        {ICON["suche"]}
        <span class="visually-hidden">Seite durchsuchen</span>
      </button>
      <button type="button" class="icon-button menu-toggle" aria-expanded="false" aria-controls="hauptmenue">
        {ICON["menue"]}
        <span class="menu-label">Menü</span>
      </button>
    </div>
    <nav class="main-nav" id="hauptmenue" aria-label="Hauptmenü" data-open="false">
      <ul>
{chr(10).join(menue)}
        <li class="nav-cta"><a href="{p}{LERNWERKSTATT}">Lernwerkstatt starten</a></li>
      </ul>
    </nav>
  </div>
</header>
""")
    return "\n".join(zeilen)


def fuss(p):
    kanaele = "\n".join(
        f'        <li><a href="{url}" rel="noopener">{ICON[k]}{name}</a></li>' for k, name, _, url in KANAELE
    )
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-brand">
      <strong>Prozesswurm</strong>
      <p>Prozessmanagement, endlich verständlich. Keine Cookies. Keine Werbung. Kein Google-Tracking.</p>
      <p class="copy-mail">Kontakt: <code>prozesswurm@gmail.com</code> <button type="button" data-copy="prozesswurm@gmail.com">Kopieren</button></p>
      <p><a href="{FEEDBACK}">Rückmeldung zur Website geben</a></p>
    </div>
    <nav aria-labelledby="fuss-entdecken">
      <h2 id="fuss-entdecken">Entdecken</h2>
      <ul>
        <li><a href="{p}{LERNWERKSTATT}">Lernwerkstatt</a></li>
        <li><a href="{p}fuer-teams/">Für Teams und Führungskräfte</a></li>
        <li><a href="{p}montags-wurm/">Montags-Wurm</a></li>
        <li><a href="{p}hoeren-und-sehen/">Hören und sehen</a></li>
        <li><a href="{p}ueber-uns/">Über uns</a></li>
      </ul>
    </nav>
    <nav aria-labelledby="fuss-kanaele">
      <h2 id="fuss-kanaele">Kanäle</h2>
      <ul>
{kanaele}
      </ul>
    </nav>
    <nav aria-labelledby="fuss-recht">
      <h2 id="fuss-recht">Rechtliches</h2>
      <ul>
        <li><a href="{p}impressum/">Impressum</a></li>
        <li><a href="{p}datenschutz/">Datenschutz</a></li>
        <li><a href="{p}barrierefreiheit/">Barrierefreiheit</a></li>
      </ul>
    </nav>
  </div>
  <div class="footer-bottom">
    <div class="wrap">
      <p>© 2026 Prozesswurm. Texte, Lieder und die Figuren Prozesswurm und Doktor Kuddelmuddel sind urheberrechtlich geschützt. Alle Bilder mit KI erstellt.</p>
      <div class="theme-switch" role="group" aria-label="Farbdarstellung">
        <button type="button" data-theme-set="light" aria-pressed="false">Hell</button>
        <button type="button" data-theme-set="auto" aria-pressed="true">Automatisch</button>
        <button type="button" data-theme-set="dark" aria-pressed="false">Dunkel</button>
      </div>
    </div>
  </div>
</footer>

<dialog class="search-dialog" id="suche" aria-labelledby="suche-titel">
  <form method="dialog" role="search">
    <h2 id="suche-titel" class="visually-hidden">Seite durchsuchen</h2>
    <div class="search-row">
      <label for="suchfeld" class="visually-hidden">Suchbegriff</label>
      <input id="suchfeld" type="search" placeholder="Wonach suchst du? Zum Beispiel Ablage" autocomplete="off">
      <button type="submit" class="icon-button" value="schliessen">Schließen</button>
    </div>
  </form>
  <ul class="search-results" id="suchergebnisse" aria-live="polite"></ul>
  <p class="search-empty" id="suchhinweis" hidden>Nichts gefunden. Versuch es mit einem anderen Wort.</p>
</dialog>
</body>
</html>
"""


# ---------- Bausteine, die Seiten über {{platzhalter}} einsetzen ----------
# Jeder Baustein bekommt die Pfad-Vorsilbe p und die Seite (Kopfzeile + Inhalt).

def daten(name):
    return json.load(open(os.path.join(DATEN, name), encoding="utf-8"))


def erster_satz(text):
    m = re.match(r"(.+?[.!?“])(\s|$)", text)
    return m.group(1) if m else text


def baustein_probleme(p, seite=None):
    d = daten("probleme.json")

    def karten(liste):
        out = []
        for x in liste:
            svg = x["svg"].replace('class="ico"', 'class="prob-ico"')
            out.append(
                f'<li><a class="prob-card" href="{p}{LERNWERKSTATT}#problem={e(x["id"])}">{svg}'
                f'<span><b>{e(x["t"])}</b><small>{e(erster_satz(x["k"]))}</small></span><i aria-hidden="true">→</i></a></li>'
            )
        return "\n".join(out)

    return f"""<div class="seg" role="tablist" aria-label="Bereich">
  <button type="button" role="tab" id="tab-job" aria-controls="panel-job" aria-selected="true" data-tab="job">Im Job</button>
  <button type="button" role="tab" id="tab-home" aria-controls="panel-home" aria-selected="false" tabindex="-1" data-tab="home">Zu Hause</button>
</div>
<ul class="prob-list" id="panel-job" role="tabpanel" aria-labelledby="tab-job" data-limit="4">
{karten(d["job"])}
</ul>
<ul class="prob-list" id="panel-home" role="tabpanel" aria-labelledby="tab-home" hidden>
{karten(d["home"])}
</ul>
<button type="button" class="link-button" data-show-all="panel-job" hidden>Alle anzeigen</button>"""


def baustein_kanaele(p, seite=None):
    return '<ul class="channels">\n' + "\n".join(
        f'  <li><a class="channel" href="{url}" rel="noopener"><span class="channel-icon">{ICON[k]}</span>'
        f'<span class="channel-text"><strong>{name}</strong><small>{text}</small></span></a></li>'
        for k, name, text, url in KANAELE
    ) + "\n</ul>"


def baustein_newsletter(p, seite=None):
    return f"""<div class="newsletter">
  <div class="newsletter-text">
    <h2 id="newsletter-titel">Den Montags-Wurm per E-Mail</h2>
    <p>Jeden Montag in deinem Postfach. Du bekommst erst eine Bestätigungsmail, abmelden geht jederzeit mit einem Klick.</p>
  </div>
  <a class="button" href="{BREVO}" rel="noopener">Kostenlos abonnieren {ICON["pfeil"]}</a>
</div>"""


def medium_link(x, art):
    if art == "lied":
        return f'https://suno.com/song/{x["id"]}', "Lied auf Suno", ICON["suno"]
    if x.get("art") == "s":
        return f'https://www.youtube.com/shorts/{x["id"]}', "Kurzvideo auf YouTube", ICON["youtube"]
    return f'https://www.youtube.com/watch?v={x["id"]}', "Video auf YouTube", ICON["youtube"]


def baustein_einstieg(p, seite=None):
    """Kleine Auswahl zum Einstieg auf „Hören und sehen“ (Liste in daten/einstieg.json)."""
    d = daten("medien.json")
    wahl = daten("einstieg.json")
    alle = {("lied", x["id"]): x for x in d["lieder"]}
    alle.update({("video", x["id"]): x for x in d["videos"]})
    out = []
    for w in wahl:
        x = alle.get((w["art"], w["id"]))
        if not x:
            continue
        url, art, icon = medium_link(x, w["art"])
        out.append(f'<li><a class="pick" href="{e(url)}" rel="noopener"><span class="media-icon">{icon}</span>'
                   f'<span class="pick-text"><small>{art}</small><b>{e(x["titel"])}</b><span>{e(w["warum"])}</span></span></a></li>')
    return '<ul class="picks">\n' + "\n".join(out) + "\n</ul>"


def baustein_medien(p, seite=None):
    d = daten("medien.json")
    kat = d["kategorien"]
    vorhanden = [k for k in kat if any(x["kat"] == k for x in d["lieder"] + d["videos"])]
    chips = ['<button type="button" class="chip" data-kat="" aria-pressed="true">Alle</button>'] + [
        f'<button type="button" class="chip" data-kat="{k}" aria-pressed="false">{e(kat[k])}</button>' for k in vorhanden
    ]
    zeilen = []
    for art, liste in (("lied", d["lieder"]), ("video", d["videos"])):
        for x in liste:
            url, text, icon = medium_link(x, art)
            zeilen.append(
                f'<li data-art="{art}" data-kat="{x["kat"]}"><a class="media-row" href="{e(url)}" rel="noopener">'
                f'<span class="media-icon">{icon}</span><span class="media-text"><b>{e(x["titel"])}</b>'
                f'<small>{text} · {e(kat.get(x["kat"], ""))}</small></span><i aria-hidden="true">→</i></a></li>'
            )
    gesamt = len(d["lieder"]) + len(d["videos"])
    return f"""<details class="all-media">
<summary><span><b>Alle {gesamt} Lieder und Videos durchsuchen</b><small>Nach Thema filtern oder nach einem Wort suchen</small></span></summary>
<div class="media-tools">
  <div class="seg seg3" role="group" aria-label="Art">
    <button type="button" data-art-set="" aria-pressed="true">Alles</button>
    <button type="button" data-art-set="lied" aria-pressed="false">Lieder ({len(d["lieder"])})</button>
    <button type="button" data-art-set="video" aria-pressed="false">Videos ({len(d["videos"])})</button>
  </div>
  <div class="filter-field">
    <label for="medienfilter">Titel suchen</label>
    <input id="medienfilter" type="search" placeholder="Zum Beispiel Hut, Chaos oder KI" autocomplete="off">
  </div>
  <div class="chips" role="group" aria-label="Thema">
    {" ".join(chips)}
  </div>
</div>
<p class="media-count" id="medienanzahl" aria-live="polite"></p>
<ul class="media-list" id="medienliste">
{chr(10).join(zeilen)}
</ul>
<p class="search-empty" id="medienleer" hidden>Nichts gefunden. Versuch es mit einem anderen Wort oder Thema.</p>
</details>"""


def ausgabe_bild(p, a, klasse, laden="lazy"):
    if not a.get("bild"):
        return ""
    return (f'<figure class="ai-figure {klasse}"><img src="{p}{e(a["bild"])}" width="960" height="540" alt="" loading="{laden}">'
            f'<span class="ai-note">Mit KI erstellt</span></figure>')


def baustein_ausgaben(p, seite=None):
    out = []
    for i, a in enumerate(daten("ausgaben.json")):
        neu = '<span class="pill">Neu</span>' if i == 0 else ""
        stich = f'<span class="tag">{e(a["stichwort"])}</span>' if a.get("stichwort") else ""
        out.append(
            f'<li><a class="issue-card" href="{p}montags-wurm/{a["pfad"]}/">{ausgabe_bild(p, a, "issue-img")}'
            f'<span class="issue-body"><span class="issue-date">{e(a["datum"])} {neu}{stich}</span>'
            f'<b>{e(a["titel"])}</b><small>{e(a["teaser"])}</small></span></a></li>'
        )
    return '<ul class="issue-list">\n' + "\n".join(out) + "\n</ul>"


def baustein_neueste(p, seite=None):
    a = daten("ausgaben.json")[0]
    return (f'<a class="mini-card" href="{p}montags-wurm/{a["pfad"]}/"><small>Neueste Ausgabe vom {e(a["datum"])}</small>'
            f'<strong>{e(a["titel"])}</strong></a>')


def baustein_neueste_gross(p, seite=None):
    a = daten("ausgaben.json")[0]
    stich = f'<span class="tag">{e(a["stichwort"])}</span>' if a.get("stichwort") else ""
    return f"""<article class="latest">
  {ausgabe_bild(p, a, "latest-img")}
  <div class="latest-text">
    <p class="issue-date">Montags-Wurm vom {e(a["datum"])} {stich}</p>
    <h3><a href="{p}montags-wurm/{a["pfad"]}/">{e(a["titel"])}</a></h3>
    <p>{e(a["teaser"])}</p>
    <div class="button-row">
      <a class="button button-primary" href="{p}montags-wurm/{a["pfad"]}/">Ausgabe lesen {ICON["pfeil"]}</a>
      <a class="button button-secondary" href="{p}montags-wurm/">Alle Ausgaben</a>
    </div>
  </div>
</article>"""


def baustein_neueste_kachel(p, seite=None):
    a = daten("ausgaben.json")[0]
    return (f'<li><a class="tile" href="{p}montags-wurm/{a["pfad"]}/"><span class="eyebrow">Montags-Wurm · {e(a["datum"])}</span>'
            f'<b>{e(a["titel"])}</b><span>{e(a["teaser"])}</span><i aria-hidden="true">→</i></a></li>')


def baustein_teilen(p, seite=None):
    url = DOMAIN + seite["pfad"]
    titel = seite["titel"]
    from urllib.parse import quote
    li = "https://www.linkedin.com/sharing/share-offsite/?url=" + quote(url, safe="")
    mail = ("mailto:?subject=" + quote(f"Lesetipp: {titel}") + "&body="
            + quote(f"Das könnte dich interessieren: {titel}\n{url}\n\nJeden Montag neu vom Prozesswurm."))
    return f"""<div class="share" role="group" aria-labelledby="teilen-titel">
  <p id="teilen-titel"><b>Weitergeben:</b> Kennst du jemanden, den das Thema gerade nervt?</p>
  <div class="share-row">
    <a class="share-btn" href="{e(li)}" rel="noopener">{ICON["linkedin"]}Auf LinkedIn teilen</a>
    <a class="share-btn" href="{e(mail)}">{ICON["post"]}Per E-Mail schicken</a>
    <span class="share-copy"><code class="visually-hidden">{e(url)}</code><button type="button" class="share-btn" data-copy="{e(url)}">{ICON["kette"]}Link kopieren</button></span>
  </div>
</div>"""


def begriff_anker(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")).strip("-")


def baustein_begriffe(p, seite=None):
    b = daten("begriffe.json")
    lek = {l["id"]: l for l in daten("lektionen.json")}
    buchstaben = []
    gruppen = {}
    for x in b:
        bu = x["t"][0].upper()
        if bu.isdigit():
            bu = "0–9"
        bu = {"Ä": "A", "Ö": "O", "Ü": "U"}.get(bu, bu)
        gruppen.setdefault(bu, []).append(x)
        if bu not in buchstaben:
            buchstaben.append(bu)
    sprung = " ".join(f'<a href="#b-{e(bu)}">{e(bu)}</a>' for bu in buchstaben)
    teile = []
    for bu in buchstaben:
        eintraege = []
        for x in gruppen[bu]:
            anker = begriff_anker(x["t"])
            l = lek.get(x.get("lektion") or "")
            mehr = (f'<a class="term-more" href="{p}{LERNWERKSTATT}lektion/{l["id"]}.html">Lektion: {e(l["t"])} '
                    f'<span class="nowrap">({l["stufe"]}, {l["min"]} Min.)</span></a>') if l else ""
            eintraege.append(f'<li id="{anker}" class="term-card" data-term="{e(x["t"].lower())}"><h3>{e(x["t"])}</h3>'
                             f'<p>{e(x["d"])}</p><p class="term-meta"><span class="tag">Stufe {e(x["stufe"])}</span>{mehr}</p></li>')
        teile.append(f'<section class="term-group" aria-labelledby="b-{e(bu)}"><h2 id="b-{e(bu)}">{e(bu)}</h2>'
                     f'<ul class="term-list">{"".join(eintraege)}</ul></section>')
    return f"""<div class="filter-field term-filter">
  <label for="begriffsfilter">Begriff suchen</label>
  <input id="begriffsfilter" type="search" placeholder="Zum Beispiel Schnittstelle, Lean oder KI-Agent" autocomplete="off">
</div>
<nav class="az" aria-label="Nach Anfangsbuchstabe springen">{sprung}</nav>
<p class="media-count" id="begriffsanzahl" aria-live="polite">{len(b)} Begriffe</p>
<div id="begriffe">{"".join(teile)}</div>
<p class="search-empty" id="begriffsleer" hidden>Diesen Begriff gibt es hier noch nicht. Schreib uns, welcher fehlt.</p>"""


def lektionen_liste(p, ids):
    lek = {l["id"]: l for l in daten("lektionen.json")}
    out = []
    for i in ids:
        l = lek.get(i.strip())
        if not l:
            sys.exit(f"Lektion {i} gibt es nicht in der Lernwerkstatt")
        out.append(f'<li><a class="lesson-card" href="{p}{LERNWERKSTATT}#lektion={l["id"]}"><span class="lesson-level">{l["stufe"]}</span>'
                   f'<span class="lesson-text"><b>{e(l["t"])}</b><small>{e(l["d"])} · {l["min"]} Min.</small></span><i aria-hidden="true">→</i></a></li>')
    return '<ul class="lesson-list">\n' + "\n".join(out) + "\n</ul>"


def lernpfad(p, name, ids):
    """Fertiger Team-Lernpfad: Karte mit Lektionen, Knopf zum Starten und Link zum Weitergeben."""
    from urllib.parse import urlencode
    ids = [i.strip() for i in ids if i.strip()]
    lek = {l["id"]: l for l in daten("lektionen.json")}
    for i in ids:
        if i not in lek:
            sys.exit(f"Lektion {i} gibt es nicht in der Lernwerkstatt")
    frag = urlencode({"team": ".".join(ids), "name": name})
    voll = f"{DOMAIN}{LERNWERKSTATT}#{frag}"
    minuten = sum(lek[i]["min"] for i in ids)
    punkte = "".join(f"<li>{e(lek[i]['t'])} <span class=\"muted nowrap\">({lek[i]['stufe']}, {lek[i]['min']} Min.)</span></li>" for i in ids)
    return f"""<article class="path-card">
  <h3>{e(name)}</h3>
  <p class="muted">{len(ids)} kurze Lektionen, zusammen etwa {minuten} Minuten</p>
  <div class="share-row">
    <a class="share-btn share-main" href="{p}{LERNWERKSTATT}#{e(frag)}">Lernpfad öffnen</a>
    <span class="share-copy"><code class="visually-hidden">{e(voll)}</code><button type="button" class="share-btn" data-copy="{e(voll)}">{ICON["kette"]}Link fürs Team kopieren</button></span>
  </div>
</article>"""


BAUSTEINE = {
    "probleme": baustein_probleme,
    "kanaele": baustein_kanaele,
    "newsletter": baustein_newsletter,
    "einstieg": baustein_einstieg,
    "medien": baustein_medien,
    "ausgaben": baustein_ausgaben,
    "neueste_gross": baustein_neueste_gross,
    "neueste_kachel": baustein_neueste_kachel,
    "neueste": baustein_neueste,
    "teilen": baustein_teilen,
    "begriffe": baustein_begriffe,
}


def bauen():
    # Lektionen und Begriffe frisch aus der Lernwerkstatt holen
    try:
        subprocess.run(["node", os.path.join(HAUPT, "_bau", "website", "aus-lernwerkstatt.js")], check=True)
    except (OSError, subprocess.CalledProcessError) as fehler:
        print("Hinweis: Lernwerkstatt-Daten nicht neu geholt, nehme die vorhandenen:", fehler)
    seiten = []
    for name in sorted(os.listdir(QUELLE)):
        if not name.endswith(".html"):
            continue
        text = open(os.path.join(QUELLE, name), encoding="utf-8").read()
        m = re.match(r"<!--(\{.*?\})-->\s*", text, re.S)
        if not m:
            sys.exit(f"Kopfzeile fehlt in {name}")
        seite = json.loads(m.group(1))
        seite["inhalt"] = text[m.end():]
        seiten.append(seite)

    for seite in seiten:
        pfad = seite["pfad"]
        tiefe = pfad.count("/") if pfad not in ("", "404.html") else 0
        p = "../" * tiefe
        if pfad == "404.html":
            p = "/"  # 404 wird unter beliebiger Adresse gezeigt, daher feste Pfade
        inhalt = seite["inhalt"].replace("{{p}}", p).replace("{{lernwerkstatt}}", p + LERNWERKSTATT).replace("{{feedback}}", e(FEEDBACK))
        for k, f in BAUSTEINE.items():
            if "{{" + k + "}}" in inhalt:
                inhalt = inhalt.replace("{{" + k + "}}", f(p, seite))
        inhalt = re.sub(r"\{\{lernpfad:([^|}]+)\|([a-z0-9, ]+)\}\}", lambda m: lernpfad(p, m.group(1).strip(), m.group(2).split(",")), inhalt)
        inhalt = re.sub(r"\{\{lektionen:([a-z0-9, ]+)\}\}", lambda m: lektionen_liste(p, m.group(1).split(",")), inhalt)
        if "{{" in inhalt:
            sys.exit(f"Unbekannter Platzhalter in {seite['pfad']}: " + re.search(r"\{\{[^}]*\}\}", inhalt).group(0))
        dokument = kopf(seite, p) + '\n<main id="inhalt">\n' + inhalt.strip() + "\n</main>\n" + fuss(p)
        ziel = os.path.join(HAUPT, pfad if pfad.endswith(".html") else os.path.join(pfad, "index.html"))
        os.makedirs(os.path.dirname(ziel) or HAUPT, exist_ok=True)
        open(ziel, "w", encoding="utf-8").write(dokument)
        print("gebaut:", os.path.relpath(ziel, HAUPT))

    # Weiterleitungen von alten Google-Sites-Adressen
    weiter = json.load(open(os.path.join(DATEN, "weiterleitungen.json"), encoding="utf-8"))
    for alt, neu in weiter.items():
        ziel = os.path.join(HAUPT, alt, "index.html")
        os.makedirs(os.path.dirname(ziel), exist_ok=True)
        tiefe = alt.strip("/").count("/") + 1
        rel = "../" * tiefe + neu
        open(ziel, "w", encoding="utf-8").write(
            f'<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<title>Weiterleitung</title>\n'
            f'<meta name="robots" content="noindex">\n<link rel="canonical" href="{DOMAIN}{neu}">\n'
            f'<meta http-equiv="refresh" content="0; url={rel}">\n</head>\n<body>\n'
            f'<p>Diese Seite ist umgezogen: <a href="{rel}">weiter zur neuen Adresse</a>.</p>\n</body>\n</html>\n'
        )
        print("weiterleitung:", alt, "->", neu)

    # Suchverzeichnis für die Suche auf der Seite: alle Seiten, Probleme, Lieder und Videos
    suche = []
    for s in seiten:
        if s.get("verstecken"):
            continue
        suche.append({"titel": s["titel"] if s["pfad"] else "Startseite", "url": s["pfad"] or "./",
                      "text": s["beschreibung"], "stichworte": s.get("stichworte", "")})
    probleme = json.load(open(os.path.join(DATEN, "probleme.json"), encoding="utf-8"))
    for bereich, liste in (("Im Job", probleme["job"]), ("Zu Hause", probleme["home"])):
        for x in liste:
            suche.append({"titel": x["t"], "url": f'{LERNWERKSTATT}#problem={x["id"]}',
                          "text": f'Lernwerkstatt · {bereich}: {x["k"]}', "stichworte": "problem nervt hilfe"})
    medien = json.load(open(os.path.join(DATEN, "medien.json"), encoding="utf-8"))
    for x in medien["lieder"]:
        suche.append({"titel": x["titel"], "url": f'https://suno.com/song/{x["id"]}', "text": "Lied auf Suno", "stichworte": "lied musik song"})
    for x in medien["videos"]:
        url = f'https://www.youtube.com/shorts/{x["id"]}' if x.get("art") == "s" else f'https://www.youtube.com/watch?v={x["id"]}'
        suche.append({"titel": x["titel"], "url": url, "text": "Video auf YouTube", "stichworte": "video film kurzvideo"})
    open(os.path.join(HAUPT, "suche.json"), "w", encoding="utf-8").write(json.dumps(suche, ensure_ascii=False, separators=(",", ":")))
    print("gebaut: suche.json mit", len(suche), "Einträgen")

    # Weiterleitungen für die alten Lernwerkstatt-Adressen (früher prozesswurm.github.io/...).
    # GitHub leitet prozesswurm.github.io/x auf www.prozesswurm.de/x um, von dort geht es hier
    # weiter nach /lernwerkstatt/x, inklusive ?… und #… (wichtig für Urkunden- und Speicherlinks).
    lw = os.path.join(HAUPT, "lernwerkstatt")
    alte = [f for f in os.listdir(lw) if f.endswith(".html") and f != "index.html"]
    alte += [os.path.join("lektion", f) for f in os.listdir(os.path.join(lw, "lektion")) if f.endswith(".html")]
    for rel in sorted(alte):
        tiefe = rel.count("/")
        ziel_rel = "../" * tiefe + "lernwerkstatt/" + rel
        bild = "urkunde-og.jpg" if rel == "urkunde.html" else "app-og.jpg"
        datei = os.path.join(HAUPT, rel)
        os.makedirs(os.path.dirname(datei), exist_ok=True)
        open(datei, "w", encoding="utf-8").write(
            '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
            '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; script-src \'unsafe-inline\'; base-uri \'none\'; form-action \'none\'">\n'
            '<title>Prozesswurm Lernwerkstatt</title>\n<meta name="robots" content="noindex">\n'
            f'<link rel="canonical" href="{DOMAIN}lernwerkstatt/{rel}">\n'
            '<meta property="og:title" content="Prozesswurm Lernwerkstatt">\n'
            f'<meta property="og:image" content="{DOMAIN}lernwerkstatt/{bild}">\n'
            f'<script>location.replace("{ziel_rel}" + location.search + location.hash);</script>\n'
            f'<meta http-equiv="refresh" content="1; url={ziel_rel}">\n</head>\n<body>\n'
            f'<p>Die Lernwerkstatt ist umgezogen: <a href="{ziel_rel}">weiter zur Lernwerkstatt</a>.</p>\n</body>\n</html>\n'
        )
    print("weiterleitungen lernwerkstatt:", len(alte))

    open(os.path.join(HAUPT, "CNAME"), "w").write("www.prozesswurm.de\n")
    open(os.path.join(HAUPT, "robots.txt"), "w").write(
        f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}sitemap.xml\nSitemap: {DOMAIN}lernwerkstatt/sitemap.xml\n")

    # Seitenverzeichnis für Suchmaschinen
    urls = [s["pfad"] for s in seiten if not s.get("verstecken") and not s["pfad"].endswith(".html")]
    open(os.path.join(HAUPT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{DOMAIN}{u}</loc></url>\n" for u in sorted(urls))
        + "</urlset>\n"
    )
    print("gebaut: sitemap.xml")

    # Vorschaubilder für LinkedIn und Co.
    open(os.path.join(HAUPT, "_bau", "website", "vorschau-liste.json"), "w", encoding="utf-8").write(
        json.dumps(VORSCHAU, ensure_ascii=False, indent=1) + "\n")
    try:
        subprocess.run(["node", os.path.join(HAUPT, "_bau", "website", "vorschaubilder.js")], check=True, cwd=HAUPT)
    except (OSError, subprocess.CalledProcessError) as fehler:
        print("Hinweis: Vorschaubilder nicht gebaut:", fehler)
    # Fehlt ein Vorschaubild (z. B. ohne Playwright), springt das allgemeine ein
    import shutil
    og = os.path.join(HAUPT, "assets", "og")
    for v in VORSCHAU:
        ziel = os.path.join(og, v["datei"] + ".jpg")
        if not os.path.exists(ziel) and os.path.exists(os.path.join(og, "start.jpg")):
            shutil.copy(os.path.join(og, "start.jpg"), ziel)
            print("Hinweis: allgemeines Vorschaubild verwendet für", v["datei"])


if __name__ == "__main__":
    bauen()
