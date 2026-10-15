"""Escenas del lote 2: concursos, causas de justificación, defraudaciones,
integridad sexual y estupefacientes."""
import math
from kit import *
from scenes import ground


# ------------------------------------------------------------ constructores genéricos

def _label(c, cx, y, txt, size=22, col=NAVY, w=230):
    c.paragraph(cx - w / 2, y, txt, "ExtraBold", size, col, max_w=w, lh=1.12, align="center")


def tiles(items, title=None, cols=3, size=22):
    """Cuadrícula de iconos con leyenda. items = [(leyenda, fn(c, cx, cy))]."""
    def scene(c, X, Y, Wd, Ht):
        top = Y + (100 if title else 40)
        if title:
            c.text(X + Wd / 2, Y + 50, title, "ExtraBold", 38, NAVY, anchor="mm")
        rows = math.ceil(len(items) / cols)
        gap = 22
        tw = (Wd - 100 - (cols - 1) * gap) / cols
        th = min(250, (Y + Ht - 40 - top - (rows - 1) * gap) / rows)
        for i, (lbl, fn) in enumerate(items):
            r_, k = divmod(i, cols)
            x = X + 50 + k * (tw + gap)
            y = top + r_ * (th + gap)
            c.rrect(x, y, tw, th, r=22, fill=WHITE, outline=NAVY, width=4)
            fn(c, x + tw / 2, y + th * 0.38)
            _label(c, x + tw / 2, y + th * 0.72, lbl, size, NAVY, tw - 20)
    return scene


def levels(items, highlight=None, title=None):
    """Barras escalonadas. items = [(leyenda, color)]."""
    def scene(c, X, Y, Wd, Ht):
        gy = ground(c, X, Y, Wd, Ht)
        n = len(items)
        bw = (Wd - 140 - (n - 1) * 24) / n
        if title:
            c.text(X + Wd / 2, Y + 50, title, "ExtraBold", 36, NAVY, anchor="mm")
        for i, (lbl, col) in enumerate(items):
            h = 150 + i * (330 / max(1, n - 1)) if n > 1 else 300
            on = highlight is None or highlight == i
            x = X + 70 + i * (bw + 24)
            c.rrect(x, gy - h, bw, h, r=18, fill=col if on else "#CFCABB")
            c.text(x + bw / 2, gy - h + 44, str(i + 1), "ExtraBold", 54, WHITE if on else "#EFEBDD", anchor="mm")
            _label(c, x + bw / 2, gy + 24, lbl, 22, NAVY if on else GREY, bw)
    return scene


def compare(left, right, split=0.5):
    """Dos mitades. left/right = (titulo, color, fn(c, cx, gy, w), pie)."""
    def scene(c, X, Y, Wd, Ht):
        gy = ground(c, X, Y, Wd, Ht)
        half = Wd * split
        c.line([(X + half, Y + 30), (X + half, Y + Ht - 30)], fill=GREY, width=3)
        for (ttl, col, fn, foot), x0, w_ in ((left, X, half), (right, X + half, Wd - half)):
            c.text(x0 + w_ / 2, Y + 50, ttl, "ExtraBold", 36, col, anchor="mm")
            fn(c, x0 + w_ / 2, gy, w_)
            if foot:
                c.paragraph(x0 + 30, Y + Ht - 62, foot, "Bold", 26, NAVY, max_w=w_ - 60, lh=1.1, align="center")
    return scene


def hero(fn, caption=None):
    def scene(c, X, Y, Wd, Ht):
        gy = ground(c, X, Y, Wd, Ht)
        fn(c, X, Y, Wd, Ht, gy)
        if caption:
            c.text(X + Wd / 2, Y + 50, caption, "ExtraBold", 34, NAVY, anchor="mm")
    return scene


# ------------------------------------------------------------ iconos para tiles
def i_heart_b(c, cx, cy): heart(c, cx, cy, 40, fill=PURPLE, broken=True)
def i_heart(c, cx, cy): heart(c, cx, cy, 40)
def i_family(c, cx, cy): family(c, cx, cy + 4, 1.2)
def i_warn(c, cx, cy): warning(c, cx, cy, 100)
def i_two(c, cx, cy): two_heads(c, cx, cy + 6, 1.2)
def i_badge(c, cx, cy): badge(c, cx, cy, 52)
def i_house(c, cx, cy): house(c, cx - 62, cy + 52, w=124, h=104)
def i_mask(c, cx, cy):
    c.ellipse(cx, cy, 40, fill=SKIN, outline=NAVY, width=3); mask(c, cx, cy, 40)
