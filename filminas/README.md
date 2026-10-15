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
Cada filmina muestra bajo el título una etiqueta:
- ✔ verde = contrastada con el texto de la ley reformatoria vigente; ✔ turquesa = contrastada con el texto ordenado de 1984 (Decreto 3992/84), sin verificar reformas posteriores; ✔ *norma y pena contrastadas* (cotejadas con el texto legal en InfoLEG),
⚠ *sin contrastar* (cargadas de memoria) o ⚠ *norma contrastada · pena sin contrastar*. Las de doctrina no llevan etiqueta.
Se fijan con el campo `ok` de cada filmina en `slides.py` / `slides2.py`.

Contrastadas con el t.o. 1984 (InfoLEG, Decreto 3992/84): arts. 34, 35, 54, 79, 81, 89 a 91, 149 bis, 150, 162, 164, 172, 173 (incs. 1, 2, 3 y 7) y 183.
Pendientes de las reformas posteriores: art. 55 (Ley 25.928), art. 58, art. 80 (Leyes 25.601, 25.816, 26.791), art. 173 inc. 16 (Ley 26.388), arts. 125 y 133, Ley 23.737 arts. 11, 14 y 17 a 21, y la cita de Arriola.
Contrastadas con la ley reformatoria: arts. 84 y 84 bis (Ley 27.347); arts. 119 (Ley 27.352), 120, 128 (Ley 27.436), 131 (Ley 26.904),
72 (Ley 27.455) y 132 (Ley 26.738); arts. 5, 6, 7, 24, 27, 44, 44 bis y 45 de la Ley 23.737 (Ley 27.302); art. 173 inc. 15 (Ley 25.930).
**Todo lo demás debe contrastarse con el texto vigente antes de usarse.**
