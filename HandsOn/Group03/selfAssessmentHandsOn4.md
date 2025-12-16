# Self-assessment Assignment 4 (Grupo 3)

## Entregables
- Archivo RML con el mapeado empleado para crear el RDF en la carpeta "mappings".
- Archivo RDF con la sintaxis de Turtle que contiene la información del CSV transformada a RDF en la carpeta "rdf".
- Archivo SPARQL con ejemplos de queries que se pueden realizar sobre el RDF creado bajo la carpeta "rdf".
- Se ha actualizado el archivo ontology.ttl en la carpeta "ontology" para mejorar el RDF generado.

## Desarrollo de la tarea
El objetivo principal de este assigment era crear un grafo de conocimiento a través de la información del CSV. Para ello hemos usado RML para la transformación del CSV al RDF. 

Antes de empezar a crear el archivo RML se han hecho unas modificaciones en el archivo "ontology.ttl" eliminando la clase que contenia la titularidad pues como esta solo puede ser privada o pública no hay necesidad de crear una clase para eso. Además, a las clases de distrito y municipio se les ha añadido una propiedad para obtener su nombre y otra para obtener su código, también, se ha modificado la clase para que se cree la URI se cree usando el código pues este es único. Por último, se han modificado los tipos de algunos objetos como los códigos para que sean números enteros.

Tras modificar la ontología, se ha procedido a la creación del RML siguiendo la estructura de la ontología. Por cada clase se ha creado un TriplesMap donde se define como va a ser la URI del sujeto y posteriormente se definen sus propiedades, eligiendo en cada propiedad la columna del CSV de la que se va a extraer la información. Una vez terminado el RML, este ha sido compilado con RMLMapper para crear el archivo RDF con sintaxis Turtle que contiene la información del grafo de conocimiento.

## Retos y complicaciones
- Uno de los mayores retos de esta tarea ha sido elegir que compilador emplear para transformar el RML a RDF pues cada compilador tenía sus pros y sus contras, sin embargo, tras investigar un poco más nos decantamos por RMLMapper pese a que su uso pueda ser algo más complicado que otros.
- Otro reto que tuvimos fue elegir que datos se merecían tener su porpia clase o ser un literal, al final decidimos que solo el distrito y el municipio fueran clases separadas.