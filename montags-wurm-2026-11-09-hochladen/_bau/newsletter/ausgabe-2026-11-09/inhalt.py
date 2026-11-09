# Inhalt: Der Montags-Wurm – 9. November 2026 (neu geschrieben, keine vereinbarte Fassung gefunden)
DATUM = "9. November 2026"
KW = "KW 46"
TITEL = "Der Montags-Wurm – 9. November 2026"
UNTERTITEL = "Lernen, wenn keiner fragt"
SLUG = "09-november-2026"
BILD_ORDNER = "2026-11-09"  # Bilder liegen unter https://www.prozesswurm.de/newsletter/<BILD_ORDNER>/
HEUTE_DRIN = "Doktor Kuddelmuddel warnt · 1. Die Lern-Viertelstunde · 2. Homeoffice und Vorschriften · 3. Drei Zahlen · 4. ARTE-Tipp · 5. Lernwerkstatt · 6. Lied der Woche · 7. Ein Satz zum Mitnehmen"
AUSGABE_URL = "https://www.prozesswurm.de/montags-wurm/09-november-2026/"
APP = "https://www.prozesswurm.de/lernwerkstatt"
WEB = "https://www.prozesswurm.de/"

L_BITKOM_WB = ("Bitkom Akademie, 17.9.2026", "https://www.presseportal.de/pm/180072/6353833")
L_BITKOM_WB2 = ("Bitkom Akademie, Weiterbildungsstudie 2026", "https://bitkom-akademie.de/weiterbildungsstudie-2026")
L_PWC = ("it-daily.net über PwC, 5.10.2026", "https://www.it-daily.net/shortnews/ki-nutzung-steigt")
L_TUEV = ("Haufe über TÜV-Verband, 20.5.2026", "https://www.haufe.de/personal/neues-lernen/tuev-weiterbildungsstudie-2026-zu-ki-weiterbildungen_589614_686216.html")
L_HO = ("Bitkom, 5.11.2026", "https://www.bitkom.org/Presse/Presseinformation/Mehr-als-jedes-zweite-Unternehmen-hat-Homeoffice-seit-Corona-zurueckgefahren")
L_BDA = ("Mittelstand Nachrichten über Forsa für die BDA, 28.10.2026", "https://www.mittelstand-nachrichten.de/aktuell/dts_wirtschaft/forsa-umfrage-fuer-bda-98-prozent-der-unternehmen-spueren-keinen-buerokratie-abbau-53-prozent-melden-sogar-mehr-belastung/")
L_ARTE = "https://www.arte.tv/de/videos/111664-001-A/wie-unser-gehirn-uns-austrickst-1-2/"
L_LIED = "https://suno.com/song/09ea53f7-b624-4d53-9943-45ea1fdf61a3"
L_HOEREN = "https://www.prozesswurm.de/hoeren-und-sehen/"

def a(t, u): return f'<a href="{u}">{t}</a>'

EINSTIEG = [
 ("p", "<b>SALVE!</b> Neue Programme, neue Regeln, neue Kollegen: Gelernt wird im Büro ständig, nur meistens nebenbei und ohne Plan. Fast alle Chefs finden Weiterbildung wichtig, aber kaum einer spricht seine Leute darauf an. Diese Woche geht es darum, wie Lernen in den Alltag passt, ohne dass jemand einen ganzen Tag dafür freinehmen muss."),
]

# Pflichtkasten nur am 9.11.2026 (Wunsch des Betreibers vom 04.11.2026), Text wörtlich
EIGENE_SACHE = dict(stil="kuddel", titel="Achtung: Doktor Kuddelmuddel hat eine Warnung", blocks=[
 ("p", "Diese Woche hat sich Doktor Kuddelmuddel einen Kasten im Montags-Wurm geschnappt. Seine dringende Bitte: Probier die Lernwerkstatt bloß nicht aus. Seine Gründe:"),
 ("ul", [
   "Sie fängt da an, wo es dir wehtut. Du tippst einfach an, was dich gerade nervt.",
   "Sechs Minuten, dann weißt du, was ein Prozess ist.",
   "Fehler sind dort erlaubt. Er kichert nur kurz im Hintergrund.",
   "Am Ende gibt es für jede Stufe eine Urkunde, auf Wunsch direkt fürs LinkedIn-Profil.",
   "Und das Allerschlimmste: kostenlos, ohne Anmeldung, ohne Cookies.",
 ]),
 ("kud", "Ich habe keine Chance."),
 ("wurm", "Hör nicht auf ihn. Fang mit der ersten Lektion an."),
 ("btn", "Erste Lektion starten", APP + "/#lektion=b01"),
])

