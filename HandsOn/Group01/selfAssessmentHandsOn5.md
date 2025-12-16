# Autoevaluación – Hands-On Assignment 5
En esta quinta entrega hemos trabajado en la reconciliación y vinculación de datos abiertos sobre accidentes de tráfico en Madrid.
El objetivo era garantizar que cada recurso descrito en el CSV tuviera un URI, estuviera vinculado con recursos externos en Wikidata y que las columnas del dataset se transformaran en propiedades RDF de acuerdo con el modelo definido.

## Archivos entregados

1. updated2.csv  
   - Dataset depurado y reconciliado en OpenRefine.  
   - Se añadió la columna `same_as_wikidata_distrito` con URIs de Wikidata para los distritos.  

2. mapping.rml  
   - Archivo de mapeo RML extendido.
   - Se verificó la sintaxis y se probó con RMLMapper.  

3. accidentes-links.ttl  
   - RDF generado a partir del CSV y el mapping.  
   
4. queries-with-links.sparql  
   - Archivo SPARQL con consultas para validar los enlaces.  
   - Incluye queries que listan accidentes con sus distritos, cuentan accidentes por distrito y verifican la presencia de `owl:sameAs`.

## Conclusión

El grupo ha cumplido los objetivos del Hands-On 5 de forma completa:  
- Se logró reconciliar la columna `distrito` con Wikidata y enlazarla mediante `owl:sameAs`. Se intentó ademas reconciliar la columna de calles pero no se pudo por la sintaxis de la columna. 
- Se generó correctamente el RDF con RMLMapper usando Java 25.  

Además, hemos aprendido a:  
- Ejecutar RMLMapper en un entorno actualizado de Java.  
- Validar RDF mediante consultas SPARQL.  
- Documentar el proceso con claridad y preparar los archivos requeridos para la entrega.
