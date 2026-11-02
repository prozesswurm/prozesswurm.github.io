# Inhalt: Der Montags-Wurm – 2. November 2026 (Text aus dem Claude-Docs-Dokument, Fassung A)
DATUM = "2. November 2026"
KW = "KW 45"
TITEL = "Der Montags-Wurm – 2. November 2026"
UNTERTITEL = "Umziehen, ohne dass etwas verloren geht"
SLUG = "02-november-2026"
BILD_ORDNER = "2026-11-02"  # Bilder liegen unter https://www.prozesswurm.de/newsletter/<BILD_ORDNER>/
HEUTE_DRIN = "In eigener Sache: die neue Website · 1. Die Umzugsliste · 2. KI aus Deutschland, Ämter online · 3. Drei Zahlen · 4. ARTE-Tipp · 5. Lernwerkstatt · 6. Kurzvideo der Woche · 7. Ein Satz zum Mitnehmen"
AUSGABE_URL = "https://www.prozesswurm.de/montags-wurm/02-november-2026"
APP = "https://www.prozesswurm.de/lernwerkstatt"
WEB = "https://www.prozesswurm.de/"

L_ERECHNUNG = ("kostenlose-erechnung.de, Stand 5.10.2026", "https://kostenlose-erechnung.de/ratgeber/e-rechnungspflicht-2027-versandpflicht/")
L_CP = ("ChannelPartner, 29.10.2026", "https://www.channelpartner.de/article/4236986/e-rechnungspflicht-rueckt-naeher.html")
L_MC = ("Mittelstand Café, 28.10.2026", "https://www.mittelstandcafe.de/anbieterwechsel-vorbereiten-40-prozent-der-unternehmen-mit-digitalimporten-wollen-wichtige-software-und-systeme-bei-bedarf-austauschen-k-nnen-2281602.html")
L_BITKOM_KI = ("Bitkom, 2.11.2026", "https://www.bitkom.org/Presse/Presseinformation/Digital-Gipfel-Unternehmen-wollen-KI-aus-Deutschland")
L_HIB = ("Deutscher Bundestag, hib, 12.10.2026", "https://www.bundestag.de/presse/hib/kurzmeldungen-1224224")
L_BITKOM_USA = ("Bitkom, 30.10.2026", "https://www.bitkom.org/Presse/Presseinformation/Midterms-Unternehmen-wuenschen-mehr-Verlaesslichkeit-von-USA")
L_BITKOM_AEMTER = ("Bitkom, 12.10.2026", "https://www.bitkom.org/Presse/Presseinformation/Analoge-Aemter-bremsen-Wirtschaft-aus")
L_ARTE = "https://www.arte.tv/de/videos/120880-013-A/re-das-ewige-pendeln-des-eu-parlaments/"
L_VIDEO = "https://www.youtube.com/shorts/Akp8DEreL5s"
L_HOEREN = "https://www.prozesswurm.de/hoeren-und-sehen/"

def a(t, u): return f'<a href="{u}">{t}</a>'

EINSTIEG = [
 ("p", "<b>SALVE!</b> Der Prozesswurm ist umgezogen, und er war nicht der Einzige. Viele Betriebe packen gerade ihre Rechnungen in ein neues System, weil die E-Rechnung kommt. Diese Woche geht es darum, wie ein Ablauf umzieht, ohne dass unterwegs etwas verloren geht."),
 ("kud", "Umziehen? Ich lasse lieber alles stehen. Dann merkt wenigstens keiner, was fehlt."),
]

