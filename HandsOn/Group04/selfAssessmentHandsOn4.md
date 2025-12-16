# Autoevaluación – Hands-On 4: Transformación de CSV a RDF (RML)

## 👤 Información del grupo
**Grupo:** **Group04**
**Integrantes:**
- Brais Gil – [@Menini10](hhttps://github.com/Menini10) 
- Gonzalo Hernández – [@gonzahv24](https://github.com/gonzahv24) 
- Pedro García – [@Pichurrin28](https://github.com/Pichurrin28) 

---

## 🎯 Objetivo de la Tarea
El objetivo principal de esta práctica fue aplicar los principios de **Linked Data** transformando el dataset limpio (`*-updated.csv`) en datos enlazados (RDF) mediante el uso de **RML Mappings**. Esto se logró:
1.  Definiendo mapeos RML que conectan las columnas del CSV con las clases y propiedades de nuestra ontología (`ns:`).
2.  Generando el grafo RDF resultante en sintaxis N-Triples.

---

## 1. Mapeo RML y Generación de RDF

### Cobertura del Modelo y Predicados

Describimos las decisiones tomadas en el mapeo RML:

* **Clases y Propiedades:** Se definieron dos Triples Maps principales, cubriendo las clases **`ns:Barrio`** y **`ns:MétricaTrimestral`** (asumiendo este nombre) y sus propiedades asociadas.
* **Prefijos y Vocabularios:** Todos los predicados del modelo se definieron usando el prefijo de la ontología **`ns:`**. También se incluyó el uso del prefijo **`time:`** para modelar correctamente los atributos temporales (Año, Trimestre).

### Generación de URIs y Literales

Explicamos cómo se generaron los identificadores y se trataron los datos:

* **Generación de URIs (Subject Map):** Utilizamos la columna **`ID_URI`** (creada en H-O 3) como plantilla para el **`rr:template`** dentro del `Subject Map`, creando URIs únicos siguiendo la estructura `http://data.smartcity.es/alquiler/metrica/{ID_URI}`. Esto respeta la estrategia Slash URI definida.
* **Tipificación de Literales:** Se asignaron tipos de dato explícitos a todos los literales, utilizando **`xsd:integer`** para `Año`, `Trimestre`, `Renta_min/med/max` y **`xsd:float`** para `m2`, `Dormitorios`, `Euros/m2` y `Desv_Tip`, asegurando la correcta tipificación del dato limpio.

---

## 📦 2. Entregables y Estructura

* **Archivo RML:** Exportado como `mappings.rml` y guardado en el subdirectorio `/mappings/`.
* **Archivo RDF:** Generado en sintaxis N-Triples como `barrios_rdf.nt` y guardado en el subdirectorio `/rdf/`.
* **Ubicación:** Se crearon los subdirectorios `/mappings` y `/rdf` y se verificó que todos los archivos están en la ubicación correcta dentro del repositorio del grupo.

---

## 💡 3. Reflexión y Dificultades

* **Dificultad Principal:** La dificultad o malentendido más grande fue al obtener el archivo rdf generado a partir de nuestro csv haciendo uso de yarrrml matey, ya que el rdf generado tenía unas 19000 líneas y no estábamos para nada seguros de que ese resultado se aproximase al resultado esperado. 
* **Lección Aprendida:** Lo más importante que hemos aprendido ha sido el cómo usar herramientas tan útiles como la mencionada yarrrml matey, ya que facilita mucho tareas que pueden ser pesadas, como la generación del archivo .rdf.

* **Dificultad Técnica Resuelta:** Nos encontramos con un problema al generar el RDF completo debido a que el CSV original usaba punto y coma (`;`) como separador y comas (`,`) para los decimales, lo que causaba conflictos con el parser de YARRRML/RML.
* **Solución:** Realizamos una limpieza adicional del CSV normalizando los separadores a comas (estándar CSV) y los decimales a puntos, lo que permitió generar correctamente las tripletas con los tipos de datos (Datatypes) correctos.
---

## Comentarios finales

Consideramos que el trabajo cumplió satisfactoriamente con los objetivos de la práctica. Conseguimos transformar el dataset tabular en un grafo RDF, conectando nuestras clases `ns:Barrio` y `ns:MétricaTrimestral` con éxito.

La práctica fue fundamental para:
* **Entender RML:** Aplicamos la sintaxis de mapeo para generar URIs y literales.
* **Cerrar el ciclo Linked Data:** Con la generación del archivo `.nt`, hemos completado el ciclo de transformación desde datos brutos hasta Linked Data.

Hemos subido todos los entregables (RML, NT, y este MD) en las ubicaciones especificadas, respetando los plazos de entrega.

---