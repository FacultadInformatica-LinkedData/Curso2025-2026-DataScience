# Hands-on Assignment 4 – Self Assessment

**Group:** 07
**Dataset:** Air Quality in Madrid (2024)

## Checklist

**Every RDF file:**

* [x] Uses the `.ttl` extension

  * The final RDF output is stored as `rdf/air_quality.ttl`.

* [x] Is serialized in the Turtle format

  * Prefixes, IRIs, and triples follow valid Turtle syntax.

* [x] Follows the resource naming strategy

  * URIs follow the agreed pattern:
    `https://carloscumbrado.github.io/HandsOn/group07/resource/<Class>/<ID>`.

* [x] Uses class and property URIs from the ontology

  * All classes and properties in the RDF (`aq:AirQualityObservation`, `aq:Station`, `aq:Pollutant`, etc.) come directly from our ontology.

---

**Every URI in the RDF files:**

* [x] Is readable and has meaning

  * Example: `.../Observation/28079004_12_8_2024_01` clearly identifies the resource.

* [x] Is not encoded as a string

  * All URIs are IRIs, not literal values.

* [x] Does not contain a double slash (`//`)

  * Confirmed in the RDF output.

---

**Every individual in the RDF files:**

* [x] Has a label with the name of the individual

  * Each individual includes an `rdfs:label`.

* [x] Has a type

  * Each individual is assigned to a class using `rdf:type`.

---

**Every value in the RDF files:**

* [x] Is trimmed

  * The CSV was cleaned during Assignment 3 to ensure no leading/trailing spaces.

* [x] Is properly encoded

  * Dates are typed as `xsd:date`, measurements as `xsd:float`, and units as `xsd:string`.

* [x] Includes its datatype

  * All literals contain explicit datatype annotations.

* [x] Uses the correct datatype

  * Numeric values use `xsd:float`; dates use `xsd:date`; labels and units use `xsd:string`.

---

## Comments on the self-assessment

* The RML mapping was made to match with the ontology created in Assignment 2.
* Each observation was modeled as an instance of `aq:AirQualityObservation` with multiple daily values attached via `aq:hasValue`.
* Stations and pollutants were generated as independent individuals and linked to each observation.
* All generated individuals include readable labels and consistent URIs following the group naming strategy.
* The final RDF results were validated using custom SPARQL queries included in `rdf/queries.sparql`.
