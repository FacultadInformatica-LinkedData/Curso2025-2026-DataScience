# Autoevaluación — Hands-on 2 (Group03)

## Entregables
- analysis.html con el análisis de datos, licencia y estrategia de URIs.
- ontology/ontology.ttl con la ontología en Turtle.
- Este documento de autoevaluación.

## Lo que analizamos
- Esquema del CSV y calidad de datos (separador ;, codificación ISO 8859-1, nulos/“0”, rangos y CRS de coordenadas).
- Licencia y derechos: CC BY 4.0; atribución obligatoria a Comunidad de Madrid.
- Estrategia de URIs: dominio smartcity de Group03, patrones estables basados en centro_codigo, slugs para municipios/distritos.

## Ontología
- Clases: CentroEducativo, Municipio, Distrito, Titularidad, TipoCentro.
- Propiedades: ubicación (municipio/distrito), titularidad, tipo de centro, dirección, contacto, estado, fecha.
- Vocabularios: RDFS/OWL, DCTERMS/DCAT (metadatos), SKOS (controlados), WGS84 (coordenadas si se convierten).

## Decisiones clave
- Usar centro_codigo como identificador estable para URIs de centros.
- Mantener CC BY 4.0 en el RDF generado con clara atribución a la fuente.
- Normalizar valores (municipio, teléfonos, situación) y documentar transformaciones.

## Retos y mitigaciones
- Valores “0” en teléfonos y CP “00000” → convertir a nulo y validar.
- Coordenadas X/Y sin lat/long → confirmar CRS y convertir a WGS84.
- Nombres con coma (“Acebeda, La”) → normalización de toponimia y creación de slugs consistentes.