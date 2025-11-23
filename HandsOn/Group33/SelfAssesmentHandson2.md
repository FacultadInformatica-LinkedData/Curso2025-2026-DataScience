## Autoevaluación — Práctica 2 (Group33)

### Entregables

* `analysis.html` – Análisis del dataset, licencia y URIs.
* `ontology/ontology.ttl` – Ontología RDF en formato Turtle.

### Análisis del dataset

El dataset **“Aforos de tráfico en la ciudad de Madrid (estaciones permanentes)”** del portal [datos.madrid.es](https://datos.madrid.es) se usó como base.
El archivo CSV (`DATOS_ESTACIONES_MARZO_2025.csv`) 


### URIs

Se usa el dominio del grupo:
`https://group33.github.io/trafico-madrid/`
Patrones:

* Estaciones → `/estacion/{codigo}`
* Mediciones → `/medicion/{codigoEstacion}/{fecha}`
