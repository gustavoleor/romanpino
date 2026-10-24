# -*- coding: utf-8 -*-
from dsl import *

# =====================================================================
H1("Capítulo 6. Art. 173: incisos 7 y 8")
# ---------------------------------------------------------------- inc 7
H2("6.1. Inciso 7: administración fraudulenta")
LEY("Art. 173 inc. 7", "El que, por disposición de la ley, de la autoridad o por un acto jurídico, tuviera a su cargo el manejo, la administración o el cuidado de bienes o intereses pecuniarios ajenos, y con el fin de procurar para sí o para un tercero un lucro indebido o para causar daño, violando sus deberes perjudicare los intereses confiados u obligare abusivamente al titular de éstos.")
FIG(14, "Administración fraudulenta.")
FICHA([("Bien jurídico", "El patrimonio confiado a la gestión de otro."),
       ("Sujeto activo", "Delito especial: solo quien tiene a su cargo el manejo, la administración o el cuidado de bienes o intereses pecuniarios ajenos."),
       ("Fuente del deber", "La ley (tutor, curador, padres respecto de los bienes del hijo, albacea, síndico), la autoridad (administrador judicial, interventor, depositario judicial) o un acto jurídico (mandato, contrato de sociedad, designación de gerente o director, administrador de consorcio)."),
       ("Conductas", "a) **Infidelidad**: perjudicar los intereses confiados violando sus deberes; b) **Abuso**: obligar abusivamente al titular."),
       ("Tipo subjetivo", "Dolo + elemento subjetivo especial: fin de procurar un lucro indebido (para sí o un tercero) o fin de causar daño."),
       ("Consumación", "Con el perjuicio a los intereses confiados (delito de resultado) o con la obligación abusiva contraída."),
       ("Pena", "Prisión de 1 mes a 6 años. Si el patrimonio es estatal, ver art. 174 inc. 5.")])
H3("a) El sujeto activo")
P("Es la figura central de la **criminalidad empresaria y patrimonial**. Solo puede cometerla quien tiene una relación de gestión sobre un patrimonio ajeno con cierta **autonomía de decisión**. El mero tenedor material de una cosa, que solo debe custodiarla y devolverla, comete retención indebida (inc. 2) y no administración fraudulenta. La diferencia está en el **poder de decisión** sobre el patrimonio.")
TAB(["Fuente", "Ejemplos de administradores"],
    [["Ley", "Padres respecto de los bienes de los hijos menores, tutores, curadores, apoyos con facultades de representación, albaceas, síndicos concursales"],
     ["Autoridad", "Administrador judicial de una sucesión o una sociedad, interventor, depositario judicial con facultades de administración"],
     ["Acto jurídico", "Apoderado con poder de administración o disposición, gerente de SRL, director de SA, administrador de consorcio (art. 2065 CCyC), fiduciario (ver inc. 12), administrador de un country"]],
    [3, 13])
H3("b) Las dos modalidades")
BUL(["**Infidelidad defraudatoria.** El administrador perjudica los intereses confiados violando sus deberes: vende por debajo del valor, compra por encima del valor a una empresa vinculada, cobra «retornos», paga gastos inexistentes, desvía fondos, deja prescribir créditos para favorecer al deudor.",
     "**Abuso.** El administrador usa las facultades de representación para **obligar** al titular de manera abusiva: firma un préstamo a nombre de la sociedad para beneficio propio, otorga garantías a favor de terceros sin causa, reconoce deudas inexistentes."])
P("El perjuicio puede consistir en una disminución del activo (enajenar, abandonar, destruir, inutilizar, emplear irregularmente lo confiado, hacer inversiones deliberadamente equivocadas) o en un aumento indebido del pasivo.")
H3("c) El elemento subjetivo")
P("A diferencia de la estafa, el tipo exige expresamente un **fin**: procurar un lucro indebido o causar daño. Esto excluye la **mala gestión** imprudente o simplemente desafortunada. El administrador que tomó una decisión comercial razonable que salió mal no comete delito. Responde civilmente si actuó con culpa (por ejemplo, arts. 59 y 274 de la Ley General de Sociedades 19.550), pero no penalmente.")
H3("d) Hecho único y prescripción")
JUR("CSJN, «Pompas, Jaime y otros s/ p.ss.aa. de defraudación», P.744.XXXVI, 03/12/2002 (recurso de hecho; tribunal de origen: Tribunal Superior de Justicia de Córdoba)",
    "No corresponde aplicar las reglas del concurso real al delito de administración fraudulenta cuando se trata de un hecho único y global que comprende varias acciones realizadas en el marco de una misma gestión.",
    "Dictamen y fallo disponibles en el sitio de PROCELAC-MPF; reseñado en Diario Judicial («Una administración, un delito»; «El “hecho único” en los delitos continuados») y en Pensamiento Penal, fallo n.º 36781.")
