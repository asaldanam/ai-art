# Continuidad, preguntas y revisión

## 1. Acordar identidad antes de consolidarla

**DO:** crear una ficha por personaje sólo con datos aprobados y referencias vistas. Distinguir invariantes de variantes autorizadas y elementos aún desconocidos. **DON'T:** convertir una sombra, perspectiva o diferencia entre capturas en una nueva versión del personaje sin preguntar.

| Ficha | DO · registrar | DON'T · asumir |
|---|---|---|
| Identidad | Nombre/ID, especie, edad aparente y referencias autorizadas. | Que el nombre de archivo pruebe clase, género o parentesco. |
| Proporciones | Altura relativa al grupo, silueta, tamaño de manos/pies, cuello y torso. | Un cuerpo humano estándar para todas las especies. |
| Cara | Vistas frontal, tres cuartos y perfil; mandíbula, nariz, cejas, ojos, orejas, colmillos y marcas. | Un perfil preciso a partir de una cara frontal oculta. |
| Pelo/pelaje | Color base, grandes masas, línea de nacimiento, mechones y longitud. | Que un reflejo cian o rosa cambie el color de diseño. |
| Equipo | Placas, grosor, motivos, cierres y asimetrías; ropa visible entre piezas. | Filigrana nueva, hombreras intercambiadas o símbolos duplicados. |
| Armas y objetos | Forma, escala respecto al cuerpo, agarre y mano de uso cuando esté fijada. | Que cualquier espada, martillo o báculo de la misma clase sea intercambiable. |
| Anatomía | Conteo y forma de dedos conforme al diseño y especie. | Cinco dedos universales o correcciones que humanicen al personaje. |
| Variantes | Daños, equipo alternativo, peinados o estados mágicos aprobados. | Que el agente pueda crear nuevas variantes durante una corrección. |

La ficha de identidad manda sobre el diseño de otra persona que aparezca en una referencia `LIGHT`. La biblia de estilo manda sobre una foto o render de identidad en lo relativo al acabado, conservando los rasgos del personaje. Si esas dos fuentes no pueden conciliarse con precisión, preguntar por el detalle conflictivo.

## 2. Preguntas que sí cambian una escena

**DO:** preguntar de forma concreta, referenciando la discrepancia o decisión. Ejemplos:

- «La vista frontal muestra dos colmillos y la lateral parece ocultar uno. ¿Conservamos ambos y tratamos el segundo como ocluido?»
- «La cara aparece muy oscura en 026. ¿Buscas esa exposición contenida o la luz más visible del grupo en 025?»
- «¿La espada emite cian y tiñe el pelo como en 035, o debe ser una hoja sin emisión?»
- «¿El proyectil está acercándose, esquivándose o pasando de largo? La captura 028 no fija ese instante por sí sola.»
- «¿La referencia de personaje fija también el equipo, o sólo rostro y proporciones?»

**DO:** consultar también decisiones visuales secundarias si no están documentadas, agrupando las preguntas. **DON'T:** volver a preguntar datos aprobados ni generar primero una alternativa canónica para luego solicitar aprobación. Avanzar sólo en lo independiente y documentado mientras se espera una respuesta necesaria.

## 3. Registrar cada escena aprobada

**DO:** conservar un registro pequeño y útil junto al resultado, dentro del proyecto, con estos datos:

```text
ID de escena y versión.
Estado: propuesta / pendiente de corrección / aprobada por el usuario.
Acción, cámara y condiciones de luz.
IDs y versiones de fichas usadas.
Archivos de referencia realmente adjuntos y rol de cada uno.
Prompt exacto y restricciones enviadas.
GPT director y generador efectivos si se exponen; en caso contrario, indicar que no se expone su identificador, sin bloquear.
Parámetros efectivos relevantes y ruta del resultado.
Continuidad: mano que porta cada arma, daño de equipo, orientación y cambios autorizados.
Desviaciones conocidas y decisión expresa del usuario sobre ellas.
```

**DON'T:** marcar «aprobada» porque el agente crea que se ve bien, inventar metadatos del servicio o tomar una salida no aprobada como nueva referencia canónica. El resultado anterior complementa las fichas originales; no las sustituye.

