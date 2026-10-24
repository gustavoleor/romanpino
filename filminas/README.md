# Filminas de Derecho Penal argentino

Láminas ilustradas (JPG 1920×1080 + PDF), una idea por lámina, texto mínimo.

- `salida/jpg/` → una imagen por filmina
- `salida/filminas-derecho-penal.pdf` → todas en un PDF

## Regenerar
```
python3 build.py            # todas
python3 build.py hurto      # solo las que contengan "hurto" en el id (y rearma el PDF)
```
Requiere Python 3 + Pillow y la tipografía Inter (`/usr/share/fonts/opentype/inter`).

## Agregar una filmina
1. Dibujar la escena en `scenes.py` (usa los pictogramas de `kit.py`).
2. Agregar un `dict` en `slides.py`: título, artículo, hasta 3 viñetas, pena.

## Control de contenido
Cada filmina muestra bajo el título una etiqueta de contraste (se fija con el campo `ok` en `slides.py` / `slides2.py`):
- ✔ verde: norma y pena contrastadas con el texto legal (última reforma localizada en InfoLEG).
- ✔ turquesa: contrastada con el texto ordenado de 1984 (Decreto 3992/84) o con la Ley 23.737 original (1989); reformas posteriores sin verificar.
- ⚠ ámbar: sin contrastar (cargada de memoria) — hoy solo Arriola (CSJN) y las dudas señaladas en cada lámina.
Las láminas de doctrina no llevan etiqueta.

Fuentes contrastadas: Código Penal t.o. 1984; Leyes 25.928 (art. 55), 25.601, 25.816 y 26.791 (art. 80), 27.347 (arts. 84, 84 bis),
25.087, 27.352, 27.436, 26.904, 26.738, 27.455 (integridad sexual), 26.842 (no modifica los arts. 125 y 133), 25.930 y 26.388 (art. 173 y 183),
Ley 23.737 original y Ley 27.302.
