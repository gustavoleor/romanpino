# -*- coding: utf-8 -*-
from dsl import *

# =====================================================================
H1("Nota preliminar: cómo usar este libro")
P("Este apunte tiene un doble destino. Sirve para **estudiar** el régimen penal de la estafa y las demás defraudaciones del Código Penal argentino y sirve para **exponer** el tema en una conferencia. Por eso cada capítulo combina tres planos: el texto legal, la explicación dogmática necesaria y la aplicación práctica (ejemplos, sumarios de jurisprudencia y consejos de litigio).")
P("Cada figura se presenta con la misma estructura, para que el lector encuentre siempre la información en el mismo lugar:")
BUL(["**Texto legal** vigente, transcripto o reproducido en su núcleo.",
     "**Ficha técnica**: bien jurídico, sujetos, conducta, objeto, tipo subjetivo, consumación, tentativa y pena.",
     "**Explicación** en lenguaje claro de cada elemento del tipo.",
     "**Ejemplos** para usar en clase o en la conferencia.",
     "**Jurisprudencia** con indicación de tribunal, fecha y fuente donde puede consultarse.",
     "**Resumen** final del tema, pensado como síntesis para repasar o para cerrar cada bloque de la exposición."])
P("Las **filminas** están intercaladas en el lugar del texto donde corresponde proyectarlas. Están numeradas y el Anexo I reproduce un guion de conferencia que indica cuándo mostrar cada una.")
H2("Criterio de fuentes")
P("El texto legal corresponde al Código Penal de la Nación (Ley 11.179, t.o. por Decreto 3992/84, con sus modificatorias) **vigente a octubre de 2026**. A esa fecha no se registran reformas a los arts. 172 a 175 bis posteriores a la Ley 26.388 (2008). El proyecto de nuevo Código Penal impulsado por el Poder Ejecutivo nacional todavía no había ingresado formalmente al Congreso: las noticias de octubre de 2026 informan que el Gobierno prevé enviarlo antes de fin de año (ver Capítulo 1).")
P("La jurisprudencia citada se seleccionó por su jerarquía (Corte Suprema de Justicia de la Nación, Tribunal Superior de Justicia de Córdoba, Cámaras de Casación) y por su utilidad práctica. En cada caso se indica la fuente pública en la que fue localizada (Pensamiento Penal, Diario Judicial, sitio del Poder Judicial de Córdoba, Ministerio Público Fiscal, Microjuris, etc.).")
OJO("**Advertencia metodológica.** Este apunte se elaboró inicialmente sin acceso directo a las bases oficiales (InfoLEG, SAIJ, CSJN y Poder Judicial de Córdoba), porque la red del entorno de trabajo no las alcanzaba. Los textos legales se reconstruyeron a partir de reproducciones públicas concordantes y los sumarios a partir de las publicaciones indicadas en cada caso. Los sumarios son **síntesis** del criterio de cada fallo y no transcripciones textuales, salvo cuando se usan comillas. Antes de citar un fallo en un escrito judicial, conviene leerlo completo en la fuente indicada. El 24/10/2026 se realizó un cotejo con InfoLEG y con la base de datos abiertos de la CSJN: el Anexo IV detalla qué se verificó, qué se corrigió y qué sigue pendiente.")

# =====================================================================
PARTE("Primera parte", "Teoría general de las defraudaciones")
H1("Capítulo 1. Ubicación, bien jurídico y evolución legislativa")
FIG(1, "Portada de la conferencia.")
H2("1.1. Ubicación sistemática")
P("El Código Penal regula los delitos contra la propiedad en el **Título VI** del Libro Segundo. Dentro de ese título, el **Capítulo IV** se denomina «Estafas y otras defraudaciones» y abarca los arts. 172 a 175 bis. A continuación, el **Capítulo V** («Quebrados y otros deudores punibles», arts. 176 a 180) contiene figuras emparentadas, porque también lesionan el patrimonio mediante fraude, en este caso en perjuicio de los acreedores.")
FIG(2, "Mapa normativo del tema.")
TAB(["Norma", "Contenido", "Pena"],
    [["Art. 172", "Estafa: figura genérica de defraudación por engaño", "Prisión de 1 mes a 6 años"],
     ["Art. 173", "Dieciséis «casos especiales de defraudación»", "La del art. 172"],
     ["Art. 174", "Defraudaciones agravadas (6 incisos)", "Prisión de 2 a 6 años (y, en ciertos casos, inhabilitación especial perpetua para funcionarios)"],
     ["Art. 175", "Defraudaciones atenuadas (4 incisos)", "Multa"],
     ["Art. 175 bis", "Usura", "Prisión de 1 a 3 años y multa; agravada de 3 a 6 años"],
     ["Arts. 176 a 180", "Quiebra fraudulenta y culpable, insolvencia fraudulenta, connivencia", "Según la figura"],
     ["Art. 185", "Excusa absolutoria entre ciertos parientes (alcanza a las defraudaciones)", "Exime de pena; subsiste la responsabilidad civil"]],
    [3, 8, 6])
