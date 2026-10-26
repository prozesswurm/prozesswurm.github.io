# Inhalt: Der Montags-Wurm – 26. Oktober 2026
DATUM = "26. Oktober 2026"
KW = "KW 44"
TITEL = "Der Montags-Wurm – 26. Oktober 2026"
UNTERTITEL = "Viele Hüte, keiner zuständig"
SLUG = "26-oktober-2026"
BILD_ORDNER = "2026-10-26"  # Bilder liegen unter https://prozesswurm.github.io/newsletter/<BILD_ORDNER>/
HEUTE_DRIN = "1. Die Hutliste · 2. Mittelstand und Beauftragte · 3. Drei Zahlen · 4. ARTE-Tipp · 5. Lernwerkstatt · 6. Lied der Woche · 7. Ein Satz zum Mitnehmen"
AUSGABE_URL = "https://www.prozesswurm.de/montags-wurm/26-oktober-2026"
APP = "https://prozesswurm.github.io"

L_OIGER = ("Oiger, 26.10.2026", "https://oiger.de/2026/10/26/wirtschaftsakademie-begruesst-ende-der-beauftragten-orgie/198961")
L_HWK = ("Handwerkskammer Halle", "https://www.hwkhalle.de/bundestag-beschliesst-neuregelung-bei-sicherheitsbeauftragten/")
L_REDWOOD = ("Redwood Software, 22.10.2026", "https://www.prnewswire.com/news-releases/77--der-unternehmen-haben-einen-preis-fur-unkontrollierte-ki-agenten-gezahlt-302916712.html")
L_KFW = ("KfW, 22.10.2026", "https://www.presseportal.de/pm/41193/6375952")
L_DSB = ("Dr. Datenschutz", "https://www.dr-datenschutz.de/faellt-die-pflicht-zum-datenschutzbeauftragten-bis-ende-2026/")
L_DHZ = ("Deutsche Handwerks Zeitung", "https://www.deutsche-handwerks-zeitung.de/123-000-sicherheitsbeauftragte-sollen-wegfallen-369622/")
L_ARTE = "https://www.arte.tv/de/videos/121276-006-A/re-wenn-arbeiter-chefs-werden/"
L_LIED = "https://suno.com/song/295bbf1f-bd81-44c1-929f-5fe933843062"
L_HOEREN = "https://www.prozesswurm.de/h%C3%B6ren-und-sehen"
L_DEMING = ("The Deming Institute", "https://deming.org/a-bad-system-will-beat-a-good-person-every-time/")

def a(t, u): return f'<a href="{u}">{t}</a>'

EINSTIEG = [
 ("p", "<b>SALVE!</b> In manchen Betrieben gibt es mehr Beauftragte als Kaffeetassen. Die Bundesregierung will jetzt ausmisten. Diese Woche geht es darum, warum ein Titel noch keine Zuständigkeit ist und wie du herausfindest, wer bei euch wirklich den Hut aufhat."),
 ("kud", "Ich bin Beauftragter für Beauftragte. Was ich genau mache? Klären wir in der nächsten Besprechung."),
]