EIGENE_SACHE = dict(titel="Der Prozesswurm ist umgezogen", blocks=[
 ("p", "Seit dem 28. Oktober liegt alles an einem Ort: auf " + a("www.prozesswurm.de", WEB) + ". Dort findest du die " + a("Lernwerkstatt", WEB + "lernwerkstatt/") + ", alle Ausgaben des Montags-Wurms, Lieder und Videos unter „Hören und sehen“ und neu die Seite " + a("„Für Teams“", WEB + "fuer-teams/") + " mit fertigen Lernpfaden zum Weiterschicken."),
 ("p", "Die Seite ist selbst gebaut statt mit Google Sites: spürbar schneller, ohne Cookies, ohne Werbung, ohne Auswertung durch Google. Sie lässt sich mit der Tastatur bedienen, hat eine gut lesbare Schrift, eine helle und eine dunkle Ansicht und eine Suche über alles. Auf der Startseite tippst du an, was dich gerade nervt, und bekommst einen Handgriff für morgen."),
 ("p", "Ehrlich gesagt: Wer in der Lernwerkstatt Fortschritt gespeichert hatte, sieht ihn unter der neuen Adresse vielleicht nicht mehr. " + a("Hier steht, was dann hilft", WEB + "lernwerkstatt/#hilfe=umzug") + ". Und perfekt ist noch nicht alles. Der Prozesswurm kriecht ja auch noch und ist kein Schmetterling."),
 ("p", "<b>Was gefällt dir, was fehlt, wo hakt es?</b> Schreib an " + a("info@prozesswurm.de", "mailto:info@prozesswurm.de") + "."),
 ("kud", "Eine Website ohne Cookies? Und wovon soll ich mich in der Kaffeepause ernähren?"),
 ("btn", "Zur neuen Website", WEB),
])

