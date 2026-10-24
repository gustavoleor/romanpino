# -*- coding: utf-8 -*-
from dsl import *

# =====================================================================
H1("Capítulo 17. Cuadro final: cómo calificar un caso")
FIG(28, "Método para calificar un caso en cinco preguntas.")
P("Para cerrar la exposición, conviene ofrecer al auditorio un **método** que puedan aplicar a cualquier caso. Las cinco preguntas de la filmina se resuelven en este orden:")
NUM(["**¿Hubo engaño, error y disposición patrimonial perjudicial?** Si la respuesta es sí, estamos ante una estafa: art. 172, salvo que el medio o el objeto coincidan con un inciso especial del art. 173 (1, 3, 9, 10) o con el art. 174.",
     "**¿El autor ya tenía legítimamente el bien o su administración?** Entonces es un abuso de confianza: retención indebida (art. 173 inc. 2), administración fraudulenta (inc. 7) o defraudación fiduciaria (inc. 12).",
     "**¿Se manipuló un sistema sin engañar a una persona, o se usó una tarjeta o sus datos?** Art. 173 inc. 16 o inc. 15.",
     "**¿La víctima es el Estado, una aseguradora o un incapaz, o se vació una empresa?** Agravante del art. 174.",
     "**¿El autor es cónyuge, ascendiente, descendiente, afín en línea recta, o hermano o cuñado conviviente?** Excusa absolutoria del art. 185: no hay pena, pero sí responsabilidad civil."])
TAB(["Si el caso es…", "Califique como…", "Pena"],
    [["Engaño + entrega de la víctima", "Estafa (art. 172)", "1 mes a 6 años"],
     ["No devuelve lo recibido en depósito o para entregar", "Retención indebida (art. 173 inc. 2)", "1 mes a 6 años"],
     ["Administrador que perjudica el patrimonio confiado", "Administración fraudulenta (art. 173 inc. 7)", "1 mes a 6 años"],
     ["Vende como libre algo embargado o como propio algo ajeno", "Estelionato (art. 173 inc. 9)", "1 mes a 6 años"],
     ["Vende dos veces lo que ya había comprometido", "Desbaratamiento (art. 173 inc. 11)", "1 mes a 6 años"],
     ["Usa una tarjeta ajena o sus datos", "Art. 173 inc. 15", "1 mes a 6 años"],
     ["Opera el home banking con claves ajenas", "Fraude informático (art. 173 inc. 16)", "1 mes a 6 años"],
     ["Estafa al Estado", "Art. 174 inc. 5", "2 a 6 años"],
     ["Se queda con una transferencia equivocada", "Art. 175 inc. 2", "Multa"],
     ["Presta dinero a tasas desproporcionadas aprovechando la necesidad", "Usura (art. 175 bis)", "1 a 3 años (3 a 6 si es habitual)"],
     ["Se insolventa durante el juicio", "Insolvencia fraudulenta (art. 179, 2.º párr.)", "6 meses a 3 años"],
     ["Entrega un cheque sin fondos en pago de una deuda previa", "Art. 302", "6 meses a 4 años e inhabilitación"]],
    [7, 6, 4])
FIG(29, "Cinco ideas fuerza para el cierre.")
RES("**Síntesis general.** La estafa es una cadena causal (ardid, error, disposición, perjuicio) y el dolo debe ser **inicial**. El art. 173 agrega casos especiales que no siempre requieren engaño (abuso de confianza, desbaratamiento, fraude informático). El art. 174 agrava por la víctima o el medio, el 175 atenúa y el 175 bis castiga la usura. En la práctica, la calificación depende de **quién dispuso y cómo**, y el éxito de la causa, de la **rapidez** y la **prueba documental**.")

