# Acabado aislado de la selección r01-02

El usuario ha seleccionado inequívocamente «Boceto 2». Tu única tarea es producir UNA generación de acabado desde ese boceto, sin cambiar encuadre, cámara, pose, escala, contactos ni masas principales. No conoces ni debes consultar otros bocetos, selecciones o resultados.

El coordinador ya sincronizó origin/main y revisó las entradas. Trabaja sólo en `C:/Users/vee_m/Pictures/Warcraft anime/output/scenes/holly-mapa-lordaeron/finals/r01-02`. No hagas commit/push ni modifiques Git, fuentes, canon, skills o registros centrales. Sólo el coordinador registra la selección y revisa los resultados.

Lee `final-package-r01-02.json` y su prompt exacto. Lee la skill imagegen y la skill warcraft-warpath-style con las guías de dibujo/acabado/revisión especificadas en el paquete. Las descripciones canónicas aplicables son identidad revisión 1 y equipo `base_blue_staff` revisión 2; la ficha completa de Holly está autorizada. El prompt ya contiene la extracción pertinente y resuelve la nueva acción de las manos, que sostienen el mapa en lugar de la pose neutra de biblioteca. No adjuntes documentación textual, ni inventes información en el prompt.

Abre cada una de las OCHO imágenes del paquete mediante `view_image` antes de la llamada. Adjunta exclusivamente esas rutas, en ese orden, con sus roles. No uses las últimas imágenes del chat. Transmite el prompt de archivo sin reformular. Guarda copia byte-idéntica como `final-v01.prompt.txt` antes de generar.

Generador: herramienta integrada OpenAI `image_gen.imagegen`; `referenced_image_paths` del paquete, `transparent_background: false`. Modelo efectivo no expuesto, sin selector, calidad, semilla, dimensión o negativo separado. Solicitud de formato en el prompt: conservar el panorama 2,4:1 del boceto. No usar CLI/API/credenciales ni otro proveedor. Una llamada inicial, sin reintentos ni correcciones autónomas.

En functions.exec usa directiva inicial `// @exec: {"yield_time_ms": 120000, "max_output_tokens": 1200}` para imagegen. Guarda la respuesta completa con store si hace falta y emite con generatedImage(result); no imprimas base64 ni el objeto entero. Copia el archivo nativo devuelto de inmediato a `final-v01.png` o extensión real. No recortes, estires ni retoques el resultado. Conservar bytes nativos.

Mide dimensiones y calcula hashes; usa struct para dimensiones PNG si Pillow no está instalado (no instalar dependencias por eso). Abre el resultado local y revisa comparación con TU boceto, identidad, túnica, manos/mapa, bastón, iluminación y estilo. Guarda `result-v01.json`: selección/agent_id, proveedor/herramienta/modelo real, opciones y adjuntos efectivos, prompt/imagen/rutas/SHA-256, dimensiones, hora con Europe/Madrid, incidencias y revisión visual concreta. No inventes metadatos ni aprobación del usuario. Un fallo sin resultado se registra sin file inventado. No reintentes; el coordinador autoriza como máximo una corrección si identifica un defecto concreto.

Devuelve imagen/informe/prompt con rutas absolutas, dimensiones, hashes y desviaciones. No hace falta esperar validación para guardar y comunicar el resultado, pero no lo declares aprobado artísticamente por el usuario.
