# Holly leyendo el mapa ante Lordaeron

- ID: `holly-mapa-lordaeron`; revisión estructural: **1**.
- Estado: **entregado y revisado por el agente**, versión activa **v04**. Aprobación artística del usuario: no registrada.
- Resultado: [final-v04.png](finals/r01-02/final-v04.png), **1942 × 809**, proporción **2,40049:1**, PNG opaco.
- Selección compositiva real del usuario: **«Boceto 2»**, archivo [r01-02 v01](sketches/r01-02/sketch-v01.png).
- Solicitud: Holly Willhelm leyendo un mapa con las ruinas de Lordaeron de fondo, usando `scene-creator` y `warcraft-warpath-style`.
- Base del proyecto al iniciar: `81400f35a7ab86a19c384aaa4c33df09b9d60a9c`. Los tres borrados locales preexistentes de la biblioteca no forman parte de esta tarea.

## Decisiones vigentes

1. Noche seca y cielo verdoso de la primera captura.
2. Bastón azul de la ficha vigente, guardado contra la espalda.
3. Exploración de cámara en tres bocetos con lectura mediante ambas manos, ruinas reconocibles al fondo y panorámico aproximadamente 2,4:1. Mapa, camino, árboles, estandartes y luz proceden de las capturas.
4. Selección inequívoca del **boceto 2**; su encuadre, cámara, pose, escala, contactos y masas principales rigen el acabado.
5. Correcciones solicitadas: «Corrige el cabezal, el labio se ve raro y se aprecian las marcas de boceto todavía».
6. Método final expresamente autorizado: **«Sí, montaje exacto y retoque del rostro»**. La autorización del método no se interpreta como aprobación artística del resultado.

## Instante, personajes y contactos

Una sola figura: Holly, detenida y concentrada en un mapa de pergamino abierto con dos extremos enrollados. Cada mano sujeta un extremo diferente; los antebrazos se conectan de forma coherente con codos y hombros. El mapa ocupa la parte baja del pecho y se inclina hacia ella. Cabeza y mirada bajan hacia el pergamino. El reverso marrón visible no lleva texto ni guías cartográficas fantasma. No hay combate ni otros personajes.

Holly conserva [identidad canónica revisión 1](../../../characters/holly_willhelm/CHARACTER.md) y el equipo complementario `base_blue_staff`, revisión 2, con [vistas aprobadas](../../../characters/holly_willhelm/warcraft-warpath-style/manifest.json). La acción solicitada sustituye las manos vacías de la pose neutra de biblioteca por el agarre del mapa.

Morfología: adulta delgada, cintura relativamente estrecha, cuello alargado, rostro ovalado estrecho, piel muy pálida intacta, ojos amarillos contenidos y bob corto ciruela con raya central. Manos pálidas esbeltas, cinco dedos intactos y uñas oscuras puntiagudas; la oclusión del agarre impide contar todos los dedos por separado. Túnica larga de torso ajustado y mangas anchas con puños claros. No se introduce calzado; los pies quedan fuera del recorte seleccionado.

El bastón rígido queda detrás del cuerpo, con cabezal sobre el hombro izquierdo anatómico y extremo inferior hacia la cadera/muslo derecho. La vara se une a una esquina del marco. El cabezal original de cuatro lados, cuatro terminales y cuatro gemas pequeñas alrededor del cristal central se ha reutilizado mediante montaje exacto, sin rediseñar su geometría.

## Entorno, escala y profundidad

Holly y mapa ocupan el primer plano izquierdo. Calzada y postes con estandartes se reducen hacia la entrada de las ruinas, al centro-derecha del fondo. Se mantienen torre rectangular de acceso, puerta en arco, murallas de piedra, torres laterales, coronamientos deteriorados, árboles altos de ramas desnudas, coníferas y terreno irregular de las referencias. La arquitectura se interpreta como fondo pintado por capas, con contraste reducido en la distancia.

Los apoyos inferiores están fuera de campo; la pose conserva un eje corporal de pie y equilibrado. Mapa y manos se separan del torso de forma legible. El contacto exacto del bastón con la espalda queda mayormente ocluido, sin hueco visible añadido.

## Cámara, encuadre, luz y estilo

Se conserva el plano de tres cuartos frontal del boceto 2, con recorte por la parte alta de la túnica inferior, cabeza inclinada, brazos doblados y mapa entre ambas manos. No se amplía el lienzo para mostrar pies ni se recentra a Holly. La entrada, camino, vegetación y estandartes mantienen sus masas principales y escala relativa.