# =====================================================================
PARTE("Anexos", "Herramientas para la conferencia y el estudio")
H1("Anexo I. Guion de la conferencia (90 minutos)")
TAB(["Tiempo", "Bloque", "Filminas", "Contenido y recursos"],
    [["0-5'", "Apertura", "1-2", "Presentación; mapa del tema; pregunta disparadora: «¿quién conoce a alguien a quien le robaron la cuenta de WhatsApp?»"],
     ["5-15'", "Conceptos básicos", "3-4", "Defraudación, estafa y abuso de confianza; bien jurídico; texto del art. 172. Ejemplo de los dos autos (Cap. 2)"],
     ["15-35'", "La estafa", "5-11", "Cadena causal; idoneidad del ardid (caso del cuento del tío); mentira y silencio; estafa triangular; consumación; dolo inicial (constructor); estafa procesal"],
     ["35-55'", "Casos especiales del art. 173", "12-18", "Recorrido de los 16 incisos; detenerse en la retención indebida (inmobiliaria), la administración fraudulenta (consorcio), el estelionato y el desbaratamiento (lote vendido dos veces); tarjetas; fraude informático; ciberestafas (caso «Meteoro»)"],
     ["55-65'", "Agravantes, atenuantes y usura", "19-21", "Fraude al Estado; transferencia por error; usura; insolvencia fraudulenta (ejemplo alimentario)"],
     ["65-75'", "Temas transversales", "22-25", "Cheques; art. 185 en familia; prescripción y salidas alternativas; competencia"],
     ["75-85'", "Práctica en Córdoba", "26-28", "Circuito del proceso; checklist de denuncia; método de calificación en 5 preguntas"],
     ["85-90'", "Cierre y preguntas", "29", "Cinco ideas fuerza; preguntas del público"]],
    [2, 4, 2, 9])
TIP("**Recursos para mantener la atención:** iniciar cada bloque con un caso real o hipotético y preguntar al auditorio «¿es estafa?» antes de dar la respuesta; usar el Anexo II como ejercicio de votación a mano alzada; cerrar cada bloque leyendo el recuadro de resumen.")

H1("Anexo II. Casos prácticos con solución")
casos = [
 ("Caso 1. El celular «vendido» por Marketplace",
  "Paula publica su celular en Marketplace. Un «comprador» le dice que ya le transfirió y le manda una captura falsa de la transferencia. Paula, sin verificar su cuenta, le entrega el celular a un cadete.",
  "**Estafa consumada (art. 172).** El ardid es la captura falsa con apariencia de comprobante; Paula, en error, dispuso del celular. La falta de verificación de la víctima podría invocarse por la defensa (deberes de autoprotección), pero la sofisticación de la captura y la práctica habitual en estas operaciones hacen idóneo el engaño."),
 ("Caso 2. El escribano que no escritura",
  "Un escribano recibe USD 80.000 de un comprador para pagar al vendedor en el acto de la escritura. La escritura se frustra y el escribano no devuelve el dinero pese a las intimaciones.",
  "**Retención indebida (art. 173 inc. 2).** El dinero se recibió en depósito con una afectación específica, y había obligación de entregarlo o devolverlo. Las intimaciones prueban el dolo. Puede concurrir responsabilidad disciplinaria y civil."),
 ("Caso 3. El hijo y la tarjeta de la madre",
  "Un hijo de 30 años que vive con su madre usa su tarjeta de crédito sin permiso para comprar equipos electrónicos.",
  "Típicamente es una defraudación con tarjeta (art. 173 inc. 15), pero rige la **excusa absolutoria del art. 185 inc. 1** (descendiente): no hay pena. La madre puede reclamar civilmente. Si un amigo lo ayudó, el amigo sí es punible."),
 ("Caso 4. La transferencia equivocada",
  "Por error de tipeo, una empresa transfiere $3.000.000 a la cuenta de Diego, que los gasta en una semana sabiendo que no le pertenecían.",
  "**Art. 175 inc. 2** (apropiación de cosa habida por error): multa. No es estafa, porque Diego no provocó el error. Además, la empresa tiene acción civil por pago indebido (arts. 1796 y ss. CCyC)."),
 ("Caso 5. El fiduciario y el edificio",
  "La desarrolladora fiduciaria de un fideicomiso al costo vende a terceros tres departamentos ya adjudicados a fiduciantes y desvía el precio a otra obra.",
  "**Defraudación fiduciaria (art. 173 inc. 12)** respecto de cada fiduciante perjudicado; puede concurrir el desbaratamiento (inc. 11). Si los compradores ignoraban la adjudicación previa, puede haber además una estafa o un estelionato en su perjuicio."),
 ("Caso 6. El deudor del juicio de daños",
  "Demandado por un accidente de tránsito, el conductor transfiere su casa a su madre por escritura, sin precio real, dos meses antes de la sentencia que lo condena a pagar $40.000.000.",
  "**Contrato simulado (art. 173 inc. 6)** y, por ocurrir durante el proceso y frustrar el cobro, **insolvencia fraudulenta (art. 179, 2.º párr.)**. La madre puede ser partícipe. En sede civil: acción de simulación o revocatoria, y medidas cautelares."),
 ("Caso 7. El pagaré completado de más",
  "Para un crédito de $500.000, una financiera hace firmar un pagaré en blanco. Ante una mora de una cuota, lo completa por $5.000.000 y lo ejecuta.",
  "**Abuso de firma en blanco (art. 173 inc. 4).** En el ejecutivo: excepciones de inhabilidad de título o de falsedad, según el caso, y la discusión de la relación de consumo subyacente (art. 36 de la Ley 24.240). En sede penal, la denuncia acompañada del contrato de crédito y de los pagos realizados."),
 ("Caso 8. El falso empleado del banco",
  "Un supuesto empleado del banco llama a un jubilado, le dice que hay un «error en su cuenta» y lo guía para que, en el cajero, «genere un código» que en realidad es una transferencia a una cuenta mula.",
  "**Estafa (art. 172)**: la víctima, engañada, realiza ella misma la operación (no hay manipulación del sistema por el autor). La idoneidad se valora en concreto (edad, urgencia, voz «institucional»). El titular de la cuenta mula puede ser partícipe si se prueba su conocimiento.")]