ABSCHNITTE = [
 dict(nr=1, name="Aktuelles aus dem Prozessmanagement", headline="Die E-Rechnung kommt: Ein neues System ist noch kein neuer Ablauf", blocks=[
  ("img", "titel.jpg", "Der Prozesswurm sitzt mit zwei gesichtslosen Helferfiguren am Tisch und hört zu, daneben zeigt er an einer Maschine einen Handgriff. Doktor Kuddelmuddel hält vor leeren Stühlen einen Vortrag mit einem riesigen Folienstapel.", "Klein anfangen statt großer Vortrag: Der Prozesswurm zeigt den Handgriff, Doktor Kuddelmuddel redet vor leeren Stühlen."),
  ("p", "In zwei Monaten wird es ernst. Ab dem 1. Januar 2027 müssen Unternehmen mit mehr als 800.000 Euro Umsatz im Vorjahr ihre Rechnungen an andere Firmen als E-Rechnung schicken. Alle anderen folgen ein Jahr später. Eine E-Rechnung ist eine Datei, die ein Programm direkt lesen kann. Ein PDF im Anhang reicht dafür nicht."),
  ("p", "Viele Betriebe fühlen sich trotzdem gut aufgestellt. In einer Umfrage des Anbieters Quadient halten 75 Prozent ihre Rechnungsabläufe für digital, aber nur 6 Prozent sehen sich als vollständig bereit. Eine Studie der Universitäten Potsdam und Erlangen-Nürnberg kommt zu einem ähnlichen Bild: 71 Prozent der meist mittelständischen Betriebe haben noch keine konkreten Schritte eingeleitet. Beides fasst ein Beitrag in ChannelPartner vom 29. Oktober zusammen, geschrieben von einem Softwareanbieter."),
  ("h3", "Was das mit deinen Abläufen zu tun hat"),
  ("p", "Ein neues System ist wie eine neue Wohnung. Wer einfach alle Kisten ungeöffnet hineinträgt, hat danach dasselbe Durcheinander, nur an einem anderen Ort. Bei Rechnungen heißt das: Wird heute ausgedruckt, abgezeichnet und in eine Excel-Liste übertragen, passiert das morgen eben am Bildschirm. Schneller wird dadurch nichts."),
  ("p", "Der bessere Weg: erst aufschreiben, wie der Ablauf heute wirklich läuft, dann entscheiden, was mitkommt. Genau dafür ist eine Prozessbeschreibung da. Und dabei fällt oft auf, dass ein Schritt nur noch existiert, weil ihn nie jemand gestrichen hat."),
  ("h3", "Handgriff der Woche: die Umzugsliste"),
  ("img", "hutliste.jpg", "Grafik: Die Umzugsliste in drei Schritten mit Beispieltabelle.", "Drei Schritte vor jedem Systemwechsel: aufschreiben, entscheiden, einen Namen dranschreiben."),
  ("ol", [
    "<b>Aufschreiben, wie es heute läuft.</b> Jeden Schritt, auch den Zettel am Bildschirm und die Liste, die „nur die Müller“ pflegt.",
    "<b>Pro Schritt entscheiden.</b> Mitnehmen, wegwerfen oder neu bauen?",
    "<b>Pro Kiste einen Namen und ein Datum.</b> Wer packt im neuen System aus, und bis wann?",
  ]),
  ("h3", "Auch ein Notausgang ist ein Ablauf"),
  ("p", "Umziehen muss man manchmal auch, wenn man gar nicht will. Laut Bitkom bereiten sich 40 Prozent der Unternehmen, die digitale Technik aus dem Ausland beziehen, darauf vor, wichtige Anbieter und Systeme bei Bedarf auszutauschen (602 befragte Unternehmen, berichtet am 28. Oktober). Wer seine Abläufe aufgeschrieben hat, kann leichter wechseln. Wer sie nur im Programm hat, zieht immer mit dem Programm um."),
  ("p", "<b>Der Handgriff:</b> Schreib für jedes wichtige Programm eine Zeile dazu: Welche Daten stecken drin, und wie bekommen wir sie heraus?"),
  ("kud", "Ich trage einfach alle Kisten ungeöffnet ins neue System. Die mit der Aufschrift ‚Sonstiges‘ mache ich dann 2035 auf."),
  ("src", [L_ERECHNUNG, L_CP, L_MC]),
 ]),
 dict(nr=2, name="Märkte und Nachrichten", headline="KI am liebsten aus Deutschland, Ämter ziehen online um", blocks=[
  ("p", "<b>Bitkom: Fast alle wollen KI aus Deutschland, kaum einer will dafür mehr zahlen.</b> Zum Digital-Gipfel hat der Branchenverband Bitkom am 2. November eine Umfrage vorgestellt. 96 Prozent der Unternehmen würden KI am liebsten von deutschen Anbietern beziehen. 64 Prozent wollen dafür aber keine Abstriche machen, also weder mehr zahlen noch auf Funktionen verzichten. US-Anbieter bevorzugen nur noch 41 Prozent, vor einem Jahr waren es 51 Prozent. Befragt wurden je rund 600 Unternehmen ab 20 Beschäftigten."),
  ("src", [L_BITKOM_KI]),
  ("p", "<b>Staatsmodernisierung: erste Ergebnisse, viel Arbeit übrig.</b> Die Bundesregierung hat dem Bundestag einen Zwischenbericht vorgelegt. Von 23 großen Vorhaben sind 5 abgeschlossen. Der Aufwand, den Firmen für Vorschriften treiben müssen, ist nach Angaben der Regierung unterm Strich um rund 1,7 Milliarden Euro gesunken (Stand 30. Juni 2026). Und rund 66 Millionen Menschen können sich inzwischen online an- und ummelden."),
  ("src", [L_HIB]),
  ("p", "<b>Was das für dich heißt:</b> Neue Werkzeuge kommen, ob aus Deutschland oder anderswo, und auch die Ämter stellen um. Wer weiß, wie die eigenen Abläufe laufen, kann ein Werkzeug austauschen, ohne jedes Mal von vorn anzufangen."),
  ("kud", "Abhängig von einem Anbieter? Ich doch nicht. Ich kann jederzeit aufhören. Nächstes Jahr. Vielleicht."),
 ]),
 dict(nr=3, name="Zahlen und Erkenntnisse", headline="Wechsel, Abhängigkeit und Ämter in Zahlen", blocks=[
  ("img", "zahlen.jpg", "Grafik mit drei Zahlen: 71 Prozent ohne konkrete Schritte zur E-Rechnung, 87 Prozent fühlen sich von US-Technik abhängig, 42 Prozent nennen unverbundene Programme als Problem.", "Drei Zahlen, eine Frage: Wer kennt seine Abläufe gut genug für den Umzug?"),
  ("ul", [
    "<b>71 Prozent</b> der meist mittelständischen Betriebe haben für die E-Rechnung noch keine konkreten Schritte eingeleitet (Studie Universität Potsdam und FAU Erlangen-Nürnberg, zitiert am 29.10.2026). <i>Heißt:</i> Zwei Monate vor dem Stichtag steht bei vielen noch der ganze Umzug an.",
    "<b>87 Prozent</b> der Unternehmen, die digitale Technik aus den USA nutzen, fühlen sich davon abhängig, 47 Prozent sogar stark (Bitkom, 30.10.2026, 602 Unternehmen). <i>Heißt:</i> Ein Plan für den Wechsel gehört zur Grundausstattung.",
    "<b>42 Prozent</b> der Unternehmen nennen Programme, die nicht miteinander verbunden sind, als Problem im Umgang mit Behörden (Bitkom, 12.10.2026, 603 Unternehmen). <i>Heißt:</i> Wo Systeme nicht zusammenpassen, tippt am Ende ein Mensch alles zweimal ab.",
  ]),
  ("src", [L_CP, L_BITKOM_USA, L_BITKOM_AEMTER]),
  ("kud", "Zwei Monate bis zur Frist sind ein entspanntes Polster. Ich fange immer an Silvester an, kurz nach dem Raclette."),
 ]),
 dict(nr=4, name="Sehenswert", headline="Re: Das ewige Pendeln des EU-Parlaments (ARTE, 31 Min.)", blocks=[
  ("img", "sehenswert.jpg", "Fernsehtipp: ARTE-Reportage Re: Das ewige Pendeln des EU-Parlaments, 31 Minuten.", None),
  ("p", "Jeden Monat zieht das Europäische Parlament für knapp vier Tage von Brüssel nach Straßburg, mit Akten, Technik und Personal. Und danach wieder zurück. Die Reportage fragt, ob sich Europa diesen Wanderzirkus noch leisten kann."),
  ("p", "Warum sich die 31 Minuten lohnen: Hier sieht man, was ein Umzug kostet, wenn er zur Gewohnheit geworden ist. Ein Ablauf, den keiner mehr erfunden hat, den aber auch keiner abschaffen kann. In der ARTE-Mediathek bis 16. Februar 2027."),
  ("btn", "Zur ARTE-Mediathek", L_ARTE),
  ("kud", "Jeden Monat umziehen ist herrlich. Man muss nie aufräumen, man packt einfach alles wieder ein."),
 ]),
 dict(nr=5, name="Aus der Lernwerkstatt", headline="Erst fragen, dann schulen", blocks=[
  ("img", "lernwerkstatt.jpg", "Drei Bildschirme der Lernwerkstatt-App zur Lektion: Start, Zum Merken, Frage.", None),
  ("p", "Zum Umzug passt die Lektion <b>„Erst fragen, dann schulen: andere fit machen für einen neuen Ablauf“</b> aus Stufe B2. Dauer: sieben Minuten. Ein kleiner Auszug:"),
  ("box", "Zum Merken", "Wer vorher fragt, schult nicht am Bedarf vorbei. Ein kurzes Häppchen für alle schlägt einen langen Tag für niemanden."),
  ("box", "Mini-Übung", "Denk an eine Schulung, die wenig gebracht hat. Was hättest du vorher gebraucht? Welche drei Dinge hättest du wirklich wissen müssen?"),
  ("box", "Teste dich", "Wer bekommt bei einem neuen Ablauf die ausführliche Vertiefung? Die Auflösung steht in der Lektion."),
  ("btn", "Lektion öffnen", APP + "/#lektion=k18"),
  ("h3", "Dein Fortschritt zieht mit: der Speicherlink"),
  ("p", "Jeden Montag wartet auf der Startseite der Lernwerkstatt eine neue Lektion der Woche. Und damit dein Fortschritt nicht noch einmal verloren geht: Unter „Fortschritt mitnehmen“ tippst du auf „Speicherlink kopieren“. Den Link legst du als Lesezeichen ab oder schickst ihn dir selbst. Öffnest du ihn auf einem anderen Gerät, ist dein Stand sofort wieder da. Alles kostenlos und ohne Anmeldung."),
  ("btn", "Zur Lektion der Woche", APP + "/#lektion-der-woche"),
 ]),
 dict(nr=6, name="Lied oder Kurzvideo der Woche", headline="Kurzvideo: Wir verändern mit dir die Welt", blocks=[
  ("img", "lied.jpg", "Kurzvideo der Woche: Wir verändern mit dir die Welt, vom Prozesswurm, sechs Sekunden.", None),
  ("p", "Sechs Sekunden Schwung für den Montag: Der Prozesswurm dreht eine Runde, die Pfeile zeigen nach vorn. Die Botschaft passt zum Umzug: Veränderung fängt nicht beim neuen System an, sondern bei dir."),
  ("btn", "Video ansehen", L_VIDEO),
  ("p", "Alle Lieder und Videos findest du auf " + a("prozesswurm.de unter „Hören und sehen“", L_HOEREN) + "."),
 ]),
]

