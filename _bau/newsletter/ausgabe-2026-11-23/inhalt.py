# Inhalt: Der Montags-Wurm – 23. November 2026 (neu geschrieben, keine vereinbarte Fassung gefunden)
DATUM = "23. November 2026"
KW = "KW 48"
TITEL = "Der Montags-Wurm – 23. November 2026"
UNTERTITEL = "Wer macht’s, wenn du weg bist?"
SLUG = "23-november-2026"
BILD_ORDNER = "2026-11-23"  # Bilder liegen unter https://www.prozesswurm.de/newsletter/<BILD_ORDNER>/
HEUTE_DRIN = "1. Der Übergabezettel · 2. Teure Geräte, volle Bücher · 3. Drei Zahlen · 4. ARTE-Tipp · 5. Lernwerkstatt · 6. Lied der Woche · 7. Ein Satz zum Mitnehmen"
AUSGABE_URL = "https://www.prozesswurm.de/montags-wurm/23-november-2026/"
APP = "https://www.prozesswurm.de/lernwerkstatt"
WEB = "https://www.prozesswurm.de/"

L_URLAUB = ("Bitkom, 22.7.2026", "https://www.bitkom.org/Presse/Presseinformation/Zwei-Drittel-im-Urlaub-beruflich-erreichbar")
L_SPEICHER = ("Bitkom, 16.11.2026", "https://www.bitkom.org/Presse/Presseinformation/Steigende-Speicherpreise-treffen-deutschen-Wirtschaft")
L_IFO = ("ifo Institut, 20.11.2026", "https://www.ifo.de/fakten/2026-11-20/geschaeftsklima-im-maschinenbau-verbessert")
L_ARTE = "https://www.arte.tv/de/videos/127468-001-A/ist-urlaub-wirklich-erholung/"
L_LIED = "https://suno.com/song/c7d90693-18ea-4ac0-93b2-b06fdd65a6c5"
L_HOEREN = "https://www.prozesswurm.de/hoeren-und-sehen/"

def a(t, u): return f'<a href="{u}">{t}</a>'

EINSTIEG = [
 ("p", "<b>SALVE!</b> Bald ist Dezember. Resturlaub, Brückentage, Betriebsferien. Und irgendwo klingelt ein Telefon am Strand oder unterm Weihnachtsbaum, weil im Betrieb keiner weiß, wo das Angebot liegt. Diese Woche geht es darum, wie du so übergibst, dass du im Urlaub wirklich weg sein kannst."),
 ("kud", "Übergabe? Ich nehme mein Wissen lieber mit in den Urlaub. Dann freuen sich alle umso mehr, wenn ich zurückkomme."),
]

