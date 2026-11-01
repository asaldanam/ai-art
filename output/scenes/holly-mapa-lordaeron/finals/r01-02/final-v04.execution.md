# Acabado v04: ejecución híbrida autorizada

Este PNG no procede de una nueva generación completa. El usuario autorizó expresamente «Sí, montaje exacto y retoque del rostro» después de dos intentos generativos que conservaron un cabezal incorrecto.

1. Base conservada: `final-v03.png`, surgida del boceto 2 seleccionado. Su prompt completo e informe están al lado de este archivo.
2. Única generación localizada: `v04-face/face-v01.png`, 1254 × 1254. Se usó la herramienta integrada OpenAI con tres entradas reales: recorte facial de v03 ampliado, retrato aprobado de Holly y referencia Warpath 003-A. El prompt exacto ejecutado está en `v04-face/face-v01.prompt.txt`; el paquete y el informe registran roles y opciones. El modelo efectivo no se expone. No hubo reintento de este componente.
3. Edición directa no generativa: `../../scripts/compose_scene_v04.py` reutiliza el cabezal original aprobado como objeto rígido con escala uniforme, rotación y traslación; conserva cuatro lados, cuatro terminales y cuatro gemas pequeñas. Aplica sólo integración de alfa/color de noche, reconstrucción local del cielo detrás del cabezal viejo y montaje del labio mediante máscara pequeña. El resto del recorte facial generado no se usa.
4. Resultado: `final-v04.png`, 1942 × 809. El archivo es una copia byte-idéntica del montaje revisado `../../work/v04/montage-v01.png`. Parámetros y huellas están en `../../work/v04/montage-v01.json`; máscaras y ampliaciones de revisión se conservan en esa carpeta.

Revisión del coordinador: composición y contactos del boceto 2, geometría del cabezal, labios, ausencia de guías de construcción, uniones y formato comprobados visualmente. Comparación de píxeles: todos los píxeles fuera de las áreas autorizadas de cabezal/cielo inmediato y boca son idénticos a v03. Se conservan los contornos de dibujo y la textura pictórica intencionales. La pequeña sombra cel bajo el labio es sombreado terminado.

Estado: entregado y revisado por el agente; el usuario no ha aprobado artísticamente esta versión todavía. La autorización del método no se registra como aprobación del resultado. Todos los intentos previos se conservan.
