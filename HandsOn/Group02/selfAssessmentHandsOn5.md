# Self Assessment – HandsOn 5 (Data Linking)

## 1. Identificación de clases y datasets enlazables

El dataset utilizado define una única clase en la ontología: `ns:MedicionDiaria`, que representa mediciones agregadas diarias del sistema de bicicletas públicas BiciMAD (horas de uso, disponibilidad, número de usos, etc.).

Esta clase no tiene un equivalente directo en bases de datos externas como Wikidata o DBpedia, ya que no existen entidades que representen “mediciones diarias de BiciMAD”. Por tanto, la clase `ns:MedicionDiaria` no es enlazable directamente.

Sin embargo, el dataset contiene la propiedad `ns:fecha`, cuyos valores representan días concretos. Cada uno de estos días sí puede enlazarse con entidades externas en Wikidata, concretamente con recursos del tipo *calendar day of a given year*. Por ello, el data linking se ha realizado a nivel de fechas.

---

## 2. Proceso de data linking

El proceso de data linking se ha llevado a cabo utilizando **OpenRefine**:

- Se ha importado el CSV limpio generado en el HandsOn anterior.
- Se ha normalizado el formato de la columna `fecha` para asegurar valores homogéneos (`YYYY-MM-DD`).
- Se ha reconciliado la columna `fecha` con Wikidata, seleccionando el tipo de entidad *calendar day of a given year*.
- Se han validado manualmente varios enlaces correctos entre fechas del dataset y sus correspondientes entidades en Wikidata.
- Se ha creado una nueva columna `wikidata_fecha` que contiene los identificadores QID de Wikidata para las fechas enlazadas.

No todas las filas han sido enlazadas, lo cual es aceptable y habitual en procesos de data linking, ya que el objetivo es demostrar la capacidad de enlazar datos con un dataset externo.

Como resultado de este proceso se han generado:
- Un fichero JSON con las operaciones de linking realizadas en OpenRefine.
- Un fichero CSV enriquecido con la columna `wikidata_fecha`.

---

## 3. Actualización de los mappings y generación del RDF

Se ha actualizado el mapping RML para incorporar el data linking:

- El mapping genera instancias de la clase `ns:MedicionDiaria` a partir de cada fila del CSV.
- Las columnas del CSV se mapean a las propiedades definidas en la ontología.
- Se ha añadido un `rr:predicateObjectMap` con la propiedad `owl:sameAs`, que enlaza cada medición diaria con la entidad de Wikidata correspondiente a su fecha, utilizando la columna `wikidata_fecha`.

El resultado es un RDF en formato Turtle que contiene enlaces `owl:sameAs` entre los recursos del dataset y recursos externos de Wikidata.

---

## 4. Consultas SPARQL

Se ha creado un fichero de consultas SPARQL que permite comprobar el correcto funcionamiento del data linking. Las consultas:

- Utilizan la ontología definida (`ns:MedicionDiaria`, `ns:fecha`).
- Hacen uso explícito de la propiedad `owl:sameAs`.
- Permiten recuperar las fechas del dataset junto con las entidades de Wikidata enlazadas.

Estas consultas demuestran que los enlaces externos se han generado correctamente y que el RDF resultante es consultable.

---

## 5. Comprobación de los criterios del assignment

- El dataset contiene enlaces `owl:sameAs` hacia un dataset externo (Wikidata).
- El proceso de linking se ha realizado con OpenRefine.
- Los mappings RML han sido actualizados para incluir los enlaces.
- Se ha generado RDF enlazado en formato Turtle.
- Se han definido consultas SPARQL que utilizan los enlaces creados.

