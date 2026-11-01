# Prompts, DO/DON’T y prevención de deriva

## Qué está documentado y qué es una propuesta de proyecto

**DO:** consultar [fuentes y límites de evidencia](sources.md). La documentación de Google aconseja describir con precisión el resultado y formular exclusiones también como una composición positiva. OpenAI explica cómo asignar funciones a referencias y separar cambios de restricciones. Son técnicas documentadas; no prueban que una frase elimine automáticamente el «AI slop».

**DON’T:** presentar los bloques siguientes como un prompt universal validado en modelos actuales. Son propuestas originales derivadas de las capturas, pendientes de prueba visual en el generador elegido. Resultados de estudios sobre difusión no demuestran eficacia en GPT Image o Nano Banana.

## Traducir «AI slop» a criterios observables

| Deriva a evitar · DON’T | Sustitución verificable · DO |
|---|---|
| Acabado 3D plástico con línea negra superpuesta. | Personajes dibujados con color base y pocas sombras de bordes nítidos; luces por planos. |
| Piel encerada, brillos cosméticos y ojos de muñeca. | Superficies limpias sin poros, ojos del tamaño y forma de la ficha, expresión construida con párpados y cejas. |
| Todo hiperdetallado, cada superficie con filigrana. | Silueta y placas grandes primero; detalle reservado a rasgos identificadores y punto narrativo. |
| Cabello como infinidad de fibras brillantes. | Mechones grandes y sombras agrupadas; reflejos que siguen formas dibujadas. |
| Fuego, luz sagrada y electricidad como la misma nube brillante. | Forma específica por efecto, emisor y trayectoria legibles, núcleo/halo separados. |
| Contraluz de neón permanente, polvo dorado y exceso de destellos. | Fuentes justificadas por escena y efectos de alcance local; oscuridad y espacios tranquilos deliberados. |
| Póster simétrico de personajes mirando a cámara. | Encuadre que sirva a una acción concreta, miradas, apoyos y oclusiones. |
| Fondo fotográfico pegado al dibujo o nitidez idéntica en todas las distancias. | Fondo pintado por masas y profundidad atmosférica; primer término, acción y distancia diferenciados. |
| Mezcla indiferenciada de estilos de anime, render de juego e ilustración promocional. | Línea angular, proporciones del proyecto, cel shading y fondos pictóricos tomados de referencias con roles explícitos. |
| Rasgos o equipo que cambian entre escenas. | Ficha canónica y última imagen aprobada como entradas reales de identidad y continuidad. |

**DON’T:** llenar el prompt de «masterpiece», «best quality», «8K», «ultra detailed», «trending», «award-winning», nombres de motores 3D o calificativos parecidos. No son pruebas de calidad y no describen este estilo. Tampoco basta escribir «no AI slop» o «no generic anime»: hay que especificar qué se verá.

## DO · Preparar un brief antes del prompt

Registrar sólo lo que cambie decisiones:

```text
ACCIÓN: instante concreto, propósito narrativo y emoción.
PERSONAJES: identificadores de fichas aprobadas, número y relación espacial.
LUGAR: geografía visible y elementos necesarios.
PLANO: tamaño de plano, altura/ángulo de cámara, dirección de mirada y recortes.
PROFUNDIDAD: primer término, plano narrativo, fondo; qué queda suave u oculto.
LUZ: ambiente + fuente dominante + dirección + dureza + alcance + sombras.
ESTILO: rasgos de la biblia que deben ser visibles en este plano.
REFERENCIAS: orden real de adjuntos, rol y qué debe/no debe copiarse de cada uno.
CONTINUIDAD: elementos invariables y cambios autorizados respecto al plano anterior.
ENTREGA: proporción, cantidad, y si se pide prompt o imagen ejecutada.
```

**DON’T:** enviar al generador toda la biblia o el atlas. Seleccionar lo relevante, resolver contradicciones y redactar un prompt coherente. La documentación extensa sirve al director; el generador necesita instrucciones concretas para la escena presente.

## Bloque positivo de estilo · base para adaptar

```text
Create a frame from the same 2D fantasy animation as the supplied STYLE references.
Match their angular character drawing, restrained facial detail, dark clean contours,
large readable silhouettes and broad armor plates. Shade characters with flat base
colors and a small number of sharply defined shadow shapes. Build hair in large
drawn locks. Render the environment as a layered painted background, with grouped
brush textures and reduced contrast in the distance. Keep the contrast between
simply shaded characters and the more painterly environment. Use scene-motivated
light with clearly placed flat highlights and shadows. Preserve quiet, low-detail
areas and a single narrative focus. Match the approved subtle A capture finish: very fine, barely visible luminance
grain, gently softened contours and small drawing irregularities, while preserving
clear cel-shadow shapes. Do not add detail or polish beyond the approved finish.
```