H2("1.2. El bien jurídico protegido")
P("La rúbrica del título habla de «propiedad», pero la doctrina argentina coincide en que el término no se usa en el sentido estricto del derecho real de dominio. Se lo toma en el sentido amplio del **art. 17 de la Constitución Nacional**, que la Corte Suprema identificó desde antiguo con «todos los intereses apreciables que un hombre puede poseer fuera de sí mismo, fuera de su vida y de su libertad» (CSJN, «Bourdieu c/ Municipalidad de la Capital», Fallos 145:307, 1925). En materia de defraudaciones esa idea equivale, en la práctica, al **patrimonio** de la víctima.")
P("Sobre qué es «patrimonio» a los fines penales hay tres concepciones:")
BUL(["**Jurídica**: el patrimonio es la suma de derechos subjetivos patrimoniales. Es demasiado estrecha, porque deja afuera expectativas y posiciones económicas valiosas que no son derechos.",
     "**Económica**: el patrimonio es todo lo que tiene valor económico, aun lo obtenido ilícitamente. Es demasiado amplia, porque obligaría a proteger, por ejemplo, el «patrimonio» del narcotraficante sobre la droga.",
     "**Mixta o jurídico-económica**, mayoritaria: el patrimonio comprende los bienes con valor económico que la persona tiene bajo una **relación reconocida o no desaprobada** por el derecho. Esta es la concepción que mejor explica los casos difíciles."])
P("La consecuencia práctica más importante es que **no hay defraudación sin perjuicio patrimonial**. Si la víctima fue engañada pero no sufrió una disminución económica efectiva, el hecho podrá ser inmoral, ilícito civil o, a lo sumo, tentativa, pero no una defraudación consumada.")
H2("1.3. Evolución legislativa")
P("El núcleo del capítulo proviene del Código de 1921. Las reformas posteriores agregaron figuras para responder a nuevas formas de criminalidad económica:")
TAB(["Ley", "Año", "Qué incorporó o modificó"],
    [["Ley 11.179", "1921", "Texto original: estafa (art. 172), casos especiales (art. 173, primeros incisos), agravantes y atenuantes"],
     ["Ley 18.934", "1971", "Incorporó la usura (art. 175 bis)"],
     ["Ley 24.441", "1995", "Art. 82: incorporó los incisos 12, 13 y 14 del art. 173 (titular fiduciario, ejecución extrajudicial, letras hipotecarias)"],
     ["Ley 25.602", "2002", "Incorporó el inciso 6 del art. 174 (afectación maliciosa de establecimientos)"],
     ["Ley 25.930", "2004", "Incorporó el inciso 15 del art. 173 (defraudación con tarjetas); B.O. 21/09/2004"],
     ["Ley 26.388", "2008", "Ley de delitos informáticos: incorporó el inciso 16 del art. 173 (manipulación informática)"]],
    [3, 2, 11])
OJO("Los incisos 7 y 11 del art. 173 tienen una historia legislativa compleja: fueron objeto de las reformas de facto de 1968 y 1976 y de la restitución de textos dispuesta por la Ley 23.077 (1984). Para citar la ley que dio su redacción actual a cada uno, conviene verificar las notas de InfoLEG.")
H2("1.4. Estado de la reforma penal (octubre de 2026)")
P("El Poder Ejecutivo nacional trabaja desde 2024 en un proyecto de nuevo Código Penal. Las noticias públicas indican que el texto fue revisado varias veces y que, a mediados de octubre de 2026, el Gobierno anunciaba su envío al Congreso **antes de fin de año** (fuente: notas periodísticas de octubre de 2026, entre ellas *El Liberal* y *Canal 26*; e *Infobae*, 05/08/2026). En abril de 2026 se había anunciado además una iniciativa para tipificar en forma específica las **estafas piramidales**.")
P("A los fines de este apunte importa una conclusión simple: **mientras no se sancione y publique una ley, rige el texto actual**. Además, si una reforma futura agravara las penas, no podría aplicarse retroactivamente a hechos anteriores (art. 18 CN y art. 2 CP, principio de ley penal más benigna).")
RES("**Resumen del capítulo.** Las defraudaciones están en el Capítulo IV del Título VI (arts. 172 a 175 bis), con un capítulo vecino sobre quebrados e insolvencia (arts. 176 a 180). El bien jurídico es la propiedad en sentido constitucional amplio, que en la práctica significa **patrimonio** con criterio jurídico-económico. Sin perjuicio patrimonial no hay defraudación consumada. El texto vigente es el de 1921 con agregados de 1971, 1995, 2002, 2004 y 2008. El proyecto de nuevo Código Penal aún no tiene sanción.")