## 4. Rúbrica de revisión visual

Comparar simultáneamente resultado y referencias relevantes. Marcar cada dimensión como **coincide**, **aproximada**, **desvía** o **no evaluable** y aportar una observación concreta. No usar una nota global que esconda errores críticos de identidad.

| Dimensión | DO · qué comprobar | DON'T · aprobar por |
|---|---|---|
| Dibujo | Línea limpia, formas angulares, detalle facial selectivo. | Que la imagen simplemente parezca «anime». |
| Sombreado | Pocas masas claras, bordes cel definidos en personajes; excepciones de halo/atmósfera localizadas. | Que tenga mucho contraste o se vea «pulida». |
| Identidad | Silueta, rasgos, proporciones y motivos del equipo aprobados; sin rasgos importados de LIGHT. | Parecido general de color o misma especie. |
| Luz | Fuente, dirección, alcance y áreas oscuras coherentes con el tratamiento elegido. | Añadir brillo para esconder una lectura pobre. |
| Materiales | Metal y cabello simplificados, piel limpia sin cera ni modelado continuo. | Mayor realismo o más textura. |
| Fondo | Pincelada agrupada y profundidad atmosférica, contraste bien distribuido. | Nivel de detalle extremo. |
| Plano | Acción y emoción, dirección de mirada, recortes y relación de escala. | Una pose atractiva que no cuenta el instante pedido. |
| Efecto | Silueta, emisor, trayectoria, núcleo y halo; interacciones con las superficies. | Nube brillante vistosa sin función espacial. |
| Integridad | Manos/arma/anatomía conforme al diseño, oclusiones coherentes y sin interfaz. | Que los fallos estén escondidos en brillos o vegetación. |

**DO:** exigir corrección de una deriva clara de identidad, estilo o acción antes de recomendar la imagen como fiel. Si una dimensión no puede evaluarse por falta de referencia, indicarlo y solicitar la evidencia pertinente. **DON'T:** garantizar uniformidad perfecta entre generaciones ni disfrazar un fallo como «variación artística».

## 5. Calibración cerrada y pruebas futuras opcionales

Se generaron nueve recreaciones de 003, 007 y 025, variando sólo el acabado solicitado. El usuario acepta la primera variante y pide terminar sin más variantes: ver [calibración](finish-calibration.md). La tabla siguiente conserva ideas de pruebas futuras, únicamente para una solicitud nueva; ninguna es necesaria para cerrar o utilizar la skill.

| Prueba | Referencias | Qué debe resistir |
|---|---|---|
| Exterior frío sin magia | 001–003 | Cel shading, metal mate, ambiente azul sin aura añadida. |
| Interior de selva | 011–013 | Identidad bajo sombras verdes y luz filtrada; fondo por capas. |
| Reacción tranquila junto al fuego | 025–026 | Noche contenida, emoción pequeña, fuente cálida de alcance local. |
| Primer plano con luz cian | 016 o 035 | Geometría del rostro y pelo bajo contraste extremo. |
| Gran plano de entorno | 008 o 014 | Jerarquía de detalle y escala, sin convertirse en paisaje fotográfico. |
| Magia de gran escala | 031–034 | Forma del efecto, blanco local y sombras legibles alrededor. |

**DO:** empezar con las pruebas que resuelvan las dudas reales del usuario. Para investigar el bloque negativo, mantener el mismo conjunto de referencias, prompt positivo, modelo y parámetros observables; comparar con/sin la restricción específica. Sin control de semilla o determinismo, anotar que una sola pareja no demuestra causalidad ni eficacia universal.

**DON'T:** generar más variantes o una batería porque exista esta tabla. La elección A valida el acabado en composiciones de control; no demuestra consistencia en cualquier personaje o acción futura.

## 6. Cuándo corregir y cuándo parar

**DO:** corregir una desviación concreta y volver a comparar. Si reaparece el mismo problema sin mejora, faltan referencias críticas o la solución exige rediseñar algo aprobado, mostrar el fallo y pedir la decisión necesaria antes de continuar la secuencia. **DON'T:** acumular reintentos ciegos, sustituir de motor para ocultar el problema o ampliar la cantidad de imágenes solicitada sin una razón acordada.
