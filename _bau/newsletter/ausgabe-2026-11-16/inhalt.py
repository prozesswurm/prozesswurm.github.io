# Inhalt: Der Montags-Wurm – 16. November 2026 (neu geschrieben, keine vereinbarte Fassung gefunden)
DATUM = "16. November 2026"
KW = "KW 47"
TITEL = "Der Montags-Wurm – 16. November 2026"
UNTERTITEL = "Hast du mal kurz?"
SLUG = "16-november-2026"
BILD_ORDNER = "2026-11-16"  # Bilder liegen unter https://www.prozesswurm.de/newsletter/<BILD_ORDNER>/
HEUTE_DRIN = "1. Die Ruhe-Stunde · 2. KI mit Not-Aus · 3. Drei Zahlen · 4. ARTE-Tipp · 5. Lernwerkstatt · 6. Kurzvideo der Woche · 7. Ein Satz zum Mitnehmen"
AUSGABE_URL = "https://www.prozesswurm.de/montags-wurm/16-november-2026/"
APP = "https://www.prozesswurm.de/lernwerkstatt"
WEB = "https://www.prozesswurm.de/"

L_YOUGOV = ("Dashöfer über YouGov für Satellite Office, 23.7.2026", "https://www.dashoefer.de/newsletter/artikel/aktuelle-yougov-studie-von-satellite-office-zeigt-das-buero-hat-kein-anwesenheits-sondern-konzentrationsproblem.html")
L_STARKER = ("Personalwirtschaft über die Studie von Starker u. a., 11.9.2022", "https://www.personalwirtschaft.de/news/hr-organisation/arbeitsunterbrechungen-verursachen-jaehrlich-114-milliarden-euro-kosten-142087/")
L_NOTAUS = ("Bitkom, 10.11.2026", "https://www.bitkom.org/Presse/Presseinformation/Deutsche-wuenschen-sich-mehr-KI-Sicherheit")
L_KIDE = ("Bitkom, 2.11.2026", "https://www.bitkom.org/Presse/Presseinformation/Digital-Gipfel-Unternehmen-wollen-KI-aus-Deutschland")
L_ARTE = "https://www.arte.tv/de/videos/121326-017-A/verliert-unser-gehirn-den-fokus/"
L_VIDEO = "https://www.youtube.com/shorts/yz38a2zIz6s"
L_HOEREN = "https://www.prozesswurm.de/hoeren-und-sehen/"

def a(t, u): return f'<a href="{u}">{t}</a>'

EINSTIEG = [
 ("p", "<b>SALVE!</b> „Hast du mal kurz?“ Drei Wörter, und der Gedanke ist weg. Ob im Büro, in der Praxis oder in der Werkstatt: Wer ständig unterbrochen wird, fängt jeden Tag dutzende Male von vorn an. Diese Woche geht es darum, wie ein Team Ruhe in den Tag bringt, ohne dass jemand unerreichbar wird."),
 ("kud", "Unterbrechen ist bei mir keine Störung. Das ist mein Arbeitsablauf."),
]

