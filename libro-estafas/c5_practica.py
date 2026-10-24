# -*- coding: utf-8 -*-
from dsl import *

# =====================================================================
PARTE("Cuarta parte", "La práctica: el proceso penal en Córdoba")
H1("Capítulo 12. La estafa en el proceso penal de Córdoba")
P("Este capítulo traslada lo estudiado al trámite concreto en la Provincia de Córdoba, regido por el **Código Procesal Penal (Ley 8123** y modificatorias). Está pensado para el abogado que asesora a la víctima o al imputado.")
FIG(26, "Circuito del proceso penal en Córdoba.")
H2("12.1. Los actores del proceso")
TAB(["Órgano", "Función en una causa por estafa"],
    [["Fiscal de Instrucción", "Dirige la investigación penal preparatoria, imputa, ordena la mayoría de las medidas de prueba, dispone el archivo o requiere la citación a juicio"],
     ["Fiscalía de Instrucción Especializada en Cibercrimen", "Creada por la Ley 10.593 en la Primera Circunscripción; investiga las ciberestafas y coordina la oficina técnica"],
     ["OECED (Oficina Especializada en Ciberdelitos y Evidencia Digital)", "Apoyo técnico en toda la provincia, con dependencia de la Fiscalía General (Res. FG 14/2025)"],
     ["Policía Judicial / Unidades Judiciales", "Reciben denuncias, practican diligencias bajo dirección fiscal"],
     ["Juez de Control", "Controla la legalidad de la investigación, resuelve oposiciones, decide medidas que afectan garantías (allanamientos, prisión preventiva, embargos), resuelve sobreseimientos"],
     ["Cámara en lo Criminal y Correccional", "Tribunal de juicio (sala unipersonal o colegiada, según el caso); también interviene en el juicio abreviado"],
     ["Tribunal Superior de Justicia, Sala Penal", "Recurso de casación e inconstitucionalidad; unifica la interpretación provincial"]],
    [5, 11])
H2("12.2. La denuncia")
FIG(27, "Checklist de la denuncia de estafa.")
P("La denuncia puede presentarse ante la Fiscalía, ante la Policía Judicial o ante cualquier unidad judicial, por escrito o verbalmente. Para la estafa, una buena denuncia es la que permite al fiscal **reconstruir la cadena típica** sin tener que volver a citar a la víctima. Debe contener:")
NUM(["**Datos de la víctima y del denunciado** (todo lo que se conozca: nombre, alias, teléfono, perfil de redes, CBU/CVU, alias, patente, domicilio).",
     "**Relato cronológico** del contacto, del engaño y de la entrega, con fechas y horas.",
     "**El ardid**: qué se le dijo o mostró a la víctima y por qué le creyó (documentos, oficinas, perfiles, voces, referencias).",
     "**La disposición patrimonial**: qué entregó, cómo (efectivo, transferencia, cheque, firma) y a quién.",
     "**El perjuicio**: monto total, moneda y gastos derivados.",
     "**La prueba** que se acompaña y la que se ofrece (testigos, informes, pericias).",
     "**Las medidas urgentes** que se solicitan (bloqueo de cuentas, informes bancarios, secuestro de bienes, preservación de datos)."])
H2("12.3. La víctima en el proceso: querellante particular y actor civil")
P("La víctima de una estafa tiene dos formas de intervenir como parte, que pueden acumularse:")
BUL(["**Querellante particular**: interviene para impulsar la investigación y acreditar el delito, proponer prueba, controlar la actuación fiscal, oponerse al archivo o al sobreseimiento y recurrir en los casos que la ley autoriza (CPP Córdoba, art. 7 y regulación específica en el capítulo del querellante particular).",
     "**Actor civil**: ejerce en el proceso penal la acción resarcitoria para obtener la restitución y la indemnización (acción civil en sede penal, art. 24 y capítulo del actor civil del CPP de Córdoba). Es una alternativa a la demanda civil autónoma."])
