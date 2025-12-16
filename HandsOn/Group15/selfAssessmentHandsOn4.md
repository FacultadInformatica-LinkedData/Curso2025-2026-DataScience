# Autoevaluación Entrega 4 Práctica  – Grupo15

## Resumen del trabajo realizado.
En esta cuarta entrega nuestro objetivo era, convertir nuestro archivo csv a RDF, usando RML.

## Acciones detalladas
1.- Hemos empezado con la creación del RML.
Para ello hemos analizado las columnas del CSV y las hemos relacionado con sus propiedades correspondientes en la ontología. Generamos cuatro TriplesMasps ( Biblioteca, Dirección, Barrio y Distrito), cada uno con su sujeto, propiedades literales y sus relaciones con las otras entidades.

2.- A partir del RML, lo hemos usado para crear un fichero YARRRML (.yml), que contiene los mismos mappings que el RML, pero de una forma más sencilla y legible. 

3.- Una vez escrito el .yml hemos comprobado su validez con http://www.yamllint.com/.

4.- Una vez comprobado, hemos transformado el .yml a un fichero RDF usando la pagina https://rml.io/yarrrml/matey/ proporcionada en las transparencias de la sesión.

## Dificultades
Hemos experimentado tanto alguna dificultad a la hora de formar las tripletas por su formato en la ontología y a la hora de hacer el data transforming en YARRRNL Matey para subir el data source con el que generar el RDF.


## CONCLUSIÓN 
Hemos conseguido crear una estructura de información lista para hacer que los datos sean interoperables entre apps, permitir consultas SPARQL... mediante la transformación de estructuras de mapeo como los RML y YARRRML.