for t, h, s in casos:
    EJ(t, h + "\n**Solución:** " + s)

H1("Anexo III. Preguntas frecuentes del auditorio")
faq = [
 ("¿Si no me pagan una deuda, puedo denunciar por estafa?", "No, en principio. El incumplimiento de una deuda es un problema civil. Solo hay estafa si hubo un **engaño inicial** sin el cual usted no habría prestado o vendido. Denunciar penalmente para presionar el cobro puede exponerlo a una denuncia por falsa denuncia o a una acción por daños."),
 ("¿Si el estafador me devuelve el dinero, se termina la causa?", "No automáticamente: la estafa es de acción pública. La reparación puede habilitar la conciliación o la reparación integral (art. 59 inc. 6 CP; art. 13 bis CPP Córdoba), la suspensión del juicio a prueba o una pena menor, pero la decisión la toma el fiscal o el juez."),
 ("¿Qué hago en las primeras horas después de una estafa virtual?", "Avisar al banco por los canales oficiales, desconocer las operaciones, denunciar en la Fiscalía o en la Policía Judicial pidiendo el bloqueo de la cuenta de destino, y conservar todas las capturas y comprobantes."),
 ("¿El banco tiene que devolverme el dinero?", "Depende del caso. La jurisprudencia comercial analiza si el banco cumplió su deber de seguridad (Ley 24.240) y si el cliente actuó con la diligencia exigible. Hay fallos que condenan al banco por todo y otros que reparten la responsabilidad (por ejemplo, 50 % y 50 %)."),
 ("¿Me pueden imputar si presté mi cuenta?", "Sí. Quien presta su cuenta para recibir y reenviar dinero puede ser imputado como partícipe de la estafa o del fraude informático, o como encubridor. La defensa se centra en demostrar que no conocía el origen ilícito de los fondos."),
 ("¿Mi ex cónyuge vació la cuenta común: es delito?", "Si al momento del hecho estaban casados, aunque separados de hecho, rige la excusa absolutoria del art. 185: no hay pena, pero sí puede reclamar en el proceso de familia (liquidación de la comunidad, recompensas, daños)."),
 ("¿Cuánto tiempo tengo para denunciar una estafa?", "La acción prescribe a los 6 años desde el hecho (art. 62 inc. 2 CP), con las interrupciones del art. 67. Sin embargo, demorar la denuncia hace que se pierda la prueba digital y la posibilidad de bloquear los fondos."),
 ("¿Es lo mismo estafa que defraudación?", "La defraudación es el género; la estafa es la especie que se comete mediante engaño. El art. 173 contiene defraudaciones que no requieren engaño, como la retención indebida o la administración fraudulenta."),
 ("¿Una mentira en un contrato ya es estafa?", "No toda mentira es estafa. Debe ser idónea para engañar, causar un error determinante de la disposición patrimonial y producir un perjuicio económico. Las exageraciones comerciales habituales («el mejor producto del mercado») no suelen alcanzar."),
 ("¿Quién investiga si el estafador está en otra provincia?", "Según la CSJN, pueden ser competentes tanto el juez del lugar del ardid como el del lugar de la disposición patrimonial; se elige por economía procesal. En la práctica suele empezar a investigar el juez del domicilio de la víctima.")]
