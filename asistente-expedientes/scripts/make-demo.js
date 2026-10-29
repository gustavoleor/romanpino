'use strict';
// Crea un expediente de ejemplo 100% FICTICIO (juicio laboral) para probar la aplicación.
//   node scripts/make-demo.js [carpeta-destino]
const fs = require('node:fs');
const path = require('node:path');
const { makePdf } = require('./makePdf');

function makeDemo(dest) {
  fs.mkdirSync(dest, { recursive: true });

  fs.writeFileSync(path.join(dest, '01-demanda.txt'), `DEMANDA — EXPEDIENTE FICTICIO "PEREZ, JUAN C/ ALFA S.R.L. - ORDINARIO - DESPIDO" (material de ejemplo)

I. OBJETO. Juan Pérez, por derecho propio, promueve demanda contra Alfa S.R.L. por la suma de $4.850.000 en concepto de indemnización por despido sin causa, preaviso, integración del mes de despido y diferencias salariales.

II. HECHOS. El actor ingresó a trabajar para la demandada el 1 de marzo de 2018 como operario de depósito, con jornada de lunes a viernes de 8 a 17 horas. Percibía una remuneración mensual de $320.000.

El día 15 de marzo de 2023 la empresa comunicó verbalmente al actor su despido sin expresión de causa, impidiéndole el ingreso a su lugar de trabajo. El actor intimó fehacientemente por telegrama el 17 de marzo de 2023 a que se aclare su situación laboral, sin obtener respuesta.

Durante la relación laboral el actor sufrió el 12 de septiembre de 2022 un accidente en el depósito que le provocó una lesión lumbar, por la cual estuvo con licencia médica durante 30 días.

III. PRUEBA. Se ofrece: documental (recibos de sueldo, telegrama del 17/03/2023), testimonial (Sres. Carlos Gómez y Lucía Ferrer), pericial médica sobre la incapacidad derivada de la lesión lumbar.
`);

  fs.writeFileSync(path.join(dest, '02-contestacion.txt'), `CONTESTACIÓN DE DEMANDA — ALFA S.R.L. (material ficticio)

I. NEGATIVAS. Se niegan los hechos expuestos en la demanda, salvo los expresamente reconocidos.

II. HECHOS. Se reconoce que el actor trabajó para la empresa como operario de depósito. Se niega que el ingreso haya sido el 1 de marzo de 2018; el actor ingresó el 1 de septiembre de 2019, según consta en el alta ante AFIP.

Se niega el despido. El 10 de marzo de 2023 el actor dejó de concurrir a su puesto sin aviso y se lo intimó a retomar tareas por carta documento del 14 de marzo de 2023, la que no fue respondida, configurándose abandono de trabajo. La remuneración era de $290.000 mensuales.

Se niega que el actor haya sufrido accidente alguno en el establecimiento; no existe denuncia de siniestro ante la ART.

III. PRUEBA. Documental: legajo del actor, alta de AFIP, carta documento del 14/03/2023. Testimonial: Sr. Roberto Díaz (encargado de depósito).
`);

  fs.writeFileSync(path.join(dest, '03-acta-testimonial.txt'), `ACTA DE AUDIENCIA — PRUEBA TESTIMONIAL (ficticia)

Testigo Carlos Gómez (propuesto por la actora), compañero de trabajo. Preguntado por el despido, dijo: "Yo vi que el 15 de marzo el gerente le dijo a Juan que no volviera más". Preguntado por la fecha de ingreso, dijo: "Juan estaba cuando yo entré en 2019". Preguntado por el accidente, dijo: "Se lastimó la espalda levantando cajas en septiembre del año pasado".

Testigo Roberto Díaz (propuesto por la demandada), encargado de depósito. Preguntado por la asistencia del actor, dijo: "Juan faltó desde el 10 de marzo, no volvió". Preguntado por el accidente, dijo: "Yo no recuerdo que haya habido ningún accidente ese año". Preguntado por la fecha de ingreso, dijo: "El ingreso de Pérez fue a fines de 2019, más o menos".
`);

  fs.writeFileSync(
    path.join(dest, '04-pericia-medica.pdf'),
    makePdf([
      'PERICIA MEDICA (documento ficticio)\nPerito: Dr. Martín Sosa — Expediente "Pérez c/ Alfa S.R.L."\n\nI. OBJETO DE LA PERICIA\nDeterminar el estado de salud del actor y la existencia de incapacidad derivada de la lesión lumbar denunciada.',
      'II. ANTECEDENTES\nEl actor refiere un episodio lumbar en septiembre de 2022 mientras cargaba mercadería. Presenta historia clínica del Sanatorio Norte con diagnóstico de lumbalgia aguda del 13 de septiembre de 2022.',
      'III. EXAMEN FISICO\nA la inspección se constata limitación funcional leve de la columna lumbar, contractura paravertebral y Lasegue negativo. Resonancia magnética aportada: protrusión discal L4-L5 sin compromiso radicular.',
      'IV. CONCLUSIONES\nEl actor presenta una incapacidad parcial y permanente del 12% de la total obrera, por limitación funcional de columna lumbar. El perito aclara que no puede determinar el nexo causal con las tareas habituales, por existir patología degenerativa previa.',
    ])
  );

  fs.writeFileSync(path.join(dest, '05-resolucion.txt'), `AUTO INTERLOCUTORIO (ficticio)

Córdoba, 2 de octubre de 2025. Visto: el escrito de contestación de demanda. Se corre traslado a la actora por el término de cinco (5) días para que se expida sobre la documental acompañada por la demandada. Notifíquese.

Fdo.: Juez (ficticio)
`);
  return dest;
}

if (require.main === module) {
  const dest = path.resolve(process.argv[2] || path.join(__dirname, '..', 'ejemplo-expediente'));
  makeDemo(dest);
  console.log('Expediente de ejemplo creado en', dest);
}
module.exports = { makeDemo };
