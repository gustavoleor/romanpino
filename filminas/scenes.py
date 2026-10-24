"""Escenas ilustradas. Cada función dibuja dentro del panel (X, Y, Wd, Ht)."""
from kit import *


def ground(c, X, Y, Wd, Ht, col="#D9D2C0"):
    gy = Y + Ht - 100
    c.rect(X, gy, Wd, 100, fill=col)
    return gy


# ---------------------------------------------------------------- TEORÍA

def s_legalidad(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    # línea de tiempo
    c.line([(X + 70, Y + 130), (X + Wd - 70, Y + 130)], fill=NAVY, width=6)
    arrow(c, X + Wd - 140, Y + 130, X + Wd - 60, Y + 130)
    document(c, X + 220, Y + 270, w=190, h=240, lines=5, stamp=RED)
    c.text(X + 220, Y + 270, "LEY", "ExtraBold", 54, RED, anchor="mm")
    c.text(X + 220, Y + 80, "1º LA LEY", "ExtraBold", 38, TEAL, anchor="mm")
    c.text(X + Wd - 250, Y + 80, "2º EL HECHO", "ExtraBold", 38, BLUE, anchor="mm")
    arrow(c, X + 360, Y + 270, X + 520, Y + 270, fill=TEAL)
    person(c, X + Wd - 250, gy + 8, h=290, color=BLUE, pose="arms_up")
    check(c, X + Wd - 130, Y + 240, 38)
    c.text(X + Wd / 2, Y + Ht - 32, "sin ley previa  =  sin delito", "ExtraBold", 36, NAVY, anchor="mm")


def s_escalera(c, X, Y, Wd, Ht):
    steps = [("ACCIÓN", BLUE), ("TÍPICA", TEAL), ("ANTIJURÍDICA", AMBER), ("CULPABLE", RED)]
    n = len(steps)
    sw = (Wd - 140) / n
    base = Y + Ht - 70
    for i, (lbl, col) in enumerate(steps):
        h = 80 + i * 70
        x = X + 70 + i * sw
        c.rrect(x, base - h, sw - 12, h, r=18, fill=col)
        c.text(x + (sw - 12) / 2, base - h + 46, f"{i + 1}. {lbl}", "ExtraBold", 34, WHITE, anchor="mm")
    person(c, X + 70 + 3 * sw + sw / 2, base - 290, h=150, color=NAVY, pose="arms_up")
    c.text(X + 60, Y + 55, "Delito = conducta con 4 escalones", "ExtraBold", 40, NAVY)


def s_accion_omision(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    half = Wd / 2
    c.text(X + half / 2, Y + 50, "ACCIÓN", "ExtraBold", 40, BLUE, anchor="mm")
    c.text(X + half * 1.5, Y + 50, "OMISIÓN", "ExtraBold", 40, RED, anchor="mm")
    c.line([(X + half, Y + 30), (X + half, Y + Ht - 30)], fill=GREY, width=3)
    # acción: persona arroja / empuja un objeto
    person(c, X + 170, gy + 8, h=270, color=BLUE, pose="reach")
    c.rrect(X + 340, gy - 90, 80, 70, r=10, fill=AMBER, outline=NAVY, width=4)
    arrow(c, X + 430, gy - 55, X + half - 30, gy - 55, fill=BLUE)
    # omisión: persona con brazos caídos mirando a otra que pide ayuda
    person(c, X + half + 130, gy + 8, h=270, color=RED, pose="stand", face="scared")
    person(c, X + half + 360, gy + 8, h=150, color=TEAL, pose="arms_up", face="scared")
    c.text(X + half + 365, Y + 150, "¡Ayuda!", "ExtraBold", 36, TEAL, anchor="mm")
    c.ellipse(X + half + 130, Y + 190, 54, fill=WHITE, outline=NAVY, width=4)
    c.text(X + half + 130, Y + 190, "...", "ExtraBold", 50, NAVY, anchor="mm")


def s_tipicidad(c, X, Y, Wd, Ht):
    cx, cy = X + Wd / 2, Y + Ht / 2 - 10
    puzzle(c, cx - 200, cy, 1.5, fill=BLUE, knob="right")
    puzzle(c, cx + 160, cy, 1.5, fill=TEAL, knob="left")
    c.text(cx - 200, cy + 150, "CONDUCTA", "ExtraBold", 34, NAVY, anchor="mm")
    c.text(cx + 160, cy + 150, "TIPO PENAL", "ExtraBold", 34, NAVY, anchor="mm")
    check(c, cx - 20, cy - 150, 40)
    c.text(cx, Y + 60, "¿Encaja?", "ExtraBold", 46, NAVY, anchor="mm")


def s_dolo_culpa(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    half = Wd / 2
    c.text(X + half / 2, Y + 50, "DOLO", "ExtraBold", 42, RED, anchor="mm")
    c.text(X + half * 1.5, Y + 50, "CULPA", "ExtraBold", 42, AMBER_D, anchor="mm")
    c.line([(X + half, Y + 30), (X + half, Y + Ht - 30)], fill=GREY, width=3)
    target(c, X + half / 2 + 110, Y + 250, 78)
    arrow(c, X + 150, Y + 250, X + half / 2 + 40, Y + 250, fill=RED, width=10)
    person(c, X + 110, gy + 8, h=240, color=RED, pose="stand", face="sly")
    c.text(X + half / 2, Y + Ht - 32, "sabe y quiere", "Bold", 34, NAVY, anchor="mm")
    # culpa: persona distraída con celular y banana
    person(c, X + half + 150, gy + 8, h=240, color=AMBER, pose="stand")
    phone(c, X + half + 205, gy - 110, 70)
    banana(c, X + half + 330, gy - 8, 90)
    warning(c, X + half + 340, Y + 190, 100)
    c.text(X + half * 1.5, Y + Ht - 32, "no quiere, pero no se cuidó", "Bold", 30, NAVY, anchor="mm")


def s_legitima_defensa(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 230, gy + 8, h=290, color=RED, pose="point", face="angry")
    lightning(c, X + 400, Y + 170, 120)
    person(c, X + Wd - 240, gy + 8, h=290, color=BLUE, pose="stand", face="scared", flip=False)
    shield(c, X + Wd - 400, gy - 150, 170)
    c.text(X + 230, Y + 70, "AGRESIÓN", "ExtraBold", 36, RED, anchor="mm")
    c.text(X + Wd - 240, Y + 70, "DEFENSA", "ExtraBold", 36, TEAL, anchor="mm")


def s_estado_necesidad(c, X, Y, Wd, Ht):
    cx, cy = X + Wd / 2, Y + Ht / 2 + 20
    (lx, ly), (rx, ry) = scale_justice(c, cx, cy, w=420, tilt=36)
    # plato izquierdo (baja la derecha => ponemos más peso a la derecha)
    heart(c, rx, ry - 14, 48, fill=RED)
    c.text(rx, ry + 130, "MAL MAYOR", "ExtraBold", 32, RED, anchor="mm")
    # plato izquierdo: ventana rota
    c.rect(lx - 32, ly - 46, 64, 52, fill="#BFE3F5", outline=NAVY, width=4)
    c.line([(lx - 32, ly - 46), (lx + 10, ly - 6)], fill=NAVY, width=4)
    c.line([(lx + 4, ly - 46), (lx - 14, ly - 12)], fill=NAVY, width=4)
    c.text(lx, ly + 130, "MAL MENOR", "ExtraBold", 32, AMBER_D, anchor="mm")


def s_inimputable(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + Wd / 2 - 60, gy + 8, h=300, color=BLUE, pose="stand", face="scared")
    # nube sobre la cabeza con cerebro y signos de pregunta
    c.ellipse(X + Wd / 2 - 60, Y + 170, 190, 110, fill=WHITE, outline=NAVY, width=4)
    brain(c, X + Wd / 2 - 60, Y + 170, 80)
    c.text(X + Wd / 2 - 210, Y + 120, "?", "ExtraBold", 80, RED, anchor="mm")
    c.text(X + Wd / 2 + 100, Y + 210, "?", "ExtraBold", 64, AMBER, anchor="mm")
    c.text(X + Wd / 2 + 60, Y + 90, "?", "ExtraBold", 50, TEAL, anchor="mm")
    for i, r in enumerate((14, 10, 7)):
        c.ellipse(X + Wd / 2 - 60 + i * 12, Y + 295 + i * 18, r, fill=WHITE, outline=NAVY, width=3)


def s_iter(c, X, Y, Wd, Ht):
    stages = [("IDEA", GREY), ("PREPARACIÓN", GREY), ("EJECUCIÓN", AMBER), ("CONSUMACIÓN", RED), ("AGOTAMIENTO", PURPLE)]
    n = len(stages)
    gap = (Wd - 300) / (n - 1)
    y = Y + Ht / 2 - 20
    c.line([(X + 100, y), (X + Wd - 100, y)], fill=NAVY, width=8)
    for i, (lbl, col) in enumerate(stages):
        x = X + 150 + i * gap
        c.ellipse(x, y, 38, fill=col, outline=NAVY, width=4)
        c.text(x, y, str(i + 1), "ExtraBold", 36, WHITE, anchor="mm")
        c.text(x, y - 80, lbl, "ExtraBold", 28, NAVY, anchor="mm")
    # llaves de zonas
    c.rrect(X + 150 - 40, y + 70, gap + 80, 52, r=12, fill=GREY)
    c.text(X + 150 + gap / 2, y + 96, "en general impune", "Bold", 26, WHITE, anchor="mm")
    c.rrect(X + 150 + 2 * gap - 80, y + 70, 160, 52, r=12, fill=AMBER)
    c.text(X + 150 + 2 * gap, y + 96, "TENTATIVA", "ExtraBold", 24, NAVY, anchor="mm")
    c.rrect(X + 150 + 3 * gap - 80, y + 70, 160, 52, r=12, fill=RED)
    c.text(X + 150 + 3 * gap, y + 96, "DELITO", "ExtraBold", 26, WHITE, anchor="mm")


def s_autoria(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    xs = [X + 170, X + Wd / 2, X + Wd - 170]
    cols = [RED, AMBER, TEAL]
    tcols = [RED, AMBER_D, TEAL]
    lbls = ["AUTOR", "INSTIGADOR", "CÓMPLICE"]
    subs = ["ejecuta", "convence", "ayuda"]
    person(c, xs[0], gy + 8, h=270, color=cols[0], pose="reach", face="angry")
    person(c, xs[1], gy + 8, h=270, color=cols[1], pose="point", face="sly")
    person(c, xs[2], gy + 8, h=270, color=cols[2], pose="reach", flip=True)
    speech(c, xs[1] - 60, Y + 80, 200, 90, tail="left")
    c.text(xs[1] + 40, Y + 125, "¡Hacelo!", "ExtraBold", 34, NAVY, anchor="mm")
    for x, l, s_, col in zip(xs, lbls, subs, tcols):
        c.text(x, Y + 40, l, "ExtraBold", 34, col, anchor="mm")
        c.text(x, Y + Ht - 32, s_, "Bold", 30, NAVY, anchor="mm")


def s_concursos(c, X, Y, Wd, Ht):
    half = Wd / 2
    c.text(X + half / 2, Y + 50, "CONCURSO IDEAL", "ExtraBold", 36, BLUE, anchor="mm")
    c.text(X + half * 1.5, Y + 50, "CONCURSO REAL", "ExtraBold", 36, RED, anchor="mm")
    c.line([(X + half, Y + 30), (X + half, Y + Ht - 30)], fill=GREY, width=3)
    # ideal: 1 hecho -> 2 figuras
    star(c, X + 120, Y + 250, 56, AMBER)
    c.text(X + 120, Y + 250, "1", "ExtraBold", 50, NAVY, anchor="mm")
    arrow(c, X + 190, Y + 235, X + 360, Y + 175, fill=BLUE)
    arrow(c, X + 190, Y + 265, X + 360, Y + 325, fill=BLUE)
    c.rrect(X + 370, Y + 135, 190, 80, r=16, fill=BLUE)
    c.text(X + 465, Y + 175, "Figura A", "Bold", 30, WHITE, anchor="mm")
    c.rrect(X + 370, Y + 290, 190, 80, r=16, fill=BLUE)
    c.text(X + 465, Y + 330, "Figura B", "Bold", 30, WHITE, anchor="mm")
    c.text(X + half / 2, Y + 450, "se aplica la pena MAYOR", "ExtraBold", 32, NAVY, anchor="mm")
    # real: varios hechos
    for i in range(3):
        x = X + half + 80 + i * 140
        star(c, x + 40, Y + 250, 50, RED)
        c.text(x + 40, Y + 250, str(i + 1), "ExtraBold", 44, WHITE, anchor="mm")
    c.text(X + half * 1.5, Y + 385, "mínimo: el mayor", "Bold", 32, NAVY, anchor="mm")
    c.text(X + half * 1.5, Y + 430, "máximo: suma, tope 50 años", "Bold", 32, NAVY, anchor="mm")
    c.text(X + half * 1.5, Y + 500, "varios hechos independientes", "ExtraBold", 30, RED, anchor="mm")


# ---------------------------------------------------------------- DELITOS

def s_homicidio(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 220, gy + 8, h=300, color=RED, pose="point", face="sly")
    thought(c, X + 360, Y + 130, 120, 70, (X + 230, gy - 300))
    target(c, X + 360, Y + 130, 46)
    person(c, X + 560, gy + 18, h=300, color=BLUE, pose="lie")
    c.text(X + Wd / 2, Y + Ht - 32, "MATAR A OTRO", "ExtraBold", 36, NAVY, anchor="mm")


def s_agravado(c, X, Y, Wd, Ht):
    c.text(X + Wd / 2, Y + 50, "¿Qué lo agrava?", "ExtraBold", 40, NAVY, anchor="mm")
    tiles = [("VÍNCULO", "heart"), ("ENSAÑAMIENTO", "bolt"), ("VENENO", "bottle"),
             ("PRECIO", "bag"), ("ODIO / GÉNERO", "broken"), ("CRIMINIS CAUSA", "house")]
    cols = 3
    tw, th = (Wd - 120 - 2 * 24) / cols, 230
    for i, (lbl, ic) in enumerate(tiles):
        r_, k = divmod(i, cols)
        x = X + 60 + k * (tw + 24)
        y = Y + 110 + r_ * (th + 24)
        c.rrect(x, y, tw, th, r=22, fill=WHITE, outline=NAVY, width=4)
        cx, cy = x + tw / 2, y + 90
        if ic == "heart":
            heart(c, cx, cy, 42)
        elif ic == "bolt":
            lightning(c, cx, cy, 120)
        elif ic == "bottle":
            bottle(c, cx, cy + 8, 120)
        elif ic == "bag":
            moneybag(c, cx, cy, 48)
        elif ic == "broken":
            heart(c, cx, cy, 42, fill=PURPLE, broken=True)
        else:
            house(c, cx - 60, cy + 56, w=120, h=100)
        c.text(cx, y + th - 40, lbl, "ExtraBold", 24, NAVY, anchor="mm")


def s_emocion(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 300, gy + 8, h=310, color=RED, pose="arms_up", face="angry")
    for dx in (-110, 110):
        lightning(c, X + 300 + dx, Y + 150, 90)
    thermometer(c, X + 620, Y + 300, 280, 0.92)
    c.text(X + 620, Y + 90, "EMOCIÓN", "ExtraBold", 28, RED, anchor="mm")
    c.text(X + 620, Y + 125, "VIOLENTA", "ExtraBold", 28, RED, anchor="mm")


def s_culposo(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht, col="#C9C3B2")
    c.rect(X, gy + 8, Wd, 6, fill=WHITE)
    car(c, X + 60, gy + 10, w=380, color=RED, crash=True)
    person(c, X + 640, gy + 8, h=250, color=BLUE, pose="arms_up", face="scared")
    warning(c, X + 560, Y + 190, 120)
    phone(c, X + 190, Y + 220, 100)
    c.text(X + 190, Y + 150, "distracción", "Bold", 28, NAVY, anchor="mm")
    c.text(X + Wd / 2, Y + 50, "SIN QUERER, PERO SIN CUIDADO", "ExtraBold", 30, NAVY, anchor="mm")


def s_lesiones(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 200, gy + 8, h=300, color=BLUE, face="scared")
    c.rrect(X + 150, gy - 252, 100, 26, r=8, fill=WHITE, outline=NAVY, width=3)   # venda
    c.rect(X + 192, gy - 252, 16, 26, fill=RED)
    levels = [("LEVE", GREEN, 120), ("GRAVE", AMBER, 220), ("GRAVÍSIMA", RED, 320)]
    bx = X + 420
    for i, (lbl, col, h) in enumerate(levels):
        x = bx + i * 110
        c.rrect(x, gy - h, 92, h, r=14, fill=col)
        c.text(x + 46, gy - h - 24, str(i + 1), "ExtraBold", 40, col, anchor="mm")
    c.text(bx + 150, Y + 60, "3 niveles", "ExtraBold", 36, NAVY, anchor="mm")
    for i, (lbl, col, h) in enumerate(levels):
        c.text(bx + i * 110 + 46, gy + 40, lbl[:5] if lbl != "GRAVÍSIMA" else "GRAV+", "Bold", 22, NAVY, anchor="mm")


def s_amenazas(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 200, gy + 8, h=300, color=RED, pose="point", face="angry")
    speech(c, X + 360, Y + 90, 300, 150, tail="left")
    c.text(X + 510, Y + 165, "¡Te voy a", "ExtraBold", 34, RED, anchor="mm")
    c.text(X + 510, Y + 205, "arruinar!", "ExtraBold", 34, RED, anchor="mm")
    person(c, X + Wd - 150, gy + 8, h=300, color=BLUE, face="scared", flip=True)


def s_domicilio(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    house(c, X + Wd - 480, gy + 15, w=380, h=330)
    person(c, X + 200, gy + 8, h=290, color=RED, pose="run", face="sly")
    # cartel prohibido
    cx, cy = X + 340, Y + 150
    c.ellipse(cx, cy, 62, fill=WHITE, outline=RED, width=14)
    c.line([(cx - 44, cy + 44), (cx + 44, cy - 44)], fill=RED, width=14)
    c.text(X + Wd - 290, Y + 55, "CONTRA LA VOLUNTAD", "ExtraBold", 28, RED, anchor="mm")
    c.text(X + Wd - 290, Y + 92, "de quien puede excluirlo", "Bold", 26, NAVY, anchor="mm")


def s_hurto(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 330, gy + 8, h=300, color=BLUE, pose="stand")
    wallet(c, X + 380, gy - 120, 80)
    person(c, X + 520, gy + 8, h=290, color=INK, pose="reach", face="sly", flip=True)
    mask(c, X + 520, gy - 256, 34)
    c.text(X + 420, Y + 70, "SIN FUERZA", "ExtraBold", 36, TEAL, anchor="mm")
    c.text(X + 420, Y + 110, "ni violencia", "Bold", 30, NAVY, anchor="mm")
    cross(c, X + 650, Y + 90, 30)


def s_robo(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    person(c, X + 200, gy + 8, h=300, color=INK, pose="reach", face="angry")
    mask(c, X + 200, gy - 266, 34)
    lightning(c, X + 400, gy - 170, 110)
    person(c, X + 560, gy + 8, h=300, color=BLUE, pose="arms_up", face="scared", flip=True)
    wallet(c, X + 420, gy - 70, 80)
    c.text(X + Wd / 2, Y + 70, "FUERZA en las cosas  o", "ExtraBold", 32, RED, anchor="mm")
    c.text(X + Wd / 2, Y + 112, "VIOLENCIA en las personas", "ExtraBold", 32, RED, anchor="mm")


def s_estafa(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    steps = [("ENGAÑO", RED), ("ERROR", AMBER), ("DISPOSICIÓN", BLUE), ("PERJUICIO", PURPLE)]
    sw = (Wd - 120) / 4
    for i, (lbl, col) in enumerate(steps):
        x = X + 60 + i * sw
        c.rrect(x, Y + 40, sw - 18, 70, r=16, fill=col)
        c.text(x + (sw - 18) / 2, Y + 75, lbl, "ExtraBold", 22, WHITE, anchor="mm")
        if i < 3:
            arrow(c, x + sw - 16, Y + 75, x + sw + 4, Y + 75, width=5, head=14)
    person(c, X + 180, gy + 8, h=280, color=RED, pose="reach", face="sly")
    document(c, X + 380, gy - 150, w=110, h=140, lines=3, stamp=AMBER)
    person(c, X + Wd - 160, gy + 8, h=280, color=BLUE, pose="reach", flip=True)
    banknote(c, X + Wd - 330, gy - 150)
    arrow(c, X + Wd - 390, gy - 100, X + 470, gy - 100, fill=GREEN, width=6, head=18)


def s_danio(c, X, Y, Wd, Ht):
    gy = ground(c, X, Y, Wd, Ht)
    car(c, X + 90, gy + 10, w=400, color=BLUE)
    # grietas / abolladura
    star(c, X + 400, gy - 70, 50, AMBER, points=8)
    c.line([(X + 330, gy - 110), (X + 380, gy - 80), (X + 350, gy - 40)], fill=NAVY, width=5)
    person(c, X + Wd - 190, gy + 8, h=290, color=RED, pose="point", face="angry", flip=True)
    c.text(X + 300, Y + 90, "DESTRUIR · INUTILIZAR · DAÑAR", "ExtraBold", 28, NAVY, anchor="mm")
    c.text(X + 300, Y + 130, "cosa ajena", "Bold", 28, RED, anchor="mm")


def s_portada(c, X, Y, Wd, Ht):
    cx, cy = X + Wd / 2, Y + Ht / 2
    scale_justice(c, cx - 60, cy + 10, w=400, tilt=0)
    gavel(c, cx + 330, cy + 120, 1.0)
