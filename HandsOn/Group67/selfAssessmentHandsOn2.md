# Self-Assessment — Hands-On 2 (Group 67)

## Dataset
He mantenido el dataset de las *fuentes públicas de Madrid* del Hands-On 1.  
He comprobado que sigue cumpliendo los requisitos del dominio Smart City y tiene datos abiertos y reutilizables.

## Transformación a RDF
He transformado el CSV a RDF usando *OpenRefine con la extensión RDF*.  
He definido cada fuente como "schema:Place" y he aplicado vocabularios estándar como *schema.org*,*geo* y *dcterms*.  
He añadido las coordenadas en un nodo "schema:geo" con "geo:lat" y "geo:long".

## Enlazado (Linked Data)
He reconciliado las columnas *DISTRITO* y *BARRIO* con *Wikidata* mediante "reconci.link/es".  
He enlazado la mayoría de valores con URIs externas y he creado URIs internas para los que no tenían coincidencia.

## Herramientas
He usado *OpenRefine 3.7*, la *extensión RDF* y el servicio de reconciliación de *Wikidata*.  
He verificado el resultado en el *RDF Preview* y lo he exportado como "fuentes202510.ttl".

## Evaluación
He aprendido a pasar datos CSV a RDF y a enlazarlos con otros conjuntos.  
El proceso me ha ayudado a entender mejor cómo funciona el Linked Data y los vocabularios semánticos.
