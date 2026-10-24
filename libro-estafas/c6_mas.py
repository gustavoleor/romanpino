# -*- coding: utf-8 -*-
from dsl import *

# =====================================================================
H1("Capítulo 13. Las estafas más frecuentes y su encuadre")
P("Este capítulo reúne las modalidades que con mayor frecuencia llegan a los estudios jurídicos y a las fiscalías. Para cada una se indica la mecánica, la calificación probable y la prueba clave. Es material directamente utilizable para la conferencia, porque el público reconoce estos casos de inmediato.")
OJO("La calificación propuesta es **orientativa**. En cada caso concreto debe analizarse quién realizó la disposición patrimonial, si hubo engaño previo o abuso de confianza posterior y si el dolo existía al momento de contratar.")

H2("13.1. Estafas inmobiliarias")
TAB(["Modalidad", "Mecánica", "Calificación probable", "Prueba clave"],
    [["Falso dueño", "Alguien se hace pasar por propietario (DNI falso, poder falso o escritura apócrifa) y cobra la seña o el precio", "Art. 172 (nombre supuesto, falsos títulos) en concurso con falsificación o uso de documento falso (arts. 292 y 296)", "Informe de dominio; pericia documental; testimonio del escribano; cámaras del lugar de pago"],
     ["Doble venta", "El vendedor por boleto vende o hipoteca el inmueble a un tercero", "Art. 173 inc. 11 (desbaratamiento) respecto del primer comprador; estafa o estelionato respecto del segundo si se le ocultó la venta previa", "Boleto con fecha cierta; recibos; informe de dominio posterior"],
     ["Venta en pozo y fideicomisos", "Se venden unidades de una obra que nunca avanza, o el fiduciario dispone de unidades ya comprometidas", "Art. 172 (si no hubo intención de construir) o art. 173 incs. 11 y 12", "Contrato de fideicomiso; estado de la obra (constatación); pericia contable sobre el destino de los fondos"],
     ["Alquiler temporario falso", "Publicación de un inmueble ajeno o inexistente; cobro de reservas a varios interesados", "Art. 173 inc. 9 (arrendar como propio bien ajeno) o art. 172; un hecho por cada víctima", "Capturas de la publicación; comprobantes; informes a la plataforma y al banco de destino"],
     ["Inmobiliaria que no devuelve la reserva", "Recibe la reserva con afectación específica y no la restituye cuando la operación se cae", "Art. 173 inc. 2 (retención indebida)", "Recibo de reserva con sus condiciones; intimación fehaciente"]],
    [3, 5, 5, 4])

H2("13.2. Automotores")
TAB(["Modalidad", "Mecánica", "Calificación probable", "Prueba clave"],
    [["Auto con prenda o embargo oculto", "Se vende como libre un vehículo gravado", "Art. 173 inc. 9 (estelionato)", "Informe de dominio histórico; publicación de venta con la frase «libre de deudas»"],
     ["«Mellizos» o «gemelos»", "Auto robado con la documentación de otro vehículo idéntico", "Estafa al comprador (art. 172) en concurso con encubrimiento (art. 277) y falsificaciones (arts. 289, 292 y 296)", "Peritaje de grabados; informes del registro automotor; seguimiento de la cadena de ventas"],
     ["Pago con transferencia falsa", "El «comprador» exhibe un comprobante falso y retira el vehículo", "Art. 172", "Constancia bancaria de inexistencia de la transferencia; cámaras; testigos"],
     ["Planes de ahorro con «adjudicación asegurada»", "Un vendedor promete la entrega inmediata del auto si se pagan cuotas adelantadas o un «derecho de adjudicación»", "Art. 172 si la promesa era falsa desde el inicio; en otro caso, conflicto de consumo (Ley 24.240)", "Promesas escritas o grabadas; condiciones generales del plan; denuncias de otras víctimas"]],
    [3, 5, 5, 4])

