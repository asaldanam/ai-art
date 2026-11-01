# Contrato de `CHARACTER.md`

Leer al crear o revisar el personaje. Es un documento canónico reutilizable entre estilos, no un prompt de una escena.

## Ubicación e identificadores

- Raíz: `characters/<character_id>/CHARACTER.md`, relativa al proyecto activo.
- Reutilizar el ID de un personaje existente. Para uno nuevo, usar un nombre estable en minúsculas ASCII, con `_` como separador; mantener el nombre visible con su ortografía original.
- Identificar el primer atuendo como `base` si no tiene nombre propio. Los futuros atuendos tendrán IDs estables distintos y se reflejarán en los nombres de sus PNG.
- Las rutas de referencias locales en este documento son relativas al directorio del personaje; las fuentes externas conservan su ubicación real. No mover ni sobrescribir originales para acomodar la estructura. Los textos aportados se resumen fielmente y se identifican por su mensaje o archivo.

## Secciones que debe contener

1. **Nombre, revisión y aprobación.** Revisión entera creciente de identidad y diseños de atuendo; estado `draft` o `approved`. Registrar qué validó el usuario, la fecha real y una cita corta o resumen inequívoco de su respuesta. Un visto bueno a una imagen no aprueba por sí solo un nuevo texto canónico.
2. **Fuentes y funciones.** Tabla con ID, ruta/mensaje, función y rasgos que documenta. Separar identidad, atuendo y accesorio. Las fuentes de estilo se registran en su sección particular y no definen el personaje.
3. **Información pendiente y propuestas.** Enumerar conflictos y huecos. Cuando el usuario autorice rellenarlos, registrar el alcance de la autorización y distinguir las propuestas de los rasgos observados. Al validarlas, dejar constancia de que pasan a ser decisiones de diseño aprobadas. No mantener alternativas contradictorias dentro del prompt canónico.
4. **Invariantes de identidad.** Rasgos que distinguen al personaje, descritos con relaciones espaciales y lateralidad anatómica. Diferenciar anatomía y proporciones del acabado que tenía la referencia original.
5. **Prompt canónico de identidad en inglés.** Texto detallado utilizable con distintos estilos.
6. **Atuendos.** Un bloque de prompt en inglés por ID de atuendo. Describir capas, silueta, colores propios, materiales, piezas, accesorios, sujeciones y zonas posteriores y laterales que se hayan documentado o aprobado. La identidad facial común no se reescribe para cada conjunto.
7. **Límites de adaptación.** Rasgos que deben conservarse y simplificaciones permitidas. La simplificación nunca permite omitir una marca distintiva o intercambiar lados. Si el estilo exige cambiar una proporción canónica, solicitar una decisión explícita.
8. **Estilos.** Índice y sección por skill `*-style`, con enlace relativo a `<style_id>/manifest.json`, atuendos, revisión de identidad usada, estado y ancla seleccionada cuando exista. Aquí pueden figurar reglas particulares de adaptación aprobadas. No insertarlas en el prompt canónico.

## Esqueleto del bloque de prompt

Completar solo con información documentada o propuestas validadas; los encabezados no obligan a inventar datos ausentes.

```text
CANONICAL CHARACTER IDENTITY
Name and defining identity:
Species, apparent age and physical presentation:
Build, proportions and recognizable silhouette:
Face structure and distinctive features:
Skin, eyes, hair and their intrinsic colors:
Marks, scars and anatomical asymmetries:
Non-negotiable identifying features:

OUTFIT — [outfit_id]
Garment and armor layers, from inner to outer:
Shape, fit, materials and intrinsic colors:
Front, profile and back construction:
Accessories, fastenings, weapons and their anatomical placement:
Outfit-specific invariants:

PRESERVATION RULES
Preserve anatomical left/right and all identifying features.
Character identity and outfit references govern design.
Style references govern artistic rendering only.
```

No incluir medio artístico, artista, motor, estética, pincelada, cel shading, lente, pose, encuadre, fondo ni iluminación en el prompt canónico. Describir materiales físicos y colores propios sí corresponde al diseño. Si la forma original es deliberadamente exagerada y define la identidad, documentar la proporción sin convertirla en una etiqueta de estilo.

## Validación y cambios

Antes de generar candidatas, presentar el archivo y pedir validación explícita de la revisión vigente. La respuesta puede aprobar identidad y uno o varios atuendos; registrar su alcance. Si el usuario pide cambios, actualizar el borrador y volver a presentarlo. Un documento heredado sin evidencia de aprobación requiere validación.

Actualizar enlaces, estado o manifiestos no invalida el canon. Cambiar anatomía o diseño de atuendo incrementa su revisión, requiere validación y obliga a revisar qué referencias anteriores siguen siendo compatibles. Conservar las aprobaciones históricas indicando su revisión, sin atribuirlas a una nueva.
