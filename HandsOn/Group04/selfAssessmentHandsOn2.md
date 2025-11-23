<<<<<<< HEAD
# Autoevaluación – Hands-On 2: Análisis del Dataset y Ontología

## Información del grupo
**Grupo:** Group04
**Integrantes:**
- Brais Gil – [@Menini10](hhttps://github.com/Menini10)  
- Gonzalo Hernández – [@gonzahv24](https://github.com/gonzahv24)  
- Pedro García – [@Pichurrin28](https://github.com/Pichurrin28)

---

## Objetivo de la tarea
El objetivo de esta práctica fue aplicar los primeros pasos para la generación de **Linked Data** a partir de los datasets seleccionados en la práctica anterior. Esto incluyó:
1.  Un análisis detallado del esquema y la licencia del conjunto de datos.
2.  La definición de la estrategia de **Nombrado de Recursos (URI)**.
3.  El desarrollo de una **Ontología ligera** (clases y propiedades) en formato OWL utilizando sintaxis *Turtle* (`.ttl`).

Durante esta actividad también se verificó la correcta ubicación de los entregables en el repositorio:
-   `analysis.html` en la raíz.
-   El archivo `*.ttl` en `/ontology/`.
-   Este archivo de autoevaluación en la raíz.

---

## Descripción del trabajo realizado
1.  **Análisis del Dataset y Licencia:**
    Se llevó a cabo un análisis profundo de la estructura del CSV, identificando las entidades principales, los tipos de datos y los rangos de valores. Se investigó la licencia original y se justificó la licencia elegida para los Linked Data generados. Toda esta información se documentó en `analysis.html`.

2.  **Definición de la Estrategia de Nombramiento (URI):**
    Se definió una estrategia clara y persistente para la construcción de los URIs, tanto para las clases y propiedades de la ontología, como para las futuras instancias de los datos. Se especificaron el dominio, el *namespace* y los patrones de ruta.

3.  **Desarrollo de la Ontología:**
    Se diseñó una ontología ligera que modela las entidades de los datasets seleccionados. Se definieron las clases y las propiedades de objeto y de dato, asegurando que cubrieran todos los campos relevantes. La ontología fue codificada en el archivo **`[Rellenar aquí: nombre_archivo].ttl`** usando la sintaxis Turtle.

4.  **Entrega:**
    Se consolidaron todos los documentos (`analysis.html`, `ontology.ttl`, `selfAssessmentHandsOn2.md`) y se subieron a las ubicaciones correctas en el directorio `Group04` en GitHub.

---

## Aprendizajes obtenidos
Durante el desarrollo de esta práctica aprendimos a:
-   Realizar un **análisis de esquema** previo a la modelización, clave para el diseño de ontologías.
-   Comprender la importancia de la **licencia** y su impacto en la publicación de datos abiertos como Linked Data.
-   Aplicar los principios de **Linked Data** en la definición de una estrategia de **Nombrado de Recursos (URI)** coherente y desreferenciable.
-   Modelar el conocimiento del dominio, traduciendo las columnas de un CSV a **clases y propiedades OWL/RDF**.
-   Utilizar la sintaxis **Turtle** para expresar una ontología de manera legible y estándar.

---

## Dificultades encontradas

-   **Modelado de la Ontología:** La dificultad principal fue trasladar las estructuras tabulares del CSV a un **grafo RDF**. Costó definir qué columnas debían convertirse en clases, cuáles en propiedades de objeto y cuáles en propiedades de dato, especialmente en el manejo de relaciones complejas. **[Rellenar aquí con un ejemplo concreto si lo hay, ej: "Nos costó distinguir entre una clase y un atributo de dato para la columna X."]**

-   **Selección del Vocabulario:** Decidir cuándo **reutilizar términos** de ontologías existentes (como Schema.org o FOAF) y cuándo crear términos propios (en nuestro *namespace*) requirió una investigación y discusión constante para asegurar la interoperabilidad.

-   **Formato y Sintaxis Turtle:** Aunque la sintaxis Turtle es legible, asegurar la **corrección y validación** del archivo `.ttl` (especialmente en cuanto a la definición correcta de dominios y rangos) requirió el uso de herramientas de validación y una curva de aprendizaje inicial.

-   **Estrategia de URI para Instancias:** Diseñar un patrón de URI que fuera **único, persistente** y **semánticamente significativo** para cada registro de datos, basándonos en los identificadores disponibles en el CSV, fue un reto considerable.

---

## Comentarios finales
Consideramos que el trabajo cumplió satisfactoriamente con los objetivos de la práctica. La fase de análisis fue exhaustiva, lo que facilitó el desarrollo de una ontología clara y bien estructurada. La práctica ha sido fundamental para entender cómo se conceptualiza la estructura de datos tabulares en el paradigma de **Linked Data**.

---
=======
# Autoevaluación – Hands-On 2: Análisis del Dataset y Ontología

## Información del grupo
**Grupo:** Group04
**Integrantes:**
- Brais Gil – [@Menini10](hhttps://github.com/Menini10)  
- Gonzalo Hernández – [@gonzahv24](https://github.com/gonzahv24)  
- Pedro García – [@Pichurrin28](https://github.com/Pichurrin28)

---

## Objetivo de la tarea
El objetivo de esta práctica fue aplicar los primeros pasos para la generación de **Linked Data** a partir de los datasets seleccionados en la práctica anterior. Esto incluyó:
1.  Un análisis detallado del esquema y la licencia del conjunto de datos.
2.  La definición de la estrategia de **Nombrado de Recursos (URI)**.
3.  El desarrollo de una **Ontología ligera** (clases y propiedades) en formato OWL utilizando sintaxis *Turtle* (`.ttl`).

Durante esta actividad también se verificó la correcta ubicación de los entregables en el repositorio:
-   `analysis.html` en la raíz.
-   El archivo `*.ttl` en `/ontology/`.
-   Este archivo de autoevaluación en la raíz.

---

## Descripción del trabajo realizado
1.  **Análisis del Dataset y Licencia:**
    Se llevó a cabo un análisis profundo de la estructura del CSV, identificando las entidades principales, los tipos de datos y los rangos de valores. Se investigó la licencia original y se justificó la licencia elegida para los Linked Data generados. Toda esta información se documentó en `analysis.html`.

2.  **Definición de la Estrategia de Nombramiento (URI):**
    Se definió una estrategia clara y persistente para la construcción de los URIs, tanto para las clases y propiedades de la ontología, como para las futuras instancias de los datos. Se especificaron el dominio, el *namespace* y los patrones de ruta.

3.  **Desarrollo de la Ontología:**
    Se diseñó una ontología ligera que modela las entidades de los datasets seleccionados. Se definieron las clases y las propiedades de objeto y de dato, asegurando que cubrieran todos los campos relevantes. La ontología fue codificada en el archivo **`[Rellenar aquí: nombre_archivo].ttl`** usando la sintaxis Turtle.

4.  **Entrega:**
    Se consolidaron todos los documentos (`analysis.html`, `ontology.ttl`, `selfAssessmentHandsOn2.md`) y se subieron a las ubicaciones correctas en el directorio `Group04` en GitHub.

---

## Aprendizajes obtenidos
Durante el desarrollo de esta práctica aprendimos a:
-   Realizar un **análisis de esquema** previo a la modelización, clave para el diseño de ontologías.
-   Comprender la importancia de la **licencia** y su impacto en la publicación de datos abiertos como Linked Data.
-   Aplicar los principios de **Linked Data** en la definición de una estrategia de **Nombrado de Recursos (URI)** coherente y desreferenciable.
-   Modelar el conocimiento del dominio, traduciendo las columnas de un CSV a **clases y propiedades OWL/RDF**.
-   Utilizar la sintaxis **Turtle** para expresar una ontología de manera legible y estándar.

---

## Dificultades encontradas

-   **Modelado de la Ontología:** La dificultad principal fue trasladar las estructuras tabulares del CSV a un **grafo RDF**. Costó definir qué columnas debían convertirse en clases, cuáles en propiedades de objeto y cuáles en propiedades de dato, especialmente en el manejo de relaciones complejas. **[Rellenar aquí con un ejemplo concreto si lo hay, ej: "Nos costó distinguir entre una clase y un atributo de dato para la columna X."]**

-   **Selección del Vocabulario:** Decidir cuándo **reutilizar términos** de ontologías existentes (como Schema.org o FOAF) y cuándo crear términos propios (en nuestro *namespace*) requirió una investigación y discusión constante para asegurar la interoperabilidad.

-   **Formato y Sintaxis Turtle:** Aunque la sintaxis Turtle es legible, asegurar la **corrección y validación** del archivo `.ttl` (especialmente en cuanto a la definición correcta de dominios y rangos) requirió el uso de herramientas de validación y una curva de aprendizaje inicial.

-   **Estrategia de URI para Instancias:** Diseñar un patrón de URI que fuera **único, persistente** y **semánticamente significativo** para cada registro de datos, basándonos en los identificadores disponibles en el CSV, fue un reto considerable.

---

## Comentarios finales
Consideramos que el trabajo cumplió satisfactoriamente con los objetivos de la práctica. La fase de análisis fue exhaustiva, lo que facilitó el desarrollo de una ontología clara y bien estructurada. La práctica ha sido fundamental para entender cómo se conceptualiza la estructura de datos tabulares en el paradigma de **Linked Data**.

---

**Valoración General del Trabajo (1: No cumple, 5: Excelente):** **[Rellenar aquí: 4 o 5]**
>>>>>>> ee2d8f37e97607626d85d24960be63dad22fcae3