for q, a in faq:
    H3(q)
    P(a)

H1("Anexo IV. Tabla de control de fuentes")
P("Los siguientes datos se tomaron de fuentes secundarias confiables, pero conviene cotejarlos con la fuente oficial antes de citarlos en un escrito judicial.")
TAB(["Dato", "Dónde verificar", "Observación"],
    [["Texto de los arts. 172 a 180, 185 y 302 CP", "InfoLEG (Ley 11.179, texto actualizado)", "Reconstruido a partir de reproducciones concordantes"],
     ["Montos de las multas de los arts. 175 y 175 bis", "InfoLEG", "Fijados por leyes de actualización; desactualizados"],
     ["Ubicación del párrafo final del art. 174", "InfoLEG", "Alcance de «los tres incisos precedentes» tras la Ley 25.602"],
     ["Leyes que dieron su redacción actual a los incs. 7 y 11 del art. 173", "InfoLEG (notas del artículo)", "Historia legislativa compleja (1968, 1976, Ley 23.077)"],
     ["Art. 2 bis Ley 13.944 (texto y pena)", "InfoLEG", "Incorporado por la Ley 24.029"],
     ["Vigencia del régimen de ejecución extrajudicial de la Ley 24.441", "InfoLEG y CCyC", "Relevante para el art. 173 inc. 13"],
     ["CSJN «Selman» (22/05/2020): doctrina exacta", "csjn.gov.ar (CSJ 690/2017/RH1)", "Se cita a través de su comentario doctrinal"],
     ["CSJN «Pompas» (03/12/2002): cita en Fallos", "csjn.gov.ar / MPF-PROCELAC", "Se cita por número de expediente y fecha"],
     ["TSJ Córdoba: fallos de 2012 (retención indebida), 2013 (desbaratamiento) y «Bonardi»", "Buscador de jurisprudencia del Poder Judicial de Córdoba", "Completar número de sentencia y carátula"],
     ["Numeración de los artículos del CPP de Córdoba sobre el querellante, el actor civil y el juicio abreviado", "Ley 8123, texto ordenado vigente", "El art. 13 bis (Ley 10.457) está verificado"],
     ["Estado del proyecto de nuevo Código Penal", "Congreso de la Nación / Boletín Oficial", "A octubre de 2026, sin ingreso formal"]],
    [6, 5, 5])

