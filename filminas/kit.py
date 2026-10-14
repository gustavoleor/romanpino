"""Kit de dibujo: lienzo con antialiasing y pictogramas simples (estilo plano)."""
from PIL import Image, ImageDraw, ImageFont
import math

W, H, S = 1920, 1080, 2  # tamaño final y factor de supermuestreo

FONT_DIR = "/usr/share/fonts/opentype/inter/"
_fonts = {}


def font(weight, size):
    key = (weight, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(f"{FONT_DIR}Inter-{weight}.otf", int(size * S))
    return _fonts[key]


# Paleta
BG = "#F7F4EE"
NAVY = "#1B2A41"
INK = "#2B3A55"
RED = "#D64045"
TEAL = "#1D7874"
AMBER = "#F2A541"
AMBER_D = "#B96F00"
BLUE = "#3A6EA5"
GREEN = "#3E9B5F"
GREY = "#8A94A6"
LIGHT = "#E9E4D8"
WHITE = "#FFFFFF"
SKIN = "#F1C9A5"
PURPLE = "#7B4B94"


class Canvas:
    def __init__(self, bg=BG):
        self.img = Image.new("RGB", (W * S, H * S), bg)
        self.d = ImageDraw.Draw(self.img)

    # --- primitivas (coordenadas en unidades 1920x1080)
    def _p(self, pts):
        return [(x * S, y * S) for x, y in pts]

    def rect(self, x, y, w, h, fill=None, outline=None, width=0):
        self.d.rectangle([x * S, y * S, (x + w) * S, (y + h) * S], fill=fill,
                         outline=outline, width=int(width * S))

    def rrect(self, x, y, w, h, r=20, fill=None, outline=None, width=0):
        self.d.rounded_rectangle([x * S, y * S, (x + w) * S, (y + h) * S], radius=r * S,
                                 fill=fill, outline=outline, width=int(width * S))

    def ellipse(self, cx, cy, rx, ry=None, fill=None, outline=None, width=0):
        ry = rx if ry is None else ry
        self.d.ellipse([(cx - rx) * S, (cy - ry) * S, (cx + rx) * S, (cy + ry) * S],
                       fill=fill, outline=outline, width=int(width * S))

    def line(self, pts, fill=NAVY, width=6, round_ends=True):
        p = self._p(pts)
        self.d.line(p, fill=fill, width=int(width * S), joint="curve")
        if round_ends:
            r = width * S / 2
            for (x, y) in (p[0], p[-1]):
                self.d.ellipse([x - r, y - r, x + r, y + r], fill=fill)

    def poly(self, pts, fill=None, outline=None, width=0):
        self.d.polygon(self._p(pts), fill=fill, outline=outline)
        if outline and width:
            self.line(list(pts) + [pts[0]], fill=outline, width=width)

    def arc(self, cx, cy, r, a0, a1, fill=NAVY, width=6):
        self.d.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], a0, a1,
                   fill=fill, width=int(width * S))

    # --- texto
    def text_size(self, txt, weight, size):
        f = font(weight, size)
        b = self.d.textbbox((0, 0), txt, font=f)
        return (b[2] - b[0]) / S, (b[3] - b[1]) / S

    def text(self, x, y, txt, weight="Bold", size=40, fill=NAVY, anchor="la"):
        self.d.text((x * S, y * S), txt, font=font(weight, size), fill=fill, anchor=anchor)

    def wrap(self, txt, weight, size, max_w):
        words, lines, cur = txt.split(), [], ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if self.text_size(t, weight, size)[0] <= max_w or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w_
        if cur:
            lines.append(cur)
        return lines

    def paragraph(self, x, y, txt, weight="Bold", size=40, fill=NAVY, max_w=800,
                  lh=1.25, align="left"):
        yy = y
        for ln in self.wrap(txt, weight, size, max_w):
            if align == "center":
                self.text(x + max_w / 2, yy, ln, weight, size, fill, anchor="ma")
            else:
                self.text(x, yy, ln, weight, size, fill)
            yy += size * lh
        return yy

    def save(self, path, **kw):
        out = self.img.resize((W, H), Image.LANCZOS)
        out.save(path, **kw)
        return out


# ======================= PICTOGRAMAS =======================