ABSCHNITTE = [
 dict(nr=1, name="Aktuelles aus dem Prozessmanagement", headline="Hast du mal kurz? Warum jede kleine Frage länger dauert", blocks=[
  ("img", "titel.jpg", "Der Prozesswurm prüft mit zwei Lupen eine Stoppuhr und einen Briefumschlag, Doktor Kuddelmuddel starrt mit einer riesigen Lupe ins Leere.", "Wo geht die Zeit hin? Der Prozesswurm schaut genau hin."),
  ("p", "Im Sommer hat das Meinungsforschungsinstitut YouGov im Auftrag eines Anbieters von Büroflächen 965 Büroangestellte befragt. 28 Prozent sagen: Eine ganze Stunde am Stück ungestört arbeiten, das schaffen sie nicht. Bei den Frauen sind es 31 Prozent, bei den Männern 24 Prozent. Knapp jeder Dritte fühlt sich oft oder sehr oft gestört."),
  ("p", "Spannend ist, was stört. Nicht in erster Linie das Handy oder der Chat, die nennen nur 15 Prozent. Vorne liegen Telefonate und Videoanrufe (34 Prozent), Gespräche anderer (33 Prozent) und spontane Unterbrechungen (28 Prozent). Also Menschen. Meistens nette Menschen mit einer kurzen Frage."),
  ("h3", "Was das mit deinen Abläufen zu tun hat"),
  ("p", "Eine Unterbrechung kostet mehr als die zwei Minuten für die Antwort. Danach muss der Kopf den Faden wiederfinden. Eine Tagebuchstudie mit 637 Beschäftigten aus 25 Unternehmen hat das 2022 gemessen: Wissensarbeit wurde rund 15 Mal pro Stunde unterbrochen. Das Wiederhineinfinden kostete mindestens 15 Prozent der Bearbeitungszeit."),
  ("p", "Viele „kurze Fragen“ sind in Wahrheit Lücken im Ablauf. Wer fragt, wo die Vorlage liegt, wer zuständig ist oder wie der Stand ist, fragt, weil es nirgends steht. Jede Frage, die zweimal kommt, gehört aufgeschrieben. Das ist dasselbe Prinzip wie bei der Einarbeitung neuer Kollegen."),
  ("h3", "Handgriff der Woche: die Ruhe-Stunde"),
  ("img", "hutliste.jpg", "Grafik: Die Ruhe-Stunde in drei Schritten mit Beispieltabelle einer Frageliste.", "Drei Schritte für mehr Ruhe im Team: Stunde festlegen, Fragen sammeln, Wiederholtes aufschreiben."),
  ("ol", [
    "<b>Eine Stunde festlegen.</b> Gemeinsam im Team, jeden Tag zur gleichen Zeit, zum Beispiel von 9 bis 10 Uhr. In dieser Stunde wird nicht gestört, außer es brennt wirklich.",
    "<b>Fragen sammeln statt rufen.</b> Wer in der Ruhe-Stunde eine Frage hat, schreibt sie auf eine gemeinsame Liste. Danach wird alles auf einmal geklärt.",
    "<b>Was zweimal kommt, wird aufgeschrieben.</b> Die Antwort kommt an einen festen Ort, den alle kennen. Dann muss beim nächsten Mal keiner mehr fragen.",
  ]),
  ("h3", "Ruhe ist keine Frage der Raumgröße"),
  ("p", "75 Prozent der Büroangestellten in derselben Umfrage sagen, ein Großraumbüro mit sieben oder mehr Plätzen erschwere konzentriertes Arbeiten. Ruhe muss aber nicht teuer sein: ein Zeichen an der Tür, ein Hinweis im Chat, ein Telefon, das in dieser Zeit eine Kollegin übernimmt. Im Laden oder in der Pflege ist eine ganze Stunde oft nicht drin. Zwanzig Minuten für die Dokumentation, in denen jemand anderes die Klingel übernimmt, helfen auch."),
  ("kud", "Eine Ruhe-Stunde? Dann müsste ich mir meine Fragen ja vorher überlegen. Das ist mir viel zu anstrengend."),
  ("src", [L_YOUGOV, L_STARKER]),
 ]),
 dict(nr=2, name="Märkte und Nachrichten", headline="KI mit Not-Aus, am liebsten aus Deutschland", blocks=[
  ("p", "<b>Bitkom: 92 Prozent wünschen sich einen Not-Aus für alle KI-Systeme.</b> In einer repräsentativen Telefonumfrage unter 1.006 Menschen ab 16 Jahren wollen 92 Prozent, dass sich jede KI abschalten lässt. 85 Prozent wünschen sich strengere Regeln für besonders leistungsfähige KI. Trotzdem sehen 56 Prozent in KI eher eine Chance als ein Risiko. Veröffentlicht am 10. November."),
  ("src", [L_NOTAUS]),
  ("p", "<b>Fast alle Unternehmen hätten gern KI aus Deutschland, aber nicht um jeden Preis.</b> 96 Prozent würden bevorzugt KI von deutschen Anbietern nutzen. 64 Prozent aber nur, wenn sie dafür weder mehr zahlen noch auf Funktionen verzichten müssen. Befragt wurden 603 Unternehmen ab 20 Beschäftigten, veröffentlicht am 2. November zum Digital-Gipfel der Bundesregierung."),
  ("src", [L_KIDE]),
  ("p", "<b>Was das für dich heißt:</b> Ein Not-Aus ist im Grunde nur ein klarer Ablauf für den Notfall: Wer merkt, dass etwas schiefläuft, und wer darf anhalten? Das gilt für KI genauso wie für jede andere Maschine. Und wer neue Werkzeuge einführt, sollte zählen, wie viele es schon gibt. Jedes Programm mehr ist ein Fenster mehr, das sich meldet."),
  ("kud", "Not-Aus? Brauche ich nicht. Mein Chaos läuft auch ohne Strom weiter."),
 ]),
 dict(nr=3, name="Zahlen und Erkenntnisse", headline="Unterbrechungen in Zahlen", blocks=[
  ("img", "zahlen.jpg", "Grafik mit drei Zahlen: 28 Prozent schaffen keine Stunde ohne Störung, 15 Unterbrechungen pro Stunde, 34 Prozent nennen Telefonate und Videoanrufe als Störfaktor.", "Drei Zahlen, eine Frage: Wann arbeitet bei euch jemand am Stück?"),
  ("ul", [
    "<b>28 Prozent</b> der Büroangestellten schaffen keine Stunde am Stück ohne Störung (YouGov für Satellite Office, 965 Büroangestellte, berichtet am 23.7.2026). <i>Heißt:</i> Für mehr als jeden Vierten ist konzentriertes Arbeiten Glückssache.",
    "<b>15 Mal pro Stunde</b> wurde Wissensarbeit im Schnitt unterbrochen, also etwa alle vier Minuten (Starker u. a., 637 Beschäftigte aus 25 Unternehmen, Tagebuchstudie, berichtet am 11.9.2022). <i>Heißt:</i> Wer eine halbe Stunde für eine Aufgabe braucht, fängt rechnerisch sieben Mal neu an.",
    "<b>34 Prozent</b> nennen Telefonate und Videoanrufe als Störfaktor, Benachrichtigungen und Chats nur 15 Prozent (YouGov für Satellite Office, berichtet am 23.7.2026). <i>Heißt:</i> Die größte Ablenkung ist oft nicht das Handy, sondern der Mensch am anderen Ende der Leitung.",
  ]),
  ("src", [L_YOUGOV, L_STARKER]),
  ("kud", "Alle vier Minuten unterbrochen? Das ist doch keine Störung. Das nenne ich gut vernetzt."),
 ]),
 dict(nr=4, name="Sehenswert", headline="Verliert unser Gehirn den Fokus? (ARTE, 28 Min.)", blocks=[
  ("img", "sehenswert.jpg", "Fernsehtipp: ARTE-Wissensmagazin 42 – Die Antwort auf fast alles, Folge Verliert unser Gehirn den Fokus?, 28 Minuten.", None),
  ("p", "Push-Nachrichten, kurze Videos, ständig etwas Neues: Das ARTE-Wissensmagazin „42 – Die Antwort auf fast alles“ fragt, ob unsere Konzentration wirklich schwindet. Oder ob sich unsere Aufmerksamkeit nur an eine Welt voller Reize angepasst hat. Keine Panikmache, sondern ein ruhiger Blick auf eine Frage, die viele umtreibt."),
  ("p", "Warum sich die 28 Minuten lohnen: Wer versteht, wie Aufmerksamkeit funktioniert, plant den Tag anders. Schwierige Aufgaben in die ruhige Zeit, Kleinkram gesammelt danach. In der ARTE-Mediathek, verfügbar bis 14. Dezember 2026."),
  ("btn", "Zur ARTE-Mediathek", L_ARTE),
  ("kud", "Mein Fokus ist nicht verloren. Er ist nur gerade woanders. Wo genau, sage ich dir nach dieser Nachricht."),
 ]),
 dict(nr=5, name="Aus der Lernwerkstatt", headline="Wo geht die Zeit hin?", blocks=[
  ("img", "lernwerkstatt.jpg", "Drei Bildschirme der Lernwerkstatt-App zur Lektion: Start, Zum Merken, Frage.", None),
  ("p", "Zur Ruhe-Stunde passt die Lektion <b>„Zeit- und Informationsanalyse: wo genau hakt es?“</b> aus Stufe B2. Dauer: sieben Minuten. Ein kleiner Auszug:"),
  ("box", "Zum Merken", "Die Zeitanalyse zeigt, wo Zeit verloren geht. Die Informationsanalyse zeigt, wo Informationen hängen bleiben."),
  ("box", "Mini-Übung", "Denk an einen Ablauf. Schreib eine Stelle auf, an der vermutlich am längsten gewartet wird, und eine, an der dieselben Daten mehrmals eingetippt werden."),
  ("box", "Teste dich", "Warum sind bei der Zeitanalyse Ausreißer wichtig? Die Auflösung steht in der Lektion."),
  ("btn", "Lektion öffnen", APP + "/#lektion=k11"),
  ("h3", "Schwarz auf weiß: die Urkunde"),
  ("p", "Jeden Montag wartet auf der Startseite der Lernwerkstatt eine neue Lektion der Woche. Und wer eine Stufe geschafft hat, bekommt eine Abschlussurkunde. Zum Ausdrucken oder mit einem Klick fürs LinkedIn-Profil. Kostenlos und ohne Anmeldung."),
  ("btn", "Zur Lektion der Woche", APP + "/#lektion-der-woche"),
 ]),
 dict(nr=6, name="Lied oder Kurzvideo der Woche", headline="Kurzvideo: Wichtig oder dringend?", blocks=[
  ("img", "lied.jpg", "Kurzvideo der Woche: Wichtig oder dringend?, vom Prozesswurm, auf YouTube.", None),
  ("p", "Das Telefon klingelt, eine Mail blinkt, jemand steht in der Tür. Aber ist das gerade wichtig oder nur dringend? Ein kurzes Video vom Prozesswurm zu genau dieser Frage. Passt zur Ruhe-Stunde: erst das Wichtige, dann der Rest."),
  ("btn", "Video ansehen", L_VIDEO),
  ("p", "Alle Lieder und Videos findest du auf " + a("prozesswurm.de unter „Hören und sehen“", L_HOEREN) + "."),
 ]),
]

