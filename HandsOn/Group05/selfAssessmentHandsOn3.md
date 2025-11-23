# selfAssessmentHandsOn3.md  
### Hands-on 3 — Cleaning and Preparation  
**Grupo:** Group05  
**Ontología:** AirQualityOntology.ttl
**Dataset:** calidad-aire-4318-y-otros-mod-updated.csv

---

## 1. Descripción del dataset
El dataset contiene **mediciones de calidad del aire** procedentes de estaciones de monitoreo en Madrid (OpenAQ/EEA).
Cada fila representa una **medición puntual de un contaminante** en una ubicación y momento específicos.

**Columnas principales:**
- `id`: identificador único generado (location_id + datetimeUtc + parameter).
- `parameter`: contaminante medido (NO₂, O₃, PM10, etc.).
- `value`: valor numérico de la medición.  
- `unit`: unidad de medida.  
- `datetimeUtc`: fecha y hora UTC.  
- `timezone`: zona horaria local.  
- `latitude`, `longitude`: coordenadas geográficas.  
- `location_name_rdf`: nombre normalizado de la estación.

---

## 2. Operaciones de limpieza y preparación en OpenRefine

| Tipo de operación | Descripción | Expresión GREL / Acción |
|-------------------|--------------|--------------------------|
| **Creación de columna `id`** | Se genera un identificador único concatenando las columnas `location_id`, `datetimeUtc` y `parameter`. | `cells["location_id"].value + "_" + cells["datetimeUtc"].value + "_" + cells["parameter"].value` |
| **Eliminación de columnas** | Se eliminaron columnas no necesarias para el modelo RDF: `location_id`, `location_name`, `datetimeLocal`, `provider`. | — |
| **Limpieza de texto** | Se aplicó `value.trim()` para eliminar espacios en blanco en todas las columnas relevantes: `id`, `location_name_rdf`, `parameter`, `value`, `unit`, `datetimeUtc`, `timezone`, `latitude`, `longitude`. | `value.trim()` |
| **Verificación de unicidad de `id`** | Cada fila tiene un identificador único tras la concatenación. | — |
| **Control de tipos de datos** | Las columnas `value` (decimal) y `datetimeUtc` (fecha ISO) se verificaron en formato correcto. | — |

 **Resultado:**  
El dataset queda limpio, con todas las columnas normalizadas, sin espacios extra, con identificadores únicos y preparado para transformación RDF.

---

## 3. Relación con la ontología `AirQualityOntology`

| Clase | Descripción | Fuente CSV |
|--------|--------------|-------------|
| `Medicion` | Observación puntual de un contaminante | Cada fila del dataset |
| `Ubicacion` | Estación o punto de medición | `location_name_rdf`, `latitude`, `longitude` |
| `Contaminante` | Sustancia medida | `parameter` |

| Propiedad | Dominio | Rango | Columna CSV |
|------------|----------|--------|--------------|
| `valor` | `Medicion` | `xsd:decimal` | `value` |
| `unidad` | `Medicion` | `xsd:string` | `unit` |
| `fechaHora` | `Medicion` | `xsd:dateTime` | `datetimeUtc` |
| `tieneId` | `Medicion` | `xsd:string` | `id` |
| `tieneZonaHoraria` | `Medicion` | `xsd:string` | `timezone` |
| `enUbicacion` | `Medicion` | `Ubicacion` | `location_name_rdf` |
| `mideParametro` | `Medicion` | `Contaminante` | `parameter` |

---

## 4. Validación del dataset limpio
- Todas las celdas se encuentran sin espacios ni caracteres no deseados.  
- Los tipos de datos (`decimal`, `string`, `dateTime`) son consistentes.  
- El identificador `id` es **único y persistente**.  
- Cada clase y propiedad de la ontología tiene correspondencia en el CSV.  
- Dataset listo para su transformación RDF con OpenRefine RDF extension.

---

## 5. Evaluación final

| Criterio | Cumple | Comentario |
|-----------|:------:|------------|
| Cada recurso tiene identificador único | Sí | Generado con concatenación de 3 campos |
| Cada clase tiene instancia en el CSV |  Sí | Medición, Ubicación, Contaminante |
| Cada columna tiene propiedad RDF asociada | Sí | Definidas en la tabla anterior |
| Columnas limpias y tipadas | Sí | value.trim aplicado y verificado |
| Dataset listo para exportar a RDF | Sí | Validado conforme a AirQualityOntology |

---

📁 **Archivos entregados:**
- `/csv/calidad-aire-4318-y-otros-mod-updated.csv`
- `/openrefine/history.json`
- `AirQualityOntology.ttl`
- `selfAssessmentHandsOn3.md`
