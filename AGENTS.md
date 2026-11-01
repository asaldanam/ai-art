# Instrucciones para agentes

## Sincronización antes de trabajar

Cada vez que se solicite una tarea en este repositorio:

1. Ejecutar `git status` al comenzar para comprobar el estado de la copia local.
2. Consultar el estado del remoto, incluyendo los cambios nuevos de `origin/main` (por ejemplo, mediante `git fetch origin main` y la comparación con `origin/main`).
3. Si `origin/main` contiene commits que no están en la copia local, ejecutar `git pull origin main` antes de realizar cualquier otra acción.
4. Si el `pull` produce conflictos, detener el trabajo y pedir al usuario que elija si desea que el agente los resuelva. Si lo desea, el usuario deberá indicar también cómo resolverlos cuando haya más de una interpretación razonable.

No sobrescribir cambios locales ni resolver conflictos de forma arbitraria.

## Finalización de la tarea

Cuando la tarea haya terminado:

1. Comprobar `git status` y revisar el diff.
2. Si la tarea generó cambios en archivos existentes o añadió archivos nuevos, preparar únicamente esos cambios, crear un commit descriptivo y hacer `git push origin main` automáticamente.
3. No crear commits ni hacer push si la tarea no produjo cambios.
4. No incluir en el commit cambios preexistentes o ajenos a la tarea.
5. Si el commit o el push falla, no forzar la actualización del remoto; informar al usuario y solicitar instrucciones.