**DO:** incluir sólo las frases pertinentes. En un plano detalle sin paisaje no se debe inventar un fondo pintado complejo para cumplir este bloque. Sustituir referencias genéricas por los adjuntos reales y concretar acción, cámara y luz a continuación.

## Prompt negativo principal · lenguaje natural

Para la herramienta de imágenes de OpenAI, que es el flujo confirmado, usar un bloque de restricciones dentro del prompt. No inventar un parámetro `negative_prompt` cuando el contrato de la herramienta no lo tenga.

```text
DO NOT introduce photorealistic skin, pores, waxy facial rendering, glossy plastic
surfaces, 3D or game-render material shading, smooth airbrushed modeling across
every surface, mirror-chrome armor, or individually rendered hair strands. Do not
replace the reference character design with oversized doll-like eyes, chibi
proportions, a generic idealized face, cosmetic blush or decorative eye sparkles.
Do not add ornamental armor details, gems, straps, runes, particles, rim lights or
lens flares that are absent from the design or unmotivated by the scene. Do not
make every background layer equally sharp or equally detailed. Do not turn this
into a promotional poster, a symmetrical lineup, or a different anime aesthetic.
Preserve the specified identity, outfit, anatomy and equipment. Exclude loading
indicators, playback controls, UI, captions and unrequested text.
```

**DO:** acortar este bloque a los riesgos reales del plano y escribir la alternativa positiva correspondiente. Para una acción con ojos emisivos, mantenerlos si la ficha los exige; para una escena con una estrella de luz sagrada, conservarla aunque se excluyan destellos de lente decorativos.

**DON’T:** tratar el bloque como una lista infalible, repetirlo varias veces, o prohibir un rasgo que una referencia y la escena requieren. Evitar listas interminables de defectos anatómicos que no fijan el diseño deseado.

## Versión breve para un campo negativo real

Sólo si el modelo o interfaz documenta un campo negativo independiente; su eficacia debe comprobarse allí. Esta versión no usa sintaxis de pesos, embeddings ni flags de otro motor.

```text
photorealistic skin, waxy faces, glossy plastic, 3D game-render shading,
airbrushed character volumes, mirror-chrome armor, individual hair strands,
oversized doll eyes, chibi proportions, generic idealized faces, cosmetic blush,
gratuitous armor filigree, arbitrary runes, unmotivated rim lighting,
uniformly sharp backgrounds, ornamental particle clutter, promotional poster
composition, loading indicators, playback UI, captions, unrequested text
```

**DON’T:** copiar `--no`, `(bad anatomy:1.4)`, `EasyNegative`, CFG, samplers o seeds de guías de Stable Diffusion/Midjourney a una interfaz que no los soporte. «Semilla fija» tampoco es una garantía de identidad entre solicitudes.

## Negativos condicionales y sus excepciones

| Caso | DO · restricción específica | DON’T · prohibición indiscriminada |
|---|---|---|
| 004, trigo próximo suave | Mantener rostro y acción definidos; reservar suavidad al primer término y distancia. | `no blur`, `everything tack sharp`. |
| 008, valle | Reducir contraste con distancia y conservar grandes formas geográficas. | `no haze`, `no soft background`. |
| 016, 034–035, luz extrema | Mantener sombras faciales geométricas y claros localizados. | `no harsh shadows`, `no flat shading`. |
| 018, 032–033, pico mágico | Conservar forma del efecto y sombras alrededor del núcleo blanco. | `no glow`, `no bloom`, `no overexposure` sin matiz. |
| 006, 026, 030, noche | Conservar ojos o silueta legibles dentro de valores bajos. | `no darkness`, `bright evenly lit face`. |
| 030–032, espacio vacío | Mantener vacío narrativo y único foco luminoso. | `no empty background`, `fill all negative space`. |
| 027, 029, acción | Conservar escorzo, recortes y tela dinámica con anatomía coherente. | `no asymmetry`, `no cropped limbs`. |
| 043, fondo gestual | Preservar dirección del grito y estrías si se pide ese tratamiento. | `no speed lines` como regla universal. |

## Plantilla de prompt final

Comunicar con el usuario en español. Los ejemplos en inglés son una plantilla, no una afirmación de superioridad del idioma. Mantener el idioma que el usuario prefiera o que admita el flujo concreto.