def person(c, x, y, h=300, color=BLUE, pose="stand", skin=SKIN, face="happy", flip=False,
           hair=None):
    """Figura humana plana. (x, y) = pies. h = altura total."""
    s = h / 300.0
    d = -1 if flip else 1
    head_r = 34 * s
    if pose == "lie":  # acostado, a la derecha de x
        c.rrect(x, y - 54 * s, 190 * s, 54 * s, r=26 * s, fill=color)          # cuerpo
        c.rrect(x + 130 * s, y - 44 * s, 90 * s, 22 * s, r=11 * s, fill=INK)   # piernas
        c.ellipse(x - 30 * s, y - 34 * s, head_r, fill=skin)
        _face(c, x - 30 * s, y - 34 * s, head_r, "dead")
        return
    cx = x
    top = y - h
    # piernas
    leg_c = INK
    if pose == "run":
        c.line([(cx, y - 110 * s), (cx + 55 * s * d, y)], fill=leg_c, width=26 * s)
        c.line([(cx, y - 110 * s), (cx - 45 * s * d, y - 10 * s)], fill=leg_c, width=26 * s)
    else:
        c.line([(cx - 20 * s, y - 120 * s), (cx - 24 * s, y)], fill=leg_c, width=26 * s)
        c.line([(cx + 20 * s, y - 120 * s), (cx + 24 * s, y)], fill=leg_c, width=26 * s)
    # torso
    c.rrect(cx - 46 * s, top + 70 * s, 92 * s, 150 * s, r=34 * s, fill=color)
    # brazos
    sh_y = top + 100 * s
    if pose == "arms_up":
        c.line([(cx - 40 * s, sh_y), (cx - 85 * s, sh_y - 80 * s)], fill=color, width=24 * s)
        c.line([(cx + 40 * s, sh_y), (cx + 85 * s, sh_y - 80 * s)], fill=color, width=24 * s)
        c.ellipse(cx - 85 * s, sh_y - 85 * s, 14 * s, fill=skin)
        c.ellipse(cx + 85 * s, sh_y - 85 * s, 14 * s, fill=skin)
    elif pose == "point":
        c.line([(cx - 40 * s, sh_y), (cx - 60 * s, sh_y + 90 * s)], fill=color, width=24 * s)
        c.line([(cx + 40 * s * d, sh_y), (cx + 140 * s * d, sh_y + 10 * s)], fill=color, width=24 * s)
        c.ellipse(cx + 145 * s * d, sh_y + 10 * s, 14 * s, fill=skin)
    elif pose == "reach":
        c.line([(cx - 40 * s * d, sh_y), (cx - 55 * s * d, sh_y + 90 * s)], fill=color, width=24 * s)
        c.line([(cx + 40 * s * d, sh_y + 10 * s), (cx + 130 * s * d, sh_y + 55 * s)], fill=color, width=24 * s)
        c.ellipse(cx + 135 * s * d, sh_y + 57 * s, 14 * s, fill=skin)
    else:
        c.line([(cx - 40 * s, sh_y), (cx - 62 * s, sh_y + 100 * s)], fill=color, width=24 * s)
        c.line([(cx + 40 * s, sh_y), (cx + 62 * s, sh_y + 100 * s)], fill=color, width=24 * s)
    # cabeza
    hy = top + head_r
    c.ellipse(cx, hy, head_r, fill=skin)
    if hair:
        c.d.pieslice([(cx - head_r) * S, (hy - head_r) * S, (cx + head_r) * S, (hy + head_r) * S],
                     180, 360, fill=hair)
    _face(c, cx, hy, head_r, face)


