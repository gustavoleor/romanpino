"""Orden final del deck: une el lote 1 (slides.py) y el lote 2 (slides2.py)."""
from slides import SLIDES as _BASE
from slides2 import NEW as _NEW

_BY_ID = {s["id"]: s for s in _BASE + _NEW}

ORDER = [
    # Teoría general
    "t01-legalidad", "t02-concepto", "t03-accion-omision", "t04-tipicidad", "t05-dolo-culpa",
    "t08-inimputabilidad", "t09-iter-criminis", "t10-autoria",
    # Concurso de delitos
    "t11-concursos", "c01-aparente", "c02-continuado", "c03-calculo", "c04-unificacion",
    # Causas de justificación
    "j01-introduccion", "t06-legitima-defensa", "j02-defensa-privilegiada", "j03-defensa-terceros",
    "j04-deber-derecho", "t07-estado-necesidad", "j05-necesidad-justifica-exculpa", "j06-exceso",
    "j07-consentimiento", "j08-justificacion-vs-exculpacion", "j09-obediencia",
    # Delitos contra las personas y la libertad
    "d01-homicidio-simple", "d02-homicidio-agravado", "d03-emocion-violenta", "d04-homicidio-culposo",
    "d05-lesiones", "d06-amenazas", "d07-violacion-domicilio",
    # Propiedad: hurto, robo, estafa y defraudaciones, daño
    "d08-hurto", "d09-robo", "d10-estafa", "e01-hurto-vs-estafa", "e02-ardides",
    "e03-defraudaciones-especiales", "e04-administracion-fraudulenta", "e05-retencion-indebida",
    "e06-tarjeta", "e07-informatica", "d11-danio",
    # Integridad sexual
    "x01-integridad-sexual", "x02-abuso-simple", "x03-ultrajante", "x04-acceso-carnal", "x05-agravantes",
    "x06-estupro", "x07-edades", "x08-pornografia-infantil", "x09-grooming", "x10-accion-penal",
    "x11-corrupcion", "x12-cooperacion",
    # Estupefacientes
    "n01-panorama", "n02-comercio", "n03-entrega", "n04-siembra", "n05-introduccion", "n06-organizar",
    "n07-precursores", "n08-personas-juridicas", "n09-tenencia", "n10-arriola",
]

assert len(ORDER) == len(set(ORDER)) == len(_BY_ID), (len(ORDER), len(_BY_ID), set(_BY_ID) ^ set(ORDER))
SLIDES = [_BY_ID[i] for i in ORDER]