H2("13.3. Estafas financieras y de inversión")
TAB(["Modalidad", "Mecánica", "Calificación probable", "Prueba clave"],
    [["Esquema Ponzi o piramidal", "Rentas altas «garantizadas», pagadas con el dinero de nuevos inversores", "Art. 172 reiterado; asociación ilícita (art. 210); intermediación financiera no autorizada (art. 310); lavado (art. 303)", "Contratos; comprobantes; pericia contable; informes de la CNV y del BCRA sobre falta de autorización"],
     ["Falsas inversiones en criptoactivos o divisas", "Plataformas de trading falsas que muestran ganancias ficticias e impiden el retiro", "Art. 172 (o art. 173 inc. 16 si se manipula el sistema de la víctima)", "Capturas de la plataforma; transferencias a exchanges; trazabilidad de la cadena de bloques"],
     ["Préstamos falsos", "Se ofrece un crédito y se cobran por adelantado «gastos de otorgamiento» o «seguros»", "Art. 172", "Publicidad; chats; comprobantes de pago"],
     ["Usura", "Préstamos con intereses desproporcionados a personas en situación de necesidad", "Art. 175 bis (agravado si es profesional o habitual)", "Planillas de cobro; tarjetas retenidas; testimonio de varias víctimas"]],
    [3, 5, 5, 4])
JUR("Causa «Generación Zoe» (esquema piramidal)",
    "Un tribunal de Goya (Corrientes) condenó en febrero de 2025 a Leonardo Cositorto como jefe de una asociación ilícita y coautor de 98 estafas con un esquema piramidal, a 12 años de prisión. En la investigación tramitada en Villa María (Córdoba), con 295 víctimas, la Cámara de Río Tercero confirmó en mayo de 2025 la elevación a juicio. En junio de 2026 el expediente estaba ante la Corte Suprema para resolver qué tribunal debe juzgarlo (justicia provincial o federal).",
    "Chequeado, «Generación Zoe: las claves de la causa…»; Infobae y CNN (21/02/2025); El Diario del Centro del País (23/06/2026); Radio Villa María.")

H2("13.4. Estafas a personas mayores y vulnerables")
BUL(["**Cuento del tío telefónico.** Variantes: el nieto accidentado, el falso policía o abogado que pide dinero para evitar una detención, el falso empleado de ANSES o del banco que anuncia un «cambio de billetes» o una «actualización de datos». Calificación: **art. 172**. Prueba clave: registros de llamadas, testimonio del «cadete», cámaras de la cuadra, seguimiento del dinero.",
     "**Estafa sentimental (romance scam).** Relación virtual con un perfil falso que, tras semanas de contacto, pide dinero para un viaje, una emergencia o un trámite aduanero. Calificación: **art. 172**, con un hecho por cada entrega si no hay unidad de designio. Prueba clave: chats completos, transferencias y análisis de las imágenes del perfil.",
     "**Abuso de personas con restricciones a la capacidad** para hacerles firmar poderes, cesiones o préstamos. Calificación: **art. 174 inc. 2** si hay abuso de su necesidad o inexperiencia; **art. 173 inc. 3** si hay engaño sobre lo que se firma."])
TIP("En las causas con víctimas mayores, pida que la **declaración** de la víctima se registre en video lo antes posible (para preservar su testimonio) y destaque su **situación concreta** de vulnerabilidad para fundar la idoneidad del engaño y, en la etapa de pena, la mayor gravedad del hecho (arts. 40 y 41 CP).")

H2("13.5. Estafas laborales y profesionales")
BUL(["**Falsas ofertas de empleo.** Se exige el pago de un «curso», un «uniforme» o un «apto médico» para un trabajo inexistente. Calificación: **art. 172**.",
     "**Falso abogado o gestor.** Cobra honorarios o «gastos» por un trámite que nunca inicia, o por «arreglar» con un funcionario. Calificación: **art. 172** (calidad simulada, ejercicio ilegal de la profesión) o **art. 173 inc. 10** (venta de humo). Si usa la matrícula de otro, concurre la usurpación de títulos (art. 247).",
     "**Abogado que retiene fondos del cliente.** Cobra la indemnización y no la rinde. Calificación: **art. 173 inc. 2** o **inc. 7**. Si además perjudicó deliberadamente la causa, concurre el **patrocinio infiel** (art. 271).",
     "**Prestaciones médicas facturadas y no realizadas** a obras sociales. Calificación: **art. 172** o, si el ente es estatal, **art. 174 inc. 5**."])