ABSCHNITTE = [
 dict(nr=1, name="Aktuelles aus dem Prozessmanagement", headline="Wer macht’s, wenn du weg bist?", blocks=[
  ("img", "titel.jpg", "Der Prozesswurm spielt einem Mitspieler den Ball genau in den Lauf. Daneben stolpert Doktor Kuddelmuddel über drei Bälle gleichzeitig.", "Der Pass muss ankommen. Im Fußball wie bei der Übergabe vor dem Urlaub."),
  ("p", "Im Sommer hat der Digitalverband Bitkom Berufstätige gefragt, ob sie im Urlaub für die Arbeit erreichbar sind. Zwei Drittel sagen ja: 66 Prozent. Das ist seit Jahren fast gleich, 2025 waren es 67 Prozent, 2024 auch 66. Die meisten lesen Kurznachrichten oder gehen ans Telefon."),
  ("p", "Spannend ist das Warum. Nur 16 Prozent der Erreichbaren tun es aus eigenem Antrieb. 53 Prozent sagen, die Kolleginnen und Kollegen erwarten es. 47 Prozent nennen die Vorgesetzten, 34 Prozent die Kundschaft."),
  ("h3", "Was das mit deinen Abläufen zu tun hat"),
  ("p", "Wenn Kollegen anrufen, dann meistens nicht aus Bosheit. Sie rufen an, weil sie nicht weiterwissen. Das Wissen steckt in einem einzigen Kopf, und dieser Kopf liegt gerade in der Sonne. Das ist kein Charakterfehler, sondern eine Lücke im Ablauf. Dieselbe Lücke, um die es im Oktober bei der Frage ging, wer eigentlich den Hut auf hat."),
  ("p", "Eine gute Übergabe ist wie ein Pass im Fußball: Sie zählt erst, wenn sie ankommt. Ein Zettel, den keiner findet, ist kein Pass. Eine Vertretung, die nicht weiß, was sie entscheiden darf, auch nicht."),
  ("h3", "Handgriff der Woche: der Übergabezettel"),
  ("img", "hutliste.jpg", "Grafik: Der Übergabezettel in drei Schritten (Offenes aufschreiben, Übergeben, Bescheid sagen) mit einer Beispieltabelle.", "Drei Schritte, bevor du gehst: aufschreiben, übergeben, Bescheid sagen."),
  ("ol", [
    "<b>Offenes aufschreiben.</b> Eine Zeile pro Vorgang: Was läuft gerade, was wird fällig, wo liegen die Unterlagen? Am besten eine Woche vorher, nicht am letzten Nachmittag.",
    "<b>Übergeben.</b> Zu jedem Vorgang ein Name. Dann eine Viertelstunde gemeinsam durchgehen, solange du noch da bist. Und klären: Was darf die Vertretung selbst entscheiden?",
    "<b>Bescheid sagen.</b> Eine Abwesenheitsnotiz mit Rückkehrdatum und Ansprechperson. Wer dir schreibt, weiß dann sofort, an wen er sich wenden kann.",
  ]),
  ("h3", "Die Pflege macht es seit Jahren vor"),
  ("p", "In Krankenhaus und Pflegeheim ist die Übergabe Alltag: Bei jedem Schichtwechsel wird gesagt, was los war und worauf die nächste Schicht achten muss. Im Büro, im Laden oder in der Werkstatt passiert das oft nur zweimal im Jahr, vor dem großen Urlaub. Dabei hilft derselbe Zettel auch, wenn jemand ganz plötzlich krank wird. Wer ihn laufend pflegt, muss vor dem Urlaub nur noch nachschauen."),
  ("kud", "Ein Übergabezettel? Dann könnte ja jemand anderes meine Arbeit machen. Und am Ende merkt keiner, dass ich weg war."),
  ("src", [L_URLAUB]),
 ]),
 dict(nr=2, name="Märkte und Nachrichten", headline="Teure Geräte, volle Auftragsbücher", blocks=[
  ("p", "<b>Drei von vier Unternehmen zahlen mehr für IT.</b> Weil Speicherchips teurer geworden sind, haben 75 Prozent der Unternehmen in den letzten zwölf Monaten mehr für Computer und andere IT-Ausstattung bezahlt. Von diesen nutzen 69 Prozent ihre Geräte jetzt länger, 48 Prozent verschieben geplante Anschaffungen. Befragt wurden 603 Unternehmen ab 20 Beschäftigten, veröffentlicht am 16. November."),
  ("src", [L_SPEICHER]),
  ("p", "<b>Der Maschinenbau schöpft Hoffnung.</b> Das Geschäftsklima im deutschen Maschinenbau ist laut ifo Institut auf 7,6 Punkte gestiegen, nach 4,1 im September. Die Lage wird erstmals seit dem Winter 2023 wieder positiv bewertet, die Auftragsbücher füllen sich den vierten Monat in Folge. Neue Stellen planen die Firmen aber noch nicht: Die Beschäftigungserwartungen bleiben im Minus. Veröffentlicht am 20. November."),
  ("src", [L_IFO]),
  ("p", "<b>Was das für dich heißt:</b> Wenn Geräte länger halten müssen, lohnt sich eine einfache Liste: Welches Gerät, wie alt, wer kümmert sich darum? Und wenn mehr Aufträge kommen, aber nicht mehr Leute, muss dasselbe Team mehr schaffen. Dann kostet jede holprige Übergabe doppelt."),
  ("kud", "Geräte länger nutzen? Mein Drucker ist von 2011. Das nenne ich nicht sparen. Das nenne ich Treue."),
 ]),
 dict(nr=3, name="Zahlen und Erkenntnisse", headline="Urlaub mit Handy in der Tasche", blocks=[
  ("img", "zahlen.jpg", "Grafik mit drei Zahlen: 66 Prozent waren im Sommerurlaub erreichbar, 53 Prozent der Erreichbaren sagen, die Kollegen erwarten es, 75 Prozent der Unternehmen zahlen mehr für IT-Geräte.", "Drei Zahlen, eine Frage: Wer ruft bei dir im Urlaub an, und warum?"),
  ("ul", [
    "<b>66 Prozent</b> der Berufstätigen mit Sommerurlaub waren dort beruflich erreichbar (Bitkom Research, 358 Berufstätige, telefonisch befragt, veröffentlicht am 22.7.2026). <i>Heißt:</i> Für zwei von drei Menschen ist Urlaub nur ein Ortswechsel.",
    "<b>53 Prozent</b> der Erreichbaren sagen, die Kolleginnen und Kollegen erwarten das, nur 16 Prozent tun es aus eigenem Antrieb (Bitkom Research, 22.7.2026). <i>Heißt:</i> Der Druck kommt selten vom Chef allein, sondern aus dem Team, das ohne dich nicht weiterweiß.",
    "<b>75 Prozent</b> der Unternehmen haben in den letzten zwölf Monaten mehr für IT-Geräte bezahlt (Bitkom Research, 603 Unternehmen ab 20 Beschäftigten, veröffentlicht am 16.11.2026). <i>Heißt:</i> Wer weiß, welche Geräte er hat und wie alt sie sind, kann besser planen als einer, der erst beim Ausfall nachschaut.",
  ]),
  ("src", [L_URLAUB, L_SPEICHER]),
  ("kud", "Zwei Drittel erreichbar? Ich gehe im Urlaub auch immer ran. Ich sage dann nur, dass ich gerade nichts weiß."),
 ]),
 dict(nr=4, name="Sehenswert", headline="Ist Urlaub wirklich Erholung? (ARTE, 29 Min.)", blocks=[
  ("img", "sehenswert.jpg", "Fernsehtipp: ARTE-Wissensmagazin 42 – Die Antwort auf fast alles, Folge Ist Urlaub wirklich Erholung?, 29 Minuten.", None),
  ("p", "Urlaub erholt. Das glauben fast alle. Das ARTE-Wissensmagazin „42 – Die Antwort auf fast alles“ zeigt, dass die Forschung da weniger sicher ist, als man denkt. Was im Körper passiert, wenn wir uns erholen, ist noch gar nicht genau verstanden. Und ob der Urlaub hilft oder nur die Pause davor, ist offen."),
  ("p", "Warum sich die 29 Minuten lohnen: Wer versteht, wovon Erholung abhängt, plant den Urlaub anders. Zum Beispiel so, dass das Telefon gar nicht erst klingeln muss. In der ARTE-Mediathek, verfügbar bis 24. Mai 2027."),
  ("btn", "Zur ARTE-Mediathek", L_ARTE),
  ("kud", "Ich erhole mich im Urlaub prima. Ich warte auf Anrufe aus dem Büro. Wenigstens die kommen zuverlässig."),
 ]),
 dict(nr=5, name="Aus der Lernwerkstatt", headline="Der Pass zählt mehr als der Star", blocks=[
  ("img", "lernwerkstatt.jpg", "Drei Bildschirme der Lernwerkstatt-App zur Lektion: Start, Zum Merken, Frage.", None),
  ("p", "Zum Übergabezettel passt die Lektion <b>„Was der Fußball über gute Prozesse lehrt“</b> aus Stufe B1. Dauer: sieben Minuten. Ein kleiner Auszug:"),
  ("box", "Zum Merken", "Der Pass zählt mehr als der Star."),
  ("box", "Mini-Übung", "Schau dir eine Übergabe zwischen zwei Abteilungen oder Personen an. Schreib auf, ob geregelt ist, wer wann was übergibt, oder ob es per Zuruf läuft."),
  ("box", "Teste dich", "Was ist laut Lektion wichtiger als einzelne Stars? Die Auflösung steht in der Lektion."),
  ("btn", "Lektion öffnen", APP + "/#lektion=v08"),
  ("h3", "Dein Fortschritt fährt mit in den Urlaub: der Speicherlink"),
  ("p", "Jeden Montag wartet auf der Startseite der Lernwerkstatt eine neue Lektion der Woche. Und wer zwischen den Jahren lieber auf dem Sofa als am Schreibtisch lernt: Unter „Fortschritt mitnehmen“ tippst du auf „Speicherlink kopieren“ und schickst dir den Link selbst. Auf dem anderen Gerät öffnen, und dein Stand ist wieder da. Kostenlos und ohne Anmeldung."),
  ("btn", "Zur Lektion der Woche", APP + "/#lektion-der-woche"),
 ]),
 dict(nr=6, name="Lied oder Kurzvideo der Woche", headline="Lied: Vom Suchen zum Finden", blocks=[
  ("img", "lied.jpg", "Lied der Woche: Vom Suchen zum Finden, vom Prozesswurm, auf Suno.", None),
  ("p", "Ordner, Unterordner, drei Excel-Listen mit fast demselben Namen: Wer etwas sucht, fragt am Ende doch wieder den Kollegen. Im Lied „Vom Suchen zum Finden“ hat die Sucherei ein Ende, weil das Wissen an einem Ort liegt, den alle kennen. Mit Reggae und Ska, gut für einen grauen Novembermorgen. Und genau das, was eine Vertretung braucht."),
  ("btn", "Lied anhören", L_LIED),
  ("p", "Alle Lieder und Videos findest du auf " + a("prozesswurm.de unter „Hören und sehen“", L_HOEREN) + "."),
 ]),
]

