# Self-assessment — Hands-on 2  
**Grupo:** Group02  
**Dataset:** BiciMAD — Disponibilidad de bicicletas por estación (histórico)

## 1. Análisis del conjunto de datos

Usamos el dataset histórico de **BiciMAD**, que muestra la disponibilidad de bicicletas por estación en distintas fechas y horas.  
El archivo viene en formato CSV y tiene columnas como:

- `station_id` → identificador de la estación  
- `date` y `time` → momento de la medición  
- `available_bikes` → bicis disponibles  
- `available_docks` → huecos libres  
- `lat`, `lon` → coordenadas de la estación  

Lo revisamos para entender la estructura y pensamos algunas comprobaciones básicas antes de transformarlo a RDF:
- Combinar `date` y `time` en un campo tipo timestamp ISO-8601.  
- Revisar que no haya `station_id` repetidos ni vacíos.  
- Asegurarnos de que las coordenadas estén dentro de Madrid.  
- Que `available_bikes` y `available_docks` sean siempre números positivos.  

Nos pareció un dataset bastante limpio, aunque al ser histórico puede tener días sin datos o estaciones cerradas.  
En general, es fácil de entender y tiene información útil para hacer análisis de disponibilidad.

## 2. Análisis de la licencia de la fuente

El dataset viene del **Portal de Datos Abiertos del Ayuntamiento de Madrid**.  
Según el [aviso legal oficial](https://datos.madrid.es/egob/catalogo/aviso-legal), se puede reutilizar con fines comerciales o no comerciales mientras se cite la fuente.  

Nuestra idea es mantener esa misma licencia cuando creemos los datos RDF, añadiendo el enlace en los metadatos (por ejemplo con `dcterms:license`).  

En resumen: se pueden usar los datos sin problema siempre que pongamos algo parecido a esto:

> Fuente: Ayuntamiento de Madrid — Datos Abiertos  

Nos pareció una licencia muy clara y práctica para este tipo de ejercicios.

## 3. Estrategia de nombrado de recursos (URIs)

Decidimos crear URIs simples y legibles para que sea fácil entender a qué corresponde cada recurso.

Proponemos una estructura base como esta:  

| Tipo de recurso | Patrón | Ejemplo | Descripción |

| Estación | `/station/{id}` | `https://example.org/group02/bicimad/station/123` | Identifica una estación concreta. |

| Observación | `/observation/{id}-{yyyyMMddTHHmm}` | `https://example.org/group02/bicimad/observation/123-20210115T0830` | Representa una medición en un momento determinado. |

| Lugar | `/place/{type}/{slug}` | `https://example.org/group02/bicimad/place/district/centro` | Representa un distrito o barrio. |

Pensamos que así es más fácil generar las URIs desde el propio CSV (por ejemplo, con Python o Excel).  

## 4. Comentarios finales

Esta práctica nos ayudó a entender los primeros pasos del proceso de Linked Data. También aprendimos que elegir bien las URIs y respetar la licencia son cosas muy importantes antes de publicar nada.  

En general, fue una práctica bastante útil para afianzar la parte más conceptual del curso.
