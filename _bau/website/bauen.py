#!/usr/bin/env python3
"""Prozesswurm – Seitenbaukasten.

Baut alle Seiten aus werkzeug/seiten/*.html mit gemeinsamer Kopf- und Fußzeile.
Aufruf (im Hauptordner des Archivs):  python3 _bau/website/bauen.py

Jede Quelldatei beginnt mit einer Kopfzeile in diesem Format:
<!--{"pfad": "ueber-uns/", "titel": "Über uns", "beschreibung": "...", "menue": "ueber-uns"}-->

Neue Montags-Wurm-Ausgabe: Datei _bau/website/seiten/2x-mw-JJJJ-MM-TT.html anlegen,
Eintrag oben in _bau/website/daten/ausgaben.json ergänzen, Skript laufen lassen.
"""
import html
import json
import os
import re
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
    ("start", "Start", ""),
    ("hoeren", "Hören und sehen", "hoeren-und-sehen/"),
    ("montags-wurm", "Montags-Wurm", "montags-wurm/"),
    ("ueber-uns", "Über uns", "ueber-uns/"),
]


def e(text):
    return html.escape(text, quote=True)


def kopf(seite, p):
    titel = seite["titel"]
    voller_titel = "Prozesswurm" if seite["pfad"] == "" else f"{titel} – Prozesswurm"
    bild = seite.get("bild", "assets/img/titel-zukunftsstadt.webp")
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
        <span>Menü</span>
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
      <p>Keine Cookies. Keine Werbung. Kein Google-Tracking.</p>
      <p class="copy-mail">Kontakt: <code>prozesswurm@gmail.com</code> <button type="button" data-copy="prozesswurm@gmail.com">Kopieren</button></p>
    </div>
    <nav aria-labelledby="fuss-entdecken">
      <h2 id="fuss-entdecken">Entdecken</h2>
      <ul>
        <li><a href="{p}{LERNWERKSTATT}">Lernwerkstatt</a></li>
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

def baustein_probleme(p):
    d = json.load(open(os.path.join(DATEN, "probleme.json"), encoding="utf-8"))

    def karten(liste):
        out = []
        for x in liste:
            svg = x["svg"].replace('class="ico"', 'class="prob-ico"')
            out.append(
                f'<li><a class="prob-card" href="{p}{LERNWERKSTATT}#problem={e(x["id"])}">{svg}'
                f'<span><b>{e(x["t"])}</b><small>{e(x["k"])}</small></span><i aria-hidden="true">→</i></a></li>'
            )
        return "\n".join(out)

    return f"""<div class="seg" role="tablist" aria-label="Bereich">
  <button type="button" role="tab" id="tab-job" aria-controls="panel-job" aria-selected="true" data-tab="job">Im Job</button>
  <button type="button" role="tab" id="tab-home" aria-controls="panel-home" aria-selected="false" tabindex="-1" data-tab="home">Zu Hause</button>
</div>
<ul class="prob-list" id="panel-job" role="tabpanel" aria-labelledby="tab-job" data-limit="6">
{karten(d["job"])}
</ul>
<ul class="prob-list" id="panel-home" role="tabpanel" aria-labelledby="tab-home" hidden>
{karten(d["home"])}
</ul>
<button type="button" class="link-button" data-show-all="panel-job" hidden>Alle anzeigen</button>"""


def baustein_kanaele(p):
    return '<ul class="channels">\n' + "\n".join(
        f'  <li><a class="channel" href="{url}" rel="noopener"><span class="channel-icon">{ICON[k]}</span>'
        f'<span class="channel-text"><strong>{name}</strong><small>{text}</small></span></a></li>'
        for k, name, text, url in KANAELE
    ) + "\n</ul>"