# =====================================================================
H1("Capítulo 2. La defraudación: concepto y especies")
H2("2.1. Defraudación, estafa y abuso de confianza")
P("«Defraudación» es el **género**: comprende toda lesión patrimonial causada mediante **fraude**. La ley usa el verbo «defraudar» en el art. 172 y en varios incisos del art. 173. Dentro de ese género, la doctrina distingue dos grandes especies:")
BUL(["**Estafa o fraude por engaño.** El autor induce a error a la víctima mediante un ardid o engaño, y es la propia víctima quien, equivocada, realiza la disposición patrimonial que la perjudica. El modelo es el art. 172.",
     "**Abuso de confianza.** El autor ya tiene legítimamente el bien, o su manejo, porque la víctima se lo confió. No hay un engaño inicial: el fraude consiste en **traicionar** esa confianza, sea no devolviendo lo recibido (art. 173 inc. 2), sea administrando de manera infiel (art. 173 inc. 7), sea disponiendo de bienes fideicomitidos (art. 173 inc. 12)."])
FIG(3, "Las dos especies de defraudación.")
P("La distinción no es académica. Determina **qué hay que probar**. En la estafa, la prueba gira en torno al engaño, el error y la relación causal con la entrega. En el abuso de confianza, en torno al título que obligaba a devolver o a administrar, al incumplimiento de ese deber y al perjuicio.")
EJ("Ejemplo para la conferencia: dos maneras de quedarse con un auto ajeno",
   "**Caso A.** Juan se presenta en una concesionaria con un recibo de sueldo falso y un DNI ajeno, firma un plan de pagos y se lleva un auto que nunca piensa pagar. Hay **estafa**: el engaño fue la causa de la entrega.\n**Caso B.** Pedro deja su auto en el taller de Luis para que le cambie el embrague. Luis lo repara, pero en lugar de devolverlo lo usa como propio y se niega a restituirlo pese a la carta documento de Pedro. Hay **abuso de confianza** (retención indebida, art. 173 inc. 2): Luis recibió el auto legítimamente y lo defraudó después, al no devolverlo.")
H2("2.2. Elementos comunes a toda defraudación")
P("Más allá de la especie, toda defraudación requiere:")
NUM(["Un **medio fraudulento** (engaño o abuso de confianza), que es lo que distingue estas figuras del hurto y del robo, donde el autor toma la cosa contra la voluntad de la víctima.",
     "Un **perjuicio patrimonial** efectivo, real y apreciable económicamente.",
     "**Dolo**, es decir, conocimiento y voluntad de defraudar. No existe la defraudación culposa: quien causa un perjuicio por negligencia responde civilmente, no penalmente. La única excepción en los capítulos IV y V es la quiebra culpable (art. 177), que es un delito distinto."])
H2("2.3. Diferencias con figuras vecinas")
TAB(["Figura", "Cómo obtiene el autor el bien", "Voluntad de la víctima"],
    [["Hurto (art. 162)", "Lo **toma** sin violencia", "Falta: el bien sale contra o sin su voluntad"],
     ["Robo (art. 164)", "Lo toma con fuerza en las cosas o violencia o intimidación en las personas", "Falta o está quebrada por la violencia"],
     ["Extorsión (art. 168)", "La víctima entrega por **intimidación**", "Existe, pero viciada por miedo"],
     ["Estafa (art. 172)", "La víctima entrega por **error** provocado", "Existe, pero viciada por engaño"],
     ["Abuso de confianza (art. 173 incs. 2 y 7)", "Ya lo tenía legítimamente", "Entregó voluntariamente y sin vicio"]],
    [4, 6, 6])
TIP("**Regla práctica:** en el hurto el autor *saca*, en la estafa la víctima *entrega* engañada y en la extorsión la víctima *entrega* atemorizada. Si quien entrega la cosa lo hace porque fue engañado, el caso es de estafa aunque el autor haya terminado «llevándosela».")
RES("**Resumen del capítulo.** Defraudar es lesionar un patrimonio mediante fraude. Las dos especies son la **estafa**, con engaño previo que provoca error y entrega, y el **abuso de confianza**, que traiciona la confianza de quien entregó legítimamente. Toda defraudación exige medio fraudulento, perjuicio patrimonial y dolo. Lo que la separa del hurto, el robo y la extorsión es la forma en que el bien sale del patrimonio de la víctima.")

