#!/usr/bin/env python3
"""Genera las filminas (JPG + PDF).  Uso:  python3 build.py [id-parcial ...]"""
import os, sys
from PIL import Image, ImageDraw
from kit import *
from slides_all import SLIDES
import scenes as sc
from kit import AMBER_D, GREEN, check, warning

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "salida")
JPG = os.path.join(OUT, "jpg")
FOOT = "Código Penal de la Nación (Ley 11.179, t.o.) · Contrastar con el texto vigente antes de usar"


def tint(col, k=0.075):
    col = col.lstrip("#")
    r, g, b = (int(col[i:i + 2], 16) for i in (0, 2, 4))
    bg = (0xF7, 0xF4, 0xEE)
    return "#%02x%02x%02x" % tuple(int(bg[i] * (1 - k * 3.2) + v * k * 3.2) for i, v in enumerate((r, g, b)))


def round_corners(c, x, y, w, h, r=36):
    """Recorta lo que la escena dibujó fuera del panel redondeado."""
    box = (int(x * S), int(y * S), int((x + w) * S), int((y + h) * S))
    crop = c.img.crop(box)
    mask = Image.new("L", crop.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, crop.size[0] - 1, crop.size[1] - 1], radius=r * S, fill=255)
    bg = Image.new("RGB", crop.size, BG)
    c.img.paste(Image.composite(crop, bg, mask), box[:2])


def verif_tag(c, s, xr, y):
    """Etiqueta bajo el artículo: ✔ contrastada / ⚠ sin contrastar (iconos dibujados)."""
    if s["art"] == "Doctrina":
        return
    ok = s.get("ok", False)
    txt, col = {True: ("norma y pena contrastadas", GREEN),
                False: ("sin contrastar con el texto vigente", AMBER_D),
                "parcial": ("norma contrastada · pena sin contrastar", AMBER_D)}[ok]
    tw = c.text_size(txt, "SemiBold", 22)[0]
    c.text(xr, y, txt, "SemiBold", 22, col, anchor="ra")
    ix = xr - tw - 24
    if ok is True:
        check(c, ix, y + 14, 13, fill=GREEN)
    else:
        warning(c, ix, y + 14, 28, fill=AMBER)


def header(c, s, n, total):
    label, col = s["cat"]
    c.rect(0, 0, W, 16, fill=col)
    chip(c, 90, 52, label, fill=col, size=26, pad=22)
    tsz = 84
    while c.text_size(s["title"], "ExtraBold", tsz)[0] > W - 180:
        tsz -= 4
    c.text(90, 128 + (84 - tsz) * 0.45, s["title"], "ExtraBold", tsz, NAVY)
    aw = c.text_size(s["art"], "Bold", 32)[0] + 56
    verif_tag(c, s, W - 90 - aw - 24, 70)
    c.rrect(W - 90 - aw, 56, aw, 56, r=28, fill=None, outline=NAVY, width=3)
    c.text(W - 90 - aw / 2, 84, s["art"], "Bold", 32, NAVY, anchor="mm")
    c.text(90, 1032, FOOT, "Regular", 22, GREY)
    c.text(W - 90, 1032, f"{n} / {total}", "Bold", 24, GREY, anchor="ra")


def bullets(c, items, x, y, w, col, size=44, limit=980):
    for sz in (size, 40, 36, 33, 30):
        yy = y
        for t in items:
            yy += len(c.wrap(t, "SemiBold", sz, w - 50)) * sz * 1.22 + 26
        if yy <= limit:
            break
    for t in items:
        c.ellipse(x + 14, y + sz * 0.62, 14, fill=col)
        yy = c.paragraph(x + 50, y, t, "SemiBold", sz, NAVY, max_w=w - 50, lh=1.22)
        y = yy + 26
    return y


def pena_badge(c, lines, x, y, w):
    n = len(lines)
    h = 74 + n * 58
    no_pena = lines == ["No es punible"]
    col = GREEN if no_pena else NAVY
    c.rrect(x, y, w, h, r=26, fill=col)
    c.text(x + 36, y + 20, "RESULTADO" if no_pena else "PENA", "Bold", 24, "#C9D3E6", anchor="la")
    for i, ln in enumerate(lines):
        c.text(x + 36, y + 62 + i * 58, ln, "ExtraBold", 38 if len(ln) < 30 else (32 if len(ln) < 36 else 28), WHITE)


def render(s, n, total):
    c = Canvas()
    header(c, s, n, total)
    label, col = s["cat"]
    pena = s.get("pena")
    if s["kind"] == "side":
        px, py, pw, ph = 90, 250, 930, 730
        c.rrect(px, py, pw, ph, r=36, fill=tint(col))
        s["scene"](c, px, py, pw, ph)
        round_corners(c, px, py, pw, ph)
        bx = 1090
        bw = W - 90 - bx
        hh = (74 + len(pena) * 58) if pena else 0
        bullets(c, s["bullets"], bx, 270, bw, col, limit=(980 - hh - 24) if pena else 980)
        if pena:
            pena_badge(c, pena, bx, 980 - hh, bw)
    else:
        px, py, pw, ph = 90, 250, 1740, 520
        c.rrect(px, py, pw, ph, r=36, fill=tint(col))
        s["scene"](c, px, py, pw, ph)
        round_corners(c, px, py, pw, ph)
        cw = (pw - 2 * 24) / 3
        for i, t in enumerate(s["bullets"]):
            x = px + i * (cw + 24)
            c.rrect(x, 800, cw, 180, r=24, fill=WHITE, outline=col, width=4)
            c.paragraph(x + 28, 822, t, "SemiBold", 36, NAVY, max_w=cw - 56, lh=1.2)
    return c


def cover(total):
    c = Canvas(NAVY)
    c.rect(0, 0, W, 16, fill=AMBER)
    c.text(960, 190, "DERECHO PENAL ARGENTINO", "ExtraBold", 100, WHITE, anchor="ma")
    c.text(960, 320, "Filminas ilustradas · teoría del delito y Código Penal", "Regular", 44, "#C9D3E6", anchor="ma")
    c.rrect(560, 420, 800, 520, r=40, fill="#243756")
    sc.s_portada(c, 560, 420, 800, 520)
    c.text(960, 1030, f"{total} filminas · una idea por lámina", "Regular", 26, "#8FA0BF", anchor="ma")
    return c


def main():
    os.makedirs(JPG, exist_ok=True)
    if not sys.argv[1:]:
        for f in os.listdir(JPG):
            os.remove(os.path.join(JPG, f))
    flt = sys.argv[1:]
    total = len(SLIDES) + 1
    pages = []
    cv = cover(total)
    pages.append(cv.save(os.path.join(JPG, "01-portada.jpg"), quality=93))
    for i, s in enumerate(SLIDES, start=2):
        if flt and not any(f in s["id"] for f in flt):
            # igual lo cargamos para el PDF si ya existe
            p = os.path.join(JPG, f"{i:02d}-{s['id']}.jpg")
            if os.path.exists(p):
                pages.append(Image.open(p).convert("RGB"))
            continue
        img = render(s, i, total).save(os.path.join(JPG, f"{i:02d}-{s['id']}.jpg"), quality=93)
        pages.append(img)
    pdf = os.path.join(OUT, "filminas-derecho-penal.pdf")
    pages[0].save(pdf, save_all=True, append_images=pages[1:], resolution=144)
    print(f"{len(pages)} filminas -> {OUT}")


if __name__ == "__main__":
    main()