H2("13.6. Estafas comerciales")
BUL(["**Proveedor que cobra y no entrega.** Es estafa solo si se prueba que nunca tuvo intención ni posibilidad de entregar (empresa inexistente, múltiples víctimas, desaparición). Si era un comerciante real que entró en crisis, es incumplimiento civil.",
     "**Compras con cheques sin fondos entregados en el acto**: art. 172 (ver Capítulo 11).",
     "**Entrega de mercadería de menor calidad o cantidad**: art. 173 inc. 1; con pesas o medidas falsas, art. 174 inc. 3.",
     "**Facturación de servicios inexistentes por un administrador**: art. 173 inc. 7."])
RES("**Resumen del capítulo.** Las modalidades se repiten: el falso dueño, la doble venta y el alquiler falso en lo inmobiliario; la prenda oculta y los «mellizos» en los automotores; el esquema Ponzi y los préstamos falsos en lo financiero; el cuento del tío y la estafa sentimental con las víctimas vulnerables. En todas, la calificación depende del momento del dolo, de quién dispuso y de la existencia o no de un engaño previo.")

# =====================================================================
H1("Capítulo 14. Concursos y figuras afines")
H2("14.1. Unidad y pluralidad de hechos")
P("En las defraudaciones es frecuente que el autor obtenga varias entregas de una misma víctima o que engañe a varias víctimas. Las reglas generales son:")
BUL(["**Varias entregas de una misma víctima por un mismo engaño** (por ejemplo, cuotas de una falsa inversión): según la doctrina mayoritaria, configuran un **delito continuado**, es decir, un solo hecho, cuando hay unidad de designio, homogeneidad en la conducta y un mismo titular del bien jurídico.",
     "**Varias víctimas**: cada una configura, en principio, un **hecho independiente** (concurso real, art. 55). La pena se forma sumando las escalas, con el límite del art. 55.",
     "**Administración fraudulenta**: los actos de una misma gestión forman un **hecho único** (CSJN, «Pompas»).",
     "**Un mismo hecho que encuadra en dos figuras** (por ejemplo, el uso del documento falso como ardid): **concurso ideal** (art. 54), con la pena mayor."])
H2("14.2. Relaciones con otros delitos")
TAB(["Figura vecina", "Relación con la estafa", "Solución habitual"],
    [["Hurto (art. 162)", "En el hurto el autor toma la cosa; en la estafa la víctima la entrega engañada", "Excluyentes: se califica según cómo salió el bien del patrimonio"],
     ["Extorsión (art. 168)", "En la extorsión la víctima entrega por miedo; en la estafa, por error", "Excluyentes. Si hay engaño **y** amenaza (falso secuestro virtual), suele prevalecer la extorsión"],
     ["Falsificación de documento público o privado (art. 292)", "El documento falso suele ser el ardid", "Concurso ideal o real, según la unidad o pluralidad de conductas"],
     ["Falsedad ideológica (art. 293)", "Insertar datos falsos en un instrumento público para usarlo en la estafa", "Concurso con la estafa"],
     ["Uso de documento falso (art. 296)", "Usar el documento falso como medio del engaño", "Concurso ideal con la estafa; el uso queda absorbido si lo usa el propio falsificador, según la posición mayoritaria"],
     ["Acceso ilegítimo a sistema (art. 153 bis)", "Ingresar sin autorización a una cuenta o sistema", "Concurso con el art. 173 inc. 16 (el art. 153 bis es subsidiario: «si no resultare un delito más severamente penado»)"],
     ["Asociación ilícita (art. 210)", "Organización estable de tres o más personas para cometer delitos indeterminados", "Concurso real con las estafas"],
     ["Encubrimiento (art. 277)", "Ayudar después del hecho, sin promesa anterior, a ocultar el dinero o a eludir la investigación", "Excluyente de la participación: si hubo acuerdo previo, es partícipe de la estafa"],
     ["Lavado de activos (art. 303)", "Poner en circulación el producto de la estafa con apariencia lícita", "Concurso real; el autor de la estafa puede ser autor del lavado (autolavado)"],
     ["Intermediación financiera no autorizada (art. 310)", "Captar fondos del público sin autorización", "Concurso con las estafas en los esquemas piramidales"],
     ["Usurpación de títulos (art. 247)", "Arrogarse un título profesional que no se tiene", "Concurso con la estafa por calidad simulada"],
     ["Patrocinio infiel (art. 271)", "Abogado o mandatario judicial que perjudica deliberadamente la causa confiada", "Concurso con la administración fraudulenta o la retención indebida"],
     ["Falsa denuncia (art. 245)", "Denunciar un robo inexistente para cobrar el seguro", "Concurso con la estafa (o su tentativa) contra la aseguradora"]],
    [4, 6, 6])