# =====================================================================
H1("Capítulo 3. La estafa del art. 172")
LEY("Art. 172 del Código Penal", "Será reprimido con prisión de un mes a seis años, el que defraudare a otro con nombre supuesto, calidad simulada, falsos títulos, influencia mentida, abuso de confianza o aparentando bienes, crédito, comisión, empresa o negociación o valiéndose de cualquier otro ardid o engaño.")
FIG(4, "El texto del art. 172.")
FICHA([("Bien jurídico", "Propiedad (patrimonio) de la víctima."),
       ("Sujeto activo", "Cualquier persona (delito común)."),
       ("Sujeto pasivo", "El titular del patrimonio perjudicado. Puede no coincidir con la persona engañada (estafa triangular)."),
       ("Conducta", "Defraudar mediante ardid o engaño que provoca error y una disposición patrimonial perjudicial."),
       ("Tipo subjetivo", "Dolo directo; el engaño debe ser anterior o concomitante a la disposición."),
       ("Consumación", "Con el perjuicio patrimonial (delito de resultado). No requiere que el autor obtenga lucro."),
       ("Tentativa", "Admitida: desde el comienzo del despliegue del ardid hasta antes del perjuicio."),
       ("Pena", "Prisión de un mes a seis años."),
       ("Acción", "Pública. Prescripción: 6 años (art. 62 inc. 2)."),
       ("Fuero", "Ordinario (provincial), salvo afectación de intereses federales.")])
H2("3.1. Concepto")
P("La definición clásica, de origen español y muy difundida en la doctrina argentina, es la de **José Antón Oneca**: la estafa es la conducta engañosa, con ánimo de lucro injusto, propio o ajeno, que, al determinar un error en una o varias personas, las induce a realizar un acto de disposición que causa un perjuicio en su patrimonio o en el de un tercero.")
P("De esa definición surge la **estructura típica** que la jurisprudencia argentina repite de manera constante. La Cámara Nacional en lo Criminal y Correccional, por ejemplo, la sintetiza en cuatro requisitos: **ardid o engaño, error de la víctima, disposición patrimonial y perjuicio**.")
FIG(5, "La cadena causal de la estafa.")
JUR("CNCrim. y Correc., Sala IV (caso de la pasajera de taxi)",
    "Para que una conducta encuadre en el delito de estafa son necesarios cuatro requisitos: el ardid o engaño, que provoque un error en el sujeto pasivo, que este realice una disposición patrimonial y que dicha disposición sea perjudicial. Con ese criterio se confirmó el procesamiento por estafa de una pasajera que, mediante engaño, no pagó un viaje en taxi de $61.",
    "Reseñado en Diario Judicial, nota «Una picardía que salió cara».")
H2("3.2. Primer elemento: el ardid o engaño")
H3("a) Concepto")
P("**Engaño** es toda conducta que hace aparecer como verdadero lo falso o que oculta lo verdadero. **Ardid**, según la conocida fórmula de **Sebastián Soler**, es «el astuto despliegue de medios engañosos». El ardid supone algo más que una simple mentira: una cierta **puesta en escena** (la *mise en scène* de la doctrina francesa) que da verosimilitud al engaño, como documentos, oficinas, terceros cómplices, perfiles falsos o sitios web clonados.")
P("El art. 172 enumera medios concretos y luego cierra con una cláusula general («cualquier otro ardid o engaño»). La enumeración es, por lo tanto, **ejemplificativa**: el tipo es abierto en cuanto a los medios y cerrado en cuanto a la estructura.")
H3("b) Los medios enumerados por la ley")
TAB(["Medio", "Qué significa", "Ejemplo"],
    [["Nombre supuesto", "Usar un nombre que no es el propio, sea inventado o de otra persona", "Alquilar un departamento con el nombre y los datos de un tercero"],
     ["Calidad simulada", "Atribuirse una condición personal que no se tiene (profesión, estado civil, parentesco, cargo)", "Falso médico que cobra tratamientos; falso empleado del banco"],
     ["Falsos títulos", "Invocar un título habilitante o de propiedad que no se tiene", "Quien se dice heredero o dueño para vender un inmueble"],
     ["Influencia mentida", "Simular influencia sobre quien puede decidir algo (funcionarios, jueces, empresarios)", "«Conozco al juez, por $X te saco la causa» (si se pretexta pagar al juez, ver inc. 10 del art. 173)"],
     ["Abuso de confianza", "Aprovechar una relación de confianza previa **como medio para engañar**", "El amigo de años que pide dinero para un negocio inexistente"],
     ["Aparentar bienes, crédito, comisión, empresa o negociación", "Simular solvencia, encargo o actividad económica", "Inversor que muestra una empresa ficticia; supuesto comisionista de un tercero"],
     ["Cualquier otro ardid o engaño", "Cláusula general", "Billetes falsos, sitio web clonado, falso premio, cuento del tío"]],
    [4, 6, 6])
