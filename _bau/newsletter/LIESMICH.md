# Montags-Wurm: Bauanleitung (E-Mail-Layout seit 26.10.2026)

Layout angelehnt an einen Wirtschafts-Newsletter: Kopfbanner, Begrüßung mit Lesezeit und Kalenderwoche,
„Heute drin“-Kasten, je Abschnitt eine kleine Kennzeile (1. … bis 7.) plus eigene Schlagzeile, Bilder mit Bildunterschrift,
Kuddelmuddel-Kästen mit Originalbild, Quellenzeile, grüne Knöpfe, Zitatblock, Fußzeile mit Kanälen.

1. Neuen Ordner `_bau/newsletter/ausgabe-JJJJ-MM-TT/` anlegen, `inhalt.py` aus dem jüngsten Muster kopieren und Wort für Wort neu füllen
   (DATUM, KW, UNTERTITEL, SLUG, BILD_ORDNER, HEUTE_DRIN, EINSTIEG, ABSCHNITTE 1–6, ZITAT, LinkedIn-Felder, Betreff, Vorschautext).
2. Bilder: Vorlagen in `tpl/` an die Woche anpassen (Texte), nie die Figuren verändern. App-Bildschirme der passenden Lektion mit Playwright
   nach `app-bilder/` aufnehmen (index.html#lektion=<id>, „Los geht's“, durchklicken). Dann `node bilder.js newsletter/<BILD_ORDNER>`.
   Titelbild Abschnitt 1: passendes Lektionsbild aus `bilder/<id>.webp` als `titel.jpg`; `kuddel.png` und `wurm.png` mitkopieren.
   `titelbild-linkedin.jpg` = Titelbild in 1200 × 675.
3. Bauen (im Hauptordner des Archivs ausführen):
   - `python3 _bau/newsletter/bauen.py auto newsletter/<BILD_ORDNER>/index.html _bau/newsletter/ausgabe-…` → E-Mail für Brevo und Webansicht
   - `python3 _bau/newsletter/texte.py _bau/newsletter/ausgabe-…` → out/webseite.html und out/linkedin.html
   - `python3 _bau/newsletter/md.py _bau/newsletter/ausgabe-…` → out/doc.md für das Claude-Docs-Dokument
4. Prüfen: Vorschau bei 700 und 390 Pixel Breite mit Playwright ansehen.
