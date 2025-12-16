# Hands On 4

Para esta cuarta entrega, hemos empleado las herramientas de mapeo RML y morph-kgc para transformar nuestros datos CSV a RDF.

Antes de todo ello, hemos analizado como grupo la estructura de nuestra ontología y las columnas de nuestro CSV, identificando las 11 propiedades que debíamos mapear y los tipos de datos correspondientes.

Tras dicho análisis, creamos los archivos de mapeo en formatos RML y YARRRML. Luego, usando la librería morph-kgc, generamos un archivo .nt que ya es rdf con sus respectivas tripletas.

### Archivos subido

- Mappings RML y YARRRML (`mappings/`), hospitales.rml y hospitales.yml

- Archivo RDF generado (`rdf/hospitales.nt`)

- HandsOn 4

## Conclusión

Durante el transcurso de esta práctica hemos aprendido el proceso completo de generación de Knowledge Graphs: desde el mapeo de datos crudos hasta su transformación en RDF. Hemos aprendido el uso de RML/YARRRML y a usar la libreria morph-kgc para transformar nuestros datos CSV a RDF.