ABSCHNITTE = [
 dict(nr=1, name="Aktuelles aus dem Prozessmanagement", headline="Weiterbildung: Alle finden sie wichtig, kaum einer fragt nach", blocks=[
  ("img", "titel.jpg", "Der Prozesswurm knabbert in Ruhe kleine Kekse, Doktor Kuddelmuddel beißt verzweifelt in ein dickes Buch mit der Aufschrift Wissen.", "Kleine Häppchen statt dickes Handbuch: So bleibt Wissen hängen."),
  ("p", "Die Bitkom Akademie hat im September ihre Weiterbildungsstudie 2026 vorgestellt. 82 Prozent der befragten Unternehmensleitungen nennen Weiterbildung einen zentralen Hebel für den Umbau ihres Betriebs. Bei den Beschäftigten kommt davon wenig an: Nur 21 Prozent werden von ihrer Führungskraft aktiv auf Weiterbildung angesprochen. Nur 24 Prozent haben Arbeitszeiten, in denen Lernen überhaupt vorgesehen ist. Befragt wurden 84 Unternehmensleitungen und rund 1.300 Berufstätige, nicht repräsentativ."),
  ("p", "Gleichzeitig wächst der Lernstoff. 73 Prozent der Berufstätigen nutzen laut derselben Studie KI bei der Arbeit, vor einem Jahr waren es 64 Prozent. Und 45 Prozent der Unternehmensleitungen geben zu, dass ihr Geld eher in Technik fließt als in die Menschen, die sie bedienen sollen."),
  ("h3", "Was das mit deinen Abläufen zu tun hat"),
  ("p", "Ein neues Programm ohne Einarbeitung ist wie ein neuer Ablauf, den keiner kennt. Dann entsteht, was du aus dem Büro kennst: Jeder findet seinen eigenen Weg, und nach drei Monaten gibt es fünf Arten, dieselbe Sache zu erledigen. Lernen ist deshalb kein Extra, sondern Teil des Ablaufs. Genau wie bei der Einarbeitung neuer Kollegen."),
  ("p", "Das Gute: Es braucht dafür keinen Schulungstag. Wissen bleibt besser hängen, wenn es in kleinen Stücken kommt und regelmäßig wiederholt wird. Das kennt jeder, der mal mit einer Sprach-App Vokabeln gelernt hat."),
  ("h3", "Handgriff der Woche: die Lern-Viertelstunde"),
  ("img", "hutliste.jpg", "Grafik: Die Lern-Viertelstunde in drei Schritten mit Beispieltabelle.", "Drei Schritte für eine feste Lernzeit im Team: Frage sammeln, Termin setzen, selbst ausprobieren."),
  ("ol", [
    "<b>Eine Frage pro Woche sammeln.</b> Was wurde diese Woche zweimal gefragt? Das ist das Thema.",
    "<b>Fünfzehn Minuten fest einplanen.</b> Gleicher Tag, gleiche Uhrzeit, als Termin im Kalender. Nicht „wenn mal Zeit ist“.",
    "<b>Einer zeigt es, alle probieren es.</b> Wer es kann, macht es einmal vor. Danach macht es jeder einmal selbst, Fehler eingeschlossen.",
  ]),
  ("h3", "Menschen lernen lieber von Menschen"),
  ("p", "Eine Zahl aus der Studie macht Mut: 84 Prozent der Berufstätigen würden für ihre nächste Weiterbildung lieber eine Person wählen, die sich auskennt. Die sitzt oft im Nachbarbüro. Wer im Team regelmäßig voneinander lernt, hält das Wissen im Haus, auch wenn jemand in Rente geht."),
  ("kud", "Weiterbilden? Ich war 2009 auf einer Schulung. Seitdem weiß ich alles. Vor allem, wo der Kaffee steht."),
  ("src", [L_BITKOM_WB, L_BITKOM_WB2]),
 ]),
 dict(nr=2, name="Märkte und Nachrichten", headline="Weniger Homeoffice, mehr Vorschriften", blocks=[
  ("p", "<b>Bitkom: Mehr als jedes zweite Unternehmen hat das Homeoffice zurückgefahren.</b> 56 Prozent der Unternehmen ab 20 Beschäftigten bieten heute weniger Homeoffice an als vor fünf Jahren, 17 Prozent haben es ganz abgeschafft. 65 Prozent meinen, durch Homeoffice gehe der Zusammenhalt verloren. Gleichzeitig sagen 63 Prozent, ohne Homeoffice finde man schwerer gute Leute. Befragt wurden 603 Unternehmen, veröffentlicht am 5. November."),
  ("src", [L_HO]),
  ("p", "<b>Bürokratieabbau kommt in den Betrieben nicht an.</b> In einer Forsa-Umfrage für die Bundesvereinigung der Deutschen Arbeitgeberverbände (BDA) sagen 53 Prozent der Unternehmen, die Belastung durch Vorschriften sei gestiegen. 45 Prozent merken keinen Unterschied. Zu viele Vorschriften gelten als größtes Risiko, noch vor Arbeitskosten und Energiepreisen. Befragt wurden 1.006 Unternehmen ab 10 Beschäftigten, berichtet am 28. Oktober."),
  ("src", [L_BDA]),
  ("p", "<b>Was das für dich heißt:</b> Ob im Büro oder zu Hause, Wissen wandert nicht von allein von Kopf zu Kopf. Wer weniger nebeneinander sitzt, braucht feste Gelegenheiten zum Fragen. Und wer mit immer mehr Vorschriften umgehen muss, braucht kurze, klare Erklärungen statt dicker Ordner."),
  ("kud", "Zurück ins Büro? Prima. Dann kann ich die Leute wieder persönlich durcheinanderbringen. Per Videoanruf hat das nie so richtig geklappt."),
 ]),
 dict(nr=3, name="Zahlen und Erkenntnisse", headline="Lernen im Job in Zahlen", blocks=[
  ("img", "zahlen.jpg", "Grafik mit drei Zahlen: 21 Prozent werden von der Führungskraft auf Weiterbildung angesprochen, 51 Prozent haben Zugang zu Weiterbildung, 27 Prozent der Unternehmen haben zu KI geschult.", "Drei Zahlen, eine Frage: Wann lernt bei euch eigentlich wer?"),
  ("ul", [
    "<b>21 Prozent</b> der Beschäftigten werden von ihrer Führungskraft aktiv auf Weiterbildung angesprochen (Bitkom Akademie, 17.9.2026, nicht repräsentativ). <i>Heißt:</i> Wer auf eine Einladung wartet, wartet oft lange.",
    "<b>51 Prozent</b> der Beschäftigten weltweit haben Zugang zu Weiterbildung, ein Jahr zuvor waren es 59 Prozent. Im selben Zeitraum stieg die Nutzung von KI bei der Arbeit auf 64 Prozent (PwC, rund 49.000 Befragte, berichtet am 5.10.2026). <i>Heißt:</i> Die Werkzeuge kommen schneller als das Wissen, wie man sie gut benutzt.",
    "<b>27 Prozent</b> der Unternehmen haben ihre Leute im Umgang mit KI geschult, 2024 waren es 12 Prozent. 45 Prozent sehen keinen Bedarf (TÜV-Verband, rund 500 Unternehmen, berichtet am 20.5.2026). <i>Heißt:</i> Es wird mehr, aber die meisten bringen es sich immer noch selbst bei.",
  ]),
  ("src", [L_BITKOM_WB, L_PWC, L_TUEV]),
  ("kud", "Ich frage nie nach. Wer nichts weiß, kann auch nichts falsch machen. Behaupte ich jedenfalls seit Jahren."),
 ]),
 dict(nr=4, name="Sehenswert", headline="Wie unser Gehirn uns austrickst: Mein Hirn und ich (ARTE, 53 Min.)", blocks=[
  ("img", "sehenswert.jpg", "Fernsehtipp: ARTE-Dokumentation Wie unser Gehirn uns austrickst, Teil 1: Mein Hirn und ich, 53 Minuten.", None),
  ("p", "Der Neurowissenschaftler Albert Moukheiber zeigt mit Experimenten und Zaubertricks, wie oft unser Kopf uns etwas vormacht. Was wir wahrnehmen, ist nicht immer das, was passiert. Denkfehler schleichen sich ein, ohne dass wir es merken. Teil 2 „Mein Hirn und die anderen“ (54 Minuten) zeigt, wie stark uns andere Menschen beim Denken beeinflussen."),
  ("p", "Warum sich die 53 Minuten lohnen: Wer weiß, wie das Gehirn tickt, versteht, warum ein Fehler kein Drama ist, sondern zum Lernen dazugehört. Und warum „Das haben wir immer so gemacht“ sich so richtig anfühlt, auch wenn es falsch ist. In der ARTE-Mediathek."),
  ("btn", "Zur ARTE-Mediathek", L_ARTE),
  ("kud", "Mein Gehirn trickst mich nicht aus. Wir haben eine Abmachung: Es macht, was es will, und ich nenne das Erfahrung."),
 ]),
 dict(nr=5, name="Aus der Lernwerkstatt", headline="Wissen häppchenweise lernen", blocks=[
  ("img", "lernwerkstatt.jpg", "Drei Bildschirme der Lernwerkstatt-App zur Lektion: Start, Zum Merken, Frage.", None),
  ("p", "Zur Lern-Viertelstunde passt die Lektion <b>„Wissen häppchenweise lernen: der Babbel-Effekt“</b> aus Stufe A1. Dauer: sechs Minuten. Ein kleiner Auszug:"),
  ("box", "Zum Merken", "Kleine Häppchen, regelmäßig wiederholt, bleiben besser hängen als viel Stoff auf einmal."),
  ("box", "Mini-Übung", "Schreib eine Sache aus deinem Job auf, die du selten brauchst und jedes Mal wieder nachschlagen musst. Notiere, wie du dich alle paar Wochen kurz daran erinnern könntest."),
  ("box", "Teste dich", "Was machen Sprachlern-Apps laut Lektion anders als eine lange Schulung? Die Auflösung steht in der Lektion."),
  ("btn", "Lektion öffnen", APP + "/#lektion=v10"),
  ("h3", "Sag uns, was fehlt: der Feedback-Knopf"),
  ("p", "Jeden Montag wartet auf der Startseite der Lernwerkstatt eine neue Lektion der Woche. Und wenn dir in einer Lektion etwas unklar ist oder ein Beispiel fehlt: Unter jeder Lektion gibt es einen Feedback-Knopf. Deine Nachricht geht per E-Mail direkt an den Prozesswurm. So wird die Lernwerkstatt jede Woche ein Stück besser."),
  ("btn", "Zur Lektion der Woche", APP + "/#lektion-der-woche"),
 ]),
 dict(nr=6, name="Lied oder Kurzvideo der Woche", headline="Lied: Die Lernwerkstatt", blocks=[
  ("img", "lied.jpg", "Lied der Woche: Die Lernwerkstatt, vom Prozesswurm, melodischer Pop-Rap auf Suno.", None),
  ("p", "Passend zur Warnung von Doktor Kuddelmuddel: ein melodischer Pop-Rap mit Ohrwurm-Refrain. Doktor Kuddelmuddel bringt Abläufe und Termine durcheinander, der Prozesswurm sortiert sie wieder. Und am Ende ist klar, wo man das lernt."),
  ("btn", "Lied anhören", L_LIED),
  ("p", "Alle Lieder und Videos findest du auf " + a("prozesswurm.de unter „Hören und sehen“", L_HOEREN) + "."),
 ]),
]