ZITAT = dict(
 text="Wer sich nicht vorbereitet, bereitet sich auf das Scheitern vor.",
 wer="Benjamin Franklin (zugeschrieben), amerikanischer Erfinder und Staatsmann",
 reaktion="Der Prozesswurm nickt: Eine Übergabe ist Vorbereitung für jemand anderen. Wer sie eine Woche vorher macht, hat im Urlaub Ruhe, und die Vertretung auch. Doktor Kuddelmuddel winkt ab: „Ich bereite mich nie vor. Dann kann mich auch nichts überraschen. Außer allem.“",
 quelle=("Quote Investigator zur Herkunft des Spruchs", "https://quoteinvestigator.com/2018/07/08/plan/"),
)

SCHLUSS = "Dieser Newsletter erscheint weiterhin jeden Montag. Vielen Dank für deine Zeit. Feedback, Anmerkungen oder Themenvorschläge? Schreib mir gern an info@prozesswurm.de."

# LinkedIn (Fassung B)
LI_ERSTE_ZEILE = "Zwei Drittel der Berufstätigen sind im Urlaub für die Arbeit erreichbar. Meistens, weil das Team sonst nicht weiterweiß."
LI_DANACH = "Bald ist Dezember, und mit ihm Resturlaub, Brückentage und Betriebsferien. Diese Woche geht es darum, wie du so übergibst, dass du im Urlaub wirklich weg sein kannst."
LI_FRAGE = "Wie übergebt ihr im Team vor dem Urlaub? Mit Zettel, mit Besprechung oder gar nicht? Schreib es in die Kommentare."
LI_BEGLEIT = ("66 Prozent der Berufstätigen waren im Sommerurlaub erreichbar, und mehr als die Hälfte von ihnen, weil Kolleginnen und Kollegen es erwarten. "
 "Im neuen Montags-Wurm zeigt der Prozesswurm den Übergabezettel: Offenes aufschreiben, übergeben, Bescheid sagen. "
 "Dazu ein ARTE-Tipp zur Frage, ob Urlaub wirklich erholt, und das Lied „Vom Suchen zum Finden“. "
 "Doktor Kuddelmuddel nimmt sein Wissen lieber mit in den Urlaub.")
