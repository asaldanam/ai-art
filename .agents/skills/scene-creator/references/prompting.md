# Adaptar el prompt al generador definido por el estilo

Leer al resolver el generador y antes de preparar prompts. Separar la especificación estable de escena de su redacción para un modelo concreto.

## Resolver capacidades y fuentes

1. Leer el `*-style` elegido y los documentos de configuración/modelos a los que remita. Resolver proveedor, modelo exacto o política, herramienta, idioma y formato. La política puede ser «herramienta integrada de OpenAI, preferir el más avanzado seleccionable»; no requiere un ID inventado.
2. Inspeccionar las herramientas realmente disponibles y su esquema. Comprobar que admitan las referencias y la operación necesarias. Una skill no crea acceso a un proveedor ni cambia el modelo del entorno.
3. Consultar documentación oficial vigente del modelo y la operación concretos: texto a imagen para bocetos; imagen de referencia, edición o sketch-to-render para acabados. Registrar URL, fecha de consulta y conclusiones aplicadas. No usar la guía de vídeo como sustituto de la de imágenes. Si no se puede consultar y no hay una guía vigente suficiente, declarar la incertidumbre y preguntar antes de asumir capacidades.
4. Si el generador expone únicamente herramienta/proveedor, aplicar su guía pública y los controles realmente visibles; registrar `effective_model: null` y `model_visibility: not_exposed`. No deducir qué modelo interno ejecutó la llamada. Si el estilo exige un ID que no se puede seleccionar o un control que no existe, preguntar por una alternativa.
5. No cambiar proveedor, modo, herramienta ni usar API/CLI con credenciales por conveniencia. Para OpenAI cargar la skill `imagegen` y seguir su ruta autorizada; para otro proveedor usar sus herramientas/skills disponibles. Si falta acceso, conservar los prompts y explicar qué falta. No simular generaciones ni adjuntos.

Puntos de entrada para localizar la guía vigente, no contratos permanentes de capacidades:

- [Google: generación nativa de imágenes](https://ai.google.dev/gemini-api/docs/image-generation).
- [Google: Imagen](https://ai.google.dev/gemini-api/docs/imagen).
- [Midjourney: Prompt Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics) e [Image Prompts](https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts).
- [Black Forest Labs: índice de documentación](https://docs.bfl.ai/llms.txt).
- [OpenAI: generación de imágenes](https://developers.openai.com/api/docs/guides/image-generation). Para orientación sobre productos OpenAI, aplicar además la skill `openai-docs` disponible.
- [Diffusers: control estructural](https://huggingface.co/docs/diffusers/using-diffusers/controlnet), solo si el generador y flujo elegidos lo admiten.

Si el estilo define otro modelo, localizar su documentación oficial. No limitar la skill a esta lista.

## Compilar sin cambiar el significado

Guardar el texto exacto ejecutado y, aparte, opciones de herramienta y mapa de adjuntos. No mezclar instrucciones del subagente, metadatos de archivos o documentación con texto destinado al generador.

- **Extensión:** seguir límites y recomendaciones documentadas. Si la guía aconseja concisión, priorizar restricciones y relaciones decisivas; si admite prosa detallada, conectar acciones y posiciones con frases claras. No fijar un número universal de palabras ni recortar rasgos canónicos esenciales para encajar un presupuesto inventado.
- **Negativo:** usar un campo negativo solo si existe y está documentado para ese modelo/modo. Si el motor admite restricciones en lenguaje natural, expresarlas ahí; no fingir un campo negativo separado. Registrar dónde se transmitieron. Evitar listas genéricas de tokens copiadas de otro motor.
- **Cámara:** distinguir tamaño de plano, altura, posición alrededor del sujeto, inclinación, orientación corporal y mirada. Combinar el término técnico con una consecuencia visible cuando ayude. No pedir varias cámaras incompatibles en una sola imagen.
- **Anatomía y perspectiva:** describir apoyos, distribución del peso, contactos y solapamientos importantes. Para escorzos, explicar qué está más cerca, qué se acorta visualmente y qué tapa a qué. Diferenciar izquierda anatómica de izquierda del encuadre cuando importe.
- **Lentes y medidas:** usarlas como indicaciones visuales cuando la guía las admita, sin prometer simulación óptica ni exactitud métrica. Acompañarlas del efecto buscado.
- **Morfología:** extraer proporciones y volumen de las fichas, también en criaturas, monturas y cuerpos estilizados. No confundir el acortamiento por perspectiva con un defecto anatómico ni exigir dedos visibles cuando estén legítimamente ocultos.
- **Referencias:** asignar un índice y función a cada imagen realmente adjuntada. Una ruta escrita en el prompt no adjunta el archivo. Abrir las imágenes, respetar límites de entrada y elegir vistas pertinentes. Si un límite impide cubrir información esencial, preguntar; no omitir personajes en silencio.
- **Formato:** mantener relación de aspecto y encuadre entre boceto y final. Si el motor necesita dimensiones discretas, elegir un tamaño compatible sin alterar la composición; explicar una limitación real antes de prometer formato exacto.

## Dos prompts con propósitos diferentes

El prompt estructural incluye escena, morfología mínima, pose, apoyos, cámara, masas ambientales y nivel de boceto. Excluye acabado artístico e identidad ornamental. Mantener exactamente iguales texto, negativo, adjuntos y opciones en las tres llamadas iniciales. Una semilla, si existe, se registra con su valor real; no exigirla ni prometer reproducibilidad entre llamadas. Registrar cualquier variación técnica necesaria en vez de ocultarla.

El prompt final incorpora identidad, atuendo, estilo y referencias, y formula explícitamente qué geometría conservar del boceto seleccionado. Escoger entre edición o generación condicionada según la herramienta y su guía; no tratar una descripción textual del boceto como equivalente a adjuntar el boceto. Si no existe un modo de imagen de entrada apropiado, consultar la alternativa.

En una corrección, guardar el prompt completo y las invariantes, no solo una frase de diferencias. El prompt de corrección puede diferir del base, pero no convierte el intento corregido en una cuarta propuesta de exploración.

## Alcance de las recomendaciones

Las relaciones físicas explícitas ayudan a comunicar la intención; no garantizan anatomía o perspectiva correctas. La revisión debe comprobar el resultado. Como contexto: [GenSpace](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4e582b104248a396a703646755071329-Abstract-Datasets_and_Benchmarks_Track.html) estudia fallos espaciales y [HumanBench](https://openaccess.thecvf.com/content/WACV2026/html/Jain_HumanBench_Two_Heads_No_Legs_But_Mostly_Human_the_State_WACV_2026_paper.html) evalúa generación humana. No convertir esos estudios en un ranking vigente de modelos ni en una fórmula universal de prompt.
