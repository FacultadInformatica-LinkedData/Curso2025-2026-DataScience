# Self-Assessment — HandsOn 2 (Grupo Calidad Aire Madrid)

## 1) ¿Qué entregamos?
- [x] `analysis.html` en la raíz con:
  - Análisis del dataset (esquema y valores)
  - Licenciamiento de la fuente y licencia propuesta
  - Estrategia de nombrado de recursos
- [x] Ontología en Turtle (`ontology/AirQualityOntology.ttl`)
- [x] Instanciación de ejemplo en Turtle (`ontology/AirQualityOntology-example.ttl`)
- [x] Este auto-evaluación (`selfAssessmentHandsOn2.md`)

## 2) Estrategia de nombrado
- **Dominio base**: `http://linkeddata.grup05.es/CalidadAireMadrid/`
- **Ontología**: `ontology/AirQualityOntology#` (hash para términos)
- **Datos/recursos**: `resource/{Clase}/{id}` (slash para instancias)
- **Ejemplos**:
  - `http://linkeddata.grup05.es/CalidadAireMadrid/ontology/AirQualityOntology#Medicion`
  - `http://linkeddata.grup05.es/CalidadAireMadrid/resource/Medicion/obs-2025-11-03T10-00-00Z-no2-28079004`

## 3) Ontología (qué incluye)
- **Clases**: `aq:Medicion`, `aq:Ubicacion`, `aq:Contaminante`
- **OP**: `aq:enUbicacion (Medicion→Ubicacion)`, `aq:mideParametro (Medicion→Contaminante)`
- **DP**: `aq:valor (xsd:decimal)`, `aq:unidad (xsd:string)`, `aq:fechaHora (xsd:dateTime)`
- **Convenciones**: Clases en *UpperCamelCase*, propiedades en *lowerCamelCase*

## 4) Instanciación de ejemplo
- Usa **solo individuos** (sin definir términos ontológicos).
- Crea 2 *Ubicaciones*, 2 *Contaminantes* y 2 *Mediciones*.
- Cumple dominios/rangos y tipos de datos.
- Mantiene idioma coherente (`@es`) y unidades en texto.

## 5) Licenciamiento y reutilización
- El dataset fuente tiene licencia abierta (ver `analysis.html`).
- La ontología y ejemplos se publican con licencia permitida.
- Reutilizamos vocabularios estándar: **SOSA/SSN** y **Schema.org** (para clases equivalentes y subclases).

## 6) Validación y checks
- [v] Archivo `.ttl` válido (sintaxis Turtle).
- [v] No mezcla de etiquetas en distintos idiomas.
- [v] Sin dominios/rangos múltiples.
- [v] Al menos 1 clase enlazable a otras entidades (Ubicación/Contaminante).
- [v] `*-example.ttl` **no** redefine clases/propiedades.