LI_TAGS = "#Prozessmanagement #Urlaubsvertretung #Teamleitung #Wissensmanagement #Mittelstand"

# Brevo (Fassung C)
BETREFF = "Wer macht’s, wenn du weg bist?"
BETREFF_ALT = "Urlaub ohne Anrufe: der Übergabezettel"
VORSCHAU = "Warum im Urlaub das Telefon klingelt, der Übergabezettel und ein ARTE-Tipp."

HINWEISE = [
 "Keine vereinbarte Fassung „Montags-Wurm 23. November 2026“ gefunden (Artifact-Liste, Google Drive, Archiv: kein Zweig, kein Hochlade-Ordner), Entwurf neu geschrieben.",
 "Frisch aus den letzten 7 Tagen: Bitkom zu Speicherpreisen (16.11.2026) und ifo zum Maschinenbau (20.11.2026). Die Zahlen zur Erreichbarkeit im Urlaub sind älter (Bitkom, 22.7.2026) und mit Datum genannt. Die ifo-Seite nennt keine Stichprobengröße.",
 "ARTE: arte.tv war von hier aus nicht erreichbar. Link (aus den Seitendaten), Länge 29 Min. und „verfügbar bis 24.5.2027“ stammen aus dem ARTE-Angebot in der ZDF-Mediathek. Bitte vor dem Versand kurz auf arte.tv prüfen.",
 "Lied „Vom Suchen zum Finden“: Suno-Seite gelesen (Prozesswurm-Profil, Reggae/Dub/Ska, Thema: Schluss mit der Suche in Ordnern und Listen, Wissen an einem Ort). Bitte einmal anhören.",
 "Zitat: Der Spruch wird Benjamin Franklin oft zugeschrieben, ein Beleg bei ihm fehlt laut Quote Investigator. Deshalb „(zugeschrieben)“.",
 "Lernwerkstatt: Lektion v08 (Stufe B1), diesmal ist der Speicherlink dran (16.11. Urkunde, 9.11. Feedback).",
]
