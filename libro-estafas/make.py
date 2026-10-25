# -*- coding: utf-8 -*-
"""Construye el libro en dos pasadas: la primera para medir en qué página cae cada título
y la segunda para escribir el índice con esos números."""
import json, os, re, subprocess, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
DOCX = os.path.join(HERE, "Estafas_y_defraudaciones_Codigo_Penal_argentino.docx")
PDF = os.path.join(BUILD, "Estafas_y_defraudaciones_Codigo_Penal_argentino.pdf")
os.makedirs(BUILD, exist_ok=True)

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("**", "").replace("*", "")
    return re.sub(r"[^a-z0-9]+", "", s.lower())

def build():
    subprocess.run([sys.executable, os.path.join(HERE, "build_docx.py")], check=True)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", BUILD, DOCX],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=600)

def page_texts():
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout).group(1))
    out = []
    for i in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", PDF, "-"], capture_output=True, text=True).stdout
        out.append(norm(t))
    return out

def headings():
    sys.path.insert(0, HERE)
    import importlib, dsl
    dsl.BLOCKS.clear()
    for m in ("c1_general", "c2_173a", "c3_173b", "c4_174_180", "c5_practica", "c6_mas", "c7_cierre"):
        if m in sys.modules:
            importlib.reload(sys.modules[m])
        else:
            importlib.import_module(m)
    return [b[1] for b in dsl.BLOCKS if b[0] in ("h1", "h2")]

def measure():
    pages = page_texts()
    hs = headings()
    # salta las páginas del índice: busca la primera aparición después de la última página del índice
    start = 0
    for i, t in enumerate(pages[:12]):
        if "indice" in t[:40]:
            start = i
    # el índice ocupa varias páginas; el contenido empieza donde aparece por primera vez el primer título y no hay "......"
    res, pos = {}, start + 1
    for k, h in enumerate(hs):
        key = norm(h)[:38]
        found = None
        for j in range(pos, len(pages)):
            if key in pages[j]:
                # descarta las páginas del índice (tienen muchos títulos)
                if sum(1 for x in hs[:20] if norm(x)[:25] in pages[j]) > 6:
                    continue
                found = j; break
        if found is None:
            print("NO ENCONTRADO:", h); res[str(k)] = "?"; continue
        res[str(k)] = found + 1
        pos = found
    return res, len(pages)

if __name__ == "__main__":
    tp = os.path.join(BUILD, "toc_pages.json")
    if os.path.exists(tp):
        os.remove(tp)
    build()
    for it in range(3):
        res, n = measure()
        old = json.load(open(tp)) if os.path.exists(tp) else None
        json.dump(res, open(tp, "w"))
        build()
        print("pasada", it + 1, "páginas:", n)
        if old == res:
            break
    res, n = measure()
    print("páginas finales:", n, "| índice estable:", res == json.load(open(tp)))
