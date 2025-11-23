# Self-assessment Assignment 3 (Grupo 3)

## Entregables
- Fichero JSON con los cambios empleados para la limpieza y ordenación de los datos.
- Fichero CSV con la versión actualizada y normalizada de los datasets.
- Este documento de autoevaluación.

## Lo que analizamos
- Estructura del CSV original y detección de valores inconsistentes o incompletos.
- Normalización de direcciones, nombres y códigos postales.
- Revisión de campos relevantes para la construcción del grafo.
- Verificación de la unicidad del identificador principal (`codigo_centro`).

## Decisiones clave
- Las filas que no se van a utilizar para crear el grafo no se modifican ni eliminan; se mantienen como estaban.
- Se unificaron las columnas de tipo de vía, nombre de vía y número para formar una dirección completa en mayúsculas.
- Se decidió no crear una columna nueva de URIs, ya que el campo `codigo_centro` es único y suficiente como identificador estable.
- Se agruparon los tipos de centros en clusters (por ejemplo, centros de orientación educativa y psicopedagógica, escuelas infantiles, centros de enseñanza artística, aulas hospitalarias).
- Se aplicó formato en mayúsculas a nombres de calles, municipios y distritos.

## Retos y mitigaciones
- Datos faltantes (como número de coordinador o fecha de constitución) se dejaron en blanco para mantener la integridad del dataset.
- Códigos postales, números de teléfono y fax con todos los dígitos en cero, se reemplazaron por valores en blanco.
- Direcciones con “s/n” se transformaron a valor en blanco.
- Se verificó que las transformaciones no afectaran a los campos que no intervienen en el grafo.