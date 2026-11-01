# Archivos, progreso y manifiesto por estilo

Leer antes de iniciar o reanudar las generaciones. Todas las rutas de trabajo se resuelven desde la raíz del proyecto, no desde la carpeta de esta skill.

## Estructura y nombres

```text
characters/<character_id>/
  CHARACTER.md
  <style_id>/
    manifest.json
    <character_id>_midshot_candidate_01_v01.png
    <character_id>_midshot_candidate_01_v01.prompt.txt
    <character_id>_midshot_candidate_02_v01.png
    <character_id>_midshot_candidate_02_v01.prompt.txt
    <character_id>_midshot_candidate_03_v01.png
    <character_id>_midshot_candidate_03_v01.prompt.txt
    <character_id>_midshot.png
    <character_id>_fullbody_front.png
    <character_id>_fullbody_front.prompt.txt
    ...
```

`style_id` es el nombre completo de la skill de estilo elegida, por ejemplo `warcraft-warpath-style`. Cada estilo tiene su propio manifiesto; el índice que los reúne está en `CHARACTER.md`.

El atuendo `base` sin nombre usa el prefijo `<character_id>`. Un atuendo con nombre usa `<character_id>_<outfit_id>`, también para candidatas y prompts. Por ejemplo: `holly_willhelm_ceremonial_fullbody_back.png`. El campo `outfit_id` del manifiesto es la autoridad; no deducirlo separando el nombre por guiones bajos.

Usar las nueve etiquetas `view` de `SKILL.md`. Las candidatas añaden `_candidate_01`, `_candidate_02`, `_candidate_03` y un sufijo de versión. Los detalles adicionales usan etiquetas explícitas, por ejemplo `detail_staff` o `head_profile_right`, y no sustituyen las vistas obligatorias.

Conservar las imágenes anteriores. Si una ruta ya está ocupada, usar `_v02`, `_v03`, etc. antes de `.png` y actualizar el manifiesto. Aplicar la misma regla a prompts: guardar el prompt completo realmente ejecutado junto a la imagen, no solo un bloque de diferencias. La copia final del plano medio reutiliza el prompt de su candidata y registra `derived_from`; no simular una generación adicional.

Cada PNG entregable contiene una única vista sobre transparencia real. Una miniatura de presentación, si se usa, no sustituye los archivos individuales. No generar collages ni imágenes de contacto adicionales por defecto.

## Formato JSON (UTF-8)

Usar `schema_version: 1`. El ejemplo es un manifiesto inicial válido; ampliar las listas a medida que se reciben respuestas o se producen archivos.

```json
{
  "schema_version": 1,
  "character_id": "holly_willhelm",
  "style_skill": "warcraft-warpath-style",
  "generator": {
    "tool": "image_gen",
    "model": "not_exposed"
  },
  "outfits": [
    {
      "id": "base",
      "identity_revision": 1,
      "stage": "awaiting_character_approval",
      "candidate_round": 1,
      "selected_candidate_id": null,
      "master_reference_id": null,
      "approvals": {
        "character": null,
        "selection": null,
        "sheet": null
      },
      "pending_questions": [],
      "gap_fill_decisions": [],
      "issues": []
    }
  ],
  "images": []
}
```

No inventar el modelo si la herramienta no lo expone. Cada aprobación sustituye su `null` por un objeto con `identity_revision`, `scope`, `evidence` y `recorded_at` (fecha/hora real con zona). Conservar decisiones históricas al actualizar una revisión o ronda, mediante `approval_history` si procede. El manifiesto registra respuestas reales, no una aprobación deducida del éxito técnico.

Etapas por atuendo: `needs_information`, `awaiting_character_approval`, `generating_candidates`, `awaiting_selection`, `generating_views`, `awaiting_sheet_review`, `approved`. Registrar cuestiones y volver a `needs_information` si aparece un hueco. Al reanudar, comprobar la etapa contra archivos y aprobaciones reales; corregir inconsistencias sin inventar aprobaciones. Mantener entradas separadas para futuros atuendos.

## Registro de cada imagen

```json
{
  "id": "base_midshot_candidate_01_r01",
  "file": "holly_willhelm_midshot_candidate_01_v01.png",
  "prompt_file": "holly_willhelm_midshot_candidate_01_v01.prompt.txt",
  "outfit_id": "base",
  "identity_revision": 1,
  "kind": "candidate",
  "view": "midshot",
  "status": "pending_review",
  "candidate_round": 1,
  "camera_side": "front",
  "source_ids": ["identity_front", "outfit_back", "style_01"],
  "reference_image_ids": [],
  "derived_from": null,
  "notes": []
}
```