def _face(c, cx, cy, r, mood):
    e = r * 0.32
    ey = cy - r * 0.1
    if mood == "dead":
        for sx in (-1, 1):
            ex = cx + sx * e
            c.line([(ex - 6, ey - 6), (ex + 6, ey + 6)], fill=NAVY, width=3)
            c.line([(ex - 6, ey + 6), (ex + 6, ey - 6)], fill=NAVY, width=3)
        c.line([(cx - 9, cy + r * 0.45), (cx + 9, cy + r * 0.45)], fill=NAVY, width=3)
        return
    c.ellipse(cx - e, ey, r * 0.09, fill=NAVY)
    c.ellipse(cx + e, ey, r * 0.09, fill=NAVY)
    if mood == "angry":
        c.line([(cx - e - 9, ey - 12), (cx - e + 8, ey - 5)], fill=NAVY, width=4)
        c.line([(cx + e + 9, ey - 12), (cx + e - 8, ey - 5)], fill=NAVY, width=4)
        c.line([(cx - 11, cy + r * 0.5), (cx + 11, cy + r * 0.5)], fill=NAVY, width=4)
    elif mood == "scared":
        c.ellipse(cx, cy + r * 0.5, r * 0.16, r * 0.22, fill=NAVY)
        c.line([(cx - e - 9, ey - 13), (cx - e + 8, ey - 18)], fill=NAVY, width=3)
        c.line([(cx + e + 9, ey - 13), (cx + e - 8, ey - 18)], fill=NAVY, width=3)
    elif mood == "sly":
        c.arc(cx, cy + r * 0.2, r * 0.45, 20, 160, fill=NAVY, width=4)
        c.line([(cx - e - 8, ey - 10), (cx - e + 8, ey - 6)], fill=NAVY, width=4)
    else:
        c.arc(cx, cy + r * 0.15, r * 0.45, 25, 155, fill=NAVY, width=4)


def mask(c, cx, cy, r=34):
    """Antifaz de ladrón sobre una cabeza."""
    c.rrect(cx - r, cy - r * 0.35, r * 2, r * 0.55, r=r * 0.25, fill=NAVY)
    c.ellipse(cx - r * 0.4, cy - r * 0.1, r * 0.13, fill=WHITE)
    c.ellipse(cx + r * 0.4, cy - r * 0.1, r * 0.13, fill=WHITE)


def house(c, x, y, w=300, h=240, wall=LIGHT, roof=RED, door=NAVY):
    """x,y = esquina inferior izquierda."""
    c.rect(x, y - h * 0.65, w, h * 0.65, fill=wall, outline=NAVY, width=4)
    c.poly([(x - 25, y - h * 0.65), (x + w / 2, y - h), (x + w + 25, y - h * 0.65)],
           fill=roof, outline=NAVY, width=4)
    dw = w * 0.22
    c.rect(x + w / 2 - dw / 2, y - h * 0.42, dw, h * 0.42, fill=door)
    c.ellipse(x + w / 2 + dw / 2 - 12, y - h * 0.2, 5, fill=AMBER)
    c.rect(x + w * 0.1, y - h * 0.55, w * 0.2, h * 0.2, fill="#BFE3F5", outline=NAVY, width=3)
    c.rect(x + w * 0.7, y - h * 0.55, w * 0.2, h * 0.2, fill="#BFE3F5", outline=NAVY, width=3)


def car(c, x, y, w=340, color=RED, crash=False):
    """x,y = esquina inferior izquierda."""
    h = w * 0.36
    c.rrect(x, y - h * 0.62, w, h * 0.62, r=26, fill=color, outline=NAVY, width=4)
    c.poly([(x + w * 0.2, y - h * 0.6), (x + w * 0.32, y - h), (x + w * 0.66, y - h),
            (x + w * 0.82, y - h * 0.6)], fill=color, outline=NAVY, width=4)
    c.poly([(x + w * 0.27, y - h * 0.63), (x + w * 0.35, y - h * 0.93), (x + w * 0.48, y - h * 0.93),
            (x + w * 0.48, y - h * 0.63)], fill="#BFE3F5")
    c.poly([(x + w * 0.52, y - h * 0.63), (x + w * 0.52, y - h * 0.93), (x + w * 0.64, y - h * 0.93),
            (x + w * 0.76, y - h * 0.63)], fill="#BFE3F5")
    for wx in (x + w * 0.22, x + w * 0.78):
        c.ellipse(wx, y, w * 0.095, fill=NAVY)
        c.ellipse(wx, y, w * 0.045, fill=GREY)
    if crash:
        star(c, x + w + 20, y - h * 0.4, 46, AMBER)


def star(c, cx, cy, r, fill=AMBER, points=9):
    pts = []
    for i in range(points * 2):
        ang = math.pi * i / points
        rr = r if i % 2 == 0 else r * 0.55
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    c.poly(pts, fill=fill, outline=NAVY, width=3)


