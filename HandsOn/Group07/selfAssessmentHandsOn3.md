# Hands-on assignment 3 – Self assessment

**Group:** 07  
**Dataset:** Air Quality in Madrid (2024)

## Checklist

**Every resource described in the CSV file:**

- [x] Has a unique identifier in a column (not an auto-increased integer)  
  - Each row includes the `observationID` column (e.g., `28079004_6_48_2024_01`), which identifies every `aq:AirQualityObservation`.

- [x] Is related to a class in the ontology  
  - Each row corresponds to an instance of `aq:AirQualityObservation`.

**Every class in the ontology:**

- [x] Is related to a resource described in the CSV file  
  - The CSV provides instances of `aq:AirQualityObservation`, which are connected to `aq:Station` and `aq:Pollutant` through object properties.

**Every column in the CSV file:**

- [x] Is trimmed  
  - All text fields were cleaned using `value.trim()`.

- [x] Is properly encoded (e.g., dates, booleans)  
  - `year` and `month` are numeric, daily values (`D01–D31`) are numbers, special characters and blanks were removed.

- [x] Is related to a property in the ontology  
  - Column mappings:  
    - `stationCode` -> `aq:hasStation`  
    - `pollutantCode` -> `aq:measuresPollutant`  
    - `D01–D31` -> `aq:hasValue` (for each day)  
    - Coming from `year` and `month` -> `aq:hasDate`  
    - (Unit values, if added later) -> `aq:hasUnit`

**Every property in the ontology:**

- [x] Is related to a column in the CSV file    
    - `aq:hasStation` <-> `stationCode`  
    - `aq:measuresPollutant` <-> `pollutantCode`  
    - `aq:hasValue` <-> `D##` daily columns  
    - `aq:hasDate` <-> Coming from `year`, `month`, and day number  
    - `aq:hasUnit` <-> implicit (same unit type for all pollutants)

## Comments on the self-assessment

All data was cleaned in OpenRefine:

- Removed redundant columns (`PROVINCIA`, `MUNICIPIO`, `V01–V31`).  
- Renamed column names to English and made identifiers more standard.  
- Replaced “N” and missing values with blanks.  
- Converted daily measurement columns (`D01–D31`) to numeric values.  
- Created `observationID` as a key (`samplingPoint_year_month`) to serve as the RDF URI fragment for each `aq:AirQualityObservation`.
