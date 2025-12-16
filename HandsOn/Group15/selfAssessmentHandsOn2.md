
# Hands-On 2 - Self-Assesment (Group15)

En este documento resumimos y recopilamos los pasos realizado en esta segunda práctica (Hands-On 2)

| Entregable | Ruta | Descripción |
|-------------|------|-------------|
| ✅ `analysis.html` | `/HandsOn/Group15/analysis.html` | Análisis del dataset, estudio de licencia y estrategia de URIs. |
| ✅ `bibliotecas.ttl` | `/HandsOn/Group15/ontology/bibliotecas.ttl` | Ontología OWL/Turtle desarrollada con prefijo `bib:`. |

Además de este documento

---

## 1.- Ánalisis de los datos (`analysis.html`)

**1.1.- Resumen**
Se recogen una serie de datos relevantes del conjunto como el número de registros, el número de columnas, ámbito, coordenadas, ubicabilidad o Wi-Fi.


**1.2- Esquema (principales columnas)**
En este apartado se apilan los nombres de la principales columnas junto con su tipo y una descripción de este, así como su uso RDF.


**1.3.- Calidad de datos**

**Puntos fuertes:**
- Análisis completo y estructurado, en formato claro y visual (HTML con tablas y secciones).
- Identificación explícita de campos clave (`LATITUD`, `LONGITUD`, `EQUIPAMIENTO`, `DISTRITO`, `BARRIO`).
- Inclusión de buenas prácticas para direcciones (reutilización de `schema:PostalAddress`).
- Se documenta la heurística de detección de Wi-Fi en texto libre.

**Aspectos mejorables:**
- El campo `ACCESIBILIDAD` requiere un catálogo de códigos para su normalización.
- `HORARIO` debería representarse en un modelo horario estándar (`schema:openingHoursSpecification`).
- Añadir valores cuantitativos reales de conteo de distritos y barrios.



## 2.- Análisis de licencia de la fuente 

**Cumplimiento:**
- Se identifica la fuente original: Ayuntamiento de Madrid (portal de datos abiertos y datos.gob.es).
- Se describe la política de reutilización del sector públic (atribución, integridad, actualización).
- Se propone la licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)** para los datos RDF generados.
- Se justifica su elección por compatibilidad con la publicación y reutilización abierta.



## 3.- Estrategia de nombrado de recursos (URIs)

Este punto los hemos dividido en tres apartados definiendo lo siguiente:

**Dominio y rutas:**
- Dominio base: `https://group15.linkeddata.es/`
- Espacios diferenciados:
  - `/ontology/` → clases y propiedades  
  - `/resource/` → instancias de datos
  
- **Patrones:**
  - `…/ontology/bibliotecas#Biblioteca` (clases y propiedades)
  - `…/resource/biblioteca/{PK}` (instancias de bibliotecas)
  - `…/resource/distrito/{slug-distrito}`
  - `…/resource/barrio/{slug-barrio}`
- Reglas de `slug`: minúsculas, sin acentos, con guiones.

**Negociación de contenido**
Si el servidor lo permite, servir HTML por defecto y RDF (Turtle/JSON-LD) por content negotiation.



## 4.- Ontología (bosquejo para Hands-On 2)

Nuestra ontología (ligera) está escrita en OWL usando el formato Turtle, y utilizamos el prefijo bib: que apunta al dominio https://group15.linkeddata.es/ontology/bibliotecas#. Esta contiene clases principales como **bib:Biblioteca** → subclase de `schema:Library`; propiedades de objeto - `bib:estaEnDistrito` (`Biblioteca` → `Distrito`); y propiedades de datos como - `bib:email` ↳ subPropertyOf `schema:email`.



## 5.- Trazabilidad
- `analysis.html` correctamente visualizable en navegador (UTF-8).  
- `bibliotecas.ttl` validado sintácticamente como Turtle.  
- Coherencia entre análisis, ontología y naming strategy.  
- Archivos alojados en estructura correcta del repositorio `/HandsOn/Group15/`.



## 8. Limitaciones y mejoras previstas

| Aspecto | Estado actual | Mejora prevista |
|----------|----------------|----------------|
| ACCESIBILIDAD | Códigos numéricos | Crear vocabulario SKOS de códigos |
| HORARIO | Texto libre | Usar `schema:openingHoursSpecification` |
| Dataset RDF | Parcial (2 ejemplos) | Generar todas las instancias en HO3 |
| Enlaces externos | No implementado | Alinear con URIs de Wikidata/GeoNames |

---



## Conclusión final

Hemos cumplido los requisitos solicitados en el HandsOn 2. En primer lugar, con un análisis tanto del conjunto de datos como de la licencia de este. Y además, se ha desarrollado una ontología ligera, reutilizable y bien alineada con `schema.org` y `WGS84`.

Por tanto, los contenidos están preparados para la continuación con el siguiente "assigment".