P("La doctrina posterior precisó cuándo se trata de un **hecho único**. Una sala de la Cámara Nacional en lo Criminal y Correccional exigió que concurran un mismo mandato, un único designio y una sola rendición final de cuentas, y sostuvo que los actos de administración fraudulenta cometidos en **gestiones distintas** prescriben en forma independiente (reseña en Diario Judicial).")
JUR("Precedente sobre venta a sí mismo del inmueble del mandante",
    "Se subsume en la administración fraudulenta la conducta del mandatario que vendió a sí mismo un inmueble de propiedad del mandante por un precio inferior al 75 % de su valor de mercado. La administración fraudulenta es una figura básica y autónoma, no una mera agravante.",
    "Pensamiento Penal, fallos sobre el art. 173 inc. 7 (reseñados en el mismo sitio). Verificar tribunal y fecha en la fuente.")
H3("e) Ejemplos")
EJ("El administrador del consorcio",
   "Durante tres años, el administrador de un edificio contrata siempre a la misma empresa de mantenimiento, que pertenece a su cuñado y factura el triple del valor de mercado, y además cobra expensas extraordinarias para obras que nunca se hacen. Hay **administración fraudulenta** (infidelidad), cometida con fin de lucro para un tercero y para sí. Según el criterio de «Pompas», si todo ocurrió en una misma gestión y bajo una misma rendición de cuentas, puede considerarse un **hecho único**.")
EJ("El gerente de la SRL familiar",
   "El gerente de una SRL, en conflicto con sus socios, vende la flota de camiones a una empresa de su pareja por la mitad de su valor y, con el poder de la sociedad, firma un mutuo por USD 200.000 cuyo destino es su cuenta personal. La venta configura la modalidad de **infidelidad** y el mutuo, la de **abuso** (obligar abusivamente al titular).")
EJ("El progenitor que dispone del dinero del hijo",
   "Un padre cobra la indemnización por accidente de tránsito de su hijo menor (depositada judicialmente) y la usa para comprarse un auto. Es administración fraudulenta de quien administra por **disposición de la ley** (arts. 685 y ss. CCyC). Sin embargo, como se trata de un **descendiente**, rige la **excusa absolutoria del art. 185**: no hay pena, pero sí responsabilidad civil. Por eso, en estos casos, la protección pasa por los controles judiciales del Código Civil y Comercial (depósito a plazo fijo, autorización judicial para disponer).")
TIP("Para denunciar una administración fraudulenta, acompañe el **título** que confiere la administración (poder, estatuto, acta de designación, resolución judicial), las **rendiciones de cuentas** (o la prueba de que no se rindieron) y una **pericia contable** que cuantifique el perjuicio. Sin perjuicio cuantificable la causa no avanza.")
RES("**Resumen.** La administración fraudulenta castiga al administrador de bienes ajenos (por ley, autoridad o acto jurídico) que, con fin de lucro indebido o de causar daño, viola sus deberes y perjudica el patrimonio confiado (infidelidad) u obliga abusivamente a su titular (abuso). Es un delito especial y de resultado, que exige un elemento subjetivo específico: la mala gestión culposa no es delito. Según la CSJN («Pompas», 2002), los actos de una misma gestión constituyen un **hecho único**.")

