# Hands-on Assignment 5 – Self Assessment

**Group:** 07
**Dataset:** Air Quality in Madrid (2024)

This assignment focused on linking our dataset with external Linked Open Data sources (Wikidata) and regenerating the RDF including those links.

## Checklist

## 1. Linking Operations (OpenRefine)
- Reconciled the `pollutantCode` column with Wikidata (type: chemical entity).
- Validated matches and created a new column `pollutantWikidataURI_full`.
- Exported:
  - Operations → `lodrefine/air_quality_with-links.json`
  - Updated CSV → `csv/air_quality_madrid_2024_updated_with-links.csv`

✔ Linking step completed.

## 2. Updated RML Mapping
- Added Wikidata links using:
  ```yml
  - p: owl:sameAs
    o:
      value: $(pollutantWikidataURI_full)
      type: iri
  ```
- Ensured correct datatypes and URI templates.
- Saved as `mappings/air_quality_with-links.rml`.

✔ Mapping correctly updated.

## 3. RDF Generation
- Generated RDF 
- Output: **306,268 triples**, including all `owl:sameAs` links.

✔ RDF successfully produced.

## 4. SPARQL Validation
Created `rdf/queries-with-links.sparql` including:
- Query for pollutants + Wikidata links
- Query counting observations per pollutant
- Query joining observations with stations and pollutants
- Query validating presence of `owl:sameAs`
- Query checking stations appear in observations

✔ All validation queries implemented.

## 5. Folder Structure
All required files placed correctly:

```
lodrefine/air_quality_with-links.json
csv/air_quality_madrid_2024_updated_with-links.csv
mappings/air_quality_with-links.rml
rdf/air_quality-with-links.ttl
rdf/queries-with-links.sparql
```

✔ Folder structure according to plan