ABSCHNITTE = [
 dict(nr=1, name="Aktuelles aus dem Prozessmanagement", headline="Über 70 Arten von Beauftragten, und wer kümmert sich?", blocks=[
  ("img", "titel.jpg", "Der Prozesswurm hängt drei Hüte ordentlich an ihre Haken, Doktor Kuddelmuddel trägt alle drei übereinander.", "Ordnung am Haken, Chaos auf dem Kopf: Der Prozesswurm sortiert die Hüte, Doktor Kuddelmuddel trägt sie alle."),
  ("p", "Datenschutz, Brandschutz, Abfall, Leitern, Druckluft: Für fast alles gibt es in Deutschland eine Beauftragte oder einen Beauftragten. Der Nationale Normenkontrollrat zählt über 70 Arten. Ein mittelständischer Betrieb kann bis zu 50 davon stellen müssen."),
  ("p", "Jetzt wird ausgedünnt. Für Sicherheitsbeauftragte hat der Bundestag schon im Frühjahr entschieden: Pflicht erst ab 50 Beschäftigten statt ab 21. Kleinere Betriebe brauchen nur noch einen, wenn die Gefährdungsbeurteilung eine besondere Gefahr zeigt. Die Bonner Wirtschafts-Akademie sprach am 26. Oktober vom „Ende der Beauftragten-Orgie“."),
  ("h3", "Was das mit deinen Abläufen zu tun hat"),
  ("p", "Ein Beauftragter ist ein Hut. Und ein Hut allein macht noch keinen Ablauf. Oft läuft es so: Frau Meier wird Brandschutzhelferin, weil sie am nächsten am Feuerlöscher sitzt. Was sie tun soll, wann und mit wem, steht nirgends. Der Hut liegt im Schrank, bis es brennt."),
  ("p", "Umgekehrt gilt auch: Fällt eine Pflicht weg, bleibt die Aufgabe. Unfälle sollen trotzdem nicht passieren, Daten trotzdem nicht verloren gehen. Wer Hüte abschafft, muss also klären, wer sich danach kümmert. Sonst hat am Ende keiner mehr einen Hut auf."),
  ("h3", "Handgriff der Woche: die Hutliste"),
  ("img", "hutliste.jpg", "Grafik: Die Hutliste in drei Schritten mit Beispieltabelle.", "Drei Fragen pro Hut: Welches Ergebnis? Wer hat den größten Nutzen? Darf diese Person entscheiden?"),
  ("ol", [
    "<b>Alle Hüte sammeln.</b> Beauftragte, Ansprechpartner und alles, was „immer die Meier macht“.",
    "<b>Pro Hut drei Fragen stellen.</b> Welches Ergebnis soll herauskommen? Wer hat am Ende den größten Nutzen davon? Darf diese Person auch entscheiden?",
    "<b>Aufräumen.</b> Ein Hut ohne Ergebnis fliegt raus. Ein Hut ohne Kopf wird besetzt.",
  ]),
  ("h3", "Auch KI-Agenten brauchen einen Hut"),
  ("p", "Das zweite Thema der Woche passt genau dazu. Der Software-Anbieter Redwood hat 300 Fachleute befragt, veröffentlicht am 22. Oktober. 77 Prozent hatten schon Ärger mit einem KI-Agenten, um den sich niemand richtig gekümmert hat. Ein KI-Agent ist ein Programm, das Aufgaben selbstständig erledigt. Am häufigsten gab es unerwartete Kosten für gemietete Rechenleistung, danach Störungen im Betrieb und Verstöße gegen Regeln. Nur 42 Prozent führen eine zentrale Liste ihrer Agenten. Wichtig: Die Umfrage kommt von einem Anbieter, der solche Lösungen verkauft."),
  ("p", "<b>Der Handgriff:</b> Schreib jeden KI-Helfer mit auf die Hutliste. Eine Zeile pro Agent: Was soll er erledigen, wer hat die 51 Prozent, und wer darf ihn abschalten?"),
  ("kud", "Fünfzig Beauftragte sind doch prima. Wenn etwas schiefgeht, war es garantiert einer von den anderen 49."),
  ("src", [L_OIGER, L_HWK, L_REDWOOD]),
 ]),
 dict(nr=2, name="Märkte und Nachrichten", headline="Mittelstand verdient besser, investiert aber zögerlich", blocks=[
  ("p", "<b>KfW-Mittelstandspanel: Polster ja, Mut nein.</b> Die Förderbank KfW hat am 22. Oktober ihre große Mittelstandsumfrage vorgestellt. Die Betriebe verdienen wieder besser: Im Schnitt blieben 7,5 Prozent vom Umsatz als Gewinn, die Eigenkapitalquote liegt bei 30,7 Prozent. Investiert hat 2025 aber nur 40 Prozent der 3,9 Millionen Mittelständler. Die Neuinvestitionen sanken auf 218 Milliarden Euro, nach Abzug der Preissteigerung ein Minus von 3,7 Prozent. Als Bremse nennen die Betriebe unter anderem die Bürokratie."),
  ("src", [L_KFW]),
  ("p", "<b>Datenschutzbeauftragter: Die 20-Personen-Regel wackelt, gilt aber noch.</b> Bisher braucht jeder Betrieb einen Datenschutzbeauftragten, wenn mindestens 20 Leute ständig mit Personendaten am Rechner arbeiten. Diese deutsche Sonderregel soll fallen. Der Bund will die Änderung bis Ende 2026 auf den Weg bringen. Beschlossen ist sie noch nicht, die Pflicht gilt weiter. Und die europäische Datenschutz-Grundverordnung bleibt sowieso."),
  ("src", [L_DSB, L_OIGER]),
  ("p", "<b>Was das für dich heißt:</b> Weniger Pflichten sind eine Chance, kein Freifahrtschein. Wer jetzt eine Pflicht streicht, sollte vorher in die Hutliste schauen: Welche Aufgabe hängt daran, und wer übernimmt sie?"),
  ("kud", "Keine Pflicht mehr? Prima, dann schaffe ich den Datenschutz gleich mit ab. Spart Papier."),
 ]),
 dict(nr=3, name="Zahlen und Erkenntnisse", headline="Hüte, Pflichten und KI-Agenten in Zahlen", blocks=[
  ("img", "zahlen.jpg", "Grafik mit drei Zahlen: bis zu 50 Beauftragte, 123.000 Sicherheitsbeauftragte, 42 Prozent mit Agenten-Liste.", "Drei Zahlen, eine Frage: Wer kümmert sich wirklich?"),
  ("ul", [
    "<b>Bis zu 50 Beauftragte</b> kann ein mittelständischer Betrieb stellen müssen, sagt der Nationale Normenkontrollrat (zitiert am 26.10.2026). <i>Heißt:</i> Bei so vielen Hüten verliert jeder den Überblick, auch der Chef.",
    "<b>Rund 123.000 Sicherheitsbeauftragte</b> sollen wegfallen, die Wirtschaft soll dadurch rund 135 Millionen Euro im Jahr sparen. So steht es im Konzept des Bundesarbeitsministeriums vom Oktober 2025. <i>Heißt:</i> Die Aufgabe Arbeitsschutz bleibt, sie braucht nur einen klaren Besitzer statt vieler Titel.",
    "<b>42 Prozent</b> der befragten Unternehmen führen eine zentrale Liste ihrer KI-Agenten (Redwood Software, Oktober 2026, 300 Befragte). <i>Heißt:</i> Mehr als die Hälfte weiß nicht genau, welche Agenten bei ihr gerade arbeiten.",
  ]),
  ("src", [L_OIGER, L_DHZ, L_REDWOOD]),
  ("kud", "Eine Liste aller Agenten? Ich führe lieber eine Liste meiner Ausreden. Die ist wenigstens vollständig."),
 ]),
 dict(nr=4, name="Sehenswert", headline="Re: Wenn Arbeiter Chefs werden (ARTE, 31 Min.)", blocks=[
  ("img", "sehenswert.jpg", "Fernsehtipp: ARTE-Reportage Re: Wenn Arbeiter Chefs werden, 31 Minuten.", "Der Fernsehtipp der Woche, verfügbar in der ARTE-Mediathek bis 22. März 2028."),
  ("p", "Eine Wollspinnerei in Lothringen soll schließen. Ein Teil der Belegschaft macht nicht mit, gründet eine Genossenschaft und übernimmt den Betrieb selbst. Die Produktionsleiterin wird dabei ohne Vorbereitung Vorstandsvorsitzende. Plötzlich Prozesse am Hals, und zwar richtig."),
  ("p", "Warum sich die 31 Minuten lohnen: Die Reportage zeigt sehr ehrlich, was passiert, wenn die Hüte neu verteilt werden. Mehr Mitsprache, mehr Schwung, aber auch mehr Druck auf weniger Schultern."),
  ("btn", "Zur ARTE-Mediathek", L_ARTE),
  ("kud", "Alle sind Chef? Endlich kann ich jeden fragen und muss bei keinem nachhaken."),
 ]),
 dict(nr=5, name="Aus der Lernwerkstatt", headline="Wer hat den Hut auf? Die 51-Prozent-Regel", blocks=[
  ("img", "lernwerkstatt.jpg", "Drei Bildschirme der Lernwerkstatt-App: Start der Lektion, Merksatz, Quizfrage.", "So sieht die Lektion in der App aus: Start, Merksatz, drei Fragen."),
  ("p", "Passend zum Thema gibt es in der Prozesswurm Lernwerkstatt die Lektion <b>„Wer hat den Hut auf? Die 51-Prozent-Regel“</b> aus Stufe A2. Dauer: sieben Minuten. Ein kleiner Auszug:"),
  ("box", "Zum Merken", "Wer am Ende den größten Nutzen hat, trägt die Hauptverantwortung. Bildlich: Wer trinkt am Ende die Limonade im Baumhaus?"),
  ("box", "Mini-Übung", "Denk an eine Aufgabe mit mehreren Beteiligten. Schreib auf, wer am Ende den größten Nutzen vom Ergebnis hat. Diese Person hat die 51 Prozent."),
  ("box", "Teste dich", "Bei der Einarbeitung baut die IT den Laptop auf, die Personalabteilung macht den Vertrag. Wer hat die 51 Prozent? Die Auflösung steht in der Lektion."),
  ("btn", "Lektion öffnen", APP + "/#lektion=v07"),
  ("h3", "Neu: die Lektion der Woche"),
  ("img", "lektion-der-woche.jpg", "Der Prozesswurm kocht Kaffee Schritt für Schritt, Doktor Kuddelmuddel kippt Pulver in kaltes Wasser.", "Lektion der Woche: Was ist überhaupt ein Prozess? Der Prozesswurm erklärt es mit der Kaffeemaschine."),
  ("p", "Ab heute zeigt die Lernwerkstatt jeden Montag auf der Startseite eine Lektion der Woche. Den Anfang macht A1: <b>„Was ist überhaupt ein Prozess?“</b> In sechs Minuten erklärt der Prozesswurm am Beispiel Kaffeekochen, was einen Ablauf zum Prozess macht. Wer nur eine Lektion pro Woche schafft, bleibt so trotzdem dran."),
  ("p", "Und wer alle Stufen geschafft hat, bekommt eine Abschlussurkunde zum Herunterladen, auf Wunsch direkt fürs LinkedIn-Profil. Alles kostenlos und ohne Anmeldung."),
  ("btn", "Zur Lektion der Woche", APP + "/#lektion-der-woche"),
 ]),
 dict(nr=6, name="Song oder Short der Woche", headline="Lied: Wer hat den Hut auf?", blocks=[
  ("img", "lied.jpg", "Lied der Woche: Wer hat den Hut auf? vom Prozesswurm, 3:14 Minuten.", None),
  ("p", "Das Lied zur Lektion: Der Prozesswurm erklärt die 51-Prozent-Regel zu Pop mit Clubbeat, mit dem Baumhaus und dem Beispiel aus der Einarbeitung. Passt zur Hutliste, weil es genau die Frage stellt, die diese Woche zählt: Wer trägt das Gewicht?"),
  ("btn", "Lied anhören", L_LIED),
  ("p", "Alle Lieder und Videos findest du auf " + a("prozesswurm.de unter „Hören und sehen“", L_HOEREN) + "."),
 ]),
]