ZITAT = dict(
 text="Wer überall ist, ist nirgends.",
 wer="Seneca, römischer Philosoph, im 2. Brief an seinen Freund Lucilius",
 reaktion="Der Prozesswurm nickt: Wer bei jeder Frage sofort springt, ist bei keiner Aufgabe richtig da. Die Ruhe-Stunde schenkt dem Team wenigstens eine Stunde am Tag, in der jeder ganz bei einer Sache ist. Doktor Kuddelmuddel ist stolz: „Überall gleichzeitig? Das nenne ich Präsenz. Dass mich trotzdem nie einer findet, ist ein ganz anderes Thema.“",
 quelle=("The Latin Library, Seneca, Epistulae morales, Buch I, Brief 2", "https://www.thelatinlibrary.com/sen/seneca.ep1.shtml"),
)

SCHLUSS = "Dieser Newsletter erscheint weiterhin jeden Montag. Vielen Dank für deine Zeit. Feedback, Anmerkungen oder Themenvorschläge? Schreib mir gern an info@prozesswurm.de."

# LinkedIn (Fassung B)
LI_ERSTE_ZEILE = "28 Prozent der Büroangestellten schaffen keine Stunde am Stück ohne Störung."
LI_DANACH = "„Hast du mal kurz?“ Drei Wörter, und der Gedanke ist weg. Diese Woche geht es darum, wie ein Team Ruhe in den Tag bringt, ohne dass jemand unerreichbar wird."
LI_FRAGE = "Wie schützt ihr im Team eure ruhige Zeit? Oder gibt es die gar nicht? Schreib es in die Kommentare."
LI_BEGLEIT = ("Mehr als jeder Vierte im Büro schafft keine Stunde am Stück ohne Störung, und die meisten Störungen kommen nicht vom Handy, sondern von Menschen mit einer kurzen Frage. "
 "Im neuen Montags-Wurm zeigt der Prozesswurm die Ruhe-Stunde: Stunde festlegen, Fragen sammeln, Wiederholtes aufschreiben. "
 "Dazu ein ARTE-Tipp zur Frage, ob unser Gehirn den Fokus verliert, und das Kurzvideo „Wichtig oder dringend?“. "
 "Doktor Kuddelmuddel findet, Unterbrechen sei kein Störfaktor, sondern sein Arbeitsablauf.")
