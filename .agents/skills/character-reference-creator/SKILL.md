---
name: character-reference-creator
description: "Crea una identidad visual canónica en inglés y referencias de personaje a partir de texto, renders, bocetos o imágenes, junto con una skill *-style obligatoria. Incluye validación del personaje, elección entre tres candidatas y nueve vistas PNG transparentes con manifiesto por estilo. Úsala al crear o continuar estas bibliotecas; no para ilustraciones aisladas."
---

# Character Reference Creator

Separar identidad, atuendo y representación artística. Las instrucciones y preguntas se comunican en español; el prompt canónico y los prompts ejecutados se escriben en inglés. Guardar los resultados bajo `characters/` en la raíz del proyecto activo.

## 0. Comprobar requisitos y recuperar el estado

- Exigir una skill disponible cuyo nombre termine en `-style`, elegida por el usuario o ya confirmada en el contexto de este personaje. Leerla y aplicar sus referencias y reglas pertinentes. Si falta, detener el flujo y pedir cuál debe acompañar a esta skill. Una imagen de estilo por sí sola no la sustituye. No elegir otra skill por semejanza del nombre.
- Exigir un personaje identificable y referencias mínimas de su identidad y atuendo inicial. Se admite texto suficiente como única fuente, además de renders ingame, bocetos, fotografías o ilustraciones. Pedir las referencias si faltan; no exigir imágenes cuando el texto sea suficiente.
- Revisar el `CHARACTER.md`, los manifiestos y las aprobaciones existentes antes de generar nada. Usar los identificadores y rutas existentes. Un archivo o una imagen heredados no están aprobados solo por existir.
- Abrir las imágenes locales antes de describirlas o usarlas como referencia. Asignar a cada fuente un ID y su función: identidad, atuendo, accesorio o estilo. Comparar las fuentes; no resolver contradicciones por cuenta propia.
- Si falta información necesaria para alguna vista, incluso sobre espalda, lados, manos o accesorios, **parar y preguntar**: enumerar los huecos y ofrecer que el usuario los complete o autorice que la skill proponga cómo rellenarlos. Avanzar únicamente en lo que no dependa de esa respuesta. No interpretar el silencio como autorización.
- La autorización para rellenar huecos permite proponer solo esos detalles. Documentarlos como propuestas, diferenciados de lo observado, y someterlos a la validación del paso 1 antes de generar. Si aparecen nuevos huecos más adelante, volver a esta pausa.

La identidad aprobada rige anatomía y diseño; la skill de estilo rige representación. Las exigencias de este flujo —vistas de referencia, encuadres y transparencia— prevalecen sobre valores predeterminados de escena como fondo o formato panorámico. Si una regla obligatoria del estilo impide respetar la identidad o producir las referencias, explicar el conflicto y pedir una decisión.

## 1. Escribir y validar `CHARACTER.md`

Leer [el formato del personaje](references/character-document.md) al crear o modificar el documento. Usar `characters/<character_id>/CHARACTER.md` y conservar las secciones existentes que sigan siendo válidas.

Redactar un prompt detallado en inglés que describa identidad y atuendos sin introducir estilo artístico: proporciones, rostro, piel, ojos, cabello, silueta, materiales, colores, marcas y disposición de piezas. Identificar izquierda y derecha anatómicas. Registrar también límites de adaptación, fuentes, propuestas y cuestiones pendientes. No deducir canon por conocimiento genérico de un juego.

Guardar como borrador y presentar el archivo enlazado, las propuestas y las dudas. **Pedir al usuario que valide el documento y detenerse antes de generar imágenes.** Registrar la aprobación real con su alcance, revisión del documento y evidencia del mensaje; no autovalidar el prompt. Reutilizar una revisión ya aprobada si sigue intacta y cubre el atuendo solicitado. Las revisiones de identidad o diseño de atuendo requieren nueva validación; añadir enlaces o estado de estilo no cambia la revisión de identidad.

## 2. Generar exactamente tres candidatas y solicitar elección

Leer [el contrato de archivos y manifiesto](references/manifest.md) antes de escribir el primer manifiesto. Crearlo al iniciar el trabajo del estilo y actualizarlo después de cada resultado o respuesta del usuario.

Con el documento validado, cargar la skill `imagegen` disponible y usar la herramienta integrada de imágenes por defecto. Si no está disponible, informar y detener la generación; no sustituir proveedor o modo sin autorización. Esta skill no genera imágenes durante su propia creación o edición.

Generar **tres imágenes independientes**, una por llamada, del mismo personaje y atuendo en **plano medio frontal**, de cintura hacia arriba, a la altura de los ojos, expresión neutra y pose comparable. Solicitar fondo transparente desde estas candidatas para poder reutilizar la elegida sin regenerarla. Mantener encuadre, luz y canon constantes.

Las tres son interpretaciones del mismo diseño dentro de la misma skill de estilo: pueden variar el tratamiento gráfico y la simplificación permitidos por ella; no cambiar anatomía, colores de identidad, peinado, atuendo ni accesorios. Si el estilo deja poco margen, producir tres tomas independientes sin forzar diferencias de diseño. Los detalles abiertos ya deben estar resueltos en el paso 1.

Construir cada prompt con bloques separados: identidad canónica, atuendo, funciones de los adjuntos, reglas del estilo, encuadre y restricciones. Adjuntar las imágenes reales que se vayan a usar; escribir una ruta en el prompt no las adjunta. Las referencias artísticas solo aportan representación, nunca la identidad de los personajes que aparezcan en ellas.

