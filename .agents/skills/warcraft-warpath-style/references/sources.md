# Fuentes consultadas y alcance

Consulta: **2026-11-01**. Los enlaces externos respaldan mecánica de prompting y selección de modelos; el estilo artístico se analiza a partir de las capturas locales. No se atribuye la biblia visual a documentación externa.

## Fuentes primarias

1. [Google · Nano Banana image generation](https://ai.google.dev/gemini-api/docs/image-generation). Recomienda precisión visual, revisión iterativa y formulaciones positivas de exclusiones. Documenta que capacidades y límites de referencias varían por modelo. **Aplicación:** describir el resultado deseado y adaptar cada solicitud al contrato real. No prueba una fórmula «anti AI slop» ni garantiza identidad perfecta.
2. [OpenAI · Image prompting](https://developers.openai.com/api/docs/guides/image-prompting). Explica cómo definir composición, asignar roles a imágenes y separar lo que cambia de lo que debe preservarse. **Aplicación:** manifiesto de adjuntos, restricciones explícitas y revisión del resultado. Los prompts de esta skill son originales; no se han copiado sus ejemplos.
3. [OpenAI · Image generation](https://developers.openai.com/api/docs/guides/image-generation). Describe generación y edición, y reconoce límites de consistencia en elementos recurrentes. **Aplicación:** no prometer continuidad garantizada ni dar por equivalente el modelo de conversación y el generador.
4. [OpenAI · Using GPT-6 / guía vigente](https://developers.openai.com/api/docs/guides/latest-model) y [ficha de GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra). En la fecha consultada, identifica Astra como opción de máxima capacidad general. **Aplicación:** orientar la preferencia por el modelo más avanzado entre las opciones realmente disponibles. No se exige verificarlo ni detenerse si la herramienta no expone su identidad. La documentación pública no prueba el acceso de la cuenta ni el modelo efectivo de una sesión.
5. [Ban y colaboradores · Understanding the Impact of Negative Prompts: When and How Do They Take Effect?](https://arxiv.org/abs/2406.02965), 2024. Estudia mecanismos y efectos temporales en modelos de difusión. **Aplicación:** evidencia de que la negativa depende del mecanismo de generación; no extrapolar sintaxis o resultados directamente a Nano Banana o GPT Image.
6. [Park y colaboradores · Guiding What Not to Generate: Automated Negative Prompting for Text-Image Alignment](https://arxiv.org/abs/2512.07702), 2025. Investiga selección de negativas para corregir alineación en difusión. **Aplicación:** apoyo limitado al diagnóstico de errores concretos, no validación de un prompt universal para este proyecto ni de las plantillas propuestas aquí.
7. [OpenAI · Using skills to accelerate OSS maintenance](https://developers.openai.com/blog/skills-agents-sdk). Documenta la ubicación local `.agents/skills/`. **Aplicación:** colocar este paquete dentro de esa estructura del proyecto, sin copiar imágenes ni instalarlo en el perfil global. La disponibilidad efectiva en el selector depende de que el entorno cargue ese proyecto.

## Resultado de la búsqueda solicitada

**DO:** distinguir «hay técnicas documentadas y estudios sobre prompts negativos» de «existe un prompt validado que elimina cualquier acabado genérico». No se ha localizado en estas fuentes una validación de esa segunda afirmación para este estilo, Nano Banana o GPT Image.

**DON’T:** presentar listas virales de etiquetas de calidad como evidencia experimental. El prompt negativo del proyecto se valida contra resultados y capturas, no por popularidad de la lista.

## Niveles de confianza

| Nivel | Qué incluye | Qué no demuestra |
|---|---|---|
| Observación directa | Encuadre, color, contornos, solapes, presencia de interfaz en 024. | Lente real, intención del autor, software, duración o acción temporal exacta. |
| Inferencia visual | Dirección aparente de luz, separación de planos, función narrativa probable. | Metadatos físicos ni continuidad perfecta del vídeo. |
| Documentación del proveedor | Funciones y parámetros que el proveedor publica en la fecha consultada. | Acceso efectivo de la cuenta, ausencia de fallback o rendimiento en nuestras escenas. |
| Propuesta de dirección | DO/DON’T, plantillas, rúbrica y selección de referencias de esta skill. | Que ya se haya probado con imágenes nuevas. |

Después de la redacción inicial se generaron nueve recreaciones de control con image_gen.imagegen. El usuario acepta el acabado de la primera variante y cierra la calibración. La selección valida ese acabado en las composiciones probadas; no demuestra continuidad en cualquier escena nueva. Véase [calibración de acabado](finish-calibration.md).