ZITAT = dict(
 text="Die größte Gefahr in Zeiten des Umbruchs ist nicht der Umbruch selbst, sondern mit der Logik von gestern zu handeln.",
 wer="Peter F. Drucker (zugeschrieben), Vordenker des modernen Managements",
 reaktion="Der Prozesswurm nickt: Deshalb erst die Umzugsliste, dann das neue System. Doktor Kuddelmuddel ist begeistert: „Logik von gestern? Ich habe nicht mal Logik von heute. Damit bin ich ja völlig zukunftssicher.“",
 quelle=("Bruno Marion", "https://brunomarion.com/drucker-turbulent-times/"),
)

SCHLUSS = "Dieser Newsletter erscheint weiterhin jeden Montag. Vielen Dank für deine Zeit. Feedback, Anmerkungen oder Themenvorschläge? Schreib mir gern an info@prozesswurm.de."

# LinkedIn (Fassung B)
LI_ERSTE_ZEILE = "75 Prozent halten ihre Rechnungen für digital. Nur 6 Prozent sind für die E-Rechnung wirklich bereit."
LI_DANACH = "Der Prozesswurm ist umgezogen, und viele Betriebe tun es gerade auch: Die Rechnungen ziehen in ein neues System. Diese Woche geht es darum, wie ein Ablauf umzieht, ohne dass unterwegs etwas verloren geht."
LI_FRAGE = "Was habt ihr beim letzten Systemwechsel ungeöffnet mitgeschleppt? Schreib es in die Kommentare."
LI_BEGLEIT = ("Ab 1. Januar 2027 kommt für viele Betriebe die E-Rechnung, und mit ihr ein neues System. "
 "Im neuen Montags-Wurm zeigt der Prozesswurm die Umzugsliste: aufschreiben, entscheiden, einen Namen dranschreiben. "
 "In eigener Sache: Der Prozesswurm ist selbst umgezogen, alles liegt jetzt auf prozesswurm.de, schneller und ohne Cookies. "
 "Sag uns in den Kommentaren, was gefällt und wo es hakt. "
 "Doktor Kuddelmuddel trägt derweil alle Kisten ungeöffnet ins neue System.")
LI_TAGS = "#Prozessmanagement #ERechnung #Mittelstand #Digitalisierung #Veränderung"

# Brevo (Fassung C)
BETREFF = "Umziehen, ohne dass etwas verloren geht"
BETREFF_ALT = "Neues System, alter Ablauf? Die Umzugsliste"
VORSCHAU = "Die Umzugsliste vor der E-Rechnung, ein ARTE-Tipp und die neue Website."

HINWEISE = [
 "E-Rechnung: Pflicht zum Ausstellen ab 1.1.2027 bei mehr als 800.000 Euro Vorjahresumsatz, für alle übrigen ab 1.1.2028 (§ 27 Abs. 38 UStG, geprüft über kostenlose-erechnung.de).",
 "75 % und 6 % aus der Quadient-Studie (Anbieterstudie), 71 % aus der Studie Uni Potsdam / FAU, beide über ChannelPartner vom 29.10.2026 (Gastbeitrag eines Anbieters). Im Text so gekennzeichnet.",
 "Drucker-Zitat ohne Fundstelle im Buch von 1980, deshalb „zugeschrieben“.",
]