ZITAT = dict(
 text="Erfahrung ist der Name, den jeder seinen Fehlern gibt.",
 wer="Oscar Wilde, irischer Schriftsteller, im Theaterstück „Lady Windermeres Fächer“ (1892)",
 reaktion="Der Prozesswurm nickt: Fehler sind nur dann verschenkt, wenn keiner darüber redet. Deshalb gehört zur Lern-Viertelstunde auch das Danebenliegen. Doktor Kuddelmuddel strahlt: „Dann bin ich der erfahrenste Mensch im ganzen Haus.“",
 quelle=("Project Gutenberg, Lady Windermere's Fan, 3. Akt", "https://www.gutenberg.org/files/790/790-h/790-h.htm"),
)

SCHLUSS = "Dieser Newsletter erscheint weiterhin jeden Montag. Vielen Dank für deine Zeit. Feedback, Anmerkungen oder Themenvorschläge? Schreib mir gern an info@prozesswurm.de."

# LinkedIn (Fassung B)
LI_ERSTE_ZEILE = "82 Prozent der Chefs finden Weiterbildung wichtig. Nur 21 Prozent der Beschäftigten werden darauf angesprochen."
LI_DANACH = "Gelernt wird im Büro ständig, nur meistens nebenbei und ohne Plan. Diese Woche geht es darum, wie Lernen in den Alltag passt, ohne dass jemand einen ganzen Tag dafür freinehmen muss."
LI_FRAGE = "Wann habt ihr zuletzt im Team bewusst etwas voneinander gelernt? Schreib es in die Kommentare."
LI_BEGLEIT = ("Fast alle Chefs finden Weiterbildung wichtig, aber nur jeder Fünfte spricht seine Leute darauf an. "
 "Im neuen Montags-Wurm zeigt der Prozesswurm die Lern-Viertelstunde: eine Frage sammeln, fünfzehn Minuten einplanen, selbst ausprobieren. "
 "Dazu ein ARTE-Tipp über die Tricks unseres Gehirns und das Lied „Die Lernwerkstatt“. "
 "Doktor Kuddelmuddel warnt diese Woche eindringlich vor der Lernwerkstatt. Hört nicht auf ihn.")
