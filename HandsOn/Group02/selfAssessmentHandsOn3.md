# Autoevaluación — Hands-on 3  
**Grupo:** Group02  
**Dataset:** BiciMAD — Disponibilidad diaria y uso de bicicletas (31/10/2022)

## 1. Limpieza e importación del conjunto de datos

Para esta práctica usamos el mismo dataset de **BiciMAD** empleado en ejercicios anteriores.  
El archivo original `bici_disponibilidad20221031.csv` fue importado en **OpenRefine / LODRefine** usando codificación UTF-8.  
Verificamos la correcta detección de columnas y filas antes de iniciar la limpieza.

Las columnas iniciales incluían:  
- `DIA` — fecha de la observación  
- `TOTAL_USOS`, `TOTAL_HORAS_USO`, `TOTAL_HORAS_SERVICIO`, `TOTAL_HORAS_DISPONIBLES`  
- `BICIS_MEDIA_DISPONIBLES`, `USO_POR_ABONADOS_OCASIONALES`, `USO_POR_ABONADOS_ANUALES`  

Comprobamos que los valores fueran coherentes (sin negativos ni vacíos) y que las fechas correspondieran al formato esperado.

## 2. Operaciones de limpieza y transformación

Se realizaron las siguientes acciones dentro de OpenRefine:

1. **Eliminación de espacios en blanco** mediante *Trim whitespace*.  
2. **Renombrado de columnas** para hacerlas coherentes con las propiedades de la ontología:  
   - `DIA` → `fecha`  
   - `TOTAL_USOS` → `totalUsoAlDia`  
   - `TOTAL_HORAS_USO` → `horasTotalesDeUso`  
   - `TOTAL_HORAS_SERVICIO` → `horasTotalesDeServicio`  
   - `TOTAL_HORAS_DISPONIBLES` → `horasTotalesDeDisponibilidad`  
   - `BICIS_MEDIA_DISPONIBLES` → `bicicletasMediasDisponibilidad`  
   - `USO_POR_ABONADOS_OCASIONALES` → `usoPorAbonadosOcasionales`  
   - `USO_POR_ABONADOS_ANUALES` → `usoPorAbonadosAnuales`  
3. **Conversión de tipos de datos:**  
   - Aplicación de *To number* en las columnas numéricas.  
   - Transformación de `fecha` con la expresión `toDate(value, "dd/MM/yyyy")`.  
4. **Eliminación de filas vacías o duplicadas** mediante *Facet by blank / duplicates*.  
5. **Verificación final** de rangos y consistencia de los valores.

## 3. Exportación de resultados

Tras completar la limpieza:

- Se exportó el historial de operaciones como  
  **`bici_cleaning_operations.json`**, almacenado en `/HandsOn/Group02/lodrefine/`.  
- Se exportó el dataset limpio como  
  **`bici_disponibilidad20221031-updated.csv`**, guardado en `/HandsOn/Group02/csv/`.

Ambos archivos permiten reproducir y verificar todas las transformaciones realizadas.

## 4. Comentarios finales

La práctica nos permitió comprender mejor el proceso de preparación de datos previo a la generación de RDF.  
OpenRefine resultó muy útil para aplicar transformaciones sin perder trazabilidad, gracias al archivo JSON.  
El dataset final quedó completamente limpio y alineado con los nombres de propiedades de la ontología desarrollada en la práctica anterior.
