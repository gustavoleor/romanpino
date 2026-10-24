# -*- coding: utf-8 -*-
from dsl import *

# =====================================================================
H1("Capítulo 4. Cuestiones comunes de fondo")
P("Antes de recorrer las figuras especiales conviene fijar algunas reglas de la parte general que se aplican a todas las defraudaciones y que son las que más se discuten en la práctica.")
FIG(24, "Consecuencias procesales y de fondo.")
H2("4.1. Acción penal")
P("Todas las defraudaciones son delitos de **acción pública** (art. 71 CP). No dependen de instancia privada, porque no figuran en el art. 72. La consecuencia es doble: el fiscal debe investigar de oficio apenas toma conocimiento del hecho, y el **desistimiento de la víctima no extingue la acción**. El arrepentimiento o el acuerdo económico pueden tener efectos (conciliación, reparación integral, criterios de oportunidad, suspensión del juicio a prueba), pero solo a través de los institutos que la ley prevé.")
H2("4.2. Prescripción")
P("Según el art. 62 inc. 2 CP, la acción prescribe en el **máximo de la pena** prevista para el delito, que nunca puede exceder de doce años ni bajar de dos. Aplicado a nuestras figuras:")
TAB(["Figura", "Máximo de la pena", "Plazo de prescripción"],
    [["Estafa (art. 172) y art. 173", "6 años", "6 años"],
     ["Art. 174", "6 años", "6 años"],
     ["Art. 175 (multa)", "Multa", "2 años (art. 62 inc. 5)"],
     ["Usura (art. 175 bis, 1.º y 2.º párrafo)", "3 años", "3 años"],
     ["Usura profesional o habitual (art. 175 bis, último párrafo)", "6 años", "6 años"],
     ["Quiebra fraudulenta (art. 176)", "6 años", "6 años"],
     ["Quiebra culpable (art. 177)", "1 año", "2 años (mínimo legal)"],
     ["Insolvencia fraudulenta (art. 179)", "3 años", "3 años"],
     ["Connivencia (art. 180)", "1 año", "2 años (mínimo legal)"]],
    [7, 4, 5])
P("El plazo corre **desde la medianoche del día en que se cometió el delito** o, si fuese continuo, desde que cesó de cometerse (art. 63). Se **interrumpe** por los actos del art. 67 (la comisión de otro delito, el primer llamado a indagatoria o declaración de imputado, el requerimiento de elevación a juicio, la citación a juicio y la sentencia condenatoria aunque no esté firme) y se **suspende** en los casos de ese mismo artículo, entre ellos mientras un funcionario público involucrado siga en su cargo.")
TIP("En las defraudaciones de larga duración (administración fraudulenta, desbaratamiento con actos sucesivos), determinar **cuándo se consumó** el hecho define si la acción está prescripta. La CSJN, en «Pompas» (ver Capítulo 6), consideró la gestión fraudulenta como un **hecho único**: la prescripción empieza a correr desde el último acto de esa gestión. En los fraudes previsionales, la jurisprudencia citada en el Capítulo 9 califica la obtención fraudulenta de un beneficio como delito instantáneo de efectos permanentes.")
H2("4.3. Autoría y participación")
P("Las reglas generales (arts. 45 a 49 CP) se aplican plenamente. En las estafas organizadas aparecen roles que conviene distinguir: quien diseña el ardid y lo dirige (autor o coautor), quien llama o chatea con la víctima (coautor por división de funciones), quien presta su cuenta para recibir el dinero (la llamada **cuenta mula**: partícipe necesario o secundario, según su aporte y su conocimiento) y quien después ayuda a ocultar el dinero sin acuerdo previo (encubrimiento, art. 277, o lavado de activos, art. 303, según el caso).")
JUR("CNCrim. y Correc., Sala VII, «G., R. M.», causa CCC 31.240/2021/CA1, 02/11/2022",
    "Se confirmó el procesamiento del titular de la cuenta receptora de los fondos de un fraude informático como **partícipe necesario**. La decisión no se apoyó solo en la titularidad de la cuenta, sino en un conjunto de circunstancias: la recepción del dinero, su giro inmediato en varias operaciones y su disposición posterior. El aporte de la cuenta sirvió para la consumación material del ilícito.",
    "Pensamiento Penal, fallo n.º 90530; Diario Judicial, «Mulero informático atrapado».")