OJO("El «abuso de confianza» del art. 172 no es el mismo que el de los incs. 2 y 7 del art. 173. En el art. 172 la confianza es un **instrumento del engaño**: la víctima entrega *porque confía* y es engañada. En el art. 173 incs. 2 y 7, la víctima entrega legítimamente y el fraude es **posterior**, cuando el autor incumple su deber de restituir o administrar.")
H3("c) La idoneidad del ardid")
P("El problema más debatido de la estafa es determinar **cuándo el engaño es suficiente**. No todo engaño es típico. La pregunta es si debe medirse con un parámetro general o atendiendo a la víctima concreta.")
FIG(6, "Teorías sobre la idoneidad del ardid.")
BUL(["**Tesis objetiva.** El ardid debe ser apto para engañar a una persona de inteligencia y diligencia medias. Los engaños groseros no son típicos. La crítica es que deja sin protección a las víctimas más vulnerables (ancianos, personas con escasa instrucción), que son precisamente el blanco preferido de los estafadores.",
     "**Tesis subjetiva.** Basta con que el ardid haya engañado de hecho a la víctima concreta, según su edad, su cultura y su situación. La crítica es que, llevada al extremo, convierte en estafa cualquier mentira que haya funcionado.",
     "**Tesis mixta o de la imputación objetiva**, hoy muy difundida. El engaño debe crear un **riesgo jurídicamente desaprobado** de que la víctima disponga perjudicialmente. Al evaluar ese riesgo se considera la situación concreta de la víctima, pero también los **deberes de autoprotección** que razonablemente le eran exigibles. Si la víctima pudo descubrir el engaño con un mínimo de diligencia y no lo hizo, el error podría no ser imputable al autor."])
JUR("CSJN, «Selman, Christian José s/ estafa y estafa en grado de tentativa –dos hechos– en concurso real», CSJ 690/2017/RH1, sentencia del 22/05/2020",
    "Precedente de la Corte Suprema que la doctrina toma como punto de partida para discutir la idoneidad del engaño y el alcance de los deberes de autoprotección de la víctima en la estafa. El comentario de Pablo G. Fossaroli («Los deberes de autoprotección en el delito de estafa. A propósito del fallo “Selman” de la CSJN») repasa las distintas posiciones y sostiene que la tesis funcionalista es la adecuada y respeta el principio de mínima intervención.",
    "Pensamiento Penal, doctrina n.º 89746. Se recomienda leer el fallo completo en el sitio de la CSJN antes de citar su doctrina.")
TIP("**Para el litigio.** Si usted **acusa o querella**, describa con detalle la situación concreta de la víctima (edad, nivel de instrucción, urgencia, relación previa con el autor) y la sofisticación del ardid (documentos, logos, voces, perfiles), para mostrar que el engaño creó un riesgo real. Si **defiende**, examine si el engaño era burdo y si la víctima omitió verificaciones elementales que le eran exigibles por su profesión o actividad (un banco, una inmobiliaria, un comerciante habitual).")
H3("d) Mentira, silencio y omisión")
FIG(7, "Ardid, mera mentira y silencio.")
P("**La mera mentira.** Para un sector de la doctrina, la simple afirmación falsa, sin apoyo en ningún hecho exterior, no alcanza: hace falta el «despliegue» que caracteriza al ardid. Para otro sector, el art. 172 menciona expresamente el «engaño» junto al «ardid», de modo que una mentira idónea, que efectivamente provoque error, puede ser típica. En la práctica, los tribunales suelen admitir la mentira como engaño cuando se inserta en un **contexto** que la hace creíble, por ejemplo cuando la víctima tenía razones para confiar en quien mentía.")
P("**El silencio.** Callar no es, en principio, engañar. Sin embargo, el silencio puede ser típico cuando el autor tenía un **deber jurídico de informar** (por ley, por contrato o por la buena fe negocial, arts. 9, 961 y 1061 del Código Civil y Comercial) y su omisión hizo que la víctima dispusiera en error. Es típico el caso del vendedor que oculta que la cosa vendida es robada o que el inmueble está embargado (en este último supuesto, ver el art. 173 inc. 9).")
JUR("Tribunal Superior de Justicia de Córdoba, Sala Penal (1967), citado en una reseña sobre estafa procesal",
    "La sola afirmación o el silencio contrarios a la verdad, que integran una petición injusta, no configuran el engaño propio de la estafa.",
    "Báez, Julio C. y Outeda, Diego M., «Estafa procesal. Reseña de jurisprudencia», Biblioteca del Poder Judicial de Córdoba.")
