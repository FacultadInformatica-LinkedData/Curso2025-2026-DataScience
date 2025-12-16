# Self Assessment — Hands-on 4  
**Grupo:** Group02
**Tema:** Transformación de CSV a RDF mediante RML

## 1. Definición y comprensión de los mapeos RML

En este hands-on aprendimos a transformar datos CSV a RDF usando **RML** y la herramienta **Morph-KGC**.  
Entendimos cómo funcionan los elementos clave del modelo:

- `rml:LogicalSource`
- `rr:TriplesMap`
- `rr:SubjectMap`
- `rr:PredicateObjectMap`
- `rr:ObjectMap` y `rml:reference`
- Uso de `rr:template` para construir URIs

El objetivo era describir los datos del dataset de BiciMAD usando nuestra ontología “bike”.

---

## 2. Archivos creados en el proyecto

### ✓ Archivo RML (`/mappings/mapping.rml`)
Creamos un archivo de mapeo donde definimos:

- La fuente `bicimad-updated.csv`
- Dos TriplesMap:
  - Bicis usadas por día
  - Sistema de bicicletas compartidas
- URIs generadas por plantilla basadas en fechas
- Propiedades con tipos de datos (`xsd:integer`, `xsd:double`, `xsd:dateTime`…)

El archivo es sintáctica y estructuralmente correcto.

---

### ✓ Archivo YML (opcional) (`/mappings/mapping.yml`)
Incluimos un archivo para permitir la ejecución con Morph-KGC, indicando:

- Ruta de entrada del CSV  
- Archivo de mapeo RML  
- Archivo RDF de salida  

---

### ✓ Archivo RDF (`/rdf/data.nt`)
Generamos un archivo N-Triples con más de 29.000 triples, validado sin errores.  
Comprobamos:

- Sintaxis correcta  
- URIs generadas correctamente  
- Tipos de datos consistentes  
- Relación entre entidades según los mapeos  

---

## 3. Validación del trabajo

Las validaciones realizadas incluyeron:

- Carga del `.nt` en un triplestore
- Consultas SPARQL simples (filtrar fechas, contar triples…)
- Comprobación de los namespaces y de la estructura de los sujetos creados
- Verificación de los mapeos mediante un parser de RDF/Turtle

---

## 4. Dificultades encontradas

- Ajuste de rutas relativas para Morph-KGC  
- Diferencias entre `rml:reference` y `rr:constant`  
- Decidir la URI base y las plantillas adecuadas  
- Verificar tipos de datos para evitar errores silenciosos  

---

## 5. Valoración personal

Este hands-on permitió:

- Comprender la transformación de datos tabulares a RDF  
- Aprender a escribir y depurar mappings RML  
- Conectar la ontología creada en prácticas previas con datos reales  

