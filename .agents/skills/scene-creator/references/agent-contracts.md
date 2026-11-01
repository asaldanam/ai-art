# Contexto y entregas de los subagentes

Leer antes de despachar bocetos o acabados. El coordinador prepara prompts, asigna archivos, revisa resultados y mantiene el estado. Los trabajadores ejecutan una rama cada uno y no escriben el manifiesto compartido.

## Aislamiento

- Crear agentes nuevos sin heredar la conversación (`fork_turns="none"` cuando se exponga). No basta con pedir que ignoren bocetos que ya están en su contexto.
- Dar rutas absolutas de los recursos autorizados. No pedir que recorran otras carpetas de escena para descubrir referencias. Los agentes comparten filesystem: el aislamiento depende también de qué rutas se les autoriza leer.
- Cada agente escribe en una carpeta exclusiva de su rama. No modifica fuentes, fichas, skills, otros resultados ni registro central. No hace commit ni push; el coordinador cumple las instrucciones del proyecto al finalizar la tarea.
- Si la plataforma no permite aislar el contexto o delegar, informar y pedir alternativa. No sustituirlo silenciosamente por llamadas del coordinador. Si solo falta capacidad simultánea, escalonar los agentes; independencia no exige concurrencia.
- No usar el parámetro de modelo del subagente para intentar seleccionar el modelo de imagen. El proveedor y sus controles se transmiten en la configuración de ejecución; no inventar opciones de la herramienta.

## Paquete de boceto

Todos reciben lo mismo, salvo `branch_id` y `output_dir`:

```text
Tarea: ejecutar una sola generación del boceto asignado.
Prompt: archivo con el texto exacto; transmitirlo sin reformular.
Negativo: texto/campo o ausencia, según la configuración resuelta.
Entradas: imágenes estructurales o ejemplo de boceto, con índice y función.
Configuración: proveedor, modelo/política, herramienta, opciones expuestas,
formato y guía oficial aplicable; instrucciones de ejecución pertinentes.
Contexto auxiliar: especificación estructural, morfología mínima,
restricciones y libertades comunes. No añadir este contexto al prompt.
Salida: branch_id y output_dir exclusivos.
```

No incluir las fichas artísticas completas ni los ejemplos de arte final en este paquete. Si una referencia original es imprescindible para una morfología inusual, el coordinador debe decidir cómo aportar esa información sin convertir el boceto en acabado y registrar el rol de esa entrada; cualquier adjunto estructural elegido debe ser el mismo para los tres trabajadores. No añadir referencias por iniciativa individual.

Pedir que guarden inmediatamente la imagen original devuelta y el prompt realmente enviado; informen del ID de agente, herramienta/modelo observado, opciones efectivas, adjuntos reales, rutas, limitaciones y fallos. Si aparece una duda bloqueante, que la devuelvan al coordinador antes de generar. No autoaprobar, rediseñar ni reintentar por cuenta propia.

El coordinador compara los tres textos/configuraciones iniciales con el paquete congelado. Una desviación de ejecución se registra; no se presenta como una interpretación del mismo prompt.

## Paquete de acabado

Una selección por trabajador nuevo. Proporcionar:

1. Especificación de escena y compromisos compositivos vigentes, extraídos por el coordinador, sin enlaces a otros bocetos.
2. Prompt final completo, negativo si aplica, generador y configuración resueltos.
3. **Solo el boceto que debe desarrollar**, identificado como ancla estructural.
4. Skill `*-style`, documentos y referencias visuales pertinentes, con rutas y funciones explícitas.
5. Descripciones canónicas y referencias de todos los personajes presentes, revisiones y atuendos. Elegir vistas que cubran las partes que aparecerán.
6. Carpeta exclusiva y contrato de devolución como el del boceto.

No entregar el `manifest.json` central o un `SCENE.md` que enlace otros bocetos: pasar extractos suficientes. No transmitir la historia de propuestas descartadas. Si un documento fuente contiene resultados de otras ramas, extraer la parte pertinente sin alterar el original.

Adjuntar imágenes reales mediante los mecanismos soportados. No usar automáticamente «las últimas imágenes del chat», porque podrían incluir otras propuestas; preferir rutas explícitas cuando la herramienta las admita. Inspeccionar cada archivo local antes de usarlo. Mantener el contexto limitado a esa rama también en las correcciones.

## Correcciones y coordinación

El trabajador ejecuta inicialmente una generación. Solo el coordinador autoriza el intento de corrección tras revisar un defecto concreto. El máximo automático es uno por boceto y uno por acabado, en la ronda o versión seleccionada actual; los fallos de herramienta también consumen ese intento automático si se reintenta. No reiniciar el contador creando otro agente o versión. Rondas adicionales requieren petición o autorización explícita del usuario.

Una corrección conserva la versión anterior y añade un archivo y prompt nuevos. Cuando sea apropiado para la herramienta, puede adjuntar su resultado defectuoso como objetivo de edición además de las referencias de esa rama, dejando explícito qué cambiar y qué preservar. No incorporar bocetos ajenos. Una corrección estructural del boceto necesita confirmación de selección antes de pasar al acabado.

Si una rama falla, recoger sus errores sin inventar rutas y continuar lo independiente. El coordinador conserva las demás ramas y comunica el progreso real; no repite todas las generaciones para corregir una sola.