OJO("La sola titularidad de la cuenta receptora **es un indicio, no una prueba** de participación. Muchas cuentas mula pertenecen a personas a las que les robaron la identidad o que fueron engañadas («trabajo desde casa», «te deposito por error, devolvémelo»). Hay que investigar el **conocimiento** del titular.")
H2("4.4. La excusa absolutoria del art. 185 (defraudaciones en familia)")
LEY("Art. 185 del Código Penal (núcleo)", "Están exentos de responsabilidad criminal, sin perjuicio de la civil, por los hurtos, defraudaciones o daños que recíprocamente se causaren: 1. Los cónyuges, ascendientes, descendientes y afines en la línea recta; 2. El consorte viudo, respecto de las cosas de la pertenencia de su difunto cónyuge, mientras no hayan pasado a poder de otro; 3. Los hermanos y cuñados, si viviesen juntos. La excepción establecida en el párrafo anterior, no es aplicable a los extraños que participen del delito.")
FIG(23, "La excusa absolutoria entre parientes.")
P("Es una norma de enorme importancia para quienes ejercen el **derecho de familia**. El delito existe (el hecho es típico, antijurídico y culpable), pero la ley **renuncia a la pena** para preservar la armonía familiar. Por eso subsiste la **responsabilidad civil**: la víctima puede reclamar la restitución y los daños en sede civil o de familia.")
BUL(["Alcanza a **hurtos, defraudaciones y daños**. No alcanza al robo, a la extorsión ni a la usura.",
     "El vínculo debe existir **al momento del hecho**. La jurisprudencia aplicó la excusa aunque el divorcio se haya decretado después del hecho.",
     "Entre **cónyuges**, la Cámara Nacional en lo Criminal y Correccional aplicó la excusa aun cuando estaban **separados de hecho**, porque la ley atiende al vínculo legal.",
     "Respecto de las **uniones convivenciales** (arts. 509 y ss. CCyC), la cuestión está abierta: hay un precedente que asimiló la unión convivencial a la categoría de cónyuge y absolvió por daño, pero la analogía *in bonam partem* no es pacífica.",
     "**No beneficia a los extraños** que participen en el hecho (por ejemplo, el amante que ayuda al cónyuge a vaciar la cuenta común)."])
JUR("CNCrim. y Correc., Sala IV (excusa absolutoria entre cónyuges separados de hecho)",
    "Se confirmó que la excusa absolutoria del art. 185, inc. 1, se aplica a la defraudación cometida entre cónyuges separados de hecho, porque el vínculo matrimonial subsistía al momento del hecho.",
    "abogados.com.ar, «Confirman que la excusa absolutoria del art. 185, inciso 1°, del Código Penal aplica ante la defraudación entre cónyuges separados de hecho».")
JUR("Precedente sobre unión convivencial (art. 185 y daño)",
    "Se asimiló la unión convivencial a la categoría de cónyuge a los fines del art. 185 y se absolvió por el delito de daño.",
    "Pensamiento Penal, fallo n.º 44305, «Daño. Asimilación de la unión convivencial a la categoría de cónyuge. Absolución». Verificar tribunal y fecha en la fuente.")
EJ("Ejemplo para abogados de familia",
   "En pleno divorcio, el marido usa el poder general que su esposa le había otorgado años atrás para vender un auto ganancial registrado a nombre de ella y se queda con el precio. En abstracto podría ser una administración fraudulenta (art. 173 inc. 7), pero **el art. 185 inc. 1 lo exime de pena**. La vía es civil: liquidación de la comunidad, recompensas (arts. 488 y ss. CCyC) y daños. Distinto es el caso si el comprador conocía la maniobra y participó en ella: **el extraño no está amparado** por la excusa.")
