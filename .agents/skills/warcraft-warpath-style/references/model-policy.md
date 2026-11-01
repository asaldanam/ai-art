# Política de modelos · preferir el más avanzado disponible

**Decisión vigente del usuario, 2026-11-01:** se retira la exigencia de comprobar el modelo más avanzado y parar si no puede usarse. Queda una preferencia por el más avanzado cuando haya varias opciones disponibles.

| DO | DON'T |
|---|---|
| Distinguir el GPT director, que analiza y redacta, del generador que produce píxeles mediante la herramienta de imágenes de OpenAI. | Afirmar que ambos papeles usan necesariamente el mismo modelo. |
| Si hay varios modelos seleccionables, preferir el más avanzado apropiado para cada papel. Consultar documentación oficial vigente cuando haga falta compararlos. | Elegir sólo por el número de versión o exigir acceso a un modelo que el entorno no ofrece. |
| Usar la herramienta integrada de imágenes cuando sea la opción disponible. Registrar el modelo si se expone; en caso contrario indicar «modelo efectivo no expuesto por la herramienta». | Inventar el modelo efectivo, prometer un selector inexistente o bloquear la generación por no conocer ese identificador. |
| Mantener GPT/OpenAI como flujo confirmado. Si sólo se pide un prompt, entregarlo sin generar. | Cambiar a Nano Banana u otro proveedor sin una instrucción explícita. |
| Comunicar fallos reales de acceso o ejecución y conservar lo ya preparado. | Confundir un identificador opaco con una indisponibilidad del generador. |
| Si la herramienta no puede generar, explicar el fallo y la opción necesaria para continuar. | Fingir una generación o cambiar de proveedor en silencio. |

La skill orienta la elección; no cambia por sí sola el modelo de la aplicación. No añadir campos ficticios de modelo a agents/openai.yaml ni exigir comprobaciones imposibles antes de trabajar.

Fuentes para comparaciones futuras: [modelos GPT](https://developers.openai.com/api/docs/guides/latest-model) y [generación de imágenes](https://developers.openai.com/api/docs/guides/image-generation). No fijar un modelo como «el más avanzado» para siempre. La documentación pública no demuestra cuál ejecuta una herramienta opaca.

En las pruebas se usó image_gen.imagegen; la interfaz no expuso identificador de modelo ni selector. Esto queda documentado y no impide utilizar las variantes aceptadas.