H2("3.3. Segundo elemento: el error")
P("El error es la **falsa representación de la realidad** que el engaño provoca en la mente de la víctima. Debe existir una relación causal: el error tiene que ser **consecuencia** del ardid y, a su vez, la **causa** de la disposición.")
P("De allí surgen tres consecuencias prácticas:")
BUL(["**Si la víctima sabía la verdad** y dispuso igual (por ejemplo, para «seguirle el juego» al autor y poder denunciarlo, o por lástima), no hay error y el hecho queda, a lo sumo, en **tentativa**.",
     "**Las máquinas no se equivocan.** Solo una persona humana puede caer en error. Por eso, cuando el perjuicio se causa engañando o manipulando un sistema (un cajero automático, un home banking), la estafa clásica presentaba problemas de tipicidad. Para cerrar esa laguna el legislador incorporó los incisos 15 (tarjetas, «aunque lo hiciere por medio de una operación automática») y 16 (manipulación informática) del art. 173.",
     "**La duda no excluye el error.** Quien entrega dudando, pero movido por el engaño, también yerra."])
H2("3.4. Tercer elemento: la disposición patrimonial")
P("La disposición patrimonial es el **acto voluntario de la víctima** (entregar dinero o cosas, transferir, firmar, pagar, prestar un servicio, renunciar a un crédito) que produce directamente el perjuicio. Es el elemento que separa la estafa del hurto: en la estafa la víctima **se perjudica a sí misma**, aunque engañada.")
P("Puede consistir en una acción (pagar, entregar) o en una omisión (no cobrar, no reclamar). Quien dispone no tiene que ser el titular del patrimonio: basta con que tenga **facultad** de hecho o de derecho para disponer sobre él. De esa idea nace la estafa triangular.")
H3("La estafa triangular")
FIG(8, "Estafa triangular: engañado distinto del perjudicado.")
P("Hay estafa triangular cuando la persona **engañada**, que es también quien realiza la disposición, es **distinta** del titular del patrimonio perjudicado. El cajero de un banco que paga un cheque falso, el empleado de una empresa que entrega mercadería a un falso transportista o el juez que dicta una sentencia sobre la base de prueba falsa (estafa procesal) son engañados que disponen sobre un patrimonio ajeno.")
P("El requisito es que el engañado-disponente tenga una **relación** con el patrimonio perjudicado que le permita disponer de él (facultad jurídica o, al menos, una posición fáctica de cercanía, según la tesis que se adopte). Si cualquier tercero sin ninguna vinculación con el bien es engañado para que lo entregue, el caso se acerca más a una autoría mediata de hurto.")
H2("3.5. Cuarto elemento: el perjuicio")
P("El perjuicio es la **disminución del valor económico** del patrimonio de la víctima, comparando su estado antes y después de la disposición. Debe ser **efectivo, real y apreciable en dinero**: la mera puesta en peligro del patrimonio no alcanza para la consumación.")
BUL(["**Compensación.** Si la víctima recibe a cambio una contraprestación de valor equivalente, en principio no hay perjuicio. Sin embargo, la jurisprudencia y la doctrina admiten perjuicio cuando lo recibido **no sirve al fin** para el cual se contrató (la llamada frustración del fin): por ejemplo, quien compra un tractor «nuevo» y recibe uno reacondicionado de igual precio de mercado.",
     "**Reparación posterior.** Devolver lo obtenido después de consumado el delito **no borra la estafa**. Puede incidir en la pena (art. 41 CP), habilitar la suspensión del juicio a prueba o la extinción por reparación integral (art. 59 inc. 6), pero no hace desaparecer el perjuicio ya causado.",
     "**Monto.** La ley no fija un mínimo. Una estafa de bajo monto es típica (el caso del taxi por $61 lo demuestra), aunque puede justificar soluciones alternativas como la conciliación, los criterios de oportunidad o la pena mínima."])
H2("3.6. Tipo subjetivo")
P("La estafa es un delito **doloso**. El autor debe conocer la falsedad de lo que afirma o simula y querer que la víctima, engañada, disponga en su perjuicio. La doctrina mayoritaria exige **dolo directo**, por la propia estructura de la figura: quien usa un ardid para obtener una entrega persigue ese resultado.")
P("El texto argentino, a diferencia del español, no menciona expresamente el «ánimo de lucro». Para un sector de la doctrina ese ánimo está implícito en la idea de defraudar; para otro, basta el dolo de perjudicar. En la práctica la discusión tiene poca relevancia, porque el lucro casi siempre está presente.")
H3("El momento del dolo: dolo inicial y dolo posterior")
P("El dolo debe estar presente **en el momento del engaño**, antes o al tiempo de la disposición patrimonial. Este es el criterio que separa la estafa del simple incumplimiento contractual.")
FIG(10, "Estafa contractual frente a incumplimiento civil.")
EJ("Ejemplo: el constructor que no termina la obra",
   "Un constructor cobra el 50 % de una obra y la abandona a mitad de camino. **Si al contratar tenía intención de cumplir** y luego se fundió, se enfermó o decidió no seguir, hay incumplimiento contractual (responsabilidad civil, arts. 1716 y ss. CCyC), no estafa: el dolo, si existe, es posterior (*dolo subsequens*). **Si en cambio usó una identidad falsa, cobró anticipos a diez clientes en el mismo mes y desapareció**, esos indicios permiten inferir que nunca quiso construir: el contrato fue el ardid y hay estafa (*dolo in contrahendo*).")
