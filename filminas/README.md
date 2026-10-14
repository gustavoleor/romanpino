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
Las penas se cargaron del Código Penal (Ley 11.179, t.o. y reformas). Sólo las de los arts. 84 y 84 bis
fueron contrastadas con el texto de la Ley 27.347 (InfoLEG); `verif=True` marca esas láminas con “✔ contrastada”.
**Contrastar el resto con el texto vigente antes de usarlas.**
