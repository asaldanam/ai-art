# Acabado aceptado · variante 1 / A

El 2026-11-01 el usuario indicó: «Termina de crear la skill sin necesidad de más variantes. Me vale con la variante 1 de ambos casos».

Se adopta la primera variante **A / sutil** como referencia de acabado. Las dos vistas del guerrero permiten compararla en luz fría y luz cálida:

| Caso | Control original | Primera variante guardada |
|---|---|---|
| 003 · defensa en ambiente frío | [003](warpath/003_human-warrior-defending-stance.png) | [003-A](calibration/003-A.png) |
| 007 · exploración con luz cálida | [007](warpath/007_human-warrior-scouting-mountain-pass.png) | [007-A](calibration/007-A.png) |

La tanda también produjo variantes de 025. No se atribuye a ese caso una aprobación individual que el último mensaje no identifica. La petición de terminar cierra la calibración: no exige otra elección ni más imágenes. Las 43 capturas mantienen su autoridad visual.

## DO / DON'T · aplicar el acabado

| DO | DON'T |
|---|---|
| Conservar grano de luminancia muy fino y apenas visible, bordes ligeramente suaves y pequeñas irregularidades de dibujo. | Grano grueso de película, ruido cromático fuerte, pixelado artificial o aspecto de papel rugoso. |
| Mantener las formas angulares y las masas de sombra cel definidas bajo la suavidad de captura. | Aplicar desenfoque general hasta borrar rasgos, dedos, contornos o límites de sombra. |
| Usar un acabado algo más contenido que el de las variantes medias, sin eliminar la textura. | Volver a una línea vectorial cortante o a un render pulido/plástico. |
| Mantener atmósfera y desenfoque de profundidad según la escena original. | Igualar profundidad atmosférica y suavidad superficial como si fueran un único filtro. |
| Usar estas imágenes para acabado; tomar identidad, equipo, pose y escena de las referencias asignadas a esos papeles. | Copiar al guerrero en una escena de otro personaje porque 003-A o 007-A sean el ejemplo de textura. |
| Excluir carga, cursor, reproducción, subtítulos y demás interfaz. | Replicar el indicador de 024 como una imperfección estética. |

## Bloque de acabado para prompts futuros

```text
Use the approved subtle captured-animation finish: very fine, barely visible
luminance grain, gently softened dark contours and small drawing irregularities.
Preserve the angular drawing and broad, sharply shaped cel shadows underneath.
Keep facial features and silhouettes readable. Match the approved A references;
do not make the image vector-sharp, glossy or heavily denoised, and do not add
coarse grain, smeared outlines, playback controls or loading indicators.
```

No pedir recrear toda la imagen cuando el usuario solicite una escena nueva. Para editar una imagen existente, indicar explícitamente qué cambia y qué permanece.

## Ejecución y alcance

Se ejecutaron nueve solicitudes independientes: 003, 007 y 025, con variantes A/B/C de acabado. Se guardan aquí los dos ejemplos A relevantes a la elección y sus prompts exactos. [Registro de la tanda](calibration/run.json).

Estas pruebas evalúan el acabado conservando una composición de control; no son una prueba completa de consistencia de personajes en poses y acciones nuevas. No se alteraron las capturas originales. No hay más pruebas pendientes para terminar la skill.
