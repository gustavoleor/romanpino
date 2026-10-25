# -*- coding: utf-8 -*-
"""Mini lenguaje para escribir el contenido del libro.
Cada función agrega un bloque a la lista BLOCKS, que luego build_docx.py convierte a Word."""
BLOCKS = []

def H1(t): BLOCKS.append(("h1", t))          # capítulo (nueva página)
def PARTE(t, sub=""): BLOCKS.append(("parte", t, sub))  # portadilla de parte
def H2(t): BLOCKS.append(("h2", t))
def H3(t): BLOCKS.append(("h3", t))
def P(t): BLOCKS.append(("p", t))
def LEY(ref, t): BLOCKS.append(("ley", ref, t))      # texto legal
def RES(t): BLOCKS.append(("res", t))                # resumen del tema
def EJ(tit, t): BLOCKS.append(("ej", tit, t))        # ejemplo práctico
def JUR(cita, t, fuente=""): BLOCKS.append(("jur", cita, t, fuente))  # sumario jurisprudencial
def TIP(t): BLOCKS.append(("tip", t))                # consejo práctico
def OJO(t): BLOCKS.append(("ojo", t))                # advertencia / punto a verificar
def BUL(items): BLOCKS.append(("bul", items))
def NUM(items): BLOCKS.append(("num", items))
def TAB(headers, rows, widths=None): BLOCKS.append(("tab", headers, rows, widths))
def FIG(n, cap): BLOCKS.append(("fig", n, cap))      # filmina n
def FICHA(rows): BLOCKS.append(("ficha", rows))      # ficha técnica (pares clave/valor)
def PB(): BLOCKS.append(("pb",))