TIP("Indicios útiles para probar el **dolo inicial**: uso de identidades o domicilios falsos; inexistencia de la empresa o del bien ofrecido; pluralidad de víctimas con la misma mecánica; desaparición inmediata tras cobrar; falta absoluta de actos de ejecución; transferencia inmediata de los fondos a terceros; antecedentes por hechos similares.")
H2("3.7. Consumación y tentativa")
FIG(9, "Consumación y tentativa.")
P("La estafa se **consuma** cuando se produce el perjuicio patrimonial, que normalmente coincide con la disposición. No hace falta que el autor obtenga efectivamente el beneficio: si la víctima transfirió el dinero a una cuenta que el banco bloqueó antes de que el autor lo retirara, el perjuicio ya se produjo y el delito está consumado.")
P("Hay **tentativa** (art. 42 CP) desde que el autor comienza a desplegar el ardid frente a la víctima y hasta antes del perjuicio. La pena se reduce de un tercio a la mitad (art. 44). Los actos preparatorios (comprar un chip, diseñar un sitio falso) son impunes, salvo que constituyan delitos autónomos, como la falsificación de documentos o el acceso ilegítimo a un sistema (art. 153 bis).")
P("Si el ardid era absolutamente inidóneo, se discute si hay **tentativa inidónea** (delito imposible, art. 44, último párrafo: pena atenuada o exención) o directamente atipicidad.")
H2("3.8. La estafa procesal")
FIG(11, "La estafa procesal.")
P("La estafa procesal es una modalidad de estafa triangular. Una de las partes de un juicio, mediante ardid (documentos falsos, testigos preparados, pericias fraguadas), induce a error al juez y obtiene una resolución que perjudica patrimonialmente a la contraparte. El juez es el **engañado** y la **sentencia** funciona como la **disposición patrimonial** sobre el patrimonio ajeno.")
P("Los puntos más discutidos son:")
BUL(["**Idoneidad.** Se exige un ardid y no basta la simple afirmación falsa contenida en la demanda, porque el proceso ya prevé mecanismos de contradicción y prueba. Por eso la jurisprudencia es estricta con la idoneidad del engaño procesal.",
     "**Tentativa.** Según una reseña de la jurisprudencia de la Cámara Federal de Casación Penal, la tentativa se configura con la presentación engañosa dirigida al juez. Se consuma con la resolución que produce el perjuicio (por ejemplo, la orden de lanzamiento o la transferencia de fondos embargados).",
     "**Concurso** con el uso de documento falso (art. 296) y con el falso testimonio (art. 275)."])
JUR("Tribunal de Casación Penal de la Provincia de Buenos Aires, Sala IV, «P., J. L.», 28/07/2020",
    "Los imputados presentaron documentación para justificar una posesión inexistente, denunciaron una falsa usurpación invocando ser apoderados del propietario de unas tierras y lograron que el juez ordenara un lanzamiento. El tribunal lo calificó como estafa procesal: una estafa en triángulo en la que el destinatario de la maniobra engañosa es el juez.",
    "Microjuris Al Día Argentina, 24/08/2020.")
JUR("Cámara Federal de Casación Penal (tentativa de estafa procesal; recibo falso)",
    "En un juicio de daños se presentó un recibo que la pericia caligráfica determinó falso. El tribunal absolvió por considerar que, en las circunstancias del caso, el engaño no era idóneo para inducir a error al juez.",
    "Colegio de Abogados de Morón, «Tentativa de estafa procesal: no era un “engaño idóneo”».")
JUR("Cámara Federal de Casación Penal, Sala IV, «Alenda Masutti» (2017) y «Mohabed» (2014)",
    "Precedentes sobre la estafa procesal analizados por la doctrina. En «Alenda Masutti» se discutió si la obtención de una medida cautelar sobre la base de una presentación engañosa desvirtúa la inidoneidad del engaño. En «Mohabed» se analizó el aporte de pruebas falsas al proceso.",
    "«El delito de estafa procesal y sus problemas concursales según la jurisprudencia», revista *Pensar en Derecho* n.º 13, Facultad de Derecho (UBA).")
