#!/usr/bin/env python3
"""Lektionsbild vorbereiten: auf 1200 px Breite bringen, kleinen Hinweis
"Mit KI erstellt" unten rechts einfügen und als bilder/<id>.webp speichern.

Regel: Jedes Lektionsbild in der App bekommt diesen Hinweis.

Aufruf:  python3 _bau/ki_hinweis.py <quelle.png|jpg|webp> <id> [<quelle> <id> ...]
Beispiel: python3 _bau/ki_hinweis.py ~/Downloads/01-08_....png b08
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT = "Mit KI erstellt"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def hinweis(src, out):
    im = Image.open(src).convert("RGB")
    if im.width != 1200:
        im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
    im = im.convert("RGBA")
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = ImageFont.truetype(FONT, 15)
    x0, y0, x1, y1 = d.textbbox((0, 0), TEXT, font=f)
    w, h = x1 - x0, y1 - y0
    px, py, rand = 8, 4, 10
    bx1, by1 = im.width - rand, im.height - rand
    bx0, by0 = bx1 - w - 2 * px, by1 - h - 2 * py
    d.rounded_rectangle((bx0, by0, bx1, by1), radius=6, fill=(0, 0, 0, 95))
    d.text((bx0 + px - x0, by0 + py - y0), TEXT, font=f, fill=(255, 255, 255, 215))
    Image.alpha_composite(im, lay).convert("RGB").save(out, "WEBP", quality=82, method=6)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or len(a) % 2:
        sys.exit(__doc__)
    for src, pid in zip(a[::2], a[1::2]):
        out = os.path.join(ROOT, "bilder", f"{pid}.webp")
        hinweis(src, out)
        print(pid, "->", out)
