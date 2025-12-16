# Autoevaluación – Hands-On 3: Limpieza y Transformación de Datos con OpenRefine

## 👤 Información del grupo
**Grupo:** **Group04**
**Integrantes:** - Brais Gil – [@Menini10](hhttps://github.com/Menini10) 
- Gonzalo Hernández – [@gonzahv24](https://github.com/gonzahv24) 
- Pedro García – [@Pichurrin28](https://github.com/Pichurrin28) 

---

## 🎯 Objetivo de la Tarea
El objetivo de esta práctica fue usar **OpenRefine** para limpiar y transformar nuestro conjunto de datos (CSV), aplicando las correcciones necesarias para eliminar inconsistencias de formato y preparar los datos para la siguiente etapa de generación de Linked Data.

---

## 🧹 1. Tareas de Limpieza y Transformación Realizadas

Hemos aplicado las siguientes operaciones clave a los datos en OpenRefine:

* **Normalización de Strings (Barrios):**
    * Utilizamos la función **`value.trim()`** en la columna **`barrio`** para eliminar espacios en blanco al inicio o al final de los nombres. Esto asegura que cada barrio tenga un identificador de texto único y consistente.
* **Conversión de Decimales y Tipo de Dato:**
    * Aplicamos la expresión GREL **`value.replace(",", ".")`** en las columnas **`dormitorios`**, **`banyos`**, **`euros_m2`** y **`desv_tipica`** para reemplazar la coma decimal por el punto decimal.
    * Posteriormente, convertimos todos los valores de estas columnas al **tipo numérico** (float) usando **`value.toNumber()`**.
* **Manejo de Valores Nulos e Inconsistencias:**
    * Identificamos valores nulos en la columna **`banyos`** y aplicamos una transformación para **imputar** esos valores, rellenándolos con la **media aritmética** de toda la columna.
    * Eliminamos filas donde la columna **`euros_m2`** contenía el valor `0`, ya que se consideró un error o *outlier* que distorsionaría los datos reales de renta.
    * **`desv_tipica`:** Revisamos esta columna que presentaba valores nulos y muy dispersos, y decidimos **mantener los valores nulos** (`null`) en el dataset final, ya que representan la ausencia de datos estadísticos fiables y una imputación podría distorsionar la interpretación de la renta media.
* **Preparación de URIs (Clave Única):**
    * Creamos una nueva columna llamada **`ID_URI`** concatenando los campos **`barrio`**, **`anyo`** y **`trimestre`** con un guion (`-`). Por ejemplo: `alipark-2020-4`. Esto proporciona un identificador único para generar los URIs de instancia según nuestra Estrategia de Nombrado.

---

## 📦 2. Entregables y Estructura

* **Archivo JSON de Operaciones:** * Hemos exportado el historial de transformaciones de OpenRefine a un archivo JSON y lo hemos subido al directorio `/openrefine/`.
* **Archivo CSV Actualizado:** * El dataset final, limpio y con la columna `ID_URI` lista, fue exportado como `*-updated.csv` y subido a `/csv/`.
* **Ubicación:** * Confirmamos que todos los entregables están en las carpetas correctas dentro del repositorio.

---

## 💡 3. Reflexión y Dificultades

* **Dificultad Principal:** La parte más delicada fue decidir la estrategia de **imputación** de los nulos en la columna `banyos` y tener que eliminar las filas con `euros_m2 = 0` para mantener la calidad del dataset.
* **Lección Aprendida:** La principal lección que nos llevamos es la potencia y la sencillez visual de OpenRefine para detectar y corregir errores de formato (como las comas decimales), algo que es tedioso de hacer manualmente.

---

## Comentarios finales

Consideramos que el trabajo cumplió satisfactoriamente con los objetivos de la práctica. La fase de limpieza de datos con OpenRefine resultó crucial para validar los problemas identificados en el Hands-On 2 (errores de formato, nulos) y transformarlos de manera eficiente.

La práctica fue fundamental para:
* **Asegurar la calidad del dato:** Garantizando que las columnas numéricas sean interpretadas correctamente en futuras etapas de generación RDF.
* **Facilitar la generación de URIs:** La creación de la columna **`ID_URI`** simplificará enormemente el proceso de vinculación de recursos en la siguiente práctica.

---