H1("Anexo V. Glosario")
glos = [
 ("Abuso de confianza", "Defraudación en la que el autor, que ya tenía legítimamente el bien o su manejo, traiciona el deber de devolverlo o de administrarlo fielmente."),
 ("Ardid", "Despliegue astuto de medios engañosos (puesta en escena) que da verosimilitud a la mentira."),
 ("Cuenta mula", "Cuenta bancaria o virtual usada para recibir y reenviar el dinero obtenido mediante una estafa, a fin de dificultar el rastreo."),
 ("Defraudación", "Género de delitos que lesionan el patrimonio mediante fraude (engaño o abuso de confianza)."),
 ("Desbaratamiento", "Frustración de un derecho sobre un bien acordado previamente a otro por un precio o como garantía (art. 173 inc. 11)."),
 ("Disposición patrimonial", "Acto de la víctima (entregar, pagar, firmar, renunciar) que produce el perjuicio."),
 ("Dolo inicial (in contrahendo)", "Intención defraudatoria presente al momento de contratar; distingue la estafa del incumplimiento civil."),
 ("Error", "Falsa representación de la realidad provocada por el engaño."),
 ("Estafa procesal", "Estafa triangular en la que el engañado es el juez y la disposición patrimonial es su resolución."),
 ("Estafa triangular", "Estafa en la que la persona engañada (y que dispone) es distinta del titular del patrimonio perjudicado."),
 ("Estelionato", "Venta o gravamen de bienes litigiosos, embargados o gravados como libres, o de bienes ajenos como propios (art. 173 inc. 9)."),
 ("Excusa absolutoria", "Causa personal que excluye la pena aunque exista delito (art. 185)."),
 ("Insolvencia fraudulenta", "Ocultamiento o desaparición de bienes durante un proceso o después de la condena para frustrar el cobro (art. 179, 2.º párrafo)."),
 ("Perjuicio", "Disminución efectiva del valor económico del patrimonio de la víctima."),
 ("Phishing", "Captación de claves o datos personales mediante mensajes o sitios que imitan a entidades legítimas."),
 ("SIM swapping", "Obtención fraudulenta de un duplicado del chip telefónico de la víctima para recibir sus códigos de verificación."),
 ("Usura", "Obtener intereses o ventajas evidentemente desproporcionadas aprovechando la necesidad, ligereza o inexperiencia de otro (art. 175 bis).")]
TAB(["Término", "Definición"], [[a, b] for a, b in glos], [4, 12])