OJO("No existe en el Código Penal un tipo autónomo general de **suplantación de identidad digital**. La doctrina advierte que esa laguna dificulta encuadrar algunas modalidades de phishing, y hay proyectos de ley para tipificarla. Mientras tanto, la suplantación se valora como **medio** del ardid (nombre supuesto, art. 172) o a través de las falsificaciones documentales y del acceso ilegítimo.")
H2("14.3. Personas jurídicas")
P("El Código Penal no prevé, como regla general, la responsabilidad penal de las personas jurídicas por estafa. El régimen de la **Ley 27.401** se limita a un catálogo de delitos vinculados con la corrupción (art. 1), en el que no figura la estafa. Cuando una estafa se comete a través de una empresa, responden penalmente las **personas humanas** que intervinieron (directores, gerentes, empleados) según las reglas de autoría y participación, y la empresa responde **civilmente**.")
RES("**Resumen del capítulo.** Varias entregas de una misma víctima por el mismo engaño suelen formar un delito continuado; varias víctimas, un concurso real. La falsificación y el uso de documentos falsos concurren con la estafa. La extorsión y el hurto se excluyen con ella según cómo salió el bien. El encubrimiento supone ayuda posterior sin acuerdo previo. La estafa no genera responsabilidad penal de la persona jurídica.")

# =====================================================================
H1("Capítulo 15. Estrategias de litigio: acusación y defensa")
P("Este capítulo está pensado para el ejercicio profesional. Reúne los argumentos y los puntos de prueba que se repiten en los juicios por defraudación, tanto desde la posición de la víctima querellante como desde la defensa del imputado.")
H2("15.1. Desde la querella")
P("La **teoría del caso** de la querella debe probar cada eslabón de la cadena típica con un medio de prueba concreto:")
TAB(["Elemento", "Qué hay que probar", "Medios de prueba"],
    [["Ardid", "Qué se dijo o se mostró y por qué era creíble", "Documentos usados, publicaciones, perfiles, chats, grabaciones, testigos de la puesta en escena"],
     ["Error", "Que la víctima creyó lo que se le dijo", "Declaración de la víctima; conducta posterior coherente con el engaño (reclamos, denuncias)"],
     ["Disposición", "Qué entregó la víctima, cuándo y a quién", "Comprobantes bancarios, recibos, escrituras, remitos"],
     ["Perjuicio", "La disminución patrimonial y su monto", "Pericia contable; tasaciones; cotizaciones de moneda a la fecha"],
     ["Dolo inicial", "Que el autor nunca quiso cumplir", "Identidad falsa; inexistencia de la empresa; pluralidad de víctimas; desaparición; destino inmediato de los fondos; antecedentes"],
     ["Autoría", "Quién estaba detrás de cada rol", "Informes de titularidad de cuentas y líneas; IP; cámaras; secuestro de dispositivos; análisis de vínculos"]],
    [3, 5, 8])