def heart(c, cx, cy, r=40, fill=RED, broken=False):
    c.ellipse(cx - r * 0.5, cy - r * 0.3, r * 0.55, fill=fill)
    c.ellipse(cx + r * 0.5, cy - r * 0.3, r * 0.55, fill=fill)
    c.poly([(cx - r * 1.03, cy - r * 0.05), (cx + r * 1.03, cy - r * 0.05), (cx, cy + r * 1.05)], fill=fill)
    if broken:
        c.line([(cx, cy - r * 0.7), (cx - 8, cy - 5), (cx + 8, cy + 14), (cx - 2, cy + r * 0.9)],
               fill=BG, width=6)


def moneybag(c, cx, cy, r=60):
    c.ellipse(cx, cy + r * 0.2, r, r * 0.95, fill=AMBER, outline=NAVY, width=4)
    c.poly([(cx - r * 0.35, cy - r * 0.62), (cx + r * 0.35, cy - r * 0.62), (cx + r * 0.2, cy - r * 0.9),
            (cx - r * 0.2, cy - r * 0.9)], fill=AMBER, outline=NAVY, width=4)
    c.text(cx, cy + r * 0.2, "$", "ExtraBold", int(r * 1.0), NAVY, anchor="mm")


def banknote(c, cx, cy, w=120, h=64, fill=GREEN):
    c.rrect(cx - w / 2, cy - h / 2, w, h, r=8, fill=fill, outline=NAVY, width=3)
    c.ellipse(cx, cy, h * 0.27, fill="#BFE8CB", outline=NAVY, width=2)
    c.text(cx, cy, "$", "ExtraBold", int(h * 0.38), NAVY, anchor="mm")


def wallet(c, cx, cy, w=110):
    h = w * 0.72
    c.rrect(cx - w / 2, cy - h / 2, w, h, r=14, fill="#8B5A2B", outline=NAVY, width=4)
    c.rrect(cx + w * 0.1, cy - h * 0.14, w * 0.4, h * 0.3, r=8, fill=AMBER, outline=NAVY, width=3)


def bottle(c, cx, cy, h=130, fill=PURPLE):
    c.rrect(cx - h * 0.28, cy - h * 0.2, h * 0.56, h * 0.7, r=14, fill=fill, outline=NAVY, width=4)
    c.rect(cx - h * 0.1, cy - h * 0.55, h * 0.2, h * 0.38, fill=fill, outline=NAVY, width=4)
    c.rect(cx - h * 0.14, cy - h * 0.62, h * 0.28, h * 0.1, fill=NAVY)
    c.text(cx, cy + h * 0.14, "!", "ExtraBold", int(h * 0.38), WHITE, anchor="mm")


def lightning(c, cx, cy, h=120, fill=AMBER):
    pts = [(cx + h * 0.1, cy - h / 2), (cx - h * 0.25, cy + h * 0.05), (cx - h * 0.02, cy + h * 0.05),
           (cx - h * 0.12, cy + h / 2), (cx + h * 0.28, cy - h * 0.1), (cx + h * 0.03, cy - h * 0.1)]
    c.poly(pts, fill=fill, outline=NAVY, width=3)


def speech(c, x, y, w, h, fill=WHITE, tail="left", outline=NAVY):
    c.rrect(x, y, w, h, r=28, fill=fill, outline=outline, width=4)
    if tail == "left":
        c.poly([(x + 40, y + h - 4), (x + 20, y + h + 40), (x + 85, y + h - 4)], fill=fill)
        c.line([(x + 40, y + h), (x + 20, y + h + 40), (x + 85, y + h)], fill=outline, width=4)
        c.line([(x + 41, y + h - 1), (x + 84, y + h - 1)], fill=fill, width=6, round_ends=False)
    else:
        c.poly([(x + w - 40, y + h - 4), (x + w - 20, y + h + 40), (x + w - 85, y + h - 4)], fill=fill)
        c.line([(x + w - 40, y + h), (x + w - 20, y + h + 40), (x + w - 85, y + h)], fill=outline, width=4)
        c.line([(x + w - 41, y + h - 1), (x + w - 84, y + h - 1)], fill=fill, width=6, round_ends=False)


def thought(c, cx, cy, rx, ry, tail_to):
    """Nube de pensamiento con burbujitas hacia tail_to (x, y)."""
    tx, ty = tail_to
    for f, r in ((0.45, 15), (0.66, 11), (0.84, 7)):
        c.ellipse(cx + (tx - cx) * f, cy + ry + (ty - cy - ry) * f, r, fill=WHITE, outline=NAVY, width=3)
    c.ellipse(cx, cy, rx, ry, fill=WHITE, outline=NAVY, width=4)