- `id`: único en todo el manifiesto, también entre rondas, revisiones y atuendos.
- `file` y `prompt_file`: rutas relativas al manifiesto y contenidas en el directorio del estilo. Solo registrar archivos que existan; guardar fallos de llamadas en `issues`.
- `identity_revision`: revisión canónica realmente utilizada. No reasignar imágenes antiguas a una nueva revisión sin revisión explícita.
- `kind`: `candidate`, `reference` o `detail`. La copia final de la candidata elegida es `reference`, `view: midshot`, con `derived_from` apuntando al ID de la candidata. El atuendo indica sus IDs en `selected_candidate_id` y `master_reference_id`.
- `status`: `pending_review`, `selected`, `not_selected`, `approved`, `rejected` o `superseded`. Usar `selected`/`not_selected` para las candidatas después de la elección. Las referencias activas están en `pending_review` o `approved`; solo una activa por vista, atuendo y revisión. Marcar como `superseded` una referencia reemplazada, conservando su archivo.
- `candidate_round`: ronda de elección en candidatas; `null` en otras imágenes. Una nueva ronda requiere solicitud del usuario. Generar tres candidatas por ronda. Si se autoriza corregir una candidata, marcar su versión anterior como `superseded` y conservarla; mantener tres candidatas vigentes en esa ronda.
- `camera_side`: `front`, `back`, `left` o `right`; los dos últimos describen el lado anatómico visible en perfil o tres cuartos.
- `source_ids`: fuentes realmente adjuntadas a esa llamada, cuyos roles y ubicaciones se registran en `CHARACTER.md`, incluida su sección de estilo. No listar fuentes que solo se hayan mencionado en el texto.
- `reference_image_ids`: IDs de imágenes generadas del manifiesto que se hayan adjuntado. Para referencias aprobadas de otro estilo/atuendo, registrar su ruta y función en el documento o en una nota explícita. `derived_from` registra una copia o derivación material, no sustituye esta lista de adjuntos.

Guardar todas las imágenes producidas, incluidas las candidatas descartadas y las versiones rechazadas. Los resultados defectuosos pueden permanecer como `rejected` y anotarse; no tratarlos como referencias activas. Si se copia una referencia facial compatible a otro atuendo, registrar la procedencia y verificar que sigue siendo válida para ese atuendo. No incrementar el número de generaciones por hacer una copia.

## Cuándo avanzar

| Etapa | Evidencia necesaria para pasar a la siguiente |
|---|---|
| `needs_information` | Datos aportados o propuestas autorizadas para los huecos enumerados |
| `awaiting_character_approval` | Aprobación explícita del documento y atuendo en su revisión actual |
| `generating_candidates` | Tres PNG y sus prompts guardados en la ronda actual |
| `awaiting_selection` | Elección inequívoca de una de esas tres candidatas |
| `generating_views` | Ancla copiada y nueve referencias activas completas, comprobadas visual y técnicamente |
| `awaiting_sheet_review` | Aprobación explícita de todas las vistas del conjunto |
| `approved` | Mantener archivos, evidencias y enlace desde `CHARACTER.md` |

Seleccionar una candidata no aprueba automáticamente las otras vistas. La aprobación final se refiere a una revisión y a un atuendo concretos. Reutilizar solo las aprobaciones cuyo alcance siga siendo válido.

## Comprobación técnica

Requisitos: Python 3 y Pillow. Usar el Python que ya tenga Pillow; si no existe, instalar la dependencia en un entorno local autorizado. El comprobador no modifica imágenes ni manifiestos:

```powershell
python <skill_dir>/scripts/check_assets.py <style_dir>/manifest.json
python <skill_dir>/scripts/check_assets.py <style_dir>/manifest.json --outfit base --complete
```

La primera orden comprueba lo que existe; no exige haber terminado una sheet. La segunda exige las nueve vistas activas de la revisión vigente y del atuendo indicado, exactamente tres candidatas vigentes de su ronda actual, una candidata seleccionada y una copia idéntica como ancla. Comprueba también que las referencias activas tienen píxeles transparentes y contenido visible. Los archivos rechazados se comprueban como archivos, pero su transparencia no impide completar una sheet corregida.

Estas comprobaciones no demuestran fidelidad visual ni autenticidad de las aprobaciones. Ambas se revisan en el flujo de `SKILL.md`.
