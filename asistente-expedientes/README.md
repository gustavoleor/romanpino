# Asistente de Expedientes

Aplicación de escritorio (Electron) para trabajar con IA **sobre los documentos concretos de un juicio**: una carpeta por expediente, con PDF, DOCX y TXT.

> Herramienta de apoyo. No reemplaza el criterio del letrado: todo resultado debe ser revisado antes de usarse. Las normas y la jurisprudencia que sugiera la IA se marcan `[VERIFICAR NORMA]` y deben cotejarse con la fuente oficial.

## Qué hace

| Función | Cómo |
|---|---|
| **Análisis y resumen** | Resume partes, pretensión, hechos de cada lado, prueba y etapa procesal. |
| **Cronología** | Ordena por fecha hechos y actuaciones, cada uno con cita textual y página. Se guarda en el caso. |
| **Contradicciones** | Cruza escritos de las partes, testimoniales y prueba documental/pericial. |
| **Comparar documentos** | Demanda vs. contestación: reconocido / negado / no contestado. |
| **Redacción de escritos** | Alegatos, recursos, etc. El borrador viene precedido de un cuadro **acreditado / controvertido / sin respaldo**. |
| **Control de errores** | Revisa un borrador (de la carpeta o pegado): afirmaciones sin respaldo, omisiones, fechas y cálculos. |
| **Índice de prueba** | Tabla de la prueba documental con ubicación. |
| **Búsqueda documental** | Local e instantánea (BM25, sin IA) y "Preguntar al expediente" con respuesta citada. |
| **Plazos** | Carga manual o detección de fechas por IA; cómputo de vencimiento (hábiles/corridos) con feriados y ferias que cargás vos; avisos de escritorio y exportación `.ics` con alarmas. |
| **Exportar a Word** | Cualquier resultado a `.docx` (Times New Roman 12, tablas incluidas). |

## Cómo se evita que la IA "invente"

1. El modelo solo recibe el texto del expediente (con marcas de página) y está instruido para no afirmar nada que no surja de él ni inventar normas o fallos.
2. Cada dato debe venir como `«texto literal» [Fuente: archivo.pdf, p. 12]`.
3. **Verificación automática, hecha por la app y no por la IA:** tras cada respuesta se comprueba que el documento exista, que la página exista y que el texto entre comillas figure literalmente en esa página. Lo que no pasa el control se informa al pie del resultado.
4. Hacer clic en una cita abre el pasaje original.

## Uso

```bash
cd asistente-expedientes
npm install
npm run demo      # crea ./ejemplo-expediente (juicio laboral ficticio con contradicciones)
npm start
```

En **Ajustes**: cargá tu clave de API de Anthropic (se guarda cifrada con el almacén del sistema operativo; también se acepta `ANTHROPIC_API_KEY`), aceptá el aviso de confidencialidad y cargá feriados/ferias.

Tests: `npm test`. Instalador: `npm run dist`.

## Datos y confidencialidad

- Los documentos **no se copian ni se suben a ningún servidor propio**. El índice y los resultados se guardan en `<carpeta del caso>/.asistente/`.
- Al ejecutar una tarea, el texto de los documentos tildados se envía a la API de Anthropic. Revisá los términos de tratamiento de datos de tu cuenta y tus deberes de reserva profesional; considerá anonimizar partes antes de usarla con casos reales.
- La búsqueda local no envía nada a la nube.

## Límites actuales

- **PDF escaneados:** no hay OCR; la app los detecta y avisa. Hace falta pasarlos por OCR antes.
- **DOCX/TXT** no tienen paginación fija: se citan por "bloque" (≈3000 caracteres).
- **Expedientes muy extensos:** si superan el límite por consulta (ajustable) se envían solo las páginas más relevantes y el resultado lo indica.
- **Plazos:** la app no trae calendario judicial ni aplica reglas de cómputo propias de cada fuero; calcula con lo que cargues. Verificá siempre.

## Estructura

```
main.js / preload.js     Electron (IPC con puente aislado)
renderer/                Interfaz (HTML/CSS/JS, Markdown seguro)
src/core/                Lógica sin dependencia de Electron (testeable)
  extract.js             PDF/DOCX/TXT → páginas
  casestore.js           Carpeta = caso; índice incremental en .asistente/
  search.js              BM25 local en español
  context.js             Arma el expediente con marcas de página
  prompts.js             Reglas del sistema y tareas
  citations.js           Verificación de citas contra el expediente
  tasks.js · llm.js      Ejecución de tareas y cliente de IA
  deadlines.js           Cómputo de plazos, recordatorios, .ics
  exporter.js            Markdown → Word
```