def i_doc(c, cx, cy): document(c, cx, cy, 90, 112, lines=3, stamp=RED)
def i_phone(c, cx, cy): phone(c, cx, cy, 110)
def i_bag(c, cx, cy): moneybag(c, cx, cy + 4, 46)
def i_leaf(c, cx, cy): leaf(c, cx, cy - 6, 1.0)
def i_pill(c, cx, cy): pill(c, cx, cy, 120)
def i_truck(c, cx, cy): truck(c, cx - 70, cy + 40, 140)
def i_brief(c, cx, cy): briefcase(c, cx, cy, 100)
def i_bottle(c, cx, cy): bottle(c, cx, cy + 6, 110)
def i_box(c, cx, cy): box(c, cx, cy, 80)
def i_lock(c, cx, cy): lock(c, cx, cy, 80)
def i_card(c, cx, cy): card(c, cx, cy, 120)
def i_laptop(c, cx, cy): laptop(c, cx, cy, 120)
def i_pen(c, cx, cy): pencil_sign(c, cx, cy, 90)
def i_bolt(c, cx, cy): lightning(c, cx, cy, 100)


# ============================================================ CONCURSOS

def s_aparente(c, X, Y, Wd, Ht):
    star(c, X + 120, Y + 230, 60, AMBER)
    c.text(X + 120, Y + 230, "1", "ExtraBold", 54, NAVY, anchor="mm")
    c.text(X + 120, Y + 320, "un hecho", "Bold", 28, NAVY, anchor="mm")
    arrow(c, X + 195, Y + 215, X + 370, Y + 160, fill=TEAL)
    arrow(c, X + 195, Y + 245, X + 370, Y + 310, fill=GREY)
    c.rrect(X + 380, Y + 105, 230, 100, r=20, fill=TEAL)
    c.text(X + 495, Y + 155, "NORMA A", "ExtraBold", 32, WHITE, anchor="mm")
    check(c, X + 640, Y + 105, 30)
    c.rrect(X + 380, Y + 260, 230, 100, r=20, fill="#C9C3B2")
    c.text(X + 495, Y + 310, "NORMA B", "ExtraBold", 32, GREY, anchor="mm")
    cross(c, X + 640, Y + 260, 30, fill=GREY)
    c.text(X + Wd / 2, Y + 420, "una sola ley desplaza a la otra", "ExtraBold", 32, NAVY, anchor="mm")
    for i, t in enumerate(("ESPECIALIDAD", "SUBSIDIARIEDAD", "CONSUNCIÓN")):
        w_ = (Wd - 120 - 40) / 3
        x = X + 60 + i * (w_ + 20)
        c.rrect(x, Y + 500, w_, 90, r=18, fill=WHITE, outline=TEAL, width=4)
        c.text(x + w_ / 2, Y + 545, t, "ExtraBold", 22, TEAL, anchor="mm")


