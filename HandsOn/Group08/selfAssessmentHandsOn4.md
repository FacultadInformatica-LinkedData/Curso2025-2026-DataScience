# Self Assessment Hands-on 4

## RDF File Quality
- [x] Uses the .ttl extension.
- [x] Is serialized in the Turtle format.
- [x] Follows the resource naming strategy (e.g., http://group08.data/resource/...).
- [x] Uses class and property URIs that are the same as those used in the ontology (`ns:Station`, `ns:hasName`, etc.).

## URI Quality
- [x] Is "readable" and has some meaning (e.g., `.../Station/1406`).
- [x] Is not encoded as a string.
- [x] Does not contain a double slash.

## Individual Quality
- [x] Has a type (`rdf:type ns:Station`).
- [x] Has properties matching the CSV columns.

## Value Quality
- [x] Is trimmed (no whitespace around values).
- [x] Is properly encoded (integers for bikes, float for coords).
- [x] Includes its datatype (`^^xsd:integer`, `^^xsd:float`).