TIP("**Errores frecuentes de la víctima que conviene evitar:** denunciar como estafa una simple deuda; no intimar antes de denunciar una retención indebida; no conservar la evidencia digital en forma completa; demorar la denuncia y perder la posibilidad de bloquear los fondos; exagerar el monto del perjuicio sin respaldo documental.")
H2("15.2. Desde la defensa")
P("Las líneas de defensa más habituales en las causas por defraudación son las siguientes:")
NUM(["**Atipicidad por tratarse de un conflicto civil.** El caso es un incumplimiento contractual sin dolo inicial. Se prueba con los actos de ejecución del contrato (pagos parciales, entregas, comunicaciones), con la existencia real de la empresa y con las causas sobrevinientes del incumplimiento (crisis, enfermedad).",
     "**Falta de idoneidad del engaño.** El ardid era burdo o la víctima, por su profesión o actividad, tenía deberes de autoprotección que no cumplió (por ejemplo, una entidad financiera que no verificó la identidad).",
     "**Ausencia de error o de relación causal.** La víctima conocía la verdad o dispuso por otras razones.",
     "**Ausencia de perjuicio.** La víctima recibió una contraprestación equivalente, o el perjuicio no está acreditado ni cuantificado.",
     "**Falta de los presupuestos de las figuras especiales.** En la retención indebida: título que transfería la propiedad (mutuo), derecho de retención o falta de intimación. En la administración fraudulenta: falta de facultades de administración o ausencia del fin de lucro o de daño (mera mala gestión).",
     "**Excusa absolutoria del art. 185** en los conflictos familiares.",
     "**Prescripción** de la acción, con un cómputo cuidadoso del momento de la consumación y de los actos interruptivos (art. 67).",
     "**Incompetencia** territorial o material.",
     "**Nulidades y cuestionamientos de la prueba digital**: falta de cadena de custodia, capturas sin respaldo pericial, accesos a dispositivos sin orden judicial.",
     "**Salidas alternativas**: conciliación o reparación integral, suspensión del juicio a prueba, juicio abreviado con una pena de ejecución condicional. La **reparación temprana** es, en la práctica, la estrategia más eficaz en muchas causas por defraudación."])
OJO("Quien denuncia a sabiendas un delito inexistente puede incurrir en **falsa denuncia** (art. 245 CP) y en responsabilidad civil por **acusación calumniosa** (art. 1771 CCyC), aunque esta última exige dolo o culpa grave. Es un riesgo concreto cuando se usa la denuncia penal como herramienta de cobro.")
RES("**Resumen del capítulo.** La querella debe asignar a cada elemento del tipo un medio de prueba concreto, con especial atención al dolo inicial y a la trazabilidad del dinero. La defensa suele centrarse en la naturaleza civil del conflicto, la idoneidad del engaño, la falta de perjuicio, los presupuestos de las figuras especiales, el art. 185, la prescripción, las nulidades de la prueba digital y las salidas alternativas basadas en la reparación.")

# =====================================================================
H1("Capítulo 16. Responsabilidad civil y caso integral")
H2("16.1. La reparación del daño causado por una defraudación")
P("Toda defraudación genera, además de la responsabilidad penal, la obligación de **reparar el daño** (art. 1716 CCyC). La víctima puede reclamarla como **actor civil** en el proceso penal o en una **demanda civil** autónoma. Los rubros habituales son:")
BUL(["**Daño emergente**: la suma o el valor de los bienes entregados, con sus intereses desde la fecha de cada entrega.",
     "**Lucro cesante o pérdida de chance**: por ejemplo, la renta que habría producido el dinero o la operación frustrada, si se acredita.",
     "**Consecuencias no patrimoniales** (daño moral, art. 1741 CCyC): especialmente relevantes en las estafas a personas mayores o en las que comprometieron los ahorros de toda una vida.",
     "**Gastos**: honorarios de profesionales, pericias privadas, gastos de traslado."])
P("El plazo de prescripción de la acción de daños es, como regla, de **tres años** (art. 2561, 2.º párrafo, CCyC). Cuando la acción civil deriva de un delito, deben tenerse en cuenta las reglas de suspensión y de prejudicialidad del Código Civil y Comercial (art. 1775).")
TIP("Además del autor de la estafa, analice si hay **otros legitimados pasivos** con solvencia: el banco o la billetera virtual (deber de seguridad), la plataforma de ventas (según el caso), la inmobiliaria o el escribano que intervino, la empresa en cuyo nombre actuaba el estafador (responsabilidad por el dependiente, art. 1753 CCyC).")
H2("16.2. Caso integral: de la consulta a la sentencia")
P("Para cerrar la parte práctica, se recorre un caso completo. Es útil como ejercicio final de la conferencia.")
EJ("Los hechos",
   "Marcela y Julio, matrimonio de jubilados de la ciudad de Córdoba, firman en marzo un boleto para comprar un departamento «en pozo» en un fideicomiso. Pagan USD 45.000 en tres cuotas a la desarrolladora, que actúa como fiduciaria. En septiembre descubren que la obra está paralizada desde hace un año, que la desarrolladora vendió por escritura «su» unidad a otra persona en junio y que otras doce familias están en la misma situación. El gerente de la desarrolladora no responde.")
