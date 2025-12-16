# Hands-On Self-Assessment 2

**Group:** Grupo 11

**Date:** 2025/11/03

**Members:** [Sihan Du, Ye Jin, Channa Pan]

---

Se realiza un análisis del dataset escogido (Estaciones de Cercanías de Madrid), así como un estudio sobre su estructura (nombre, código, descripción, localización, ficha técnica en formato pdf, etc).

Por otra parte, el publicador del dataset corresponde con la Entidad Pública Empresarial Renfe-Operadora (dependiente de la “Administración del Estado”), bajo la licencia https://creativecommons.org/licenses/by/4.0/deed.es_ES, que permite a terceros compartir y modificar el dataset para cualquier propósito, incluso comercialmente.

Para la versión Linked Data generada, se propone mantener la misma licencia: CC BY 4.0.

En cuanto a la ontología que se genera:

-> Classes: Station, Province, Municipality, Facility

-> Object Properties: inMunicipality (Station → Municipality), inProvince (Station → Province), hasFacility (Station → Facility)

-> Data Properties: hasCode, hasDescription, hasLatitude, hasLongitude, hasAddress, hasCP, hasPDF
