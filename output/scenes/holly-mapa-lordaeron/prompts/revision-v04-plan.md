# Propuesta v04: montaje exacto y retoque localizado

Estado: **preparada, no ejecutada; requiere indicación del usuario**. La revisión generativa v03 mantiene cinco gemas y un cabezal poligonal. La boca y los trazos han mejorado parcialmente, sin resolver satisfactoriamente todos los defectos solicitados.

## Resultado propuesto

Conservar como base `finals/r01-02/final-v03.png`, su composición y todo lo que funciona. No regenerar la escena completa.

1. Sustituir el cabezal defectuoso por el **cabezal original exacto** de `characters/holly_willhelm/warcraft-warpath-style/holly_willhelm-base_blue_staff_three_quarter.png`, mediante edición directa no generativa. Recortar de forma no destructiva el cabezal y su unión, conservar el alfa y transformar el conjunto como objeto rígido con escala uniforme, rotación y traslación. Mantener cuatro lados, cuatro terminales, cuatro gemas pequeñas y el cristal central. Integrar la luz de noche sin redibujar la geometría. Retirar el cabezal anterior y reconstruir sólo el cielo inmediato, conservando la vara y el resto de píxeles de la escena.
2. Corregir labios y trazos de construcción persistentes del rostro sobre un **recorte localizado** de la cara de v03, usando el retrato aprobado y acabado Warpath. Reintegrar el recorte conservando la posición, tamaño, inclinación, tono y contorno del rostro. No cambiar mirada, identidad, peinado, cuello ni pose. Un intento generativo focalizado si el usuario autoriza esta parte; sin reintentos automáticos.
3. Revisar el montaje a tamaño nativo y ampliado: número exacto de elementos del bastón, unión a esquina, continuidad con vara, integración del cielo, labio sin forma de gancho y ausencia de guías de boceto en las regiones retocadas. Comparar píxeles fuera de regiones autorizadas para confirmar que el resto no se ha alterado.

## Entradas existentes, sin resultados nuevos todavía

- Base: `finals/r01-02/final-v03.png`, 1942 × 809, SHA-256 `6738b361b5aecd8928de83336fb50824805df6ca8396b90eb0314227aebbd01f`.
- Cabezal original: `characters/holly_willhelm/warcraft-warpath-style/holly_willhelm-base_blue_staff_three_quarter.png` (base de ruta: raíz del proyecto).
- Rostro aprobado: `characters/holly_willhelm/warcraft-warpath-style/holly_willhelm_midshot.png` (raíz del proyecto).
- Acabado: `.agents/skills/warcraft-warpath-style/references/calibration/003-A.png` (raíz del proyecto).

El cambio de generación completa a montaje/edición directa no se ejecutará sin la indicación expresa del usuario. Se conservarán todos los originales, recortes, instrucciones y resultados dentro de esta escena. No se afirma que esta propuesta ya haya producido una imagen.