def s_continuado(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    xs = [X + 160, X + 410, X + 660]
    for i, x in enumerate(xs):
        star(c, x, Y + 250, 56, RED)
        c.text(x, Y + 250, str(i + 1), "ExtraBold", 48, WHITE, anchor="mm")
        c.line([(x, Y + 320), (x, Y + 370)], fill=NAVY, width=5)
    c.line([(xs[0], Y + 370), (xs[-1], Y + 370)], fill=NAVY, width=5)
    c.line([(xs[1], Y + 370), (xs[1], Y + 410)], fill=NAVY, width=5)
    c.rrect(X + 270, Y + 410, 280, 90, r=22, fill=NAVY)
    c.text(X + 410, Y + 455, "1 SOLO DELITO", "ExtraBold", 32, WHITE, anchor="mm")
    c.text(X + Wd / 2, Y + 80, "VARIOS ACTOS", "ExtraBold", 38, NAVY, anchor="mm")
    c.text(X + Wd / 2, Y + 590, "una misma decisión delictiva", "Bold", 30, TEAL, anchor="mm")


def s_calculo(c, X, Y, Wd, Ht):
    c.text(X + 60, Y + 55, "Ejemplo: 3 hechos independientes", "ExtraBold", 36, NAVY)
    rows = [("A", 3, 10, BLUE), ("B", 1, 6, AMBER), ("C", 2, 8, RED)]
    x0, scale = X + 130, 40
    for i, (n, mn, mx, col) in enumerate(rows):
        y = Y + 140 + i * 110
        c.text(X + 60, y + 30, n, "ExtraBold", 48, col, anchor="lm")
        c.rrect(x0, y, mx * scale, 60, r=14, fill=col)
        c.text(x0 + 16, y + 30, f"{mn} a {mx} años", "ExtraBold", 28, WHITE, anchor="lm")
    c.rrect(X + 60, Y + 490, Wd - 120, 190, r=26, fill=NAVY)
    c.text(X + 100, Y + 535, "Mínimo: el mayor de los mínimos = 3", "ExtraBold", 32, WHITE, anchor="lm")
    c.text(X + 100, Y + 592, "Máximo: 10 + 6 + 8 = 24  (tope: 50)", "ExtraBold", 32, WHITE, anchor="lm")
    c.text(X + 100, Y + 650, "PENA: 3 a 24 años", "ExtraBold", 44, AMBER, anchor="lm")


def s_unificacion(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    for i, y in enumerate((Y + 150, Y + 330)):
        document(c, X + 160, y, 150, 170, lines=4, stamp=RED)
        c.text(X + 160, y + 105, f"SENTENCIA {i + 1}", "ExtraBold", 22, NAVY, anchor="mm")
    arrow(c, X + 260, Y + 170, X + 450, Y + 270, fill=NAVY)
    arrow(c, X + 260, Y + 320, X + 450, Y + 290, fill=NAVY)
    document(c, X + 590, Y + 270, 200, 240, lines=5, stamp=GREEN)
    c.text(X + 590, Y + 410, "PENA ÚNICA", "ExtraBold", 28, NAVY, anchor="mm")
    gavel(c, X + 640, gy - 90, 0.7)


# ============================================================ CAUSAS DE JUSTIFICACIÓN

def s_just_flujo(c, X, Y, Wd, Ht):
    c.rrect(X + 50, Y + 250, 220, 110, r=22, fill=BLUE)
    c.text(X + 160, Y + 305, "CONDUCTA TÍPICA", "ExtraBold", 28, WHITE, anchor="mm")
    arrow(c, X + 275, Y + 305, X + 345, Y + 305)
    c.poly([(X + 450, Y + 205), (X + 560, Y + 305), (X + 450, Y + 405), (X + 340, Y + 305)], fill=AMBER, outline=NAVY, width=4)
    c.text(X + 450, Y + 300, "¿CAUSA DE", "ExtraBold", 22, NAVY, anchor="mm")
    c.text(X + 450, Y + 328, "JUSTIFICACIÓN?", "ExtraBold", 22, NAVY, anchor="mm")
    arrow(c, X + 500, Y + 255, X + 640, Y + 150, fill=GREEN)
    arrow(c, X + 500, Y + 355, X + 640, Y + 460, fill=RED)
    c.text(X + 610, Y + 235, "SÍ", "ExtraBold", 30, GREEN, anchor="mm")
    c.text(X + 610, Y + 380, "NO", "ExtraBold", 30, RED, anchor="mm")
    c.rrect(X + 650, Y + 90, 250, 120, r=22, fill=GREEN)
    c.text(X + 775, Y + 150, "NO HAY DELITO", "ExtraBold", 26, WHITE, anchor="mm")
    c.rrect(X + 650, Y + 430, 250, 120, r=22, fill=RED)
    c.text(X + 775, Y + 490, "ANTIJURÍDICA", "ExtraBold", 26, WHITE, anchor="mm")


def s_privilegiada(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    moon(c, X + 110, Y + 110, 44)
    for dx, dy in ((0, 0), (90, 40), (170, -10)):
        star(c, X + 260 + dx, Y + 90 + dy, 8, WHITE, points=5)
    house(c, X + 420, gy + 15, w=360, h=320)
    ladder(c, X + 360, gy, 300)
    person(c, X + 230, gy + 8, h=280, color=INK, pose="run", face="angry")
    mask(c, X + 230, gy - 246, 34)
    person(c, X + 580, gy + 8, h=200, color=BLUE, pose="stand", face="scared")
    c.text(X + 110, Y + 190, "DE NOCHE", "ExtraBold", 30, AMBER_D, anchor="mm")


def s_terceros(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 130, gy + 8, h=290, color=RED, pose="point", face="angry")
    lightning(c, X + 250, Y + 220, 100)
    shield(c, X + 330, gy - 150, 130)
    person(c, X + 520, gy + 8, h=290, color=BLUE, pose="reach", flip=True)
    person(c, X + 760, gy + 8, h=250, color=TEAL, pose="stand", face="scared")
    c.text(X + 130, Y + 60, "AGRESOR", "ExtraBold", 30, RED, anchor="mm")
    c.text(X + 520, Y + 60, "TERCERO", "ExtraBold", 30, BLUE, anchor="mm")
    c.text(X + 760, Y + 60, "VÍCTIMA", "ExtraBold", 30, TEAL, anchor="mm")


def s_deber(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 230, gy + 8, h=300, color=BLUE, pose="point", face="happy")
    badge(c, X + 232, gy - 150, 34)
    person(c, X + 560, gy + 8, h=290, color=INK, pose="stand", face="scared")
    handcuffs(c, X + 560, gy - 120, 22)
    document(c, X + 430, Y + 190, 130, 160, lines=4, stamp=GREEN)
    c.text(X + 430, Y + 80, "ORDEN LEGAL", "ExtraBold", 26, TEAL, anchor="mm")
    check(c, X + 720, Y + 120, 36)


def n_just(c, cx, gy, w):
    scale_justice(c, cx, gy - 230, w=230, tilt=34)
    heart(c, cx + 115, gy - 230 + 118 + 34 - 10, 34)
    c.text(cx + 115, gy - 100, "vida", "Bold", 24, NAVY, anchor="mm")
    c.rect(cx - 140, gy - 230 + 118 - 34 - 32, 46, 36, fill="#BFE3F5", outline=NAVY, width=3)
    c.text(cx - 117, gy - 70, "vidrio", "Bold", 24, NAVY, anchor="mm")


def n_exc(c, cx, gy, w):
    scale_justice(c, cx, gy - 230, w=230, tilt=0)
    heart(c, cx - 115, gy - 230 + 118 - 10, 30)
    heart(c, cx + 115, gy - 230 + 118 - 10, 30, fill=BLUE)
    c.text(cx, gy - 70, "vida  =  vida", "Bold", 24, NAVY, anchor="mm")


def s_exceso(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    xl = X + 470
    for yy in range(int(Y + 110), int(gy) - 10, 36):
        c.line([(xl, yy), (xl, yy + 20)], fill=RED, width=6)
    c.text(xl, Y + 70, "LÍMITE", "ExtraBold", 32, RED, anchor="mm")
    person(c, X + 170, gy + 8, h=290, color=BLUE, pose="point", face="angry")
    arrow(c, X + 330, Y + 300, X + 700, Y + 300, fill=AMBER, width=14, head=36)
    c.text(X + 350, Y + 255, "defensa", "Bold", 28, NAVY, anchor="mm")
    c.text(X + 620, Y + 255, "exceso", "ExtraBold", 28, RED, anchor="mm")
    person(c, X + 770, gy + 8, h=250, color=INK, face="scared", flip=True)


def s_consentimiento(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 200, gy + 8, h=280, color=BLUE, face="happy")
    speech(c, X + 150, Y + 120, 160, 90, tail="left")
    c.text(X + 230, Y + 165, "Sí", "ExtraBold", 44, GREEN, anchor="mm")
    person(c, X + 600, gy + 8, h=290, color=WHITE, pose="point", face="happy", flip=True)
    c.rrect(X + 556, gy - 190, 90, 90, r=10, fill=WHITE)
    c.rect(X + 590, gy - 168, 22, 52, fill=RED)
    c.rect(X + 575, gy - 153, 52, 22, fill=RED)
    c.text(X + 400, Y + 60, "BIEN DISPONIBLE", "ExtraBold", 28, NAVY, anchor="mm")


def j_just(c, cx, gy, w):
    shield(c, cx, gy - 230, 170)
    c.text(cx, gy - 90, "el derecho lo permite", "Bold", 26, NAVY, anchor="mm")


def j_exc(c, cx, gy, w):
    brain(c, cx, gy - 260, 80)
    cross(c, cx, gy - 160, 28, fill=AMBER_D)
    c.text(cx, gy - 100, "ilícito, pero no reprochable", "Bold", 24, NAVY, anchor="mm")


def s_obediencia(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 170, gy + 8, h=300, color=AMBER, pose="point", face="angry")
    speech(c, X + 330, Y + 100, 230, 100, tail="left")
    c.text(X + 445, Y + 150, "¡Cumpla!", "ExtraBold", 36, NAVY, anchor="mm")
    document(c, X + 480, Y + 340, 120, 150, lines=4, stamp=RED)
    c.text(X + 480, Y + 430, "ORDEN", "ExtraBold", 24, NAVY, anchor="mm")
    person(c, X + 700, gy + 8, h=270, color=BLUE, pose="stand", face="scared", flip=True)


# ============================================================ ESTAFA Y DEFRAUDACIONES

def e_hurto(c, cx, gy, w):
    person(c, cx - 90, gy + 8, h=250, color=BLUE)
    person(c, cx + 80, gy + 8, h=240, color=INK, pose="reach", face="sly", flip=True)
    mask(c, cx + 80, gy - 206, 29)
    wallet(c, cx - 30, gy - 120, 66)


def e_estafa(c, cx, gy, w):
    person(c, cx - 100, gy + 8, h=250, color=RED, pose="reach", face="sly")
    person(c, cx + 110, gy + 8, h=250, color=BLUE, pose="reach", flip=True)
    banknote(c, cx + 5, gy - 140, 90, 50)
    document(c, cx - 22, gy - 200, 50, 60, lines=2)


def s_administracion(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 150, gy + 8, h=270, color=BLUE)
    c.text(X + 150, Y + 90, "TITULAR", "ExtraBold", 28, BLUE, anchor="mm")
    person(c, X + 450, gy + 8, h=290, color=AMBER, face="sly")
    briefcase(c, X + 450, gy - 110, 100)
    c.text(X + 450, Y + 90, "ADMINISTRADOR", "ExtraBold", 26, AMBER_D, anchor="mm")
    moneybag(c, X + 150, gy - 330, 44)
    arrow(c, X + 200, gy - 330, X + 380, gy - 240, fill=GREEN, width=8)
    arrow(c, X + 500, gy - 330, X + 740, gy - 250, fill=RED, width=10)
    c.text(X + 690, gy - 340, "lucro indebido", "Bold", 24, RED, anchor="mm")


def s_retencion(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 170, gy + 8, h=280, color=BLUE, pose="point", face="angry")
    speech(c, X + 120, Y + 110, 260, 90, tail="left")
    c.text(X + 250, Y + 155, "¡Devolvelo!", "ExtraBold", 30, NAVY, anchor="mm")
    person(c, X + 600, gy + 8, h=290, color=RED, face="sly", flip=True)
    box(c, X + 600, gy - 130, 90)
    c.text(X + 300, Y + 45, "depósito · comisión · administración", "Bold", 22, TEAL, anchor="mm")
    c.text(X + 690, Y + 120, "NO RESTITUYE", "ExtraBold", 28, RED, anchor="mm")


def s_tarjeta(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    card(c, X + 250, Y + 250, 260)
    chips = ["falsificada", "adulterada", "hurtada o robada", "perdida", "datos sin autorización"]
    for i, t in enumerate(chips):
        chip(c, X + 440, Y + 90 + i * 72, t, fill=RED if i < 3 else AMBER_D, size=24, pad=18)
    person(c, X + 200, gy + 8, h=240, color=INK, pose="reach", face="sly", flip=False)
    mask(c, X + 200, gy - 206, 29)


def s_informatica(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    laptop(c, X + 470, Y + 270, 330)
    lock(c, X + 470, Y + 255, 110, fill=RED)
    person(c, X + 190, gy + 8, h=270, color=INK, pose="reach", face="sly")
    mask(c, X + 190, gy - 236, 31)
    c.text(X + 470, Y + 60, "MANIPULACIÓN INFORMÁTICA", "ExtraBold", 30, NAVY, anchor="mm")
    banknote(c, X + 700, gy - 100, 120, 64)
    arrow(c, X + 560, Y + 430, X + 660, gy - 120, fill=RED, width=8)


# ============================================================ INTEGRIDAD SEXUAL

def s_integridad(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    shield(c, X + Wd / 2, Y + 270, 260, fill=PURPLE)
    c.text(X + Wd / 2, Y + 500, "LIBERTAD E INTEGRIDAD SEXUAL", "ExtraBold", 30, NAVY, anchor="mm")
    person(c, X + 130, gy + 8, h=250, color=BLUE)
    person(c, X + Wd - 130, gy + 8, h=250, color=TEAL, flip=True)


def s_abuso_simple(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 600, gy + 8, h=290, color=TEAL, pose="arms_up", face="scared")
    stop_hand(c, X + 470, Y + 250, 60)
    speech(c, X + 330, Y + 90, 190, 80, tail="right")
    c.text(X + 425, Y + 130, "¡No!", "ExtraBold", 40, RED, anchor="mm")
    person(c, X + 160, gy + 8, h=290, color=RED, pose="point", face="angry")


def s_estupro(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 200, gy + 8, h=310, color=RED, face="sly")
    person(c, X + 560, gy + 8, h=200, color=TEAL, face="scared")
    c.ellipse(X + 560, Y + 170, 62, fill=WHITE, outline=RED, width=8)
    c.text(X + 560, Y + 170, "<16", "ExtraBold", 48, RED, anchor="mm")
    c.text(X + 330, Y + 90, "MAYOR DE EDAD / PREEMINENCIA", "ExtraBold", 24, NAVY, anchor="mm")
    arrow(c, X + 290, Y + 300, X + 470, Y + 360, fill=RED, width=8)


def s_edades(c, X, Y, Wd, Ht):
    segs = [(0, 13, RED, "menor de 13"), (13, 16, AMBER, "menor de 16"), (16, 18, BLUE, "menor de 18"), (18, 24, GREY, "mayor")]
    x0, total, bw = X + 60, 24, Wd - 120
    y = Y + 110
    for a, b, col, lbl in segs:
        xa, xb = x0 + bw * a / total, x0 + bw * b / total
        c.rect(xa, y, xb - xa - 4, 90, fill=col)
    for v in (0, 13, 16, 18):
        c.text(x0 + bw * v / total, y + 125, str(v), "ExtraBold", 34, NAVY, anchor="mm")
    rows = [("Art. 119 · abuso sexual (menor de 13)", RED),
            ("Art. 120 · estupro (aprovecha inmadurez sexual)", AMBER_D),
            ("Art. 128 · pornografía infantil (menor de 18)", BLUE),
            ("Art. 131 · grooming (persona menor de edad)", PURPLE)]
    for i, (t, col) in enumerate(rows):
        yy = Y + 280 + i * 54
        c.ellipse(X + 80, yy + 22, 14, fill=col)
        c.text(X + 110, yy + 22, t, "SemiBold", 30, NAVY, anchor="lm")
    c.text(X + Wd / 2, Y + 50, "AÑOS DE EDAD", "ExtraBold", 34, NAVY, anchor="mm")


def s_pornografia(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    laptop(c, X + 330, Y + 300, 340)
    stop_hand(c, X + 330, Y + 290, 70)
    c.ellipse(X + 630, Y + 150, 64, fill=WHITE, outline=RED, width=10)
    c.text(X + 630, Y + 150, "<18", "ExtraBold", 50, RED, anchor="mm")
    for i, t in enumerate(("producir", "distribuir", "tener en su poder")):
        chip(c, X + 520, Y + 270 + i * 70, t, fill=NAVY, size=26, pad=20)


def s_grooming(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 170, gy + 8, h=300, color=RED, face="sly")
    phone(c, X + 255, gy - 140, 90)
    person(c, X + 620, gy + 8, h=190, color=TEAL)
    phone(c, X + 565, gy - 100, 70)
    chat(c, X + 330, Y + 180, 150)
    chat(c, X + 520, Y + 270, 130, fill="#CFE8DD")
    c.text(X + Wd / 2, Y + 70, "POR MEDIOS ELECTRÓNICOS", "ExtraBold", 28, NAVY, anchor="mm")


def s_accion_penal(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 170, gy + 8, h=280, color=TEAL, pose="point", face="scared")
    document(c, X + 430, Y + 220, 190, 240, lines=5, stamp=RED)
    c.text(X + 430, Y + 350, "DENUNCIA", "ExtraBold", 30, NAVY, anchor="mm")
    arrow(c, X + 290, Y + 250, X + 330, Y + 250, fill=NAVY)
    gavel(c, X + 690, gy - 110, 0.8)
    c.rrect(X + 250, Y + 70, 400, 70, r=20, fill=NAVY)
    c.text(X + 450, Y + 105, "de oficio si <18 o incapaz", "ExtraBold", 26, WHITE, anchor="mm")


def s_corrupcion(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 190, gy + 8, h=310, color=RED, pose="point", face="sly")
    person(c, X + 600, gy + 8, h=200, color=TEAL, face="scared")
    c.ellipse(X + 600, Y + 190, 60, fill=WHITE, outline=RED, width=8)
    c.text(X + 600, Y + 190, "<18", "ExtraBold", 46, RED, anchor="mm")
    c.text(X + 390, Y + 70, "AUNQUE HAYA CONSENTIMIENTO", "ExtraBold", 26, NAVY, anchor="mm")


def s_cooperacion(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 160, gy + 8, h=290, color=RED, pose="reach", face="angry")
    person(c, X + 450, gy + 8, h=270, color=AMBER, pose="reach", flip=True)
    family(c, X + 450, Y + 120, 1.0)
    person(c, X + 700, gy + 8, h=200, color=TEAL, face="scared")
    c.text(X + 160, Y + 60, "AUTOR", "ExtraBold", 28, RED, anchor="mm")
    c.text(X + 450, Y + 60, "COOPERA", "ExtraBold", 28, AMBER_D, anchor="mm")


# ============================================================ ESTUPEFACIENTES (Ley 23.737)

def s_comercio(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    truck(c, X + 60, gy + 10, 380)
    box(c, X + 150, gy - 70, 70)
    moneybag(c, X + 640, Y + 250, 70)
    arrow(c, X + 450, gy - 100, X + 560, Y + 280, fill=GREEN, width=8)
    for i, t in enumerate(("comerciar", "almacenar", "transportar", "distribuir")):
        chip(c, X + 60 + (i % 2) * 220, Y + 70 + (i // 2) * 70, t, fill=NAVY, size=24, pad=18)


def s_gratuito(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 200, gy + 8, h=290, color=RED, pose="reach", face="sly")
    person(c, X + 650, gy + 8, h=280, color=BLUE, pose="reach", flip=True)
    pill(c, X + 430, gy - 140, 110)
    c.rrect(X + 340, Y + 120, 180, 70, r=35, fill=GREEN)
    c.text(X + 430, Y + 155, "GRATIS", "ExtraBold", 30, WHITE, anchor="mm")


def s_siembra(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    for i, dx in enumerate((200, 320, 440)):
        leaf(c, X + dx, gy - 50, 1.3)
    house(c, X + 560, gy + 15, w=260, h=240)
    c.text(X + 330, Y + 80, "SIEMBRA · CULTIVO · GUARDA DE SEMILLAS", "ExtraBold", 26, NAVY, anchor="mm")
    c.text(X + 330, Y + 125, "para producir estupefacientes", "Bold", 26, TEAL, anchor="mm")


def s_introduccion(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    truck(c, X + 70, gy + 10, 340)
    c.rect(X + 470, gy - 280, 14, 280, fill=NAVY)
    c.rrect(X + 440, Y + 90, 220, 90, r=16, fill=BLUE)
    c.text(X + 550, Y + 135, "ADUANA", "ExtraBold", 34, WHITE, anchor="mm")
    arrow(c, X + 340, gy - 100, X + 740, gy - 100, fill=RED, width=10)
    c.text(X + 650, gy - 135, "destino alterado", "Bold", 24, RED, anchor="mm")


def s_organiza(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + Wd / 2, Y + 330, h=210, color=NAVY, face="sly")
    c.text(X + Wd / 2, Y + 60, "ORGANIZA O FINANCIA", "ExtraBold", 32, NAVY, anchor="mm")
    for i, dx in enumerate((-280, 0, 280)):
        x = X + Wd / 2 + dx
        arrow(c, X + Wd / 2, Y + 345, x, Y + 410, fill=GREY, width=6, head=18)
        person(c, x, Y + 610, h=170, color=[BLUE, TEAL, AMBER][i])
    moneybag(c, X + 110, Y + 200, 50)
    c.text(X + Wd / 2, Y + 668, "las conductas de los arts. 5 y 6", "Bold", 26, TEAL, anchor="mm")


def s_precursores(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    for i, dx in enumerate((150, 280, 410)):
        bottle(c, X + dx, gy - 80, 150, fill=[PURPLE, TEAL, AMBER][i])
    document(c, X + 640, Y + 250, 200, 250, lines=5, stamp=GREEN)
    c.text(X + 640, Y + 395, "REGISTRO", "ExtraBold", 26, NAVY, anchor="mm")
    c.text(X + 640, Y + 425, "DE PRECURSORES", "ExtraBold", 20, NAVY, anchor="mm")
    c.text(X + 280, Y + 80, "SUSTANCIAS QUÍMICAS CONTROLADAS", "ExtraBold", 26, NAVY, anchor="mm")


def s_pjuridica(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    c.rect(X + 150, gy - 380, 300, 380, fill=LIGHT, outline=NAVY, width=4)
    for r_ in range(4):
        for k in range(3):
            c.rect(X + 185 + k * 90, gy - 340 + r_ * 85, 50, 50, fill="#BFE3F5", outline=NAVY, width=3)
    c.rect(X + 270, gy - 70, 60, 70, fill=NAVY)
    moneybag(c, X + 620, Y + 250, 80)
    c.text(X + 620, Y + 380, "MULTA", "ExtraBold", 36, RED, anchor="mm")
    arrow(c, X + 470, Y + 250, X + 540, Y + 250, fill=NAVY)


def s_tenencia(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 250, gy + 8, h=290, color=BLUE, face="scared")
    c.rrect(X + 450, gy - 90, 70, 70, r=12, fill="#E9CFA3", outline=NAVY, width=4)
    leaf(c, X + 485, gy - 55, 0.5)
    scale_justice(c, X + 650, Y + 330, w=170, tilt=0)
    c.text(X + 650, Y + 85, "¿PARA QUÉ?", "ExtraBold", 30, NAVY, anchor="mm")
    chip(c, X + 520, Y + 150, "consumo personal", fill=GREEN, size=22, pad=16)


def s_arriola(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    gavel(c, X + 300, Y + 280, 1.3)
    c.rrect(X + 520, Y + 160, 280, 140, r=22, fill=WHITE, outline=NAVY, width=4)
    c.text(X + 660, Y + 205, "ART. 19", "ExtraBold", 34, TEAL, anchor="mm")
    c.text(X + 660, Y + 255, "Constitución", "Bold", 28, NAVY, anchor="mm")
    house(c, X + 560, gy + 15, w=220, h=200)
    c.text(X + 410, Y + 70, "ACCIONES PRIVADAS", "ExtraBold", 30, NAVY, anchor="mm")


# ---------------- Ley 23.737: agravantes, lugar, medidas, difusión, coca

def i_school(c, cx, cy):
    c.rect(cx - 55, cy - 20, 110, 70, fill=LIGHT, outline=NAVY, width=4)
    c.poly([(cx - 65, cy - 20), (cx, cy - 62), (cx + 65, cy - 20)], fill=BLUE, outline=NAVY, width=4)
    c.rect(cx - 12, cy + 12, 24, 38, fill=NAVY)

def i_pregnant(c, cx, cy):
    person(c, cx, cy + 55, 110, color=TEAL, pose="stand")


def s_lugar(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    house(c, X + 330, gy + 15, w=330, h=300)
    lock(c, X + 495, gy - 120, 70, fill=GREEN)
    person(c, X + 160, gy + 8, h=280, color=RED, pose="reach", face="sly")
    c.text(X + 160, Y + 70, "FACILITA EL LUGAR", "ExtraBold", 28, RED, anchor="mm")
    c.text(X + 650, Y + 70, "aunque sea gratis", "Bold", 26, NAVY, anchor="mm")


def s_curativa(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    steps = [("CONSUMO PERSONAL", AMBER_D), ("TRATAMIENTO", TEAL), ("SIN PENA", GREEN)]
    sw = (Wd - 140) / 3
    for i, (t, col) in enumerate(steps):
        x = X + 50 + i * (sw + 20)
        c.rrect(x, Y + 80, sw, 90, r=18, fill=col)
        c.text(x + sw / 2, Y + 125, t, "ExtraBold", 21, WHITE, anchor="mm")
        if i < 2:
            arrow(c, x + sw + 2, Y + 125, x + sw + 18, Y + 125, width=5, head=12)
    person(c, X + 220, gy + 8, h=270, color=BLUE, face="happy")
    person(c, X + 600, gy + 8, h=290, color=WHITE, pose="point", face="happy", flip=True)
    c.rrect(X + 556, gy - 190, 90, 90, r=10, fill=WHITE)
    c.rect(X + 590, gy - 168, 22, 52, fill=RED)
    c.rect(X + 575, gy - 153, 52, 22, fill=RED)
    c.text(X + Wd / 2, Y + 250, "o medida educativa si es experimentador", "Bold", 26, NAVY, anchor="mm")


def s_difusion(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 170, gy + 8, h=290, color=RED, pose="point", face="sly")
    speech(c, X + 260, Y + 100, 330, 130, tail="left")
    c.text(X + 425, Y + 165, "¡Consuman!", "ExtraBold", 36, RED, anchor="mm")
    for i, dx in enumerate((520, 620, 720)):
        person(c, X + dx, gy + 8, h=150 + (i % 2) * 20, color=[BLUE, TEAL, AMBER][i], face="scared")
    c.text(X + Wd / 2, Y + 50, "EN PÚBLICO", "ExtraBold", 30, NAVY, anchor="mm")


def s_coca(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    for dx in (170, 290, 410):
        leaf(c, X + dx, gy - 60, 1.4)
    # taza de infusión
    c.rrect(X + 560, gy - 120, 130, 100, r=18, fill=WHITE, outline=NAVY, width=4)
    c.arc(X + 700, gy - 70, 36, 270, 90, fill=NAVY, width=8)
    c.line([(X + 590, gy - 140), (X + 590, gy - 175)], fill=GREY, width=5)
    c.line([(X + 625, gy - 140), (X + 625, gy - 185)], fill=GREY, width=5)
    c.text(X + Wd / 2, Y + 70, "EN SU ESTADO NATURAL", "ExtraBold", 32, GREEN, anchor="mm")
    c.text(X + Wd / 2, Y + 118, "coqueo · masticación · infusión", "Bold", 28, NAVY, anchor="mm")
