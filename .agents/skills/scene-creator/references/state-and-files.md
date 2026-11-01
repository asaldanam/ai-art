# Especificación, archivos y estado de una escena

Leer al iniciar o reanudar una escena. Resolver la salida desde la raíz del proyecto activo, no desde esta skill. Usar `output/scenes/<scene_id>/` por defecto o la ubicación indicada por el usuario. Reutilizar IDs existentes y crear un ID descriptivo sin colisiones para una nueva escena.

## Archivos

```text
output/scenes/<scene_id>/
  SCENE.md
  manifest.json
  sources/                         copias necesarias de entradas externas
  prompts/
    sketch-r01.txt                 prompt base exacto compartido
  sketches/
    r01-01/
      sketch-v01.png
      sketch-v01.prompt.txt
      result-v01.json
      sketch-v02.png               solo si hubo corrección
      sketch-v02.prompt.txt
      result-v02.json
    r01-02/...
    r01-03/...
  finals/
    r01-01/
      final-v01.png
      final-v01.prompt.txt
      result-v01.json
```

Las extensiones de imagen reflejan el formato real; preferir PNG si está soportado y es apropiado. Nunca renombrar JPEG a PNG para aparentar conversión. No exigir transparencia a escenas ni generar collages. Las rutas de ejemplo no autorizan crear archivos que aún no existen. Usar nuevos sufijos para versiones y rondas; no sobrescribir.

Copiar las entradas externas que deban persistir, especialmente adjuntos temporales; preservar sus bytes y registrar procedencia y función. Para fichas y recursos estables del proyecto se pueden registrar rutas relativas sin duplicar bibliotecas. Guardar la revisión o huella utilizada para detectar cambios. Si el estilo impone una ubicación más restrictiva, respetarla. No mover ni borrar los originales del usuario.

## SCENE.md

Mantener una única especificación legible, con:

- ID y revisión de escena, solicitud y fuentes.
- Instante, acción, entorno, personajes/atuendos, morfología y escala.
- Relaciones espaciales, apoyos, contactos y elementos visibles importantes.
- Cámara, encuadre, formato y libertades de exploración.
- Restricciones fijas, aportaciones del agente y cuestiones pendientes.
- Skill de estilo y generador resuelto; enlaces a guía y referencias pertinentes.

No duplicar aquí todos los prompts o el historial del manifiesto. Para subagentes finales extraer solo los apartados de su rama; nunca enviar enlaces a bocetos ajenos.

## manifest.json

UTF-8, `schema_version: 1`. El coordinador escribe este registro tras cada resultado o respuesta. Estructura mínima inicial:

```json
{
  "schema_version": 1,
  "scene_id": "escena-id",
  "scene_revision": 1,
  "stage": "needs_information",
  "style_skill": {"name": "estilo-style", "path": "ruta-a-SKILL.md"},
  "generator": {
    "provider": null,
    "tool": null,
    "requested_model_or_policy": null,
    "effective_model": null,
    "model_visibility": "unresolved",
    "guide_sources": []
  },
  "format": {"aspect_ratio": null, "requested_options": {}},
  "sources": [],
  "characters": [],
  "pending_questions": [],
  "sketch_rounds": [],
  "selections": [],
  "finals": [],
  "events": []
}
```

Sustituir los valores ilustrativos al usarlo; los `null` representan información aún no resuelta. No inventar IDs de modelo ni respuestas. Las rutas de salida se expresan relativas al manifiesto; las fuentes externas o de proyecto deben indicar su base de resolución. Solo registrar `file` para archivos existentes; los intentos sin resultado van en eventos con su error.

Registrar estos datos cuando existan:

| Colección | Datos necesarios |
|---|---|
| `sources` | ID, ruta/base, función, procedencia, revisión o huella y si fue realmente adjuntada en cada intento |
| `characters` | ID, descripción, sheet/manifiesto, revisión, atuendo y estado de aprobación conocido |
| `guide_sources` | URL oficial, fecha de consulta y decisiones de formato de prompt/negativo/capacidades |
| `sketch_rounds` | ID, revisión de escena, prompt base y huella, mapa de adjuntos y opciones congelados; tres ramas 01/02/03 con sus agentes, intentos y revisión |
| `selections` | ID, archivo/versión exacta del boceto, revisión de escena, evidencia del mensaje del usuario, compromisos compositivos y vigencia |
| `finals` | ID de selección, agente, intentos, revisión estructural/de identidad/de estilo, archivo entregado e incidencias |
| `events` | Fecha/hora real con zona, acción, cambios de etapa, fallos, correcciones, decisiones y autorizaciones adicionales |

Cada intento con salida guarda ID, agente, archivo, dimensiones reales, prompt completo, opciones realmente transmitidas, negativo y su canal o ausencia, fuentes/adjuntos realmente utilizados, proveedor/modelo observado, revisión visual e incidencias. Conservar resultados rechazados o sustituidos con su estado. Separar un artefacto seleccionado de su aprobación artística final.

El archivo `result-vNN.json` es el informe de una sola ejecución del trabajador; no un segundo manifiesto. El coordinador verifica sus rutas, imágenes y datos antes de incorporarlos. Los trabajadores no reciben acceso al registro central como parte de su paquete.

## Etapas y avance

| Etapa | Condición para avanzar |
|---|---|
| `needs_information` | Requisitos críticos resueltos, estilo/generador accesibles y referencias suficientes |
| `preparing_sketches` | Especificación y paquete común congelados |
| `generating_sketches` | Tres ramas iniciales ejecutadas y resultados revisados; errores persistentes requieren decisión |
| `awaiting_selection` | Respuesta inequívoca del usuario sobre versiones concretas; mantener la pausa mientras no llegue |
| `generating_finals` | Selecciones vigentes y paquetes finales completos |
| `delivered` | Todos los acabados solicitados entregados y revisados, sin incidencias que impidan cumplir lo acordado |
| `needs_revision` | Hay ajustes o fallos pendientes; conservar las ramas terminadas y registrar dónde retomar |

Un boceto con defectos que impiden usarlo no pasa a apto por preferencia estética; aclarar cómo resolverlo. La selección de varios crea ramas separadas y un final por selección. Una solicitud de variantes adicionales cambia ese alcance explícitamente.

No hay un umbral automático de aprobación del usuario: registrar evidencia solo si responde. `delivered` no significa `approved`. Si cambia la estructura, crear nueva revisión y marcar selecciones afectadas como desactualizadas; si cambia solo el acabado, versionar ese acabado conservando la selección y su historial. Un contador de corrección no se reinicia al renombrar una rama.

## Comprobación antes de entregar o retomar

Comprobar que los archivos abren, que las rutas existen y que prompts e informes corresponden a los intentos reales. Medir dimensiones y relación de aspecto; compararlas con el formato solicitado y con el boceto de cada acabado. Una petición textual de formato no prueba que se haya cumplido. Si hay una discrepancia importante, declararla; no recortar ni estirar la imagen silenciosamente para aparentar conformidad.

Comparar los tres paquetes iniciales, revisar que cada acabado usó solo su boceto y que las selecciones se refieren a versiones vigentes. No confundir un hash coincidente o un archivo válido con corrección visual. Reabrir las imágenes para evaluar anatomía, cámara, contactos, identidad y estilo.