def target(c, cx, cy, r=60):
    for rr, col in ((r, WHITE), (r * 0.72, RED), (r * 0.46, WHITE), (r * 0.22, RED)):
        c.ellipse(cx, cy, rr, fill=col, outline=NAVY, width=3)


def scale_justice(c, cx, cy, w=360, left=None, right=None, tilt=0):
    """Balanza. tilt>0 baja el plato derecho."""
    c.rect(cx - 8, cy - 150, 16, 240, fill=NAVY)
    c.rrect(cx - 80, cy + 80, 160, 26, r=10, fill=NAVY)
    ty = cy - 150
    lx, rx = cx - w / 2, cx + w / 2
    ly, ry = ty + 30 - tilt, ty + 30 + tilt
    c.line([(lx, ly), (rx, ry)], fill=NAVY, width=10)
    c.ellipse(cx, ty, 18, fill=AMBER, outline=NAVY, width=3)
    for (px, py) in ((lx, ly), (rx, ry)):
        c.line([(px, py), (px - 70, py + 150)], fill=NAVY, width=4)
        c.line([(px, py), (px + 70, py + 150)], fill=NAVY, width=4)
        c.d.pieslice([(px - 90) * S, (py + 100) * S, (px + 90) * S, (py + 200) * S], 0, 180,
                     fill=AMBER, outline=NAVY, width=3 * S)
    return (lx, ly + 90), (rx, ry + 90)


def shield(c, cx, cy, w=170, fill=TEAL, check=True):
    h = w * 1.2
    pts = [(cx - w / 2, cy - h / 2), (cx + w / 2, cy - h / 2), (cx + w / 2, cy + h * 0.05),
           (cx, cy + h / 2), (cx - w / 2, cy + h * 0.05)]
    c.poly(pts, fill=fill, outline=NAVY, width=5)
    if check:
        c.line([(cx - w * 0.22, cy), (cx - w * 0.05, cy + h * 0.17), (cx + w * 0.26, cy - h * 0.17)],
               fill=WHITE, width=14)


def check(c, cx, cy, r=26, fill=GREEN):
    c.ellipse(cx, cy, r, fill=fill)
    c.line([(cx - r * 0.45, cy + 1), (cx - r * 0.1, cy + r * 0.38), (cx + r * 0.5, cy - r * 0.35)],
           fill=WHITE, width=max(4, r * 0.22))


def cross(c, cx, cy, r=26, fill=RED):
    c.ellipse(cx, cy, r, fill=fill)
    k = r * 0.42
    c.line([(cx - k, cy - k), (cx + k, cy + k)], fill=WHITE, width=max(4, r * 0.22))
    c.line([(cx - k, cy + k), (cx + k, cy - k)], fill=WHITE, width=max(4, r * 0.22))


def arrow(c, x0, y0, x1, y1, fill=NAVY, width=8, head=26):
    c.line([(x0, y0), (x1, y1)], fill=fill, width=width)
    ang = math.atan2(y1 - y0, x1 - x0)
    p1 = (x1 - head * math.cos(ang - 0.45), y1 - head * math.sin(ang - 0.45))
    p2 = (x1 - head * math.cos(ang + 0.45), y1 - head * math.sin(ang + 0.45))
    c.poly([(x1, y1), p1, p2], fill=fill)


def gavel(c, cx, cy, s=1.0, fill="#8B5A2B"):
    c.rrect(cx - 70 * s, cy - 40 * s, 120 * s, 56 * s, r=10 * s, fill=fill, outline=NAVY, width=4)
    c.line([(cx - 5 * s, cy + 15 * s), (cx + 70 * s, cy + 90 * s)], fill=fill, width=22 * s)
    c.rrect(cx - 100 * s, cy + 100 * s, 240 * s, 22 * s, r=8 * s, fill=NAVY)


def thermometer(c, cx, cy, h=220, level=0.9):
    c.rrect(cx - 18, cy - h / 2, 36, h, r=18, fill=WHITE, outline=NAVY, width=4)
    c.ellipse(cx, cy + h / 2 + 6, 34, fill=RED, outline=NAVY, width=4)
    c.rrect(cx - 9, cy - h / 2 + h * (1 - level), 18, h * level, r=9, fill=RED)


