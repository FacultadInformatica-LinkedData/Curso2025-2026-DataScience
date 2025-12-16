# Self Assessment — Hands-on 4  
**Grupo:** Group20  
**Dataset:** Población de Madrid (municipio, distritos y barrios)

## 1. Objetivo del hands-on
El propósito de esta práctica fue transformar un fichero CSV con datos de población de Madrid en un grafo RDF siguiendo la ontología creada en las prácticas anteriores.  
Para lograrlo, debíamos diseñar un archivo RML que definiera los mapeos necesarios y generar un fichero RDF en sintaxis N-Triples.

---

## 2. Ontología utilizada
Se empleó una ontología sencilla con las siguientes clases:

- "Ciudad"
- "Distrito"
- "Barrio"
- "RegistroPoblacion"

Y propiedades como:

- "perteneceAMunicipio"
- "perteneceADistrito"
- "esRegistroDeBarrio"
- "tieneFecha"
- "tienePoblacionTotal", "tienePoblacionHombres", "tienePoblacionMujeres"
- Códigos de municipio, distrito y barrio

---

## 3. Creación del archivo RML
El archivo "mappings/poblacion.rml" contiene cuatro TriplesMaps:

1. **Ciudad**  
   - URI: ciudad/{cod_municipio}  
   - Propiedades: código y nombre

2. **Distrito**  
   - URI: distrito/{cod_municipio}-{cod_distrito} 
   - Relación con su ciudad mediante perteneceAMunicipio

3. **Barrio**  
   - URI: barrio/{cod_municipio}-{cod_distrito}-{cod_barrio}
   - Relación con su distrito mediante perteneceADistrito

4. **RegistroPoblacion**  
   - URI: registro/{cod_municipio}-{cod_distrito}-{cod_barrio}
   - Propiedades: fecha, población total, hombres, mujeres  
   - Relación con su barrio mediante esRegistroDeBarrio


---

## 4. Generación del RDF
A partir del archivo RML, se generó un fichero en sintaxis **N-Triples** (rdf/poblacion.nt) que representa:

- Ciudades  
- Distritos  
- Barrios  
- Registros de población asociados a cada barrio  

Se comprobó que:

- Todas las URIs son consistentes con la ontología  
- Los tipos de cada recurso son correctos  
- Los literales representan adecuadamente la información del CSV  
- Las relaciones jerárquicas (ciudad → distrito → barrio → registro) están bien enlazadas  