OJO("Hay proyectos legislativos para derogar o limitar el art. 185 (por ejemplo, el expediente 1318-D-2023). A octubre de 2026 no se registra su sanción.")
H2("4.5. Medición de la pena y reparación")
P("Dentro de la escala, el juez individualiza la pena según los arts. 40 y 41 CP: monto del perjuicio, cantidad de víctimas, vulnerabilidad de la víctima, sofisticación del ardid, antecedentes y conducta posterior, en especial la **reparación** del daño. En las defraudaciones, la devolución del dinero suele ser el factor que más influye en la respuesta penal, por cuatro vías:")
BUL(["**Condena de ejecución condicional** (art. 26): si la pena impuesta no supera los tres años y se trata de una primera condena.",
     "**Suspensión del juicio a prueba** (art. 76 bis): procede en delitos con pena máxima de hasta tres años y también, según el criterio amplio de la CSJN en «Acosta» (Fallos 331:858, 2008), cuando el caso admitiría condena condicional (4.º párrafo). El imputado debe **ofrecer hacerse cargo de la reparación** del daño en la medida de lo posible.",
     "**Extinción de la acción por conciliación o reparación integral** (art. 59 inc. 6, incorporado por la Ley 27.147 de 2015), «de conformidad con lo previsto en las leyes procesales». En Córdoba, el art. 13 bis del CPP (Ley 10.457, 2017) regula la conciliación (ver Capítulo 12).",
     "**Restitución y decomiso**: la sentencia condenatoria ordena la restitución de lo obtenido y la indemnización (art. 29 CP) y el decomiso de los instrumentos y del producto del delito (art. 23 CP)."])
JUR("Tribunal Oral en lo Criminal Federal n.º 4 de San Martín (octubre de 2026)",
    "Declaró extinguida la acción penal por conciliación y sobreseyó al titular de una cuenta bancaria abierta con sus datos y documentación, que había recibido $300.000 de una estafa y los había transferido a otra persona, tras pagarle esa suma a la víctima.",
    "Justicia de Primera, 22/10/2026, «Prestó su cuenta del banco para una estafa, pagó $300.000 a su víctima y cerraron la causa».")
H2("4.6. Competencia territorial en las estafas a distancia")
FIG(25, "Competencia territorial.")
P("En las estafas telefónicas o por internet el engaño se despliega en un lugar y la disposición patrimonial se produce en otro. La Corte Suprema, que resuelve los conflictos de competencia entre jurisdicciones, sostiene que **tanto el lugar donde se desarrolló el ardid como aquel donde se verificó la disposición patrimonial** pueden fundar la competencia, y que la elección debe guiarse por razones de **economía y celeridad procesal**.")
JUR("CSJN, Fallos 311:2607 y Fallos 333:2052 (doctrina reiterada en materia de competencia por estafa)",
    "Para establecer la competencia territorial en el delito de estafa deben tenerse en cuenta tanto el lugar donde se desarrolla el ardid como aquel en el que se verifica la disposición patrimonial. La decisión entre ambos se funda en razones de economía procesal. En casos de estafas iniciadas por redes sociales, la Corte dispuso que la causa continúe ante el juzgado que previno.",
    "Pensamiento Penal, fallo n.º 90994 («CSJN: solidifica criterio de competencia en la estafa»); Erreius; Actualidad Jurídica.")
JUR("Cámara Nacional de Casación en lo Criminal y Correccional, Sala II, CCC 38624/2021/1/RH1, «N. N. s/ defraudación informática», 23/03/2022",
    "Resolvió un conflicto de competencia en una investigación por defraudación mediante manipulación informática (art. 173 inc. 16 CP) y declaró competente a la justicia nacional en lo criminal y correccional.",
    "elDial.com.")
RES("**Resumen del capítulo.** Las defraudaciones son de acción pública. La estafa prescribe a los 6 años, las figuras con multa a los 2 y la usura simple a los 3. Rigen las reglas generales de autoría y participación: la cuenta mula puede ser partícipe, pero la titularidad sola no prueba el dolo. El **art. 185** exime de pena (no de responsabilidad civil) a cónyuges, ascendientes, descendientes, afines en línea recta y hermanos o cuñados convivientes. La reparación del daño abre las puertas a la condicional, la probation y la extinción por conciliación o reparación integral. La competencia en las estafas a distancia se fija en el lugar del ardid o en el de la disposición, según la economía procesal (CSJN).")