def warning(c, cx, cy, w=130, fill=AMBER):
    h = w * 0.88
    c.poly([(cx, cy - h / 2), (cx + w / 2, cy + h / 2), (cx - w / 2, cy + h / 2)], fill=fill,
           outline=NAVY, width=5)
    c.text(cx, cy + h * 0.12, "!", "ExtraBold", int(w * 0.55), NAVY, anchor="mm")


def phone(c, cx, cy, h=120):
    w = h * 0.55
    c.rrect(cx - w / 2, cy - h / 2, w, h, r=12, fill=NAVY)
    c.rrect(cx - w / 2 + 6, cy - h / 2 + 10, w - 12, h - 26, r=6, fill="#9ED1F0")


def document(c, cx, cy, w=120, h=150, lines=4, stamp=None):
    c.rrect(cx - w / 2, cy - h / 2, w, h, r=10, fill=WHITE, outline=NAVY, width=4)
    for i in range(lines):
        c.line([(cx - w * 0.33, cy - h * 0.3 + i * h * 0.17), (cx + w * 0.33, cy - h * 0.3 + i * h * 0.17)],
               fill=GREY, width=5)
    if stamp:
        c.ellipse(cx + w * 0.22, cy + h * 0.25, w * 0.18, fill=stamp)


def brain(c, cx, cy, r=70, fill="#F4A6B8"):
    c.ellipse(cx - r * 0.45, cy, r * 0.65, r * 0.8, fill=fill, outline=NAVY, width=4)
    c.ellipse(cx + r * 0.45, cy, r * 0.65, r * 0.8, fill=fill, outline=NAVY, width=4)
    c.line([(cx, cy - r * 0.7), (cx, cy + r * 0.7)], fill=NAVY, width=3)
    c.arc(cx - r * 0.45, cy - r * 0.1, r * 0.3, 180, 330, fill=NAVY, width=3)
    c.arc(cx + r * 0.45, cy + r * 0.15, r * 0.3, 20, 190, fill=NAVY, width=3)


def banana(c, cx, cy, w=100):
    c.d.pieslice([(cx - w / 2) * S, (cy - w / 2) * S, (cx + w / 2) * S, (cy + w / 2) * S], 20, 160,
                 fill="#F6DC4E", outline=NAVY, width=3 * S)


def puzzle(c, cx, cy, s=1.0, fill=BLUE, knob="right"):
    """Pieza de puzzle simple (cuadrado con una perilla)."""
    w = 150 * s
    c.rrect(cx - w / 2, cy - w / 2, w, w, r=14 * s, fill=fill, outline=NAVY, width=4)
    if knob == "right":
        c.ellipse(cx + w / 2 + 6 * s, cy, 30 * s, fill=fill, outline=NAVY, width=4)
        c.rect(cx + w / 2 - 8 * s, cy - 22 * s, 14 * s, 44 * s, fill=fill)
    else:
        c.ellipse(cx - w / 2 + 6 * s, cy, 30 * s, fill=BG, outline=NAVY, width=4)


def chip(c, x, y, txt, fill=NAVY, color=WHITE, size=34, pad=26, weight="Bold"):
    tw, th = c.text_size(txt, weight, size)
    c.rrect(x, y, tw + pad * 2, size * 1.7, r=size * 0.85, fill=fill)
    c.text(x + pad, y + size * 0.85, txt, weight, size, color, anchor="lm")
    return tw + pad * 2


# ======================= ICONOS ADICIONALES (lote 2) =======================

def leaf(c, cx, cy, s=1.0, fill=GREEN):
    """Brote / planta simple."""
    c.line([(cx, cy + 60 * s), (cx, cy - 10 * s)], fill=NAVY, width=7 * s)
    c.ellipse(cx - 30 * s, cy - 20 * s, 34 * s, 20 * s, fill=fill, outline=NAVY, width=3)
    c.ellipse(cx + 30 * s, cy - 36 * s, 34 * s, 20 * s, fill=fill, outline=NAVY, width=3)
    c.ellipse(cx, cy + 64 * s, 40 * s, 10 * s, fill="#8B5A2B")