TIP("En las estafas de monto importante conviene constituirse en **querellante desde el inicio**: permite pedir medidas cautelares sobre los bienes del imputado (embargo, inhibición) y evita que la causa se archive por falta de impulso. En las estafas pequeñas, una buena denuncia con prueba documental suele bastar.")
OJO("La numeración de los artículos del CPP de Córdoba sobre querellante y actor civil debe verificarse en el texto ordenado vigente de la Ley 8123 antes de citarlos en un escrito.")
H2("12.4. Medidas de investigación y cautelares típicas")
TAB(["Objetivo", "Medida"],
    [["Identificar al autor", "Informes a bancos, billeteras y PSP sobre el titular de la cuenta de destino, su legajo y las IP de alta y de operación; informes a las empresas de telefonía y a las plataformas"],
     ["Seguir el dinero", "Informes de movimientos de las cuentas receptoras y de las cuentas a las que se transfirió después; requerimientos a exchanges de criptoactivos"],
     ["Evitar la pérdida de los fondos", "Bloqueo o inmovilización de saldos; embargo e inhibición de bienes del imputado"],
     ["Asegurar la prueba", "Secuestro de celulares y computadoras; orden de presentación de documentación; preservación de datos ante proveedores"],
     ["Acreditar el perjuicio", "Pericia contable; informes de valuación; comprobantes de pago"],
     ["Probar el dolo inicial", "Antecedentes de denuncias por la misma mecánica; informes de existencia de la empresa (registros públicos, AFIP/ARCA); allanamientos"]],
    [5, 11])
H2("12.5. Salidas alternativas")
TAB(["Instituto", "Fuente", "Aplicación a las defraudaciones"],
    [["Criterios de oportunidad y conciliación", "Art. 59 inc. 6 CP; art. 13 bis CPP Córdoba (Ley 10.457, 2017)", "Si la conciliación produce un acuerdo resarcitorio, el fiscal solo puede prescindir de la acción cuando la víctima haya recibido la totalidad de lo acordado (inc. 5 del art. 13 bis, según la doctrina citada)"],
     ["Suspensión del juicio a prueba", "Art. 76 bis CP", "Procede en estafas cuando la pena posible admite condena condicional (CSJN, «Acosta»); exige ofrecer reparación razonable"],
     ["Juicio abreviado", "CPP Córdoba", "Acuerdo sobre los hechos y la calificación; la pena no puede superar la pedida por el fiscal. Muy usado en las estafas reiteradas"],
     ["Extinción por pago de la multa", "Art. 64 CP", "Solo en las figuras del art. 175, que se castigan con multa"]],
    [4, 5, 7])
P("Según un trabajo publicado en la Revista de la Facultad de Derecho de la Universidad Católica de Córdoba, el art. 13 bis del CPP fue incorporado por la Ley provincial 10.457 de 2017 y regula la extinción de la acción por conciliación. Es la única disposición local vinculada directamente con el art. 59 inc. 6 CP. Una guía de la Fiscalía General (Resolución General 20/19) señala que los criterios de oportunidad son de resorte exclusivo del Ministerio Público Fiscal.")
H2("12.6. Relación entre la causa penal y el reclamo civil")
P("El Código Civil y Comercial regula la relación entre ambas acciones (arts. 1774 a 1780):")
BUL(["Las acciones civil y penal son **independientes** (art. 1774): la víctima puede demandar en sede civil sin esperar el resultado penal.",
     "Si la acción penal precede a la civil o se promueve durante su curso, el juez civil **no puede dictar sentencia** hasta la conclusión del proceso penal, con las excepciones del art. 1775 (por ejemplo, si la dilación del proceso penal provoca una frustración efectiva del derecho a ser indemnizado).",
     "La sentencia penal **condenatoria** hace cosa juzgada en sede civil respecto de la existencia del hecho principal y de la culpa del condenado (art. 1776). La **absolutoria** por inexistencia del hecho o por no ser el imputado su autor también se impone en sede civil, pero no la que absuelve por otros motivos (art. 1777)."])