LI_TAGS = "#Prozessmanagement #Weiterbildung #Lernen #Mittelstand #Einarbeitung"

# Brevo (Fassung C)
BETREFF = "Bitte nicht ausprobieren"
BETREFF_ALT = "Lernen, wenn keiner fragt: die Lern-Viertelstunde"
VORSCHAU = "Doktor Kuddelmuddel warnt, die Lern-Viertelstunde und ein ARTE-Tipp zum Gehirn."

HINWEISE = [
 "Keine vereinbarte Fassung „Montags-Wurm 9. November 2026“ gefunden (Artifact-Liste, Google Drive), Entwurf neu geschrieben.",
 "Pflichtkasten „Achtung: Doktor Kuddelmuddel hat eine Warnung“ direkt nach dem Einstieg, Text wörtlich, Knopf auf #lektion=b01. Der Kuddelmuddel-Einwurf nach dem Einstieg entfällt deshalb.",
 "Frisch aus den letzten 7 Tagen ist nur die Bitkom-Meldung zum Homeoffice (5.11.2026). Die Weiterbildungszahlen sind älter (Bitkom Akademie 17.9., PwC über it-daily 5.10., TÜV über Haufe 20.5.2026) und mit Datum genannt. Die Bitkom-Akademie-Studie ist laut Herausgeber nicht repräsentativ, im Text so gekennzeichnet.",
 "BDA/Forsa-Umfrage (28.10.2026) über Mittelstand Nachrichten (dts) gelesen, nicht über die BDA selbst.",
 "ARTE: arte.tv war von hier aus nicht erreichbar. Länge (53 bzw. 54 Min.) und Link stammen von fernsehserien.de. Das Datum „verfügbar bis“ ließ sich nicht prüfen, bitte vor dem Versand in der Mediathek nachsehen und ergänzen (Erstausstrahlung April 2026).",
 "Lied „Die Lernwerkstatt“ auf Suno geprüft (Titel, Stil Pop-Rap, Inhalt), Länge auf der Seite nicht sichtbar.",
 "Wilde-Zitat im Originaltext geprüft: „Experience is the name every one gives to their mistakes.“ (3. Akt, gesagt von Dumby). Deutsche Übertragung eigene.",
]
