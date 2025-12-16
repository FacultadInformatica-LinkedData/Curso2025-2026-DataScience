Self-Assessment GROUP14

En esta fase del trabajo hemos generado el RDF que contiene las tripletas (NTriples) de los datos pertenecientes a nuestros csv. También para todo el trabajo hemos usado un mismo mapping a pesar de usar dos csv.

Primero, con la herramienta https://rml.io/yarrrml/matey/, pasando algunas líneas de cada uno de nuestros csv en data sources, y escribiendo las reglas YARRRML correspondientes, generamos las reglas RML, basandonos en la ontologia creada anteriormente y utilizando como ejemplo la que aparece en las diapositivas.

Ya con el documento RML hecho, con Morph, usando el ejemplo que se nos ha proporcionado, y modificando la información con la nuestra (modificando el mapping y los datos), hemos creado el RDFLib.

Con el RDFLib creado hemos probado algunas querys para ver si nos funcionan.
Por ejemplo:
querry="""
SELECT ?s ?p ?o
WHERE {
  ?s ?p ?o
}"""
De esa forma podemos ver que nuestro RDF esta correctamente creado.