H1("Anexo VI. Índice de jurisprudencia citada")
TAB(["Tribunal y carátula", "Fecha", "Tema", "Fuente"],
    [["CSJN, «Bourdieu c/ Municipalidad de la Capital» (Fallos 145:307)", "1925", "Concepto constitucional de propiedad", "Fallos CSJN"],
     ["CSJN, «Pompas, Jaime y otros» (P.744.XXXVI)", "03/12/2002", "Administración fraudulenta: hecho único", "MPF-PROCELAC; Diario Judicial; Pensamiento Penal"],
     ["CSJN, «Acosta» (Fallos 331:858)", "23/04/2008", "Suspensión del juicio a prueba: tesis amplia", "Fallos CSJN"],
     ["CSJN, «Selman» (CSJ 690/2017/RH1)", "22/05/2020", "Idoneidad del engaño y autoprotección", "Pensamiento Penal (doctrina 89746)"],
     ["CSJN, Fallos 311:2607 y 333:2052", "—", "Competencia territorial en la estafa", "Pensamiento Penal (fallo 90994)"],
     ["TSJ Córdoba, Sala Penal (1967)", "1967", "Mera afirmación o silencio en la estafa procesal", "Báez-Outeda, Biblioteca PJ Córdoba"],
     ["TSJ Córdoba, Sala Penal", "04/10/2012", "Retención indebida (intimación) y administración fraudulenta", "Pensamiento Penal (fallo 34732)"],
     ["TSJ Córdoba, Sala Penal", "06/06/2013", "Desbaratamiento de derechos acordados", "El Derecho, t. 282"],
     ["TSJ Córdoba, Sala Penal, «Bonardi»", "—", "Tarjetas: uso físico y uso de datos", "Pensamiento Penal (fallo 34419)"],
     ["Cám. Crim. y Correc. 10.ª Nom. Córdoba, «Novello»", "—", "Desbaratamiento: condena efectiva", "Poder Judicial de Córdoba"],
     ["Cám. Crim. y Correc. 10.ª Nom. Córdoba, «Suárez» (caso «Meteoro»)", "06/02/2026", "Phishing, SIM swapping, cuentas mula", "Poder Judicial de Córdoba; iProUP"],
     ["Cám. Crim. y Correc. 10.ª Nom. Córdoba (autos en Marketplace)", "—", "Estafas reiteradas y asociación ilícita", "Cadena 3"],
     ["Cám. Crim. 10.ª Nom. Córdoba (tarjetas falsas)", "—", "Art. 173 inc. 15: banda de 21 condenados", "Perfil Córdoba"],
     ["CNCrim. y Correc., Sala IV (pasajera de taxi)", "—", "Los cuatro requisitos de la estafa", "Diario Judicial"],
     ["CNCrim. y Correc., Sala IV, causa 1055/11", "2011", "Retención indebida sin intimación fehaciente", "derechopenalonline.com"],
     ["CNCrim. y Correc., Sala V", "1999", "Boleto con gravámenes ocultos: estafa, no estelionato", "vLex"],
     ["CNCrim. y Correc., Sala VII, «G., R. M.»", "02/11/2022", "Cuenta mula: partícipe necesario", "Pensamiento Penal (fallo 90530)"],
     ["CNCrim. y Correc., Sala IV", "—", "Art. 185 entre cónyuges separados de hecho", "abogados.com.ar"],
     ["CNCrim. y Correc.", "1994", "Insolvencia fraudulenta: consumación", "vLex"],
     ["CNCasCC, Sala II, CCC 38624/2021/1/RH1", "23/03/2022", "Competencia en la defraudación informática", "elDial.com"],
     ["CFCP, Sala IV, «Alenda Masutti» y «Mohabed»", "2017 y 2014", "Estafa procesal", "Pensar en Derecho (UBA)"],
     ["TCPBA, Sala IV, «P., J. L.»", "28/07/2020", "Estafa procesal triangular", "Microjuris"],
     ["SCBA", "1992", "Intimación por carta documento", "vLex"],
     ["Cám. Fed. La Plata", "—", "Usura agravada: requisitos", "Pensamiento Penal (fallo 90101)"],
     ["Cám. Nac. Comercial", "2025/2026", "Phishing: responsabilidad concurrente del banco y la clienta", "Microjuris (07/01/2026)"],
     ["TOCF n.º 4 de San Martín", "Octubre de 2026", "Conciliación: titular de cuenta receptora", "Justicia de Primera"],
     ["Tribunal de Goya (Corrientes), causa «Generación Zoe»", "Febrero de 2025", "Esquema piramidal: 98 estafas y asociación ilícita", "Chequeado; Infobae"]],
    [6, 2, 5, 4])

H1("Anexo VII. Bibliografía")
P("**Obras generales y tratados (doctrina argentina)**")
BUL(["Soler, Sebastián, *Derecho Penal Argentino*, t. IV, Buenos Aires, TEA (varias ediciones).",
     "Núñez, Ricardo C., *Tratado de Derecho Penal*, Parte Especial (delitos contra la propiedad), Córdoba, Lerner (varias ediciones).",
     "Fontán Balestra, Carlos, *Tratado de Derecho Penal*, Parte Especial, Buenos Aires, Abeledo-Perrot.",
     "Creus, Carlos y Buompadre, Jorge E., *Derecho Penal. Parte Especial*, t. 1, Buenos Aires, Astrea (7.ª ed.).",
     "Donna, Edgardo A., *Derecho Penal. Parte Especial*, t. II-B, Santa Fe, Rubinzal-Culzoni.",
     "Buompadre, Jorge E., *Estafas y otras defraudaciones*, Buenos Aires, LexisNexis.",
     "Molinario, Alfredo J. y Aguirre Obarrio, Eduardo, *Los delitos*, t. II, Buenos Aires, TEA.",
     "D'Alessio, Andrés J. (dir.), *Código Penal de la Nación. Comentado y anotado*, t. II, Buenos Aires, La Ley.",
     "Baigún, David y Zaffaroni, E. Raúl (dirs.), *Código Penal y normas complementarias. Análisis doctrinal y jurisprudencial*, Buenos Aires, Hammurabi (tomos de la parte especial).",
     "Laje Anaya, Justo, *Comentarios al Código Penal. Parte Especial*, Buenos Aires, Depalma.",
     "Antón Oneca, José, voz «Estafa», en *Nueva Enciclopedia Jurídica Seix*, t. IX, Barcelona (definición clásica citada en el Capítulo 3)."])