H2("3.9. Problemas especiales")
H3("a) Estafa en negocios ilícitos")
P("¿Comete estafa quien vende «cocaína» que en realidad es harina, o quien cobra por un «arreglo» ilegal que nunca hará? Una posición niega la estafa, porque la víctima perseguía un fin ilícito y su patrimonio, en esa medida, no merece protección (concepción jurídico-económica del patrimonio). Otra afirma la estafa, porque el dinero entregado sí pertenecía legítimamente a la víctima y el engaño lo hizo salir de su patrimonio. El Código resolvió expresamente uno de estos supuestos en el art. 173 inc. 10 (defraudar «con pretexto de supuesta remuneración a los jueces u otros empleados públicos»), lo que indica que el legislador no consideró impune a quien engaña a una víctima que también obraba ilícitamente.")
H3("b) Estafa y falsificación de documentos")
P("Cuando el ardid consiste en usar un documento falso (un DNI, un poder, una escritura), concurren la estafa y la falsificación o el uso de documento falso (arts. 292 y 296). La doctrina y la jurisprudencia están divididas entre el **concurso ideal** (art. 54: un solo hecho que encuadra en ambas figuras, se aplica la pena mayor) y el **concurso real** (art. 55: hechos independientes, se suman las escalas con límites), según se considere que la falsificación y el uso integran o no una misma conducta. Si la falsificación se realizó en un momento distinto y luego se usó el documento, es más frecuente la solución del concurso real entre falsificación y estafa, con el uso absorbido.")
H3("c) Pluralidad de víctimas y de hechos")
P("Cada víctima engañada configura, en principio, un **hecho independiente** (concurso real, art. 55). Por eso, en las estafas masivas (esquemas piramidales, ventas falsas en redes sociales) las escalas penales resultantes pueden ser altas, y es habitual que concurran con **asociación ilícita** (art. 210). Un ejemplo es la causa «Generación Zoe», en la que un tribunal de Goya (Corrientes) condenó en febrero de 2025 a su líder como jefe de una asociación ilícita y coautor de 98 estafas (fuente: Chequeado e Infobae, febrero de 2025).")
H2("3.10. Ejemplos para la conferencia")
EJ("1. El falso escribano (estafa clásica con puesta en escena)",
   "Una pareja busca comprar su primera casa. Un supuesto vendedor les muestra el inmueble, les presenta a un «escribano» con oficina, sello y matrícula y les hace firmar un boleto contra la entrega de USD 20.000 de seña. Todo era falso. Hay **nombre supuesto, falsos títulos y ardid**: estafa consumada al entregar la seña (art. 172), en concurso con falsificación si se usaron documentos públicos adulterados.")
EJ("2. El cuento del tío telefónico",
   "Una mujer de 82 años recibe un llamado de su «nieto» llorando por un accidente; luego habla un «policía» que le pide dinero para evitar su detención y le manda a un «cadete» a buscarlo. Es el ejemplo de manual de la **idoneidad valorada en concreto**: la edad de la víctima, la urgencia y la puesta en escena con varios actores hacen típico un engaño que a otra persona quizás no la habría convencido.")
EJ("3. El inversor de redes sociales",
   "Un «trader» muestra en Instagram autos, viajes y capturas de ganancias y ofrece un 10 % mensual garantizado. Las primeras rentas se pagan con el dinero de los nuevos inversores. Hay **apariencia de empresa y negociación**: estafa reiterada (una por cada víctima), posiblemente asociación ilícita y, si capta fondos del público sin autorización, intermediación financiera no autorizada (art. 310 CP).")
EJ("4. No es estafa: el deudor que no paga",
   "Ana le presta $500.000 a su amigo Bruno, que le firma un pagaré. Bruno pierde su trabajo y no paga. No hubo engaño al pedir el préstamo: Bruno quería devolverlo. Es un incumplimiento que se resuelve en sede civil (juicio ejecutivo). **El derecho penal no es un medio de cobro**: denunciar penalmente para presionar el pago puede volverse en contra del acreedor.")
RES("**Resumen del capítulo.** La estafa (art. 172, prisión de 1 mes a 6 años) es una **cadena causal**: ardid o engaño, error, disposición patrimonial y perjuicio. Los medios que enumera la ley son ejemplos y la cláusula «cualquier otro ardid o engaño» los amplía. La idoneidad del engaño se evalúa hoy en concreto, considerando la vulnerabilidad de la víctima y, según la tesis de la imputación objetiva, sus deberes de autoprotección (CSJN, «Selman», 2020). El silencio solo engaña si había deber de informar. El dolo debe existir **al contratar**: el dolo posterior es incumplimiento civil. Se consuma con el perjuicio, admite tentativa y presenta modalidades especiales como la estafa triangular y la estafa procesal.")