```text
REFERENCE ROLES
Input 1 — IDENTITY: [actual approved character reference]. Preserve [specific invariants].
Input 2 — STYLE: [actual Warpath capture]. Match [drawing and rendering traits].
Input 3 — LIGHT or SHOT: [actual capture]. Use only [specific visual treatment].
Do not copy its character identity, location or pose unless explicitly requested below.

SCENE
[One precise action, characters, relationship, place and intended emotion.]

FRAMING AND DEPTH
[Shot size, camera angle and height, subject placement, gaze direction, foreground,
midground, background, deliberate occlusions and apparent scale.]

LIGHT AND SHADOW
[Ambient hue and level; visible or motivated emitter; direction, hardness and reach;
specific hard shadow shapes; where the highest values occur and where shadows remain.]

RENDERING
[Relevant positive style block, adapted to this shot.]

CONTINUITY AND CONSTRAINTS
[Identity, clothing, equipment, anatomy and changes explicitly allowed.]
[Short scene-specific negative block with positive alternatives.]

OUTPUT
[Requested aspect ratio, count, and any confirmed format constraints.]
```

No entregar esta plantilla con corchetes vacíos como si fuese un prompt terminado. Si falta un dato crítico, preguntar por él; los ejemplos siguientes son deliberadamente demostrativos y no generan un personaje canónico.

## Ejemplo A · Reacción junto a una fogata, sin magia añadida

Referencias de estilo/luz: 003 para dibujo, 025 para situación cálido/frío y 026 para contención de exposición. Adjuntar además la ficha real del personaje solicitado. No usar la identidad del guerrero como sustituto si la escena pide otro personaje.

**DO · núcleo de escena:**

```text
A restrained reaction shot beside a small night campfire. Frame the approved
character from the upper chest upward, looking just off-camera with slightly tense
eyebrows and parted lips. Keep the face mostly in muted, low-value reddish shadow,
with a modest warm accent on the lower planes facing the fire. Deep blue-violet
forest shapes sit softly behind the head. Use the reference's clean angular
contours and flat facial shadow shapes. Preserve the dark exposure and quiet mood.
```

**DON’T · corrección:**

```text
Do not turn the fire into a studio key light, brighten the whole face, add magical
particles or a glowing weapon, or exaggerate the expression into a scream.
```

## Ejemplo B · Primer plano con hoja cian

Usar ficha de identidad + 035 para la distribución de luz + 003/007 si hay que estabilizar proporciones faciales. La espada sólo se incluye si pertenece al equipo autorizado.

**DO · núcleo de luz:**

```text
The blade behind the shoulder emits white-cyan light. Place broad, sharply cut
cyan highlights on the hair locks and armor edges facing the blade, while leaving
the opposite planes in deep blue-black shadow. Keep the approved facial geometry
and small, focused eyes. The illumination changes the visible colors but not the
character's base hair color, outfit or identity.
```

**DON’T · corrección:**

```text
Do not recolor the entire hairstyle cyan, add continuous neon outlines around the
whole silhouette, or soften the face with glossy 3D shading.
```

## Ejemplo C · Gran plano de valle

Usar 008 como `STYLE+SHOT`, 007 sólo si se necesita enlazar una figura con el desfiladero. Aceptar personajes muy pequeños o ausentes según la solicitud.

**DO · núcleo de entorno:**

```text
A broad painted mountain valley seen between dark near cliffs. A winding river
leads toward pale lavender distant ridges. Build rock in broad irregular painted
facets, group vegetation into readable masses, and reduce contrast and saturation
with distance. Keep any travelers tiny enough to establish scale. Preserve large
quiet areas of sky and valley rather than adding detail everywhere.
```

**DON’T · corrección:**

```text
Do not use a photographic landscape, 3D terrain materials, equally sharp distant
foliage, or enlarge the travelers into foreground portraits.
```

## Corrección tras una primera salida

**DO:** comparar con los adjuntos, identificar una desviación visible y pedir un cambio localizado conservando lo que pasó la revisión. Ejemplo: «Mantén encuadre, identidad y paleta; reemplaza el modelado suave de la cara por tres masas de sombra definidas como en la referencia 016».

**DON’T:** repetir «menos AI slop» como única corrección o añadir veinte negativas nuevas sin diagnosticar el fallo. Si una corrección cambia el equipo o el rostro, volver a la referencia aprobada en vez de seguir acumulando deriva sobre derivados.