ZITAT = dict(
 text="Ein schlechtes System schlägt jedes Mal einen guten Menschen.",
 wer="W. Edwards Deming (zugeschrieben, Seminar 1993), Vordenker des Qualitätsmanagements",
 reaktion="Der Prozesswurm nickt: Erst die Hüte ordnen, dann über Menschen reden. Doktor Kuddelmuddel atmet auf: „Dann war ich es ja gar nicht. Das System war's. Wie immer.“",
 quelle=L_DEMING,
)

SCHLUSS = "Dieser Newsletter erscheint weiterhin jeden Montag. Vielen Dank für deine Zeit. Feedback, Anmerkungen oder Themenvorschläge? Schreib mir gern an prozesswurm@gmail.com."

# LinkedIn
LI_ERSTE_ZEILE = "Über 70 Arten von Beauftragten, bis zu 50 in einem Betrieb. Und wenn es brennt, fühlt sich trotzdem keiner zuständig."
LI_FRAGE = "Wie viele Hüte gibt es bei euch, und wie viele davon haben einen Kopf? Schreib es in die Kommentare."
LI_BEGLEIT = ("Die Bundesregierung mistet bei den Beauftragten aus. Gut so, aber ein gestrichener Titel löst noch keine Aufgabe. "
 "Im neuen Montags-Wurm zeigt der Prozesswurm die Hutliste: drei Fragen pro Hut, und am Ende weißt du, wer wirklich zuständig ist. "
 "Dazu: warum nur 42 Prozent der Unternehmen eine Liste ihrer KI-Agenten führen. "
 "Doktor Kuddelmuddel ist trotzdem zufrieden: „Ein Hut mehr fällt bei mir gar nicht auf.“")
LI_TAGS = "#Prozessmanagement #Mittelstand #Bürokratieabbau #KI #Verantwortung"

BETREFF = "Viele Hüte, keiner zuständig"
BETREFF_ALT = "50 Beauftragte und trotzdem keiner zuständig"
VORSCHAU = "Die Hutliste in drei Schritten, ein ARTE-Tipp und ein Lied zur 51-Prozent-Regel."
