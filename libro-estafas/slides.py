# -*- coding: utf-8 -*-
"""Genera las filminas (HTML) del libro sobre estafas y defraudaciones.
Luego render_slides.js las convierte a PNG con Playwright."""
import html, json, os

OUT = os.path.join(os.path.dirname(__file__), "slides_html")

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1600px;height:900px;font-family:'Inter',sans-serif;background:#F7F5F0;color:#14213D;overflow:hidden;position:relative}
.band{position:absolute;left:0;top:0;width:22px;height:900px;background:#14213D}
.band:after{content:'';position:absolute;left:0;top:0;width:22px;height:180px;background:#B23A48}
.wrap{position:absolute;left:90px;right:80px;top:60px;bottom:70px;display:flex;flex-direction:column}
.kicker{font-size:22px;letter-spacing:3px;text-transform:uppercase;color:#B23A48;font-weight:700;margin-bottom:10px}
h1{font-family:'Inter Display','Inter',sans-serif;font-size:56px;line-height:1.08;font-weight:800;color:#14213D;margin-bottom:30px}
.foot{position:absolute;left:90px;right:80px;bottom:26px;display:flex;justify-content:space-between;font-size:17px;color:#6B7280}
.foot b{color:#14213D}
ul.b{list-style:none;display:flex;flex-direction:column;gap:26px}
ul.b li{font-size:34px;line-height:1.3;padding-left:44px;position:relative}
ul.b li:before{content:'';position:absolute;left:0;top:13px;width:18px;height:18px;background:#B23A48;border-radius:3px}
ul.b li b{color:#14213D}
.small ul.b li{font-size:30px}
.flow{display:flex;align-items:stretch;gap:0;margin-top:10px}
.step{flex:1;background:#fff;border:3px solid #14213D;border-radius:18px;padding:26px 22px;display:flex;flex-direction:column;gap:12px;box-shadow:0 6px 0 #14213D}
.step .n{font-size:20px;font-weight:800;color:#fff;background:#B23A48;border-radius:30px;width:44px;height:44px;display:flex;align-items:center;justify-content:center}
.step .t{font-size:35px;font-weight:800}
.step .d{font-size:27px;line-height:1.3;color:#374151}
.arrow{width:60px;display:flex;align-items:center;justify-content:center;font-size:54px;color:#B23A48;font-weight:900}
.note{margin-top:34px;font-size:28px;background:#14213D;color:#fff;padding:20px 28px;border-radius:14px;line-height:1.35}
.note b{color:#F2C14E}
.cols{display:flex;gap:28px;flex:1}
.col{flex:1;background:#fff;border-radius:18px;border-top:12px solid #14213D;padding:24px 26px;box-shadow:0 3px 12px rgba(0,0,0,.08)}
.col.alt{border-top-color:#B23A48}
.col.gold{border-top-color:#C9A227}
.col h3{font-size:34px;font-weight:800;margin-bottom:14px}
.col ul{list-style:none;display:flex;flex-direction:column;gap:16px}
.col li{font-size:28px;line-height:1.3;padding-left:24px;position:relative}
.col li:before{content:'›';position:absolute;left:0;top:-2px;color:#B23A48;font-weight:900;font-size:28px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;flex:1}
.cell{background:#fff;border-radius:12px;padding:16px 18px;border-left:8px solid #14213D;display:flex;gap:12px;align-items:flex-start;box-shadow:0 2px 6px rgba(0,0,0,.07)}
.cell.r{border-left-color:#B23A48}
.cell .num{font-size:30px;font-weight:900;color:#B23A48;min-width:44px}
.cell .tx{font-size:22px;line-height:1.25}
.cell .tx b{display:block;font-size:23px;margin-bottom:2px}
table{border-collapse:separate;border-spacing:0;width:100%;font-size:27px;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 3px 12px rgba(0,0,0,.08)}
th{background:#14213D;color:#fff;text-align:left;padding:16px 20px;font-size:26px}
td{padding:15px 20px;border-bottom:1px solid #E5E7EB;line-height:1.28;vertical-align:top}
tr:nth-child(even) td{background:#FAF8F3}
td.k{font-weight:800;color:#B23A48;white-space:nowrap}
.cover{background:#14213D;color:#fff}
.cover .band{background:#B23A48}
.cover .band:after{background:#C9A227}
.cover h1{color:#fff;font-size:92px;margin-top:150px}
.cover .sub{font-size:36px;color:#F2C14E;font-weight:600;margin-top:10px}
.cover .meta{position:absolute;left:90px;bottom:70px;font-size:24px;color:#CBD5E1;line-height:1.5}
.quote{font-size:40px;line-height:1.4;font-weight:600;border-left:10px solid #B23A48;padding:20px 40px;background:#fff;border-radius:0 18px 18px 0}
.src{margin-top:20px;font-size:22px;color:#6B7280}
.tree{display:flex;flex-direction:column;gap:22px}
.q{display:flex;align-items:center;gap:20px}
.q .qq{flex:1.25;background:#14213D;color:#fff;font-size:28px;font-weight:700;padding:15px 22px;border-radius:12px}
.q .ar{font-size:36px;color:#B23A48;font-weight:900}
.q .aa{flex:1;background:#fff;border:3px solid #B23A48;font-size:28px;font-weight:700;padding:13px 20px;border-radius:12px}
.big{font-size:120px;font-weight:900;color:#B23A48;line-height:1}
.pill{display:inline-block;background:#B23A48;color:#fff;border-radius:30px;padding:6px 18px;font-size:20px;font-weight:700;margin-right:8px}
svg text{font-family:'Inter',sans-serif}
"""

def page(body, n, title_for_foot, cls=""):
    foot = "" if cls == "cover" else (
        f'<div class="foot"><span><b>Estafas y otras defraudaciones</b> · Código Penal argentino (arts. 172 a 180)</span><span>Filmina {n}</span></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{cls}"><div class="band"></div><div class="wrap">{body}</div>{foot}</body></html>"""

e = html.escape

def rich(s):
    # **negrita** sencilla
    out, bold = "", False
    for i, part in enumerate(s.split("**")):
        out += (f"<b>{e(part)}</b>" if i % 2 else e(part))
    return out

def head(kicker, title):
    return f'<div class="kicker">{e(kicker)}</div><h1>{rich(title)}</h1>'

def s_cover(n, title, sub, meta):
    return page(f'<h1>{e(title)}</h1><div class="sub">{e(sub)}</div><div class="meta">{meta}</div>', n, title, "cover")

def s_bullets(n, kicker, title, items, small=False):
    lis = "".join(f"<li>{rich(i)}</li>" for i in items)
    return page(f'<div class="{"small" if small else ""}">{head(kicker,title)}<ul class="b">{lis}</ul></div>', n, title)

def s_flow(n, kicker, title, steps, note=None):
    parts = []
    for i, (t, d) in enumerate(steps):
        if i:
            parts.append('<div class="arrow">→</div>')
        parts.append(f'<div class="step"><div class="n">{i+1}</div><div class="t">{e(t)}</div><div class="d">{rich(d)}</div></div>')
    nt = f'<div class="note">{rich(note)}</div>' if note else ""
    return page(head(kicker, title) + f'<div class="flow">{"".join(parts)}</div>{nt}', n, title)

def s_cols(n, kicker, title, cols, note=None):
    cls = ["", "alt", "gold", ""]
    h = ""
    for i, (hd, items) in enumerate(cols):
        lis = "".join(f"<li>{rich(x)}</li>" for x in items)
        h += f'<div class="col {cls[i%4]}"><h3>{rich(hd)}</h3><ul>{lis}</ul></div>'
    nt = f'<div class="note">{rich(note)}</div>' if note else ""
    return page(head(kicker, title) + f'<div class="cols">{h}</div>{nt}', n, title)

def s_grid(n, kicker, title, cells):
    h = ""
    for i, (num, b, t) in enumerate(cells):
        h += f'<div class="cell {"r" if i%2 else ""}"><div class="num">{e(num)}</div><div class="tx"><b>{e(b)}</b>{e(t)}</div></div>'
    return page(head(kicker, title) + f'<div class="grid">{h}</div>', n, title)

def s_table(n, kicker, title, headers, rows, note=None, fs=None):
    th = "".join(f"<th>{e(x)}</th>" for x in headers)
    tr = ""
    for r in rows:
        tr += "<tr>" + "".join((f'<td class="k">{rich(c)}</td>' if j == 0 else f"<td>{rich(c)}</td>") for j, c in enumerate(r)) + "</tr>"
    style = f' style="font-size:{fs}px"' if fs else ""
    nt = f'<div class="note">{rich(note)}</div>' if note else ""
    return page(head(kicker, title) + f'<table{style}><tr>{th}</tr>{tr}</table>{nt}', n, title)

def s_tree(n, kicker, title, qa):
    h = "".join(f'<div class="q"><div class="qq">{rich(q)}</div><div class="ar">→</div><div class="aa">{rich(a)}</div></div>' for q, a in qa)
    return page(head(kicker, title) + f'<div class="tree">{h}</div>', n, title)

def s_quote(n, kicker, title, text, src):
    return page(head(kicker, title) + f'<div class="quote">{rich(text)}</div><div class="src">{e(src)}</div>', n, title)

def s_svg(n, kicker, title, svg, note=None):
    nt = f'<div class="note">{rich(note)}</div>' if note else ""
    return page(head(kicker, title) + f'<div style="flex:1;display:flex;justify-content:center">{svg}</div>{nt}', n, title)

def triangle_svg(top, left, right, l1, l2, l3, w=1300, h=430):
    return f"""<svg width="{w}" height="{h}" viewBox="0 0 1300 430">
<defs><marker id="m" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0,0 L12,6 L0,12 z" fill="#B23A48"/></marker></defs>
<line x1="560" y1="95" x2="260" y2="330" stroke="#B23A48" stroke-width="5" marker-end="url(#m)"/>
<line x1="740" y1="95" x2="1050" y2="330" stroke="#B23A48" stroke-width="5" marker-end="url(#m)"/>
<line x1="445" y1="375" x2="850" y2="375" stroke="#14213D" stroke-width="5" stroke-dasharray="14 10" marker-end="url(#m)"/>
<rect x="470" y="10" width="360" height="90" rx="16" fill="#14213D"/><text x="650" y="66" fill="#fff" font-size="30" font-weight="800" text-anchor="middle">{e(top)}</text>
<rect x="0" y="330" width="440" height="90" rx="16" fill="#fff" stroke="#14213D" stroke-width="4"/><text x="220" y="386" fill="#14213D" font-size="28" font-weight="800" text-anchor="middle">{e(left)}</text>
<rect x="860" y="330" width="440" height="90" rx="16" fill="#fff" stroke="#B23A48" stroke-width="4"/><text x="1080" y="386" fill="#14213D" font-size="28" font-weight="800" text-anchor="middle">{e(right)}</text>
<text x="300" y="195" fill="#B23A48" font-size="24" font-weight="700" text-anchor="middle">{e(l1)}</text>
<text x="1000" y="195" fill="#B23A48" font-size="24" font-weight="700" text-anchor="middle">{e(l2)}</text>
<text x="650" y="355" fill="#14213D" font-size="21" font-weight="700" text-anchor="middle">{e(l3)}</text>
</svg>"""

def timeline_svg(points):
    # points: list of (label, sub, kind) kind: 'imp','tent','cons','ago'
    w, x0, x1, y = 1420, 120, 1300, 170
    col = {"imp": "#9CA3AF", "tent": "#C9A227", "cons": "#B23A48", "ago": "#14213D"}
    svg = [f'<svg width="{w}" height="400" viewBox="0 0 {w} 400">',
           f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#14213D" stroke-width="6"/>']
    step = (x1 - x0) / (len(points) - 1)
    for i, (lab, sub, k) in enumerate(points):
        x = x0 + i * step
        svg.append(f'<circle cx="{x}" cy="{y}" r="26" fill="{col[k]}" stroke="#fff" stroke-width="5"/>')
        svg.append(f'<text x="{x}" y="{y-50}" font-size="26" font-weight="800" fill="#14213D" text-anchor="middle">{e(lab)}</text>')
        lines = sub.split("|")
        for j, ln in enumerate(lines):
            svg.append(f'<text x="{x}" y="{y+70+j*30}" font-size="22" fill="#374151" text-anchor="middle">{e(ln)}</text>')
    svg.append("</svg>")
    return "".join(svg)

SLIDES = []
def add(f, *a, **k):
    n = len(SLIDES) + 1
    SLIDES.append(f(n, *a, **k))

# ---------------------------------------------------------------- filminas
add(s_cover, "Estafas y otras defraudaciones", "Código Penal argentino · arts. 172 a 180 y figuras conexas",
    "Apunte de estudio y conferencia<br>Doctrina · Jurisprudencia · Práctica en Córdoba<br>Texto vigente a octubre de 2026")

add(s_table, "Mapa normativo", "Dónde está el tema en el Código Penal",
    ["Ubicación", "Contenido", "Pena base"],
    [["Art. 172", "Estafa (figura genérica)", "Prisión 1 mes a 6 años"],
     ["Art. 173", "16 casos especiales de defraudación", "La del art. 172"],
     ["Art. 174", "Defraudaciones agravadas (6 incisos)", "Prisión 2 a 6 años"],
     ["Art. 175", "Defraudaciones atenuadas (4 incisos)", "Multa"],
     ["Art. 175 bis", "Usura (simple y profesional)", "Prisión 1-3 / 3-6 años + multa"],
     ["Arts. 176-180", "Quebrados y otros deudores punibles", "Variable"],
     ["Art. 185", "Excusa absolutoria entre parientes", "Exime de pena"]], fs=24,
    note="Título VI **Delitos contra la propiedad** · Capítulo IV **Estafas y otras defraudaciones** · Capítulo V **Quebrados y otros deudores punibles**")

add(s_cols, "Conceptos básicos", "Defraudación: el género y sus dos grandes especies",
    [("Estafa (fraude por engaño)", ["El autor **engaña**", "La víctima **yerra** y dispone", "El perjuicio nace del **error**", "Ej.: arts. 172; 173 incs. 1, 3, 6, 8, 9, 10"]),
     ("Abuso de confianza", ["El autor **ya tiene** el bien o su manejo", "No hay engaño inicial", "Viola un **deber** de devolver o de administrar", "Ej.: art. 173 incs. 2, 7, 12"]),
     ("Bien jurídico", ["La **propiedad** en sentido amplio (art. 17 CN)", "Equivale a **patrimonio**", "Exige **perjuicio patrimonial**", "Concepto mixto: jurídico-económico"])])

add(s_quote, "Art. 172 CP", "La norma central",
    "Será reprimido con prisión de un mes a seis años, el que defraudare a otro con **nombre supuesto, calidad simulada, falsos títulos, influencia mentida, abuso de confianza o aparentando bienes, crédito, comisión, empresa o negociación** o valiéndose de **cualquier otro ardid o engaño**.",
    "Código Penal de la Nación, Ley 11.179 (t.o. 1984 y modificatorias)")

add(s_flow, "Estructura típica", "La cadena de la estafa",
    [("Ardid o engaño", "Despliegue que **simula** o **disimula** la verdad"),
     ("Error", "Falsa representación de la realidad en la **víctima**"),
     ("Disposición patrimonial", "La víctima **entrega, paga o renuncia**: acto propio"),
     ("Perjuicio", "Disminución **económica efectiva** del patrimonio")],
    note="Cada eslabón debe ser **causa** del siguiente. Si falta uno, no hay estafa consumada. **Dolo directo:** el engaño es anterior o simultáneo a la disposición.")

add(s_cols, "El gran debate", "¿Cuándo el ardid es idóneo?",
    [("Tesis objetiva", ["Debe ser apto para engañar a un **hombre medio**", "Excluye engaños burdos", "Crítica: desprotege a víctimas vulnerables"]),
     ("Tesis subjetiva", ["Basta que **de hecho** engañe a la víctima concreta", "Atiende a edad, cultura, situación", "Crítica: amplía demasiado"]),
     ("Imputación objetiva", ["Riesgo **jurídicamente desaprobado**", "Pesan los **deberes de autoprotección**", "Debate actual en doctrina y en CSJN «Selman» (2020)"])],
    note="Postura prudente para litigar: valorar el engaño **en concreto** (víctima real), sin trasladar a ella la culpa por no desconfiar.")

add(s_table, "Ardid, mentira y silencio", "Qué engaña y qué no",
    ["Supuesto", "Regla general", "Ejemplo"],
    [["Ardid", "Típico: hay **puesta en escena**", "Falso escribano, papeles y oficina armada"],
     ["Mera mentira", "Debatido: típica si es **idónea** y genera error", "«Te pago mañana» sin intención de pagar"],
     ["Silencio", "Típico solo si hay **deber jurídico de informar**", "Vender un auto ocultando que es robado"],
     ["Engaño burdo", "Atípico o tentativa inidónea", "Billete de juguete a un cajero bancario"]])

add(s_svg, "Sujetos", "Estafa triangular: engañado ≠ perjudicado",
    triangle_svg("AUTOR (sujeto activo)", "ENGAÑADO-DISPONENTE", "PERJUDICADO", "ardid → error", "perjuicio", "disposición sobre patrimonio ajeno"),
    note="El disponente debe tener **facultad** (de hecho o de derecho) sobre el patrimonio ajeno: empleado bancario, cajero, mandatario, **juez** (estafa procesal).")

add(s_svg, "Iter criminis", "Consumación y tentativa",
    timeline_svg([("Idea", "Impune", "imp"), ("Preparación", "Impune|(salvo figuras autónomas)", "imp"),
                  ("Despliegue del ardid", "Comienzo de ejecución|= TENTATIVA", "tent"),
                  ("Disposición + perjuicio", "CONSUMACIÓN", "cons"), ("Lucro del autor", "Agotamiento|(no necesario)", "ago")]),
    note="La estafa es **delito de resultado**: se consuma con el **perjuicio**, no con el lucro. Tentativa: art. 42 CP (pena reducida de un tercio a la mitad, art. 44).")

add(s_cols, "Límite civil / penal", "Estafa o incumplimiento contractual",
    [("Incumplimiento civil", ["El deudor **quería cumplir** al contratar", "Después no pudo o no quiso", "Remedio: acción civil (CCyC)", "**Dolo posterior** (subsequens): no es estafa"]),
     ("Estafa contractual", ["El contrato es **la herramienta** del engaño", "Nunca hubo intención de cumplir", "Ej.: vender lo que no existe", "**Dolo inicial**: sí es estafa"])],
    note="Pregunta clave en la denuncia: **¿qué sabía y qué quería el autor al momento de contratar?** Indicios: identidad falsa, desaparición, multiplicidad de víctimas.")

add(s_svg, "Modalidad", "Estafa procesal",
    triangle_svg("LITIGANTE (autor)", "JUEZ (engañado)", "CONTRAPARTE (perjudicada)", "prueba falsa / ardid", "perjuicio", "sentencia = disposición patrimonial"),
    note="El juez dispone sobre el patrimonio ajeno mediante su resolución. **No basta la mera afirmación falsa** de la demanda: se exige un ardid (documento falso, testigos preparados).")

add(s_grid, "Art. 173 CP", "Los 16 casos especiales de defraudación",
    [("1", "Sustancia, calidad o cantidad", "Entrega distinta a lo pactado"), ("2", "Retención indebida", "No restituir lo recibido"),
     ("3", "Suscripción engañosa", "Hacer firmar con engaño"), ("4", "Abuso de firma en blanco", "Llenar el papel en perjuicio"),
     ("5", "Hurto impropio", "Dueño que sustrae su cosa"), ("6", "Contrato simulado", "O falsos recibos"),
     ("7", "Administración fraudulenta", "Infidelidad del gestor"), ("8", "Ocultar expedientes", "Sustituir o mutilar papeles"),
     ("9", "Estelionato", "Vender lo gravado o ajeno"), ("10", "Venta de humo", "Pretexto de coimear jueces"),
     ("11", "Desbaratamiento", "Frustrar derechos acordados"), ("12", "Fiduciario / leasing", "Disponer en perjuicio"),
     ("13", "Ejecución extrajudicial", "Sin mora o sin recaudos"), ("14", "Letras hipotecarias", "Omitir anotar pagos"),
     ("15", "Tarjetas", "Robadas, falsas o datos"), ("16", "Fraude informático", "Manipular sistemas")])

add(s_flow, "Art. 173 inc. 2", "Retención indebida paso a paso",
    [("Recepción legítima", "Dinero o mueble dado en **depósito, comisión, administración** u otro título"),
     ("Obligación de devolver", "El título obliga a **entregar o restituir**"),
     ("Intimación", "Requerimiento **fehaciente** (carta documento)"),
     ("Negativa u omisión", "No restituye **a su debido tiempo** con perjuicio")],
    note="TSJ Córdoba, Sala Penal (04/10/2012): la intimación es necesaria cuando no se restituye en término. Sin intimación fehaciente puede faltar el **dolo** (CNCrim y Correc., Sala IV, 2011).")

add(s_cols, "Art. 173 inc. 7", "Administración fraudulenta",
    [("Sujeto activo (delito especial)", ["Quien maneja, administra o cuida bienes ajenos", "Por **ley, autoridad o acto jurídico**", "Ej.: gerente, apoderado, administrador de consorcio, tutor"]),
     ("Dos modalidades", ["**Infidelidad**: perjudica los intereses confiados violando sus deberes", "**Abuso**: obliga abusivamente al titular", "Resultado: **perjuicio** al patrimonio confiado"]),
     ("Tipo subjetivo", ["Dolo + **fin de lucro indebido** (para sí o un tercero)", "o **fin de causar daño**", "CSJN «Pompas» (2002): la gestión es un **hecho único**"])])

add(s_table, "Art. 173 incs. 9 y 11", "Estelionato vs. desbaratamiento",
    ["Criterio", "Inc. 9 · Estelionato", "Inc. 11 · Desbaratamiento"],
    [["Conducta", "Vender o gravar como libres bienes **litigiosos, embargados o gravados**; vender o arrendar **lo ajeno** como propio", "Tornar **imposible, incierto o litigioso** un derecho ya acordado"],
     ["Engaño", "Sí: **ocultamiento** de la situación del bien", "No necesariamente: basta frustrar"],
     ["Víctima", "El comprador o acreedor engañado", "Quien tenía el derecho acordado"],
     ["Requisito", "Acto de venta, gravamen o arriendo", "Derecho acordado **por precio o en garantía**"],
     ["Ejemplo", "Vender un auto prendado como libre", "Vender a un tercero el lote ya comprometido por boleto"]], fs=21)

add(s_table, "Art. 173 inc. 15", "Defraudación con tarjetas",
    ["Supuesto", "Qué abarca"],
    [["Tarjeta falsificada o adulterada", "Plástico apócrifo o con datos alterados"],
     ["Hurtada, robada o perdida", "La tarjeta física salió de la esfera del titular"],
     ["Obtenida con ardid del emisor", "Se tramita con identidad o datos falsos"],
     ["Uso no autorizado de los **datos**", "No hace falta el plástico: compras online"],
     ["**Operación automática**", "Alcanza el cajero automático y el posnet"]],
    note="TSJ Córdoba, «Bonardi»: distingue el uso de la **tarjeta física** del uso no autorizado de sus **datos**. Origen: Ley 25.930 (B.O. 21/09/2004).")

add(s_cols, "Art. 173 inc. 16 vs. art. 172", "Fraude informático y ciberestafa",
    [("Estafa común (art. 172) por medios digitales", ["Se engaña a una **persona**", "La víctima transfiere **ella misma**", "Ej.: falso vendedor en Marketplace", "Ej.: WhatsApp robado que pide dinero"]),
     ("Fraude informático (art. 173 inc. 16)", ["Se **manipula un sistema**", "No hay persona engañada en la disposición", "Ej.: acceso con claves robadas y transferencia", "Incorporado por Ley 26.388 (2008)"])],
    note="Phishing: si la víctima entrega claves y el autor **transfiere él mismo** → inc. 16; si la víctima **transfiere engañada** → art. 172.")

add(s_table, "Ciberestafas", "Modalidades frecuentes y su calificación probable",
    ["Modalidad", "Mecánica", "Calificación probable"],
    [["Phishing / vishing", "Falso banco u organismo pide claves", "173 inc. 16 o 172"],
     ["SIM swapping", "Duplica el chip para recibir códigos", "173 inc. 16 (+ falsedades)"],
     ["Cuenta de WhatsApp robada", "Pide dinero a los contactos", "172"],
     ["Marketplace / alquiler falso", "Seña por un bien inexistente", "172"],
     ["Cuenta mula", "Recibe y reenvía fondos", "Partícipe necesario (art. 45) o encubrimiento"],
     ["Esquema Ponzi", "Paga rentas con aportes nuevos", "172 reiterado + 210 (+ art. 310)"]], fs=22)

add(s_table, "Art. 174 CP", "Defraudaciones agravadas: prisión de 2 a 6 años",
    ["Inc.", "Figura", "Clave"],
    [["1", "Fraude de seguros o préstamo a la gruesa", "Incendiar o destruir la cosa asegurada"],
     ["2", "Abuso de menores o incapaces", "Hacerles firmar un documento"],
     ["3", "Pesas o medidas falsas", "Defraudar al cliente en la medida"],
     ["4", "Fraude en la construcción", "Pone en peligro personas, bienes o al Estado"],
     ["5", "Fraude a la administración pública", "Perjuicio a un patrimonio estatal"],
     ["6", "Vaciamiento de empresas", "Afectar maliciosamente la explotación (Ley 25.602)"]],
    note="Funcionario o empleado público autor: **inhabilitación especial perpetua** (último párrafo).")

add(s_cols, "Arts. 175 y 175 bis", "Defraudaciones atenuadas y usura",
    [("Art. 175 · multa", ["**Inc. 1:** apropiarse de una cosa perdida o de un tesoro", "**Inc. 2:** apropiarse de lo recibido por error o caso fortuito (transferencia equivocada)", "**Inc. 3:** prestamista que vende o se apropia de la prenda", "**Inc. 4:** acreedor que exige un cheque posdatado o en blanco en garantía"]),
     ("Art. 175 bis · usura", ["Aprovechar **necesidad, ligereza o inexperiencia**", "Intereses o ventajas **evidentemente desproporcionadas**", "Prisión de 1 a 3 años + multa", "Usurero **profesional o habitual**: 3 a 6 años"])])

add(s_table, "Capítulo V", "Quebrados y otros deudores punibles",
    ["Art.", "Figura", "Pena"],
    [["176", "Quiebra fraudulenta (comerciante fallido)", "Prisión 2 a 6 años + inhab. 3 a 10"],
     ["177", "Quiebra culpable (negligencia o imprudencia)", "Prisión 1 mes a 1 año + inhab. 2 a 5"],
     ["178", "Directivos, síndicos, contadores que cooperan", "Pena del 176 o 177"],
     ["179, 1er párr.", "Concurso civil fraudulento", "Prisión 6 meses a 3 años"],
     ["179, 2.º párr.", "**Insolvencia fraudulenta** (frustrar una condena)", "Prisión 6 meses a 3 años"],
     ["180", "Connivencia en concordato o transacción", "Prisión 1 mes a 1 año"]],
    note="Clave para el abogado civilista y de familia: vaciar el patrimonio **durante el juicio o después de la sentencia** puede encuadrar en el art. 179, 2.º párrafo.")

add(s_cols, "Cheques", "¿Estafa (art. 172) o libramiento sin fondos (art. 302)?",
    [("Estafa con cheque", ["El cheque es **el ardid**", "Entrega **simultánea** a la contraprestación", "La víctima entrega **por** el cheque", "Pena: 1 mes a 6 años"]),
     ("Art. 302 CP", ["Cheque **en pago** de deuda previa", "Sin fondos y no paga en 24 h desde el aviso", "Contraorden fuera de la ley", "Formulario ajeno sin autorización", "Pena: 6 meses a 4 años + inhabilitación"])],
    note="El art. 302 es **subsidiario**: rige «siempre que no concurran las condiciones del artículo 172». El **cheque de pago diferido** es un instrumento de crédito: en principio no sirve como ardid de estafa por pago simultáneo.")

add(s_bullets, "Art. 185 CP", "Excusa absolutoria entre parientes",
    ["**No hay pena** (pero sí responsabilidad civil) por hurtos, **defraudaciones** o daños recíprocos entre:",
     "**Cónyuges**, ascendientes, descendientes y afines en línea recta",
     "**Consorte viudo**, sobre las cosas del difunto, mientras no hayan pasado a otro",
     "**Hermanos y cuñados** que **vivan juntos**",
     "**No alcanza** a los extraños que participen del delito",
     "Jurisprudencia: rige aun entre cónyuges **separados de hecho**; se discute su extensión a las **uniones convivenciales**"])

add(s_table, "Cuestiones comunes", "Consecuencias procesales y de fondo",
    ["Instituto", "Regla aplicada a la estafa (art. 172)"],
    [["Acción", "**Pública**, de oficio (no es dependiente de instancia)"],
     ["Prescripción", "Art. 62 inc. 2: máximo de la pena = **6 años** (interrupción: art. 67)"],
     ["Condena condicional", "Posible si la pena impuesta no supera **3 años** (art. 26)"],
     ["Suspensión del juicio a prueba", "Art. 76 bis, 4.º párr. (CSJN «Acosta», 2008); exige **ofrecer reparación**"],
     ["Reparación integral", "Art. 59 inc. 6 (Ley 27.147); en Córdoba, art. 13 bis CPP (Ley 10.457)"],
     ["Tentativa", "Arts. 42 y 44: pena reducida de un tercio a la mitad"]])

add(s_bullets, "Competencia territorial", "¿Dónde se investiga la estafa a distancia?",
    ["CSJN (Fallos 311:2607 y 333:2052): son relevantes **tanto** el lugar donde se **desplegó el ardid** como el lugar donde se produjo la **disposición patrimonial**",
     "Se decide por **economía y celeridad procesal**: donde esté la mayor parte de la prueba, de los imputados o de las víctimas",
     "Ciberestafas: suele prevenir el juez del **domicilio de la víctima** o de la cuenta de destino",
     "Córdoba: **Fiscalía de Instrucción Especializada en Cibercrimen** (Ley 10.593) y **OECED** (Res. FG 14/2025)"])

add(s_flow, "Práctica en Córdoba", "Circuito del proceso penal (CPP Ley 8123)",
    [("Denuncia", "Fiscalía, Policía o **denuncia web**; constitución como **querellante particular**"),
     ("Investigación penal preparatoria", "Dirige el **Fiscal de Instrucción**; controla el **Juez de Control**"),
     ("Medidas urgentes", "Informes bancarios, **bloqueo de fondos**, secuestro, pericias digitales"),
     ("Juicio", "**Cámara en lo Criminal y Correccional**; opción de juicio abreviado")],
    note="En paralelo: **actor civil** (restitución e indemnización) o vía civil autónoma (art. 1774 y ss. CCyC).")

add(s_bullets, "Checklist", "La denuncia de estafa que funciona",
    ["**Relato cronológico**: quién, cuándo, dónde, cómo fue el engaño",
     "**Por qué creíste**: cuál fue el ardid (documentos, perfiles, llamadas)",
     "**Disposición**: qué entregaste o transferiste, con comprobantes (CBU/CVU, alias, montos)",
     "**Perjuicio**: monto total y moneda; gastos derivados",
     "**Evidencia digital**: capturas con fecha, URL, número telefónico, correos con encabezados",
     "**Pedir medidas urgentes**: bloqueo de la cuenta de destino e informes al banco o billetera"], small=True)

add(s_tree, "Método", "Cómo calificar el caso en 5 preguntas",
    [("¿Hubo **engaño** que causó error y una disposición patrimonial?", "Art. 172 (o inciso especial del 173)"),
     ("¿El autor **ya tenía** el bien o lo administraba?", "Abuso de confianza: art. 173 incs. 2 o 7"),
     ("¿Se **manipuló un sistema** sin engañar a una persona?", "Art. 173 inc. 16 (o inc. 15 si hay tarjeta)"),
     ("¿Hay víctima **Estado**, seguro, incapaz o empresa vaciada?", "Agravante del art. 174"),
     ("¿El autor es **pariente** que convive o es cónyuge?", "Excusa absolutoria del art. 185")])

add(s_bullets, "Cierre", "Cinco ideas fuerza",
    ["La estafa es una **cadena causal**: ardid → error → disposición → perjuicio",
     "Lo decisivo es el **dolo inicial**: separa la estafa del incumplimiento civil",
     "El art. 173 **no exige siempre engaño**: también castiga el **abuso de confianza**",
     "En lo digital, distinguir **persona engañada** (art. 172) de **sistema manipulado** (art. 173 inc. 16)",
     "En la práctica: **rapidez** (bloqueo de fondos), **prueba documental** y **querella**"])

def main():
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        os.remove(os.path.join(OUT, f))
    for i, h in enumerate(SLIDES, 1):
        with open(os.path.join(OUT, f"s{i:02d}.html"), "w", encoding="utf-8") as fh:
            fh.write(h)
    print(len(SLIDES), "filminas generadas")

if __name__ == "__main__":
    main()
