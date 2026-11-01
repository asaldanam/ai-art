---
name: warcraft-warpath-style
description: "Dirige, redacta prompts y revisa escenas de fantasía con el estilo específico de las 43 capturas Warpath del proyecto Warcraft anime. Usa reglas DO/DON'T, referencias por plano e iluminación y controles de continuidad para personajes aprobados. Se aplica al pedir este estilo o continuar sus escenas; no a cualquier petición genérica de anime."
---

# Warcraft · estilo Warpath

Reproducir el lenguaje visual observado: personajes de dibujo angular, contornos oscuros limpios, sombreado cel de pocas masas, armaduras de grandes placas, fondos pictóricos por capas y luz motivada por la escena. No basta «anime épico» o «cinematográfico».

## DO / DON'T · empezar por los requisitos reales

| DO | DON'T |
|---|---|
| Aplicar la [configuración confirmada](references/project-config.md): Warcraft, generación con OpenAI, acabado A y panorámico aproximadamente 2,4:1 por defecto. | Reabrir preferencias ya confirmadas o producir más variantes de calibración sin solicitud. |
| Aplicar la [preferencia de modelos](references/model-policy.md): elegir el más avanzado entre los disponibles cuando haya varias opciones seleccionables. | Confundir el GPT director con el generador, prometer un selector inexistente o inventar el identificador efectivo. |
| Si la herramienta no revela su modelo, indicarlo y continuar. Si faltan referencias visuales necesarias, pedir únicamente las que falten. | Bloquear el trabajo por no verificar el modelo, o describir referencias inaccesibles como si se hubieran visto. |
| Respetar la solicitud actual del usuario por encima de estas preferencias; si cambia una regla, registrar el cambio explícito. | Presentar una preferencia de proyecto como una limitación técnica o política universal. |
| Mantener imágenes originales y cualquier copia, recorte, miniatura o fotograma derivado dentro de `C:\Users\vee_m\Pictures\Warcraft anime`. | Exportarlas a la carpeta global de skills, temporales externos o a otro proyecto para hacer esta skill autocontenida. |

Las imágenes originales y el vídeo fuente están dentro de `references/warpath/`, en esta skill. Resolver rutas desde los documentos de la skill, no desde el directorio de trabajo del agente. Verificar inventario con [manifest.json](references/manifest.json) y, si se necesita comprobar integridad, ejecutar `python scripts/check_references.py` desde esta carpeta. El comprobador es de sólo lectura.

La regla de ubicación trata del almacenamiento local de originales y derivados. Si sólo se piden prompts, no subir imágenes ni generar: entregar las rutas y explicar qué adjuntar cuando se ejecute la escena.

## DO / DON'T · cargar la evidencia pertinente

1. **DO:** leer la [biblia de estilo](references/style-bible.md) y el [acabado A aceptado](references/finish-calibration.md) al comenzar. **DON'T:** sustituirlos por un estudio, artista o etiqueta genérica de anime. Consultar las [observaciones del vídeo](references/video-observations.md) cuando ayuden a interpretar las capturas.
2. **DO:** usar el [índice de referencias](references/reference-index.md) para localizar la familia de luz y plano de la nueva escena; después leer sólo las fichas del atlas pertinentes y abrir sus imágenes. **DON'T:** cargar las 43 en cada generación o describir imágenes que no se han visto.
3. **DO:** consultar [001–014](references/atlas-001-014.md) para exteriores, presentación y selva; [015–029](references/atlas-015-029.md) para combate, fuego, arcano, magenta y fogata; [030–043](references/atlas-030-043.md) para luz sagrada, exposición extrema, detalles y reacción. **DON'T:** asumir por el nombre de archivo la cronología, identidad o fuente de luz que no se ve.
4. **DO:** abrir fichas aprobadas de los personajes solicitados y la última escena aprobada si existe. **DON'T:** copiar la identidad de una captura usada como ejemplo de iluminación, o inventar una ficha canónica a partir de una sola vista.

## DO / DON'T · construir la escena

| DO | DON'T |
|---|---|
| Definir un instante y una intención: acción, emoción, sujetos y relación espacial. | Generar una pose de póster porque «fantasía épica» no aporta una acción. |
| Separar tamaño de plano, altura/ángulo de cámara y capas de profundidad. Usar ≈2,4:1 por defecto y otro formato cuando el usuario lo pida. | Afirmar lentes o diafragmas exactos del original, o usar un primer plano para toda escena. |
| Identificar ambiente, emisor principal, dirección, dureza, alcance y áreas que quedan en sombra. | Añadir contraluz, neón, partículas y luces de relleno universales. |
| Conservar cel shading en personajes y pincelada agrupada en fondos; detalle selectivo y siluetas fuertes. | Sustituirlos por render de videojuego, piel plástica, sombreado aerografiado o filigrana arbitraria. |
| Formular DO y DON'T específicos del plano; usar [prompts y negativos](references/prompting-and-negatives.md). | Prometer una fórmula «anti AI slop» validada o enviar listas de tokens de otro motor sin soporte. |
| Asignar a cada adjunto real un rol: STYLE, IDENTITY, LIGHT, SHOT o CONTINUITY. | Suponer que mencionar una ruta en el texto equivale a adjuntar la imagen al generador. |

Antes de cualquier decisión visual no documentada, incluso secundaria, preguntar de forma concreta y agrupada. Avanzar sólo en lo independiente y ya documentado. No repetir preguntas ya resueltas. Ver [continuidad y revisión](references/review-and-continuity.md).

## DO / DON'T · entregar según la solicitud

- **DO · Sólo prompt:** entregar el prompt completo, un bloque negativo compatible, relación de archivos que deben adjuntarse y su función, y las decisiones visuales que no sean obvias. Indicar «prompt preparado; generación no ejecutada». **DON'T:** generar píxeles o afirmar que las referencias ya se adjuntaron.
- **DO · Imagen solicitada:** usar la herramienta de imágenes de OpenAI; leer su esquema actual, cargar las referencias reales y producir la cantidad solicitada. La falta de identificador del modelo no impide generar. Si no hay acceso al generador elegido, indicarlo y parar esa ejecución; el usuario puede pedir sólo el prompt. **DON'T:** sustituir el flujo OpenAI confirmado por Nano Banana u otro proveedor en silencio.
- **DO · Revisión:** comparar imagen y referencias con la [rúbrica](references/review-and-continuity.md); describir desviaciones concretas y distinguir pruebas documentales de pruebas visuales. **DON'T:** aprobar por «aspecto bonito» si hay deriva de identidad o estilo.
- **DO · Corrección:** preservar lo que ya funciona y cambiar la desviación identificada; mostrar la propuesta si requiere cambiar una decisión canónica. **DON'T:** encadenar rediseños o generaciones ilimitadas sin revisar si se está alejando de la referencia.

## Fuentes y estado de validación

Consultar [fuentes](references/sources.md) cuando se discutan eficacia de negativas, límites del generador o vigencia de modelos. Las técnicas documentadas no convierten los prompts de proyecto en resultados garantizados. La skill contiene análisis de 43 capturas, observaciones de un muestreo del vídeo y calibración de acabado A aceptada. Está finalizada; no requiere más variantes. Las fichas de personajes se incorporarán cuando el usuario las facilite.