# ---------------------------------------------------------------- inc 8
H2("6.2. Inciso 8: sustitución, ocultación o mutilación de documentos")
LEY("Art. 173 inc. 8", "El que cometiere defraudación, substituyendo, ocultando o mutilando algún proceso, expediente, documento u otro papel importante.")
FICHA([("Sujeto activo", "Cualquier persona (si es funcionario a cargo de la custodia, ver arts. 255 y 294)."),
       ("Objeto", "Proceso, expediente, documento u otro papel importante, es decir, con relevancia patrimonial para la víctima."),
       ("Conductas", "Sustituir (reemplazar por otro), ocultar (impedir que se conozca o se use) o mutilar (destruir parcialmente)."),
       ("Exigencia", "Que la conducta produzca una defraudación: perjuicio patrimonial."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("La diferencia con los delitos contra la fe pública (supresión de documentos, art. 294) y contra la administración pública (violación de sellos y documentos, arts. 254 y 255) está en la **finalidad y el resultado patrimonial**: aquí el documento se ataca **para defraudar** y se causa un perjuicio económico.")
EJ("Ejemplo: el recibo que desaparece del expediente",
   "En un juicio ejecutivo, el deudor había acompañado el recibo original de pago. El ejecutante, al compulsar el expediente en papel, retira la foja con el recibo y prosigue la ejecución hasta cobrar dos veces. Hay **defraudación por ocultación de documento** (art. 173 inc. 8), que puede concurrir con la estafa procesal.")
RES("**Resumen.** El inciso 8 castiga la defraudación cometida sustituyendo, ocultando o mutilando expedientes, documentos o papeles importantes. Se diferencia de los delitos contra la fe pública por su finalidad y su resultado patrimonial.")

# =====================================================================
H1("Capítulo 7. Art. 173: incisos 9 a 14")
FIG(15, "Estelionato frente a desbaratamiento de derechos acordados.")
# ---------------------------------------------------------------- inc 9
H2("7.1. Inciso 9: estelionato")
LEY("Art. 173 inc. 9", "El que vendiere o gravare como bienes libres, los que fueren litigiosos o estuvieren embargados o gravados; y el que vendiere, gravare o arrendare como propios, bienes ajenos.")
FICHA([("Sujeto activo", "Quien vende, grava o arrienda el bien (normalmente, su titular o un falso titular)."),
       ("Sujeto pasivo", "El comprador, el acreedor hipotecario o prendario o el locatario engañado."),
       ("Objeto", "Bienes muebles o inmuebles: litigiosos, embargados o gravados (primera parte) o ajenos (segunda parte)."),
       ("Conductas", "Primera parte: vender o gravar **como libres** bienes que no lo son. Segunda parte: vender, gravar o arrendar **como propios** bienes ajenos."),
       ("Engaño", "Implícito en el «como»: ocultar la situación real del bien."),
       ("Consumación", "Con el perjuicio (pago del precio, otorgamiento del crédito, pago del alquiler)."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("El estelionato es una **estafa con un ardid específico**: ocultar la situación jurídica del bien. Lo que engaña a la víctima es la apariencia de un bien libre o propio. Por eso, si el comprador **conocía** el embargo o la ajenidad y aceptó igual, no hay engaño ni delito.")
BUL(["**Litigioso**: el bien es objeto de un juicio en el que se discute un derecho sobre él.",
     "**Embargado**: pesa una medida cautelar que lo afecta al pago de un crédito.",
     "**Gravado**: tiene un derecho real de garantía (hipoteca, prenda) o una restricción.",
     "**Ajeno**: pertenece a otro, total o parcialmente."])
JUR("CNCrim. y Correc., Sala V (1999)",
    "La suscripción de un boleto de compraventa ocultando al comprador la preexistencia de hipotecas o embargos no configura estelionato, porque la promesa de venta no es una venta. Esa conducta constituye el delito de **estafa** (art. 172).",
    "vLex Argentina, voz «Estelionato art. 173» (sumario editorial).")
OJO("El criterio anterior es importante en la práctica: en las operaciones instrumentadas con **boleto**, la calificación suele ser estafa genérica (art. 172) y no estelionato, aunque la pena es la misma. Algunos autores sostienen, en cambio, que el boleto es una compraventa en los términos del art. 1170 CCyC y que el estelionato se configura igual.")
EJ("Ejemplo moderno: el alquiler temporario falso",
   "Una persona publica en una plataforma de alquileres temporarios un departamento en la costa que no le pertenece, con fotos tomadas de otro anuncio. Cobra la seña y el total por transferencia a varias familias para la misma quincena. Es un supuesto de **arrendar como propio un bien ajeno** (art. 173 inc. 9, segunda parte) o, si ni siquiera tenía acceso al inmueble, de estafa genérica con apariencia de bienes (art. 172). Hay tantos hechos como familias engañadas.")
EJ("Ejemplo clásico: el auto prendado",
   "Martín vende su camioneta por un portal de clasificados, declara que está «libre de deudas» y entrega un informe de dominio viejo. En realidad tiene una prenda vigente con un banco. El comprador paga el precio y, meses después, el banco secuestra la camioneta. Hay **estelionato** (vender como libre un bien gravado).")
RES("**Resumen.** El estelionato castiga a quien vende o grava como libres bienes litigiosos, embargados o gravados, y a quien vende, grava o arrienda como propios bienes ajenos. El engaño consiste en ocultar la verdadera situación del bien. Según un criterio jurisprudencial, el boleto de compraventa no es venta y el caso se califica como estafa del art. 172.")

# ---------------------------------------------------------------- inc 10
H2("7.2. Inciso 10: «venta de humo»")
LEY("Art. 173 inc. 10", "El que defraudare, con pretexto de supuesta remuneración a los jueces u otros empleados públicos.")
FICHA([("Sujeto activo", "Cualquier persona (frecuentemente, gestores, intermediarios o falsos abogados)."),
       ("Sujeto pasivo", "Quien entrega el dinero creyendo que será destinado a un funcionario."),
       ("Conducta", "Obtener dinero u otra ventaja con el pretexto de que se usará para remunerar a un juez o empleado público."),
       ("Elemento clave", "La remuneración es **supuesta**: el autor no piensa entregarla. Si efectivamente la entrega, hay cohecho activo (art. 258) y no defraudación."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("Es la clásica **venta de humo**: el autor vende una influencia inexistente o, aunque la tuviera, no piensa usarla. Se diferencia de la «influencia mentida» del art. 172 porque el pretexto es específicamente una **remuneración** (un soborno) a un funcionario. El inciso muestra que el engaño a una víctima que, a su vez, pretendía algo ilícito (sobornar) es igualmente punible para el estafador.")
P("¿Responde también la víctima? Quien entrega dinero para que se soborne a un juez podría haber incurrido en una tentativa de cohecho activo (art. 258). La cuestión es discutida, pero en la práctica la víctima suele aparecer como denunciante o como testigo, y conviene advertirle de ese riesgo antes de presentar la denuncia.")
EJ("Ejemplo",
   "Un detenido recibe en el penal la visita de un «gestor» que le asegura que, por $2.000.000, el fiscal pedirá su libertad, porque «hay que arreglar» con él. La familia paga. El fiscal nunca supo nada. Hay **defraudación del art. 173 inc. 10**.")
RES("**Resumen.** El inciso 10 castiga la venta de humo: obtener dinero con el pretexto de remunerar (sobornar) a jueces o funcionarios, sin intención de hacerlo. Si el autor realmente entrega el soborno, el delito es cohecho.")

# ---------------------------------------------------------------- inc 11
H2("7.3. Inciso 11: desbaratamiento de derechos acordados")
LEY("Art. 173 inc. 11", "El que tornare imposible, incierto o litigioso el derecho sobre un bien o el cumplimiento, en las condiciones pactadas, de una obligación referente al mismo, sea mediante cualquier acto jurídico relativo al mismo bien, aunque no importe enajenación, o removiéndolo, reteniéndolo, ocultándolo o dañándolo, siempre que el derecho o la obligación hubieran sido acordados a otro por un precio o como garantía.")
FICHA([("Bien jurídico", "El patrimonio del titular de un derecho acordado sobre un bien."),
       ("Sujeto activo", "Quien acordó el derecho o asumió la obligación (vendedor por boleto, deudor prendario o hipotecario, cedente)."),
       ("Sujeto pasivo", "Quien adquirió el derecho por un precio o como garantía."),
       ("Presupuesto", "Un derecho sobre un bien o una obligación referente a él, acordado a otro **por un precio o como garantía**."),
       ("Medios", "Cualquier acto jurídico relativo al bien (aunque no sea enajenación: hipotecarlo, alquilarlo, darlo en leasing) o actos materiales (removerlo, retenerlo, ocultarlo, dañarlo)."),
       ("Resultado", "Tornar **imposible, incierto o litigioso** el derecho o el cumplimiento de la obligación."),
       ("Consumación", "Con el acto ulterior, jurídico o material, que frustra el derecho o el cumplimiento."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("Es la figura que el abogado civilista encuentra con más frecuencia en los conflictos inmobiliarios. A diferencia del estelionato, **no requiere engaño a la víctima** en el momento de la contratación. Lo punible es el acto **posterior** con el que el autor desbarata el derecho que él mismo había acordado.")
P("El caso de manual es la **doble venta**: el vendedor firma un boleto, cobra todo o parte del precio y entrega o no la posesión, y luego vende o hipoteca el mismo inmueble a un tercero, que inscribe primero. El primer comprador ve su derecho tornado incierto o litigioso. Otros supuestos son el deudor prendario que oculta o vende el auto prendado y el vendedor que, después de firmar el boleto, constituye un usufructo o alquila el inmueble por largo plazo a un tercero.")
JUR("Tribunal Superior de Justicia de Córdoba, Sala Penal, 06/06/2013",
    "Precedente sobre desbaratamiento de derechos acordados (art. 173 inc. 11 CP) en un caso de compraventa inmobiliaria, remate del inmueble y ejecución hipotecaria.",
    "Citado en doctrina sobre compraventa inmobiliaria y ejecución hipotecaria (nota publicada en *El Derecho*, t. 282, 2018). Consultar el texto completo en el buscador de jurisprudencia del Poder Judicial de Córdoba.")
JUR("Cámara en lo Criminal y Correccional de 10.ª Nominación de Córdoba, «Novello, Claudio Ricardo», SAC 9169518",
    "Condenó a un contador público a tres años de prisión de cumplimiento efectivo por el delito de desbaratamiento de derechos acordados, en relación con un inmueble adquirido «en pozo». Sostuvo que el tipo no exige que el precio esté pagado y que el perjuicio no se limita a la disminución del activo (pago del precio), sino que puede consistir en el aumento del pasivo.",
    "Poder Judicial de Córdoba, sección Novedades («Condena efectiva a un contador público por el delito…») y documento adjunto del expediente.")
P("En cuanto a la **consumación**, la jurisprudencia sostiene que el delito se consuma con el acto o hecho ulterior, jurídico o material, del autor que frustra el derecho o el cumplimiento de la obligación. Un antiguo criterio, recogido en la *Revista del Notariado*, sostuvo que las obligaciones de hacer no son susceptibles de desbaratamiento. Es una posición discutible, que conviene verificar antes de invocarla.")
EJ("Ejemplo: el lote vendido dos veces",
   "Lucía compra por boleto un lote en un loteo de Córdoba, paga el precio en 36 cuotas y recibe la posesión. Antes de escriturar, el loteador vende el mismo lote por escritura a un tercero de buena fe, que lo inscribe. El derecho de Lucía se tornó **litigioso**: deberá discutir la oponibilidad de su boleto (art. 1170 CCyC). Hay **desbaratamiento de derechos acordados** (art. 173 inc. 11). Si el loteador ocultó al segundo comprador la venta anterior, hay además una estafa o un estelionato en perjuicio de este.")
TIP("Para denunciar: acompañar el **boleto** (con fecha cierta, si es posible), la prueba del pago del **precio** y de la entrega de la posesión, y el **informe de dominio** que muestra el acto posterior (venta, hipoteca, embargo). En paralelo, en sede civil, puede trabarse una **anotación de litis** o una prohibición de innovar para evitar nuevos desplazamientos del bien.")
RES("**Resumen.** El inciso 11 castiga a quien, después de haber acordado a otro un derecho sobre un bien por un precio o como garantía, lo torna imposible, incierto o litigioso mediante actos jurídicos (vender, hipotecar, alquilar) o materiales (ocultar, retener, dañar). No exige engaño inicial. Es la figura de la doble venta inmobiliaria y del deudor prendario que hace desaparecer el bien.")

# ---------------------------------------------------------------- inc 12
H2("7.4. Inciso 12: fiduciario, administrador de fondos comunes y dador de leasing")
LEY("Art. 173 inc. 12", "El titular fiduciario, el administrador de fondos comunes de inversión o el dador de un contrato de leasing, que en beneficio propio o de un tercero dispusiere, gravare o perjudicare los bienes y de esta manera defraudare los derechos de los cocontratantes.")
FICHA([("Origen", "Art. 82 de la Ley 24.441 (1995)."),
       ("Sujeto activo", "Delito especial: el fiduciario (arts. 1666 y ss. CCyC), el administrador (sociedad gerente) de un fondo común de inversión o el dador de un leasing (arts. 1227 y ss. CCyC)."),
       ("Sujeto pasivo", "Los cocontratantes: fiduciante, beneficiario, fideicomisario, cuotapartistas, tomador del leasing."),
       ("Conducta", "Disponer, gravar o perjudicar los bienes en beneficio propio o de un tercero."),
       ("Resultado", "Defraudar los derechos de los cocontratantes (perjuicio)."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("En estos contratos el sujeto activo es **dueño** (fiduciario) o titular formal de los bienes, aunque se trata de una propiedad fiduciaria o afectada a un fin. Por eso no encajaba con claridad en la administración fraudulenta ni en la retención indebida, y el legislador creó una figura específica, conocida como **defraudación fiduciaria**.")
EJ("Ejemplo cordobés: el fideicomiso inmobiliario al costo",
   "En un fideicomiso para construir un edificio, decenas de fiduciantes-beneficiarios aportan cuotas a cambio de la adjudicación futura de un departamento. El fiduciario (la desarrolladora) vende a terceros, por fuera del fideicomiso, unidades ya asignadas a los fiduciantes y además hipoteca el terreno para financiar otra obra propia. Hay **defraudación fiduciaria** (art. 173 inc. 12). Según el caso, puede concurrir con el desbaratamiento (inc. 11) respecto de cada unidad comprometida.")
RES("**Resumen.** El inciso 12 castiga al fiduciario, al administrador de fondos comunes de inversión y al dador de leasing que, en beneficio propio o de un tercero, disponen, gravan o perjudican los bienes y defraudan a sus cocontratantes. Es la figura de los fideicomisos inmobiliarios mal administrados.")

# ---------------------------------------------------------------- inc 13 y 14
H2("7.5. Incisos 13 y 14: ejecución extrajudicial abusiva y letras hipotecarias")
LEY("Art. 173 inc. 13", "El que encontrándose autorizado para ejecutar extrajudicialmente un inmueble lo ejecutara en perjuicio del deudor, a sabiendas de que el mismo no se encuentra en mora, o maliciosamente omitiera cumplimentar los recaudos establecidos para la subasta mediante dicho procedimiento especial.")
LEY("Art. 173 inc. 14", "El tenedor de letras hipotecarias que, en perjuicio del deudor o de terceros, omitiera consignar en el título los pagos recibidos.")
P("Ambos incisos fueron incorporados por la **Ley 24.441** como contrapeso penal de los instrumentos que esa ley creó para agilizar el crédito hipotecario: el régimen especial de **ejecución extrajudicial** de hipotecas y las **letras hipotecarias**.")
BUL(["**Inciso 13.** Castiga dos conductas del acreedor autorizado a ejecutar extrajudicialmente: ejecutar **sabiendo que el deudor no está en mora** o **omitir maliciosamente** los recaudos de la subasta (publicidad, tasación, constatación), en perjuicio del deudor.",
     "**Inciso 14.** Castiga al tenedor de una letra hipotecaria que no anota en el título los pagos que recibió, de modo que el deudor (o un tercero adquirente de la letra) puede verse obligado a pagar dos veces."])
OJO("Son figuras de **escasa aplicación práctica**. Conviene verificar en cada caso la vigencia y el alcance actual del régimen especial de ejecución hipotecaria y de las letras hipotecarias de la Ley 24.441, ya que el Código Civil y Comercial (Ley 26.994) derogó otros capítulos de esa ley (fideicomiso y leasing, hoy regulados en el propio Código).")
RES("**Resumen.** Los incisos 13 y 14 protegen al deudor hipotecario frente a los abusos del régimen de la Ley 24.441: la ejecución extrajudicial sin mora o sin los recaudos de la subasta, y la omisión de anotar pagos en las letras hipotecarias. Su uso en tribunales es poco frecuente.")

# =====================================================================
H1("Capítulo 8. Art. 173: incisos 15 y 16 y las ciberestafas")
# ---------------------------------------------------------------- inc 15
H2("8.1. Inciso 15: defraudación con tarjetas de compra, crédito o débito")
LEY("Art. 173 inc. 15", "El que defraudare mediante el uso de una tarjeta de compra, crédito o débito, cuando la misma hubiere sido falsificada, adulterada, hurtada, robada, perdida u obtenida del legítimo emisor mediante ardid o engaño, o mediante el uso no autorizado de sus datos, aunque lo hiciere por medio de una operación automática.")
FIG(16, "Defraudación con tarjetas.")
FICHA([("Origen", "Ley 25.930 (B.O. 21/09/2004)."),
       ("Sujeto activo", "Cualquier persona que usa la tarjeta o sus datos."),
       ("Sujeto pasivo", "El titular de la tarjeta, el emisor o el comercio, según quién soporte el perjuicio."),
       ("Objeto", "Tarjeta de compra, crédito o débito, o sus datos."),
       ("Supuestos", "Tarjeta falsificada o adulterada; hurtada, robada o perdida; obtenida del emisor mediante ardid; uso no autorizado de los datos."),
       ("Medio", "Uso ante una persona o mediante una «operación automática» (cajero, posnet, compra en línea)."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("El inciso resolvió un problema serio. Antes de 2004, el uso de una tarjeta robada en un cajero automático no podía calificarse como estafa, porque **la máquina no se equivoca** (no hay error en una persona), y tampoco como hurto con facilidad, porque el dinero sale por una operación autorizada por el sistema. La fórmula «aunque lo hiciere por medio de una operación automática» cerró esa laguna.")
P("**Relación con el apoderamiento de la tarjeta.** Si el autor primero roba la cartera con la tarjeta y luego la usa, hay dos hechos: el **robo** (art. 164) y la **defraudación con tarjeta** (art. 173 inc. 15), en concurso real. La mera tenencia de una tarjeta de origen ilegítimo no configura el inciso 15, que exige el **uso** defraudatorio.")
JUR("Tribunal Superior de Justicia de Córdoba, Sala Penal, «Bonardi, Oscar Enrique», Sentencia n.º 111, 18/05/2012 (expte. «B», 68/11)",
    "El art. 173 inc. 15 prevé dos grandes supuestos: el uso de una **tarjeta física** (falsificada, adulterada, hurtada, robada, perdida u obtenida mediante ardid del emisor) y el **uso no autorizado de los datos** de la tarjeta, en el que no se requiere el empleo del plástico sino solo de sus datos. En el caso, las extracciones se hicieron en distintos cajeros automáticos con tarjetas apócrifas y claves.",
    "Pensamiento Penal, fallo n.º 34419. La Cámara Novena del Crimen había condenado al imputado como coautor de defraudación por uso no autorizado de datos de tarjetas de débito (38 hechos), descartando el primer supuesto porque no se hallaron las tarjetas empleadas. Leer la parte dispositiva en el texto completo antes de citar el resultado del recurso.")
JUR("Cámara en lo Criminal de 10.ª Nominación de Córdoba (banda de tarjetas falsas)",
    "Condenó a 21 integrantes de una organización que defraudó a una emisora de tarjetas regional con plásticos confeccionados con datos falsos o de personas que no los habían autorizado, que distribuían, y que montaba sociedades fantasma para generar comprobantes y pagos.",
    "Perfil Córdoba, «Condenaron a la banda que defraudó con plásticos truchos de Naranja X».")
EJ("Ejemplos",
   "**a)** Le roban la billetera a Sofía en el colectivo y, una hora después, con su tarjeta de débito se compran celulares en un comercio con posnet: **robo o hurto + art. 173 inc. 15** (tarjeta robada o hurtada, uso ante persona y operación automática).\n**b)** Un empleado de un hotel copia los datos de las tarjetas de los huéspedes y compra pasajes por internet: **art. 173 inc. 15** (uso no autorizado de los datos).\n**c)** Alguien obtiene una tarjeta de crédito del banco presentando un DNI adulterado y la usa: **art. 173 inc. 15** (tarjeta obtenida del emisor mediante ardid) en concurso con el uso de documento falso.")
RES("**Resumen.** El inciso 15 castiga la defraudación mediante el uso de tarjetas falsificadas, adulteradas, robadas, hurtadas, perdidas u obtenidas con ardid del emisor, y el uso no autorizado de sus datos, aun por operación automática. Cierra la laguna del cajero automático. El apoderamiento previo de la tarjeta concurre en forma real.")

# ---------------------------------------------------------------- inc 16
H2("8.2. Inciso 16: defraudación mediante manipulación informática")
LEY("Art. 173 inc. 16", "El que defraudare a otro mediante cualquier técnica de manipulación informática que altere el normal funcionamiento de un sistema informático o la transmisión de datos.")
FIG(17, "Fraude informático frente a estafa por medios digitales.")
FICHA([("Origen", "Art. 9 de la Ley 26.388 de delitos informáticos (sancionada el 04/06/2008, promulgada de hecho el 24/06/2008)."),
       ("Sujeto activo", "Cualquier persona."),
       ("Sujeto pasivo", "El titular del patrimonio perjudicado (cliente, banco, comercio)."),
       ("Conducta", "Defraudar mediante una técnica de manipulación informática."),
       ("Resultado intermedio", "Alterar el normal funcionamiento de un sistema informático o la transmisión de datos."),
       ("Resultado final", "Perjuicio patrimonial."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("El inciso 16 es la versión argentina del **fraude informático** de la legislación comparada. Su estructura es paralela a la estafa, pero **sustituye el engaño a una persona por la manipulación de un sistema**: el autor no hace que alguien se equivoque, sino que hace que un sistema produzca un resultado (una transferencia, un crédito, una baja de deuda) que no debería haber producido.")
H3("a) ¿Qué es «manipulación informática»?")
P("Abarca la introducción de datos falsos, la alteración de programas, la interferencia en la transmisión de datos y, según la posición mayoritaria en la práctica judicial, el **uso no autorizado de credenciales ajenas** (usuario, clave, token) para operar un home banking o una billetera virtual. Este último punto es discutido: hay quien sostiene que, si el autor usa claves verdaderas, el sistema funciona «normalmente» y no hay manipulación. La doctrina también advierte que la **suplantación de identidad** no está prevista como medio específico, lo que dificulta encuadrar algunas modalidades de phishing.")
H3("b) Línea divisoria con el art. 172")
P("La pregunta decisiva es **quién realiza la disposición patrimonial**:")
BUL(["Si la **víctima**, engañada por un mensaje, un llamado o un perfil falso, **transfiere ella misma** el dinero, hay una persona en error que dispone: es **estafa (art. 172)**, aunque todo haya ocurrido por medios electrónicos.",
     "Si la víctima **entrega sus claves** (o el autor las obtiene de otro modo) y es el **autor quien opera** el sistema y transfiere el dinero, no hay persona que disponga en error: es **fraude informático (art. 173 inc. 16)**."])
JUR("Cámara de Apelaciones en lo Penal, Contravencional y de Faltas de la Ciudad de Buenos Aires (conflicto de competencia)",
    "Al discutir la competencia, la Cámara sostuvo que la conducta descripta en el art. 173 inc. 16 ya se encontraba prevista como delito en el art. 172. Por eso, que el inciso 16 sea posterior a la Ley 24.588 no bastaba para atribuir la competencia a la justicia local.",
    "Biblioteca del Colegio de Abogados de Mar del Plata (documento del fallo). Leer el análisis completo en la fuente.")
JUR("Cámara en lo Criminal y Correccional de 10.ª Nominación de Córdoba, «Suárez, Víctor Ignacio» (caso «Meteoro»), SAC 12074663, fundamentos del 06/02/2026",
    "Condenó a seis años de prisión al líder de una estructura que vaciaba cuentas bancarias y billeteras virtuales mediante **phishing, SIM swapping, apoderamiento de cuentas de WhatsApp** (para pedir dinero a los contactos de las víctimas) y el uso de **cuentas mula** para mover los fondos.",
    "Poder Judicial de Córdoba (documento del expediente); iProUP, «Condenaron a “Meteoro”, el estafador experto en fugas que vaciaba billeteras virtuales».")
RES("**Resumen.** El inciso 16 castiga la defraudación mediante cualquier técnica de manipulación informática que altere el funcionamiento de un sistema o la transmisión de datos. Reemplaza el engaño a una persona por la manipulación de un sistema. Si la víctima transfiere engañada, es art. 172; si el autor opera el sistema con datos o claves obtenidos ilegítimamente, es art. 173 inc. 16.")

# ---------------------------------------------------------------- ciberestafas
H2("8.3. Las ciberestafas en la práctica")
FIG(18, "Modalidades de ciberestafa y su calificación probable.")
P("La mayoría de las estafas que hoy llegan a los estudios jurídicos son digitales. La tabla resume las modalidades más frecuentes y su calificación probable. En todos los casos, la calificación final depende de **quién hizo la transferencia** y de **cómo se obtuvo el acceso**.")
TAB(["Modalidad", "Cómo funciona", "Calificación probable"],
    [["Phishing (correo o SMS falso)", "Sitio clonado del banco o de un organismo que captura usuario y clave", "Art. 173 inc. 16 (si opera el autor); acceso ilegítimo (art. 153 bis)"],
     ["Vishing (llamada)", "Falso empleado bancario que guía a la víctima en el cajero o el home banking", "Art. 172 (si transfiere la víctima) o art. 173 inc. 16"],
     ["SIM swapping", "El autor obtiene un duplicado del chip de la víctima y recibe sus códigos de verificación", "Art. 173 inc. 16, más falsedades documentales si usó un DNI falso"],
     ["Robo de cuenta de WhatsApp", "Con el código de verificación toma la cuenta y pide dinero a los contactos", "Art. 172 respecto de cada contacto que transfiere"],
     ["Marketplace o alquiler falso", "Venta o alquiler de bienes inexistentes contra seña", "Art. 172 o art. 173 inc. 9"],
     ["Préstamos falsos", "Ofrecen un crédito y cobran «gastos de otorgamiento»", "Art. 172"],
     ["Inversiones o esquemas Ponzi", "Promesas de rentas altas pagadas con aportes de nuevos inversores", "Art. 172 reiterado; asociación ilícita (art. 210); intermediación financiera no autorizada (art. 310)"],
     ["Cuenta mula", "Persona que presta su cuenta para recibir y reenviar el dinero", "Partícipe (art. 45/46) o encubrimiento (art. 277), según su conocimiento"]],
    [4, 7, 6])
JUR("Cámara en lo Criminal y Correccional de 10.ª Nominación de Córdoba (sala unipersonal), estafas en la venta de automóviles por Marketplace",
    "Condenó a once personas que integraban una asociación ilícita dedicada a cometer estafas en la comercialización de automóviles, con víctimas captadas en su mayoría a través de Marketplace. Las conductas se encuadraron en estafa (39 hechos) y asociación ilícita.",
    "Cadena 3, «Condenan a banda que cometía estafas en la comercialización de autos en Córdoba»; Comercio y Justicia.")
H3("Prueba y medidas urgentes en una ciberestafa")
NUM(["**Denunciar de inmediato** y pedir el **bloqueo** de la cuenta o CVU de destino. Las primeras horas son decisivas: el dinero suele salir en minutos hacia otras cuentas o hacia criptoactivos.",
     "**Notificar al propio banco** por los canales oficiales y pedir constancia (número de reclamo), el desconocimiento de las operaciones y la reversión cuando corresponda.",
     "**Preservar la evidencia**: capturas de pantalla completas (con fecha, hora y número o usuario), exportación del chat, enlaces (URL), correos con encabezados, comprobantes de transferencia con CBU/CVU y alias de destino.",
     "**Pedir medidas de investigación**: informes a la entidad de destino sobre el titular de la cuenta, su legajo y las IP de alta y de operación; informes a las empresas de telefonía (titularidad de la línea, duplicados de SIM) y a las plataformas (Meta, Mercado Libre) mediante los canales previstos para autoridades.",
     "**En Córdoba**, la investigación suele quedar a cargo de la **Fiscalía de Instrucción Especializada en Cibercrimen** (Ley 10.593) con el apoyo técnico de la **Oficina Especializada en Ciberdelitos y Evidencia Digital** (OECED, Resolución FG 14/2025)."])
H3("La responsabilidad civil del banco")
P("En paralelo con la causa penal, la víctima puede reclamar al banco o a la billetera virtual con fundamento en el deber de seguridad y en la Ley de Defensa del Consumidor (Ley 24.240). La jurisprudencia comercial es abundante y tiende a distribuir la responsabilidad según la conducta de cada parte.")
JUR("Cámara Nacional de Apelaciones en lo Comercial (phishing bancario; préstamo no solicitado)",
    "Declaró nulo un préstamo no solicitado, obtenido por un tercero tras un phishing, y atribuyó la responsabilidad de forma **concurrente, 50 % y 50 %**, entre el banco y la clienta, manteniendo la indemnización por daño moral.",
    "Microjuris Al Día Argentina, 07/01/2026.")
OJO("La acción civil contra el banco es **independiente** de la penal (arts. 1774 y ss. CCyC). No es necesario esperar la sentencia penal para demandar, aunque el juez civil puede suspender el dictado de la sentencia en los casos del art. 1775 CCyC.")
RES("**Resumen.** Las ciberestafas se califican según quién dispone: si la víctima transfiere engañada, art. 172; si el autor opera el sistema, art. 173 inc. 16; si se usa una tarjeta o sus datos, inc. 15. Las estafas masivas suman asociación ilícita. La cuenta mula puede ser partícipe o encubridora según su conocimiento. Lo decisivo en la práctica es la **rapidez** (bloqueo de fondos), la **preservación de la evidencia digital** y, en paralelo, el reclamo civil contra la entidad financiera.")