Noche seca de cielo verde apagado, ambiente tenue amplio y pequeños focos locales existentes en la entrada. El pergamino y el bastón no se convierten en emisores. Se conservan la palidez de Holly, cabello ciruela, ojos amarillos y equipo azul bajo esta luz. Sin luna, lluvia, nieve ni efectos añadidos.

Representación Warpath: dibujo angular, contornos oscuros selectivos, sombras cel en masas amplias y fondo pictórico por capas. Acabado A sutil con grano fino y suavidad ligera. Se han eliminado las guías de construcción, el rayado exploratorio de la figura y las líneas fantasma del pergamino; permanecen los contornos intencionales y la pincelada del fondo.

## Fuentes y roles

- [Captura de acción](sources/scene-action.jpg): acción, mapa, lugar y ambiente seco; se ignoran bastón rojo y render de juego.
- [Captura de arquitectura](sources/lordaeron-architecture.jpg): puerta, camino, murallas, árboles y estandartes; se ignora su lluvia.
- `boceto-3.png` de `scene-creator`: sólo nivel de construcción, compartido en las tres ejecuciones iniciales.
- Fichas aprobadas de Holly: retrato para identidad/labios y vista equipada de tres cuartos para túnica/equipo.
- Bastón aislado aprobado de tres cuartos: geometría original reutilizada directamente en v04.
- Referencias Warpath 003-A, 006 y 019: dibujo/acabado, exposición nocturna y profundidad pintada. Los paquetes e informes distinguen referencias consultadas de adjuntos realmente enviados.
- Las dos entradas externas fueron copiadas byte-idénticamente y se conservan dentro del proyecto. Fuentes y huellas: [manifest.json](manifest.json).

## Generador, intentos y método final

Proveedor generativo: **OpenAI**, herramienta integrada `image_gen.imagegen`. Modelo efectivo **no expuesto**, sin selector. Restricciones en prosa dentro del prompt; fondo opaco. La herramienta reveló durante ejecución un máximo de cinco adjuntos, no anunciado en su esquema visible.

Tres trabajadores independientes con contexto vacío ejecutaron el mismo prompt estructural y las mismas tres imágenes en orden. Los tres bocetos son 1942 × 809; sus composiciones resultaron parecidas y el entorno fue más detallado que el nivel esquemático solicitado. Se conservaron y revisaron antes de la selección real.

- v01 de acabado: rechazo técnico por ocho adjuntos; no produjo imagen.
- v02: acabado desde cinco referencias, con cabezal incorrecto.
- v03: corrección adicional autorizada de cabezal, labios y marcas; conservó el cabezal incorrecto y mejoró parcialmente la limpieza.
- **v04 activa**: montaje no generativo del cabezal original más un único retoque generativo localizado de labios, integrado mediante una máscara pequeña. No se regeneró la escena completa. Parámetros, máscaras, recortes e intentos anteriores permanecen archivados.

Guías oficiales consultadas el 2026-11-01: [generación de imágenes](https://developers.openai.com/api/docs/guides/image-generation) y [prompts de imagen](https://developers.openai.com/api/docs/guides/image-prompting). Se aplicaron roles por entrada, contactos explícitos y restricciones de conservación; las capacidades efectivas proceden del esquema y errores observados de la herramienta.

## Revisión y continuación

Resultado activo revisado a tamaño nativo, cabezal ampliado 4× y rostro 6×. Se comprobaron geometría del bastón, unión, labios, limpieza, composición, contactos, formato y ausencia de interfaz. La sombra pequeña bajo el labio es una masa cel intencional. Comparación de píxeles: **todos los píxeles fuera de las zonas autorizadas de cabezal/cielo inmediato y boca son idénticos a v03**.

No hay preguntas pendientes ni más generaciones programadas. La entrega no implica aprobación artística del usuario ni modifica el canon del personaje. Para continuar, partir de v04 y conservar los compromisos de la selección 2 salvo nueva instrucción.

- [Resultado activo](finals/r01-02/final-v04.png).
- [Ejecución híbrida y prompts reales](finals/r01-02/final-v04.execution.md).
- [Informe técnico y visual](finals/r01-02/result-v04.json).
- [Script reproducible](scripts/compose_scene_v04.py).
- [Parámetros y huellas del montaje](work/v04/montage-v01.json).