Guardar las tres imágenes y sus prompts completos. Mostrarlas como **1, 2 y 3**, con sus rutas, y **pedir que el usuario elija una; detenerse**. No elegir por él ni inferir selección por una valoración ambigua. Si no elige ninguna, recoger los cambios pedidos; no generar rondas adicionales automáticamente.

Revisar antes de mostrarlas que respeten identidad, estilo, encuadre y transparencia. Señalar los defectos que impidan usar alguna como ancla y consultar su corrección; no promover una candidata defectuosa a referencia canónica. Una corrección que cambie la candidata elegida requiere confirmar de nuevo la elección antes de continuar.

Registrar la elección y copiar, sin alterar píxeles, la candidata seleccionada al archivo final `..._midshot.png`. Ese archivo es el ancla visual de este estilo y atuendo. Conservar también las candidatas no elegidas en el manifiesto.

## 3. Completar las nueve vistas independientes

El conjunto base incluye el plano medio elegido y **ocho generaciones adicionales**:

| Etiqueta de archivo / `view` | Vista |
|---|---|
| `midshot` | Plano medio frontal elegido |
| `fullbody_front` | Cuerpo entero frontal |
| `fullbody_profile` | Cuerpo entero de perfil |
| `fullbody_back` | Cuerpo entero de espaldas |
| `fullbody_three_quarter` | Cuerpo entero a tres cuartos |
| `head_front` | Cabeza y hombros frontal |
| `head_profile` | Cabeza y hombros de perfil |
| `head_three_quarter` | Cabeza y hombros a tres cuartos |
| `head_back` | Cabeza y hombros de espaldas |

Producir una vista por PNG con transparencia real, sin paneles múltiples, rótulos, fondos pintados, cuadrículas de transparencia dibujadas ni suelo. Usar pose neutra, A-pose suave para el cuerpo entero, personaje completo sin recortes accidentales y margen suficiente. Mantener escala, proporciones y altura de cámara comparables dentro de cada familia de planos. La iluminación debe revelar el diseño con claridad y respetar el tratamiento del estilo, sin convertir sombras en marcas permanentes.

Como convención de cámara, mostrar el lado izquierdo anatómico en perfiles y tres cuartos, y registrarlo. Una asimetría esencial en el otro lado puede requerir una vista adicional identificada como detalle; documentar la necesidad antes de añadirla. La convención de cámara no autoriza inventar rasgos ocultos.

Para cada nueva generación usar el texto canónico, la candidata elegida y las fuentes originales pertinentes. Añadir vistas ya revisadas solo como apoyo. No derivar cada imagen exclusivamente de la anterior. Mantener la identidad facial al cambiar de atuendo; una sheet aprobada de otro estilo puede aportar identidad, nunca sustituir las fuentes del estilo solicitado.

Guardar cada salida y su prompt inmediatamente en el directorio del estilo. Registrar toda imagen generada, incluidas las rechazadas y las sustituidas. Si falla una llamada, registrar el fallo y las vistas pendientes sin inventar archivos. Si se detecta deriva, señalar el defecto concreto y corregir esa vista; tras dos correcciones fallidas de una misma vista, parar y consultar antes de otra ronda.

En futuros atuendos, conservar la identidad aprobada y añadir el ID de atuendo al nombre de archivo según el contrato. Las referencias faciales compatibles pueden reutilizarse mediante copias explícitas y trazables; completar las nueve vistas del conjunto solicitado sin repetir generaciones innecesarias. Validar primero cualquier nuevo diseño de atuendo.

## 4. Revisar, aprobar y enlazar el estilo

Verificar los archivos con el comprobador de solo lectura de esta skill (Python 3 y Pillow):

```powershell
python <skill_dir>/scripts/check_assets.py <style_dir>/manifest.json --outfit base --complete
```

El comprobador revisa rutas, archivos PNG, transparencia y vistas obligatorias; no decide la identidad ni la aprobación artística. Inspeccionar además las imágenes: rostro, silueta, proporciones, colores, asimetrías, número y posición de piezas, correspondencia entre ángulos y fidelidad al estilo. Revisar visualmente los bordes sobre un visor con transparencia; tener canal alfa no demuestra que el recorte sea correcto. Si la transparencia falla, corregirla con la herramienta de imágenes conservando la identidad, sin sustituirla por un fondo plano.

Mostrar las nueve vistas enlazadas y separadas, con cualquier incidencia, y **pedir la aprobación final de la sheet; detenerse**. Mantener `awaiting_sheet_review` hasta una respuesta explícita. Una aprobación parcial solo aprueba las imágenes indicadas. Corregir únicamente las vistas solicitadas, conservar el historial y volver a presentar el conjunto afectado. Solo marcar el conjunto como `approved` cuando todas sus vistas obligatorias hayan sido aprobadas por el usuario y las comprobaciones hayan pasado.

Crear o actualizar en `CHARACTER.md` una sección por estilo que enlace su `manifest.json` y liste los atuendos y su estado. Ese índice reúne todos los estilos; cada manifiesto lista las imágenes de su propio estilo. Mantener el índice también durante el trabajo pendiente para poder reanudarlo. Entregar los enlaces a `CHARACTER.md`, al manifiesto y a las imágenes aprobadas.

## Reanudar sin perder aprobaciones

Leer primero `CHARACTER.md` y el manifiesto correspondiente; retomar la etapa registrada sin repetir validaciones, elecciones o generaciones ya resueltas. Si cambian rasgos canónicos, incrementar la revisión de identidad y señalar qué conjuntos quedan desactualizados: las imágenes de una revisión previa no prueban la nueva. La elección del ancla y la aprobación final deben corresponder a la revisión y al atuendo vigentes. Conservar el historial y los archivos anteriores, sin reemplazar versiones aprobadas silenciosamente.
