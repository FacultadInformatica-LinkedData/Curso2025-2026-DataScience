# Self-Assessment Hands-On 4

## Every RDF file
- Cumple la extensión `.ttl`.
- Está serializado correctamente en Turtle.
- Sigue la resource naming strategy definida.
- Utiliza las URIs de clases y propiedades exactamente iguales a las de la ontología.

## Every URI in the RDF files
- Es legible y tiene significado (no se usan identificadores auto-incrementados).
- No está codificada como cadena.
- No contiene doble slash (“//”) salvo en el esquema del IRI.

## Every individual in the RDF files
- Tiene un label con el nombre del individuo.
- Tiene un tipo (`rdf:type`) correctamente asignado.

## Every value in the RDF files
- Está trimmeado.
- Está correctamente codificado (incluye fechas, números, etc.).
- Incluye su datatype.
- Usa el datatype correcto en cada caso.