LI_TAGS = "#Prozessmanagement #Konzentration #Teamleitung #Büroalltag #Mittelstand"

# Brevo (Fassung C)
BETREFF = "Hast du mal kurz?"
BETREFF_ALT = "Ständig unterbrochen? Die Ruhe-Stunde"
VORSCHAU = "Warum jede kurze Frage länger dauert, die Ruhe-Stunde und ein ARTE-Tipp zum Fokus."

HINWEISE = [
 "Keine vereinbarte Fassung „Montags-Wurm 16. November 2026“ gefunden (Artifact-Liste, Google Drive, Archiv: kein Zweig, kein Hochlade-Ordner), Entwurf neu geschrieben.",
 "Frisch aus den letzten 7 Tagen ist nur die Bitkom-Meldung zum KI-Not-Aus (10.11.2026). Die Bitkom-Meldung zu KI aus Deutschland ist vom 2.11.2026. Die Zahlen zu Unterbrechungen sind älter und mit Datum genannt: YouGov-Umfrage im Auftrag von Satellite Office (einem Anbieter von Büroflächen, also nicht neutral), berichtet von Dashöfer am 23.7.2026; Tagebuchstudie von Starker u. a. (2022), berichtet von Personalwirtschaft am 11.9.2022.",
 "ARTE: arte.tv war von hier aus nicht erreichbar. Link, Länge (28 Min., laut anderer Quelle 27 Min.) und „verfügbar bis 14.12.2026“ stammen aus dem ARTE-Angebot in der ZDF-Mediathek. Bitte vor dem Versand kurz auf arte.tv prüfen.",
 "Kurzvideo „Wichtig oder dringend?“: YouTube ließ sich von hier aus nicht öffnen. Titel und Link stammen aus der Mediathek der Lernwerkstatt (dort der Lektion k10 zugeordnet). Die Beschreibung im Text ist bewusst allgemein gehalten. Bitte das Video vor dem Versand einmal ansehen.",
 "Seneca-Zitat im lateinischen Original geprüft: „Nusquam est qui ubique est.“ (Epistulae morales, Brief 2, Abschnitt 2). Deutsche Übertragung gängig.",
 "Lernwerkstatt: Lektion k11 (Stufe B2), diesmal ist die Urkunde dran (9.11. Feedback, 2.11. Speicherlink).",
]