def baustein_newsletter(p):
    return f"""<div class="newsletter">
  <div class="newsletter-text">
    <h2 id="newsletter-titel">Den Montags-Wurm per E-Mail</h2>
    <p>Jeden Montag in deinem Postfach. Du bekommst erst eine Bestätigungsmail, abmelden geht jederzeit mit einem Klick.</p>
  </div>
  <a class="button" href="{BREVO}" rel="noopener">Kostenlos abonnieren {ICON["pfeil"]}</a>
</div>"""


def baustein_medien(p):
    d = json.load(open(os.path.join(DATEN, "medien.json"), encoding="utf-8"))
    kat = d["kategorien"]
    vorhanden = [k for k in kat if any(x["kat"] == k for x in d["lieder"] + d["videos"])]
    chips = ['<button type="button" class="chip" data-kat="" aria-pressed="true">Alle</button>'] + [
        f'<button type="button" class="chip" data-kat="{k}" aria-pressed="false">{e(kat[k])}</button>' for k in vorhanden
    ]
    zeilen = []
    for x in d["lieder"]:
        zeilen.append(
            f'<li data-art="lied" data-kat="{x["kat"]}"><a class="media-row" href="https://suno.com/song/{e(x["id"])}" rel="noopener">'
            f'<span class="media-icon">{ICON["suno"]}</span><span class="media-text"><b>{e(x["titel"])}</b>'
            f'<small>Lied auf Suno · {e(kat.get(x["kat"], ""))}</small></span><i aria-hidden="true">→</i></a></li>'
        )
    for x in d["videos"]:
        art = "Kurzvideo" if x.get("art") == "s" else "Video"
        url = f'https://www.youtube.com/shorts/{x["id"]}' if x.get("art") == "s" else f'https://www.youtube.com/watch?v={x["id"]}'
        zeilen.append(
            f'<li data-art="video" data-kat="{x["kat"]}"><a class="media-row" href="{e(url)}" rel="noopener">'
            f'<span class="media-icon">{ICON["youtube"]}</span><span class="media-text"><b>{e(x["titel"])}</b>'
            f'<small>{art} auf YouTube · {e(kat.get(x["kat"], ""))}</small></span><i aria-hidden="true">→</i></a></li>'
        )
    return f"""<div class="media-tools">
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
<p class="search-empty" id="medienleer" hidden>Nichts gefunden. Versuch es mit einem anderen Wort oder Thema.</p>"""


def baustein_ausgaben(p):
    d = json.load(open(os.path.join(DATEN, "ausgaben.json"), encoding="utf-8"))
    out = []
    for i, a in enumerate(d):
        neu = '<span class="pill">Neu</span>' if i == 0 else ""
        out.append(
            f'<li><a class="issue-card" href="{p}montags-wurm/{a["pfad"]}/"><span class="issue-date">{e(a["datum"])} {neu}</span>'
            f'<b>{e(a["titel"])}</b><small>{e(a["teaser"])}</small></a></li>'
        )
    return '<ul class="issue-list">\n' + "\n".join(out) + "\n</ul>"


def baustein_neueste(p):
    a = json.load(open(os.path.join(DATEN, "ausgaben.json"), encoding="utf-8"))[0]
    return (f'<a class="mini-card" href="{p}montags-wurm/{a["pfad"]}/"><small>Neueste Ausgabe vom {e(a["datum"])}</small>'
            f'<strong>{e(a["titel"])}</strong></a>')


BAUSTEINE = {
    "probleme": baustein_probleme,
    "kanaele": baustein_kanaele,
    "newsletter": baustein_newsletter,
    "medien": baustein_medien,
    "ausgaben": baustein_ausgaben,
    "neueste": baustein_neueste,
}


def bauen():
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
        inhalt = seite["inhalt"].replace("{{p}}", p).replace("{{lernwerkstatt}}", p + LERNWERKSTATT)
        for k, f in BAUSTEINE.items():
            if "{{" + k + "}}" in inhalt:
                inhalt = inhalt.replace("{{" + k + "}}", f(p))
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


if __name__ == "__main__":
    bauen()