TIP("En las estafas inmobiliarias y en las defraudaciones societarias, la estrategia más eficaz suele combinar **ambas vías**: la denuncia penal (con querella) para acceder rápidamente a la prueba y a las medidas cautelares, y la demanda civil (cumplimiento, nulidad, simulación, daños) con **anotación de litis** o **prohibición de innovar** sobre los bienes.")
H2("12.7. Modelos de escritos")
OJO("Los modelos son orientativos. Adapte los datos, verifique la numeración de los artículos del CPP de Córdoba vigente y la competencia, y revise los requisitos formales de cada presentación.")
H3("a) Denuncia penal por estafa")
P("**FORMULA DENUNCIA PENAL. SOLICITA MEDIDAS URGENTES.**")
P("Sr./Sra. Fiscal de Instrucción: [NOMBRE], DNI [...], con domicilio real en [...], por derecho propio y con el patrocinio letrado de [ABOGADO], M.P. [...], constituyendo domicilio procesal en [...] y electrónico en [...], comparezco y digo:")
P("**I. Objeto.** Formulo denuncia penal contra [NOMBRE o «quienes resulten responsables»], por el delito de estafa (art. 172 CP) [o el inciso del art. 173 que corresponda], en virtud de los hechos que paso a exponer.")
P("**II. Hechos.** El día [fecha], a las [hora], [relato cronológico del contacto]. El denunciado se presentó como [calidad simulada / nombre supuesto] y me exhibió [documentos, perfiles, oficinas]. Convencido de la veracidad de lo que se me decía, el día [fecha] entregué / transferí la suma de [monto] a la cuenta CBU/CVU [...], alias [...], de titularidad de [...]. Posteriormente, [cómo se descubrió el engaño]. Sufrí así un perjuicio patrimonial de [monto].")
P("**III. Calificación.** Los hechos encuadran, prima facie, en el delito de estafa (art. 172 CP): existió un ardid ([describir]) que me indujo a error ([describir]), en virtud del cual realicé una disposición patrimonial ([describir]) que me causó un perjuicio de [monto].")
P("**IV. Prueba.** Acompaño: a) capturas de pantalla de las conversaciones (con número, fecha y hora); b) comprobantes de transferencia; c) [otros]. Ofrezco: a) testimonial de [...]; b) informativa a [banco/billetera] para que informe titularidad, datos de alta, IP y movimientos de la cuenta de destino; c) informativa a [empresa de telefonía] sobre la titularidad de la línea [...].")
P("**V. Medidas urgentes.** Solicito se ordene con carácter urgente: a) el **bloqueo / inmovilización** de los fondos existentes en la cuenta [...] y en las cuentas a las que se hubieran transferido; b) la preservación de los datos de tráfico y de la cuenta del perfil [...].")
P("**VI. Petitorio.** Por lo expuesto, solicito: 1) Se tenga por formulada la denuncia; 2) Se ordenen las medidas urgentes solicitadas; 3) [Si corresponde] se me tenga por constituido en querellante particular en los términos del art. 7 y concordantes del CPP. Proveer de conformidad. SERÁ JUSTICIA.")
H3("b) Intimación previa por retención indebida (carta documento)")
P("«Intimo a usted para que, en el plazo de 48 horas de recibida la presente, me restituya [la suma de $... / el bien ...] que le entregué el día [...] en carácter de [depósito / mandato para cobrar / comisión], conforme [instrumento]. Vencido el plazo sin la restitución, iniciaré las acciones civiles y penales correspondientes, incluida la denuncia por defraudación por retención indebida (art. 173 inc. 2 CP). Queda usted debidamente notificado.»")
TIP("La intimación debe identificar con precisión **qué** se reclama, **por qué título** se entregó y **en qué plazo** debe restituirse. Es la pieza central para probar el dolo en la retención indebida.")
RES("**Resumen del capítulo.** En Córdoba la investigación la dirige el Fiscal de Instrucción, con control del Juez de Control; las ciberestafas se concentran en la Fiscalía especializada en Cibercrimen y la OECED. La víctima puede ser **querellante particular** y **actor civil**. Las medidas clave son el bloqueo de fondos, los informes bancarios y de telefonía y la pericia contable. Las salidas alternativas (conciliación, art. 13 bis CPP; probation; juicio abreviado) giran en torno a la **reparación**. Las acciones civil y penal son independientes, con las reglas de prejudicialidad de los arts. 1774 a 1780 CCyC.")