H3("Paso 1. La consulta: ¿es civil o penal?")
P("Hay indicios de **dolo**: la obra estaba paralizada **antes** de que Marcela y Julio firmaran (por lo que se les ocultó un dato esencial), la unidad se vendió a un tercero mientras ellos seguían pagando y hay otras doce víctimas. El caso excede el incumplimiento contractual.")
H3("Paso 2. La calificación")
BUL(["Respecto de Marcela y Julio: **defraudación fiduciaria** (art. 173 inc. 12), porque el fiduciario dispuso en beneficio propio de una unidad comprometida, y **desbaratamiento de derechos acordados** (art. 173 inc. 11), porque tornó litigioso el derecho que les había acordado por precio. Si se prueba que cuando firmaron ya se sabía que la obra no seguiría, también **estafa** (art. 172) por ocultamiento de información esencial que la fiduciaria tenía el deber de dar.",
     "Respecto del comprador de junio: posible **estafa o estelionato** si se le ocultó la venta anterior.",
     "Respecto de las doce familias: **un hecho por cada una** (concurso real).",
     "Si hay una estructura estable de tres o más personas dedicada a estas maniobras, **asociación ilícita** (art. 210)."])
H3("Paso 3. Las primeras medidas")
NUM(["**Carta documento** a la fiduciaria intimando a informar el estado de la obra, a rendir cuentas (arts. 1675 y concordantes CCyC) y a abstenerse de disponer de las unidades.",
     "**Denuncia penal** en la Fiscalía de Instrucción, con **constitución como querellantes particulares**, acompañando el contrato de fideicomiso, el boleto, los recibos, el informe de dominio que muestra la venta de junio y fotos de la obra.",
     "**Pedido de medidas**: informes registrales de todas las unidades; informes bancarios de las cuentas del fideicomiso y de la fiduciaria; pericia contable sobre el destino de los fondos; embargo e inhibición de bienes de la fiduciaria y de sus directivos.",
     "**En sede civil**, de manera simultánea: medida cautelar de anotación de litis o prohibición de innovar sobre el terreno y las unidades, y evaluación de la acción de remoción del fiduciario (art. 1678 CCyC)."])
H3("Paso 4. La investigación y el juicio")
P("La pericia contable demuestra que el 60 % de los fondos del fideicomiso se transfirió a otra sociedad del grupo. El fiscal imputa al gerente y a dos directivos por defraudación fiduciaria y desbaratamiento reiterados. La defensa plantea que se trata de un conflicto civil por la crisis del sector y ofrece entregar unidades de otra obra a las familias.")
H3("Paso 5. Las salidas posibles")
BUL(["**Conciliación** (art. 13 bis CPP Córdoba): si las familias aceptan las unidades ofrecidas u otra reparación y la reciben íntegramente, el fiscal puede prescindir de la acción.",
     "**Juicio abreviado**: los imputados reconocen los hechos a cambio de una pena acordada, eventualmente de ejecución condicional si no supera los tres años.",
     "**Juicio común**: la Cámara en lo Criminal y Correccional valora la prueba; si condena, fija la pena dentro de la escala resultante del concurso real y ordena la restitución y la indemnización (art. 29 CP) si hubo actor civil."])
RES("**Resumen del capítulo.** La defraudación obliga a reparar el daño emergente, el lucro cesante, las consecuencias no patrimoniales y los gastos. La acción de daños prescribe, como regla, a los tres años. Conviene buscar otros responsables solventes. El caso integral muestra la secuencia práctica: distinguir lo civil de lo penal, calificar con precisión, intimar, denunciar con querella, pedir medidas patrimoniales y elegir la salida procesal más conveniente.")
