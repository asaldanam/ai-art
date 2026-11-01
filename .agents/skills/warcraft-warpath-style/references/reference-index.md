# Selección de referencias

## Rutas y autoridad

Las imágenes originales están en `references/warpath/` respecto a la carpeta raíz de esta skill. Desde este archivo están en `warpath/`. Se mantienen dentro de la skill, sin renombrar ni normalizar los originales.

**DO:** resolver las rutas respecto al archivo que contiene el enlace y abrir las imágenes reales. Comprobar lectura antes de prometer fidelidad. **DON’T:** suponer que el generador recibe una imagen por mencionar su nombre o ruta en el prompt. Sólo cuenta como referencia visual cuando el archivo está efectivamente adjunto o cargado en la herramienta.

**DO:** usar los nombres para encontrar archivos; las fichas del atlas describen lo visible. **DON’T:** usar etiquetas de clase, raza o acción como evidencia visual concluyente. Las identidades definitivas se fijarán con el usuario.

## Ruta rápida por necesidad

| Necesidad | Abrir primero | Complementar con | Atlas |
|---|---|---|---|
| Línea, cara y armadura con lectura clara | 003, 007, 010 | 006 para perfil; 005 para masas robustas | [001–014](atlas-001-014.md) |
| Nieve y exterior frío | 001–002 | 003 para cara en ambiente frío | [001–014](atlas-001-014.md) |
| Campo cálido, primer término suave | 004 | 005 para acción en la misma familia | [001–014](atlas-001-014.md) |
| Montaña, perspectiva atmosférica | 007–008 | 009 para protagonista en sombra | [001–014](atlas-001-014.md) |
| Selva y luz filtrada | 011–013 | 014 para escala y haces en dosel | [001–014](atlas-001-014.md) |
| Noche contenida | 006, 026 | 030 para figura pequeña en oscuridad | [001–014](atlas-001-014.md), [015–029](atlas-015-029.md), [030–043](atlas-030-043.md) |
| Grupo nocturno, amenaza | 019 | 014, 024 para marcos y escala | [015–029](atlas-015-029.md) |
| Magia cian / electricidad | 015–016 | 035 para luz sobre cabello y acero | [015–029](atlas-015-029.md), [030–043](atlas-030-043.md) |
| Fuego y acción | 017–018, 029 | 028 para escala y trayectoria | [015–029](atlas-015-029.md) |
| Arcano azul violeta | 020–021 | 015 para superposición geométrica | [015–029](atlas-015-029.md) |
| Magenta ascendente | 022–024 | 023 para arma y manos | [015–029](atlas-015-029.md) |
| Fogata y descanso | 025 | 026 para reacción oscura | [015–029](atlas-015-029.md) |
| Luz roja / retroceso | 027 | 043 para perfil expresivo, no para copiar fondo | [015–029](atlas-015-029.md), [030–043](atlas-030-043.md) |
| Luz sagrada, escala del efecto | 030–033 | 034 para esfuerzo cercano; 015 para otro color | [030–043](atlas-030-043.md), [015–029](atlas-015-029.md) |
| Luz sagrada en manos y rostro | 037–040 | 041 para columnas y grupos | [030–043](atlas-030-043.md) |
| Reacción con polvo cálido | 036 | 042 para luz rosada sobre tonos azules | [030–043](atlas-030-043.md) |
| Perfil de máxima intensidad | 043 | Ficha aprobada del personaje | [030–043](atlas-030-043.md) |

## Cómo formar el conjunto de entrada

**DO:** asignar una función concreta a cada archivo: `STYLE` (dibujo y acabado), `IDENTITY` (personaje), `LIGHT` (tratamiento de luz), `SHOT` (composición), `CONTINUITY` (último fotograma aprobado). Una imagen puede tener dos funciones si se explican. Priorizar las referencias necesarias para la escena dentro del límite real de la herramienta; no cargar las 43 por defecto.

**DON’T:** mezclar 004, 016, 024 y 043 como cuatro estilos equivalentes sin explicar qué tomar de cada una; ese conjunto empuja hacia una media cromática contradictoria. No pedir copiar el personaje de una captura usada sólo como `LIGHT`.

Ejemplo de asignación —no representa archivos ya adjuntos—:

| Orden de entrada | Rol | Qué tomar | Qué no trasladar |
|---|---|---|---|
| 1 · ficha aprobada del personaje solicitado | IDENTITY | Rostro, proporciones, equipo y colores base. | Pose neutra de la ficha, si la nueva escena pide otra. |
| 2 · 007 | STYLE | Línea, simplificación facial, cel shading y relación figura/fondo. | Identidad del guerrero y luz cálida de montaña. |
| 3 · 025 | LIGHT | Contraste entre fuego cálido y noche fría; caída del foco. | Grupo, posición de cámara o bosque concreto si no se solicitan. |

**DO:** pasar esta asignación al generador usando los números reales de adjunto; si cambia el orden, actualizar el texto. **DON’T:** confiar en nombres internos que la herramienta no muestra o afirmar que una referencia de texto sustituye una imagen ausente.

## Referencias complementarias y vídeo

Las 43 capturas bastan para una biblia de estilo estático. El vídeo aporta información adicional cuando el trabajo depende de orden de acciones, movimiento de cámara, continuidad del equipo, oscilación de exposición o distinción entre dibujo de un fotograma y artefacto de reproducción.

**DO:** solicitar el vídeo sólo para resolver una duda concreta; examinar fotogramas anteriores y posteriores al acontecimiento pertinente y registrar sus tiempos cuando el archivo permita verificarlos. Todo fotograma extraído, miniatura o recorte debe permanecer dentro de la raíz `Warcraft anime`.

**DON’T:** inferir duración, velocidad o secuencia exacta a partir de una sola captura. No exigir el vídeo para redactar prompts estáticos que las referencias ya permiten resolver. Nuevos fotogramas son evidencia adicional, no una sustitución automática de las decisiones ya aprobadas.

## Acabado confirmado y vídeo

**DO:** usar el [acabado A aceptado](finish-calibration.md) como calibración de grano y suavidad; consultar las [observaciones del vídeo](video-observations.md) para evidencia complementaria. **DON'T:** generar más variantes para ratificar una elección ya aceptada.