# =====================================================================
PARTE("Segunda parte", "Los casos especiales de defraudación (art. 173)")
H1("Capítulo 5. Art. 173: incisos 1 a 6")
LEY("Art. 173, encabezado", "Sin perjuicio de la disposición general del artículo precedente, se considerarán casos especiales de defraudación y sufrirán la pena que él establece: […]")
FIG(12, "Los dieciséis incisos del art. 173.")
P("El art. 173 enumera dieciséis supuestos que el legislador quiso dejar fuera de toda duda. Todos tienen **la misma pena que la estafa** (prisión de un mes a seis años) y todos exigen, por ser «casos de defraudación», un **perjuicio patrimonial**. Algunos son verdaderas estafas con un medio específico (incs. 1, 3, 9, 10). Otros son abusos de confianza, sin engaño inicial (incs. 2, 7, 12, 14). Y otros castigan frustraciones de derechos (inc. 11) o fraudes contra sistemas (incs. 15 y 16).")
TIP("El encabezado dice «sin perjuicio de la disposición general del artículo precedente». Si un caso no encaja exactamente en un inciso, todavía puede encuadrar en el art. 172. Y si encaja en un inciso, este desplaza al art. 172 por **especialidad**. En la imputación conviene citar siempre el inciso específico.")

# ---------------------------------------------------------------- inc 1
H2("5.1. Inciso 1: defraudación en la sustancia, calidad o cantidad")
LEY("Art. 173 inc. 1", "El que defraudare a otro en la substancia, calidad o cantidad de las cosas que le entregue en virtud de contrato o de un título obligatorio.")
FICHA([("Sujeto activo", "Quien está obligado a entregar cosas en virtud de un contrato o de un título obligatorio (vendedor, proveedor, depositario, contratista)."),
       ("Sujeto pasivo", "El acreedor de la entrega."),
       ("Conducta", "Entregar cosas distintas a las debidas en su sustancia (naturaleza), calidad (categoría, pureza) o cantidad (peso, número, medida)."),
       ("Presupuesto", "Una obligación de entregar preexistente (contrato o título obligatorio)."),
       ("Tipo subjetivo", "Dolo: saber que se entrega algo distinto y querer que el acreedor lo reciba como si fuera lo debido."),
       ("Consumación", "Cuando el acreedor recibe la cosa y sufre el perjuicio (paga o da por cumplida la obligación)."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("Es una **estafa en el cumplimiento** de un contrato válido. La obligación nació lícitamente, pero el deudor, al cumplir, engaña sobre lo que entrega. Por eso se diferencia de la estafa contractual del art. 172, en la que el engaño es la causa del contrato mismo.")
BUL(["**Sustancia**: la cosa es de otra naturaleza (se entrega latón por oro, aceite de girasol por aceite de oliva).",
     "**Calidad**: es de la misma naturaleza pero de categoría inferior (un vino de mesa por un reserva, cereal con humedad o cuerpos extraños por encima del estándar pactado).",
     "**Cantidad**: se entrega menos de lo debido (bolsas de cemento con menos kilos, menos metros de cable)."])
P("Cuando el fraude en la cantidad se comete usando **pesas o medidas falsas**, el hecho se agrava y pasa al art. 174 inc. 3 (prisión de 2 a 6 años). Si se trata de alimentos o medicamentos adulterados de modo peligroso para la salud, concurren los delitos contra la salud pública (arts. 200 y 201 CP).")
EJ("Ejemplo: el corralón y el hormigón",
   "Una empresa contrata 30 m³ de hormigón H-30 para una losa. El proveedor, sabiendo que no tiene stock de esa calidad, entrega H-17 con remitos que dicen H-30 y cobra el precio total. Hay defraudación **en la calidad** (art. 173 inc. 1). Si además la losa compromete la seguridad del edificio, puede concurrir el fraude en la construcción del art. 174 inc. 4.")
RES("**Resumen.** El inciso 1 castiga al deudor que, al cumplir un contrato válido, entrega dolosamente cosas de distinta sustancia, calidad o cantidad. Requiere obligación previa de entregar, engaño en la entrega y perjuicio. Si se usan pesas o medidas falsas, se aplica la agravante del art. 174 inc. 3.")

# ---------------------------------------------------------------- inc 2
H2("5.2. Inciso 2: retención indebida")
LEY("Art. 173 inc. 2", "El que con perjuicio de otro se negare a restituir o no restituyere a su debido tiempo, dinero, efectos o cualquier otra cosa mueble que se le haya dado en depósito, comisión o administración u otro título que produzca obligación de entregar o devolver.")
FIG(13, "La retención indebida paso a paso.")
FICHA([("Bien jurídico", "Propiedad: el derecho del titular a recuperar la cosa entregada."),
       ("Sujeto activo", "Quien recibió la cosa por un título que lo obliga a entregar o devolver (depositario, comisionista, mandatario, cobrador, administrador, locatario de cosa mueble, comodatario)."),
       ("Sujeto pasivo", "Quien tiene derecho a la restitución (el que entregó o el tercero destinatario)."),
       ("Objeto", "Dinero, efectos (títulos, valores) o cualquier cosa mueble. No inmuebles."),
       ("Conductas", "a) Negarse a restituir; b) no restituir a su debido tiempo."),
       ("Presupuestos", "Tenencia legítima previa; título que obligue a entregar o devolver; exigibilidad de la restitución."),
       ("Tipo subjetivo", "Dolo: conocer la obligación de restituir y querer no hacerlo."),
       ("Consumación", "Con la negativa o con el vencimiento del plazo sin restituir, con perjuicio. En la práctica, después de la intimación."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
H3("a) Estructura")
P("Es el caso típico de **abuso de confianza**. El autor recibió legítimamente la cosa, sin engaño. Lo punible es lo que hace después: en lugar de restituirla cuando debe, la retiene, la usa como propia o dispone de ella.")
P("El título debe generar una **obligación de entregar o devolver la misma cosa** (o, si es dinero, de entregar o rendir esa suma a quien corresponde). Por eso quedan fuera los títulos que **transfieren la propiedad**. Quien recibe dinero en préstamo (mutuo, art. 1525 CCyC) se hace dueño de ese dinero y solo debe devolver otro tanto: si no paga, es un deudor incumplido, no un defraudador.")
TAB(["Título", "¿Típico?", "Por qué"],
    [["Depósito, comodato, locación de cosa mueble", "Sí", "Obligan a devolver la misma cosa"],
     ["Mandato o comisión para cobrar y rendir", "Sí", "Lo cobrado pertenece al mandante"],
     ["Administración de fondos ajenos", "Sí (o inc. 7)", "Obliga a rendir cuentas y entregar"],
     ["Mutuo (préstamo de dinero)", "No", "Transfiere la propiedad del dinero"],
     ["Compraventa con precio impago", "No", "El comprador es dueño; hay solo deuda"],
     ["Cheque recibido para descontar con libre disponibilidad", "No", "El agente podía disponer del valor"]],
    [6, 3, 7])
H3("b) La intimación")
P("La ley no menciona la intimación, pero la jurisprudencia la considera **necesaria** en la mayoría de los casos, porque es lo que permite saber si el autor se **niega** a restituir o si la restitución está **vencida** y el autor lo sabe. La intimación **fehaciente** (carta documento, telegrama, acta notarial, requerimiento judicial) es además la mejor prueba del **dolo**.")
JUR("Tribunal Superior de Justicia de Córdoba, Sala Penal, «Lange», Sentencia n.º 195, 01/08/2012 (retención indebida y administración fraudulenta)",
    "La retención indebida supone una tenencia legítimamente adquirida que el tenedor no restituye; es un delito doloso, que exige conocer la obligación de devolver. La intimación es necesaria para tipificar la figura cuando la cosa no se restituye en término. En la administración fraudulenta, en cambio, se exige un fin específico: procurar un lucro indebido o causar daño.",
    "Pensamiento Penal, fallo n.º 34732; número y fecha confirmados por su cita en TSJ Córdoba, «Bustos», S. n.º 463, 09/11/2018.")
JUR("Tribunal Superior de Justicia de Córdoba, Sala Penal, «Bustos, Ricardo Alberto», Sentencia n.º 463, 09/11/2018 (SAC 1399480; vocales López Peña, Tarditti y Cáceres de Bollati)",
    "Al resolver los recursos de casación contra la sentencia absolutoria de la Cámara en lo Criminal y Correccional de Cruz del Eje (S. n.º 40, 06/07/2017), la Sala reiteró que la retención indebida requiere la entrega de una cosa mueble con la obligación de devolver esa misma cosa a su debido tiempo, y que el autor tiene sobre ella un poder de hecho legítimamente adquirido en virtud del negocio jurídico acordado (con cita de «Lange»).",
    "Portal de jurisprudencia del Poder Judicial de Córdoba (jurisprudencia.justiciacordoba.gob.ar). Leer la parte dispositiva en el texto completo antes de citar el resultado del recurso.")
JUR("CNCrim. y Correc., Sala IV, causa 1055/11 (2011)",
    "Se descartó el dolo del art. 173 inc. 2 porque no existió una intimación fehaciente que acreditara que el imputado conocía su deber de restituir: los requerimientos habían sido solo verbales.",
    "derechopenalonline.com, «Retención indebida. Atipicidad. Intimación fehaciente».")
JUR("Suprema Corte de Justicia de la Provincia de Buenos Aires (1992)",
    "Consideró suficiente la intimación cursada por carta documento para tener por configurada la negativa a restituir.",
    "vLex Argentina (sumario editorial).")
H3("c) Supuestos frecuentes")
BUL(["**El abogado que cobra para su cliente y no le entrega el dinero.** El profesional percibe la indemnización depositada en el expediente o pagada por la aseguradora y no la rinde. Es un caso típico de retención indebida (o de administración fraudulenta si gestionaba fondos en forma más amplia). Puede retener sus honorarios regulados o pactados, pero no el capital del cliente.",
     "**El cobrador o vendedor que no rinde lo cobrado** a su empleador.",
     "**El empleado que retiene las herramientas de trabajo** (notebook, celular, vehículo) después del despido. La jurisprudencia admitió la figura, aunque hay que valorar si el trabajador alega un **derecho de retención** como garantía de créditos laborales.",
     "**El socio o ex administrador que retiene los libros contables** de la sociedad.",
     "**El taller o el depósito** que se niega a devolver el vehículo sin derecho a hacerlo."])
OJO("El **derecho de retención** (arts. 2587 y ss. CCyC) excluye la tipicidad. Quien retiene una cosa ajena porque tiene un crédito originado en ella (el mecánico al que no le pagaron la reparación) ejerce un derecho y no comete delito. Si el dueño se lleva la cosa sin pagar, quien comete delito es el dueño (art. 173 inc. 5).")
EJ("Ejemplo para la conferencia: la seña de la inmobiliaria",
   "Una inmobiliaria recibe USD 10.000 como depósito de garantía de una reserva de compra, con instrucción escrita de entregarlos al vendedor si se firma la escritura o de devolverlos al comprador si la operación se cae. La operación se cae, el comprador intima por carta documento y la inmobiliaria no devuelve el dinero porque lo usó para pagar sueldos. Hay **retención indebida**: el dinero se recibió con una afectación específica, no como propio.")
RES("**Resumen.** El inciso 2 castiga a quien, habiendo recibido legítimamente dinero o cosas muebles por un título que lo obliga a devolverlas o entregarlas, se niega a hacerlo o no lo hace a tiempo, con perjuicio. Es un abuso de confianza sin engaño inicial. No alcanza los títulos que transfieren la propiedad (mutuo). La **intimación fehaciente** es clave como prueba del dolo, y el derecho de retención excluye el delito.")

# ---------------------------------------------------------------- inc 3
H2("5.3. Inciso 3: suscripción engañosa de documento")
LEY("Art. 173 inc. 3", "El que defraudare, haciendo suscribir con engaño algún documento.")
FICHA([("Sujeto activo", "Cualquier persona."),
       ("Sujeto pasivo", "Quien firma engañado o el tercero perjudicado por el documento."),
       ("Conducta", "Hacer firmar un documento mediante engaño, defraudando."),
       ("Objeto", "Cualquier documento con efectos patrimoniales: pagaré, recibo, poder, cesión, boleto."),
       ("Tipo subjetivo", "Dolo directo."),
       ("Consumación", "Con el perjuicio patrimonial derivado del documento. Para un sector doctrinario basta la firma, si el documento tiene por sí eficacia dispositiva; para otro, hace falta el uso que produce el perjuicio."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("Es una estafa en la que la **disposición patrimonial es la firma**. El engaño puede recaer sobre la naturaleza del documento (la víctima cree firmar un recibo y firma un pagaré), sobre su contenido (cree que reconoce $10.000 y dice $100.000) o sobre sus efectos (cree firmar una autorización de trámite y firma un poder para vender).")
P("Se distingue del art. 174 inc. 2, que castiga con pena mayor a quien hace firmar un documento a un **menor o incapaz** abusando de sus necesidades, pasiones o inexperiencia. Allí no es necesario el engaño: basta el abuso.")
EJ("Ejemplo: el «trámite de ANSES»",
   "Un gestor visita a un jubilado y le dice que debe firmar unos formularios para cobrar un retroactivo. Entre los papeles hay un poder especial irrevocable para cobrar sus haberes y una cesión de derechos litigiosos a favor del gestor. El jubilado firma confiado. Hay **suscripción engañosa** (art. 173 inc. 3). Si además el jubilado tuviera una restricción a la capacidad declarada, podría encuadrar en el art. 174 inc. 2.")
RES("**Resumen.** El inciso 3 es una estafa cuya disposición patrimonial consiste en **firmar** un documento por engaño sobre su naturaleza, contenido o efectos. Requiere perjuicio patrimonial. Si la víctima es menor o incapaz y hay abuso, se aplica el art. 174 inc. 2.")

# ---------------------------------------------------------------- inc 4
H2("5.4. Inciso 4: abuso de firma en blanco")
LEY("Art. 173 inc. 4", "El que cometiere alguna defraudación abusando de firma en blanco, extendiendo con ella algún documento en perjuicio del mismo que la dio o de tercero.")
FICHA([("Sujeto activo", "Quien recibió voluntariamente un papel firmado en blanco (total o parcialmente) con un mandato o pacto sobre cómo completarlo."),
       ("Sujeto pasivo", "El firmante o un tercero perjudicado."),
       ("Conducta", "Completar el documento en forma contraria a lo pactado («abusar» de la firma), extendiendo un documento perjudicial."),
       ("Presupuesto", "Entrega voluntaria de la firma en blanco. Si la firma fue sustraída o el papel se obtuvo sin entrega voluntaria, el caso se desplaza a la falsificación documental."),
       ("Consumación", "Con el perjuicio derivado del documento completado abusivamente."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("Es un **abuso de confianza documental**. El firmante confió en quien recibió el papel firmado y este lo completó traicionando lo acordado. Es muy frecuente en la práctica con los **pagarés en blanco** firmados en garantía de créditos de consumo, alquileres o planes de ahorro, y con **cheques firmados en blanco** entregados a empleados o socios.")
EJ("Ejemplo: el pagaré de garantía",
   "Para alquilar un local, el inquilino firma un pagaré en blanco como garantía de los alquileres, con la indicación escrita de que solo puede completarse por el monto adeudado al término del contrato. Al finalizar, el locador lo completa por una suma diez veces mayor y lo ejecuta. Hay **abuso de firma en blanco** (art. 173 inc. 4). En el juicio ejecutivo, el deudor puede oponer la excepción de inhabilidad de título o de falsedad, según el caso, y la denuncia penal puede fundar un pedido de suspensión o una medida cautelar.")
RES("**Resumen.** El inciso 4 castiga a quien completa un documento firmado en blanco en contra de lo pactado con el firmante y causa perjuicio. Supone una entrega **voluntaria** de la firma; si fue sustraída, hay falsificación. Es el delito típico del pagaré en blanco completado por montos indebidos.")

# ---------------------------------------------------------------- inc 5
H2("5.5. Inciso 5: sustracción de la cosa propia (hurto impropio)")
LEY("Art. 173 inc. 5", "El dueño de una cosa mueble que la sustrajere de quien la tenga legítimamente en su poder, con perjuicio del mismo o de tercero.")
FICHA([("Sujeto activo", "Solo el **dueño** de la cosa (delito especial)."),
       ("Sujeto pasivo", "Quien la tiene legítimamente (acreedor prendario, retenedor, locatario, depositario, comodatario) o el tercero perjudicado."),
       ("Objeto", "Cosa mueble propia."),
       ("Conducta", "Sustraer: sacar la cosa de la esfera de custodia del tenedor legítimo sin su consentimiento."),
       ("Consumación", "Con la sustracción que causa perjuicio (el tenedor pierde su garantía o su derecho de uso)."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("Nadie puede hurtar una cosa propia, porque el hurto exige que la cosa sea «total o parcialmente ajena» (art. 162). Este inciso cubre ese vacío: el dueño que **se lleva su propia cosa** de manos de quien tenía un derecho a tenerla perjudica el derecho de ese tenedor. Por eso la doctrina lo llama **hurto impropio** o furtum possessionis.")
EJ("Ejemplo: el auto en el taller",
   "Carlos deja su auto en un taller para reparar el motor. Terminado el trabajo, el mecánico ejerce su derecho de retención hasta que le paguen (art. 2587 CCyC). Una noche, Carlos usa la llave de repuesto y se lleva el auto sin pagar. Carlos es el dueño, pero sustrajo la cosa de quien la tenía legítimamente, con perjuicio: comete el delito del **art. 173 inc. 5**.")
RES("**Resumen.** El inciso 5 castiga al dueño de una cosa mueble que la sustrae de quien la tiene legítimamente (por prenda, retención, locación o depósito), con perjuicio. Cubre el vacío del hurto, que exige cosa ajena.")

# ---------------------------------------------------------------- inc 6
H2("5.6. Inciso 6: contrato simulado y falsos recibos")
LEY("Art. 173 inc. 6", "El que otorgare en perjuicio de otro, un contrato simulado o falsos recibos.")
FICHA([("Sujeto activo", "Quien otorga (celebra o firma) el contrato simulado o el recibo falso, y su contraparte si actúa en connivencia."),
       ("Sujeto pasivo", "El tercero perjudicado (normalmente, un acreedor)."),
       ("Conducta", "Otorgar un contrato simulado (art. 333 CCyC: encubre el carácter jurídico de un acto o contiene cláusulas o fechas no sinceras) o recibos falsos."),
       ("Tipo subjetivo", "Dolo de perjudicar a otro mediante la apariencia creada."),
       ("Consumación", "Con el perjuicio derivado del acto simulado o del recibo falso (para un sector, basta el otorgamiento con aptitud para perjudicar)."),
       ("Pena", "Prisión de 1 mes a 6 años.")])
P("El inciso castiga la **simulación ilícita**, es decir, la que perjudica a terceros (art. 334 CCyC). La simulación lícita, que no perjudica a nadie, es irrelevante para el derecho penal. El recibo falso es el que documenta un pago inexistente y se usa para liberarse de una deuda o para reclamar algo que no corresponde.")
EJ("Ejemplo: la venta al hermano",
   "Ante una demanda por daños que sabe que va a perder, Roberto «vende» su única casa a su hermano por escritura pública, por un precio que nunca se paga, y sigue viviendo en ella. Cuando el acreedor quiere embargar, la casa ya no figura a su nombre. Hay **contrato simulado en perjuicio de otro** (art. 173 inc. 6). Como el acto se realizó durante el curso de un proceso, puede concurrir la **insolvencia fraudulenta** del art. 179, segundo párrafo. En sede civil, el acreedor dispone de la acción de simulación (arts. 333 a 337 CCyC) y de la acción revocatoria o pauliana (arts. 338 a 342 CCyC).")
RES("**Resumen.** El inciso 6 castiga la simulación ilícita (contrato aparente en perjuicio de un tercero) y el otorgamiento de recibos falsos. Es frecuente para burlar a los acreedores y puede concurrir con la insolvencia fraudulenta. Coexiste con las acciones civiles de simulación y revocatoria.")