def pill(c, cx, cy, w=110, fill=RED):
    h = w * 0.42
    c.rrect(cx - w / 2, cy - h / 2, w, h, r=h / 2, fill=WHITE, outline=NAVY, width=4)
    c.d.pieslice([(cx - w / 2) * S, (cy - h / 2) * S, (cx - w / 2 + h) * S, (cy + h / 2) * S], 90, 270, fill=fill)
    c.rect(cx - w / 2 + h / 2, cy - h / 2 + 2, w / 2 - h / 2, h - 4, fill=fill)
    c.rrect(cx - w / 2, cy - h / 2, w, h, r=h / 2, outline=NAVY, width=4)
    c.line([(cx, cy - h / 2), (cx, cy + h / 2)], fill=NAVY, width=4, round_ends=False)


def box(c, cx, cy, w=110, fill="#C99A5B"):
    c.rect(cx - w / 2, cy - w / 2, w, w, fill=fill, outline=NAVY, width=4)
    c.rect(cx - 10, cy - w / 2, 20, w, fill="#E9CFA3")
    c.line([(cx - w / 2, cy - w / 2), (cx + w / 2, cy - w / 2)], fill=NAVY, width=4, round_ends=False)


def truck(c, x, y, w=300, color=BLUE):
    """x,y = esquina inferior izquierda."""
    h = w * 0.36
    c.rect(x, y - h, w * 0.66, h, fill=WHITE, outline=NAVY, width=4)
    c.rrect(x + w * 0.68, y - h * 0.75, w * 0.32, h * 0.75, r=12, fill=color, outline=NAVY, width=4)
    c.rect(x + w * 0.76, y - h * 0.65, w * 0.14, h * 0.3, fill="#BFE3F5")
    for wx in (x + w * 0.16, x + w * 0.52, x + w * 0.86):
        c.ellipse(wx, y + 2, w * 0.06, fill=NAVY)
        c.ellipse(wx, y + 2, w * 0.025, fill=GREY)


def card(c, cx, cy, w=150, fill=BLUE):
    h = w * 0.63
    c.rrect(cx - w / 2, cy - h / 2, w, h, r=14, fill=fill, outline=NAVY, width=4)
    c.rect(cx - w / 2, cy - h * 0.22, w, h * 0.2, fill=NAVY)
    c.rrect(cx - w * 0.38, cy + h * 0.12, w * 0.26, h * 0.2, r=4, fill=AMBER)
    c.line([(cx + w * 0.1, cy + h * 0.25), (cx + w * 0.38, cy + h * 0.25)], fill=WHITE, width=5)


def laptop(c, cx, cy, w=150, fill=NAVY):
    h = w * 0.6
    c.rrect(cx - w * 0.42, cy - h / 2, w * 0.84, h, r=10, fill=fill)
    c.rect(cx - w * 0.37, cy - h / 2 + 8, w * 0.74, h - 16, fill="#9ED1F0")
    c.rrect(cx - w / 2, cy + h / 2, w, h * 0.12, r=6, fill=GREY, outline=NAVY, width=3)


def briefcase(c, cx, cy, w=130, fill="#8B5A2B"):
    h = w * 0.7
    c.rrect(cx - w * 0.2, cy - h / 2 - 14, w * 0.4, 26, r=8, outline=NAVY, width=5)
    c.rrect(cx - w / 2, cy - h / 2, w, h, r=14, fill=fill, outline=NAVY, width=4)
    c.rect(cx - w / 2, cy - 4, w, 8, fill=NAVY)
    c.rrect(cx - 12, cy - 12, 24, 22, r=5, fill=AMBER, outline=NAVY, width=3)


def badge(c, cx, cy, r=50, fill=BLUE):
    pts = []
    for i in range(12):
        ang = math.pi * i / 6
        rr = r if i % 2 == 0 else r * 0.82
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    c.poly(pts, fill=fill, outline=NAVY, width=3)
    c.ellipse(cx, cy, r * 0.52, fill=AMBER, outline=NAVY, width=3)
    star(c, cx, cy, r * 0.34, NAVY, points=5)


def handcuffs(c, cx, cy, r=34):
    c.ellipse(cx - r * 1.2, cy, r, outline=NAVY, width=9)
    c.ellipse(cx + r * 1.2, cy, r, outline=NAVY, width=9)
    c.line([(cx - r * 0.2, cy), (cx + r * 0.2, cy)], fill=NAVY, width=8)


