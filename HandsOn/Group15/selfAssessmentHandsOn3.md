# Autoevaluación Entrega 3 Práctica  – Grupo15

## Resumen del trabajo realizado.
En esta tercera entrega de la práctica nuestro objetivo era eliminar incongruencias y dar sencillez a nuestro csv mediante de la creación de columnas normalizadas, separación de texto, elección de información clave en ciertas celdas... Todo ello con el uso de la herramienta Openrefine para así poder facilitar nuestra ontología.

## Acciones detalladas
1.- El texto en nombre ha sido normalizado y limpiado eliminando los espacios extra (con trim) y convirtiendo los nombres en títulos (con toTitlecase). De la misma manera se ha procedido en distritos, barrios.

2.- El texto en equipamiento también ha sido normalizado y limpiado, en esta ocasión convirtiendo todo en minúsculas (con toLowercase).

3.- A continuación, se han creado dos nuevas columnas como son tieneWifi y tieneInternetPublico extrayendo la información proporcionada en equipamiento y plasmandola en una nueva categoría.

4.- Además, se ha creado una columna dirección a partir de la unión de clasevia, nombrevia y num, que proporciona la dirección completa de cada biblioteca sin dejar detalle.

5.- Se han creado tanto distrito_slug como barrio_slug mediante la normalización con texto en minúsculas, sin acentos y con guiones de las columnas distrito y barrio.

6.- Se han originado 3 columnas a partir de la columna accesibiliad para separar la parte natural de la decimal. Accesibilidad 1 representa la parte natural; Accesibilidad 2 las décimas ; y Accesibilidad 3 las centésimas.

7.- Por último, latitud y longitud han sido convertidas a números.


## Conclusión
Todos los cambios realizados han sido guardados en un nuevo csv: bibliotectas_update.csv ; y las operaciones han sido almacenadas en un documento JSON: operations.json. Ahora, podemos decir que nuestro csv es óptimo y está limpio.