P("**Comentarios y artículos consultados en línea**")
BUL(["Rodríguez, Pedro, «Estafa y otras defraudaciones» y «Casos especiales de defraudación», en *Código Penal comentado de acceso libre*, Asociación Pensamiento Penal.",
     "Favarotto, Ricardo S., «Quebrados y otros deudores punibles», en *Código Penal comentado de acceso libre*, Asociación Pensamiento Penal.",
     "Fossaroli, Pablo G., «Los deberes de autoprotección en el delito de estafa. A propósito del fallo “Selman” de la CSJN», Pensamiento Penal.",
     "Báez, Julio C. y Outeda, Diego M., «Estafa procesal. Reseña de jurisprudencia», Biblioteca del Poder Judicial de Córdoba.",
     "«El delito de estafa procesal y sus problemas concursales según la jurisprudencia», *Pensar en Derecho* n.º 13, Facultad de Derecho (UBA).",
     "Terragni, Marco A., «Estafa con tarjetas de crédito», «Desbaratamiento de derechos acordados», «Apostillas sobre la insolvencia alimentaria fraudulenta» y «Excusa absolutoria», terragnijurista.com.ar.",
     "Jantus, Pablo, «Defraudación con tarjetas de compra, crédito o débito (art. 173, inc. 15 del C.P.)», en *Delitos contra la propiedad II*, pp. 679-711 (catálogo de la Biblioteca de la CSJN).",
     "Ziffer, Patricia S. (dir.), *Jurisprudencia de Casación Penal* (administración fraudulenta y fraude a la administración pública).",
     "Revista de la Facultad de Derecho de la Universidad Católica de Córdoba, trabajo sobre el art. 13 bis del CPP de Córdoba y el art. 59 inc. 6 CP."])
P("**Normativa**")
BUL(["Constitución Nacional, arts. 17 y 18.",
     "Código Penal de la Nación (Ley 11.179, t.o. 1984 y modificatorias): arts. 2, 23, 26, 29, 40-49, 54-55, 59, 62-67, 71-72, 76 bis, 162-164, 168, 172-180, 185, 210, 245, 254-255, 258, 275, 277, 292-296, 302-303, 310.",
     "Leyes 18.934, 24.441, 24.452, 25.602, 25.930, 26.388, 27.147 y 13.944 (art. 2 bis, Ley 24.029).",
     "Código Civil y Comercial de la Nación (Ley 26.994): arts. 9, 31 y ss., 332-342, 488 y ss., 509 y ss., 685 y ss., 771, 961, 1061, 1170, 1227 y ss., 1525, 1666 y ss., 1716, 1774-1780, 1796, 1955-1956, 2065, 2229, 2587.",
     "Ley General de Sociedades 19.550 (arts. 59 y 274); Ley de Concursos y Quiebras 24.522 (art. 39); Ley de Defensa del Consumidor 24.240; Ley de Metrología Legal 19.511.",
     "Provincia de Córdoba: Código Procesal Penal (Ley 8123 y modificatorias, en especial la Ley 10.457, art. 13 bis); Ley 10.593 (Fiscalía de Instrucción Especializada en Cibercrimen); Resolución FG 14/2025 (OECED)."])