def family(c, cx, cy, s=1.0):
    for dx, r, col in ((-34, 20, BLUE), (34, 20, RED), (0, 14, AMBER)):
        c.ellipse(cx + dx * s, cy - 24 * s + (12 * s if dx == 0 else 0), r * s, fill=SKIN, outline=NAVY, width=3)
        c.rrect(cx + dx * s - r * s, cy - 2 * s + (12 * s if dx == 0 else 0), 2 * r * s, 48 * s - (12 * s if dx == 0 else 0),
                r=r * s * 0.8, fill=col)


def two_heads(c, cx, cy, s=1.0):
    for dx, col in ((-30, RED), (30, BLUE)):
        c.ellipse(cx + dx * s, cy - 18 * s, 22 * s, fill=SKIN, outline=NAVY, width=3)
        c.rrect(cx + dx * s - 26 * s, cy + 6 * s, 52 * s, 46 * s, r=18 * s, fill=col)


def chat(c, cx, cy, w=130, fill=WHITE):
    c.rrect(cx - w / 2, cy - w * 0.32, w, w * 0.6, r=22, fill=fill, outline=NAVY, width=4)
    c.poly([(cx - w * 0.25, cy + w * 0.26), (cx - w * 0.35, cy + w * 0.5), (cx - w * 0.05, cy + w * 0.26)], fill=fill)
    c.line([(cx - w * 0.25, cy + w * 0.27), (cx - w * 0.35, cy + w * 0.5), (cx - w * 0.05, cy + w * 0.27)], fill=NAVY, width=4)
    for i in (-1, 0, 1):
        c.ellipse(cx + i * w * 0.22, cy - w * 0.02, 8, fill=NAVY)


def moon(c, cx, cy, r=46):
    c.ellipse(cx, cy, r, fill=AMBER)
    c.ellipse(cx + r * 0.45, cy - r * 0.25, r * 0.85, fill=NAVY)


def ladder(c, x, y, h=200, w=60):
    c.line([(x, y), (x + 20, y - h)], fill="#8B5A2B", width=8)
    c.line([(x + w, y), (x + w + 20, y - h)], fill="#8B5A2B", width=8)
    for i in range(1, 6):
        t = i / 6
        c.line([(x + 20 * t, y - h * t), (x + w + 20 * t, y - h * t)], fill="#8B5A2B", width=6)


def stop_hand(c, cx, cy, r=60):
    pts = [(cx + r * math.cos(math.pi / 8 + i * math.pi / 4), cy + r * math.sin(math.pi / 8 + i * math.pi / 4))
           for i in range(8)]
    c.poly(pts, fill=RED, outline=NAVY, width=4)
    c.text(cx, cy, "NO", "ExtraBold", int(r * 0.85), WHITE, anchor="mm")


def clock(c, cx, cy, r=50):
    c.ellipse(cx, cy, r, fill=WHITE, outline=NAVY, width=5)
    c.line([(cx, cy), (cx, cy - r * 0.6)], fill=NAVY, width=5)
    c.line([(cx, cy), (cx + r * 0.45, cy + r * 0.2)], fill=RED, width=5)


def lock(c, cx, cy, w=90, fill=AMBER):
    c.arc(cx, cy - w * 0.3, w * 0.32, 180, 360, fill=NAVY, width=9)
    c.rrect(cx - w / 2, cy - w * 0.2, w, w * 0.75, r=12, fill=fill, outline=NAVY, width=4)
    c.ellipse(cx, cy + w * 0.12, 9, fill=NAVY)


def sheet_stack(c, cx, cy, w=110, h=140, fill=WHITE):
    for k in (2, 1, 0):
        document(c, cx + k * 14, cy - k * 10, w, h, lines=3 if k == 0 else 0)


def pencil_sign(c, cx, cy, w=130):
    document(c, cx, cy, w, w * 1.2, lines=3)
    c.line([(cx - w * 0.2, cy + w * 0.5), (cx + w * 0.35, cy + w * 0.05)], fill=AMBER, width=12)
    c.poly([(cx - w * 0.28, cy + w * 0.6), (cx - w * 0.22, cy + w * 0.46), (cx - w * 0.12, cy + w * 0.56)], fill=NAVY)
