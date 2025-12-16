# Auto-evaluación Práctica 3: Limpieza y Preparación de Datos

*Grupo:* Group33
*Tema:* Aforos de tráfico en la ciudad de Madrid (Madrid 2025)

---

## 1. Justificación de las Tareas de Limpieza y Transformación

El objetivo de esta práctica fue adecuar el archivo CSV original (⁠ datos_estacion_marzo.csv ⁠) para que su *estructura y formato fueran compatibles con el modelo de grafo RDF* definido por la ontología. El formato inicial, diseñado para ser tabular, no cumplía los requisitos para un mapeo semántico eficiente.

### 1.1. Transformación Estructural (La Decisión Crítica)

La tarea más importante fue la reestructuración completa del dataset:

•⁠  ⁠*Problema:* El dataset venía en formato ancho (wide format), con 24 columnas (⁠ HOR1 ⁠ a ⁠ HOR24 ⁠) conteniendo las mediciones horarias. En el modelo RDF, *cada medición horaria debe ser un recurso individual* (⁠ :Medicion ⁠).
•⁠  ⁠*Solución:* Se aplicó la operación *Transponer columnas a filas (Pivotado)*. Esto expandió cada fila diaria en 24 filas individuales, creando dos columnas clave: ⁠ Hora_Codigo ⁠ (código de la hora) y ⁠ Valor_Intensidad ⁠ (valor de la medición).

### 1.2. Mapeo Semántico y Consistencia de Datos

Para asegurar la calidad de los literales y la usabilidad en la Tarea 4 (Mapeo RML), se realizaron las siguientes adaptaciones:

•⁠  ⁠*Generación de Fecha/Hora (⁠ xsd:dateTime ⁠):* Se combinó la fecha (⁠ fecha_dia ⁠) y el código horario (⁠ Hora_Codigo ⁠) en una nueva columna, *⁠ FECHA_HORA_RDF ⁠. Se utilizó una expresión para formatearla estrictamente como *⁠ AAAA-MM-DDTHH:MM:SS ⁠**, que es el requisito para el tipo de dato ⁠ xsd:dateTime ⁠.
•⁠  ⁠*Corrección de Decimales:* Se estandarizó la columna ⁠ Valor_Intensidad ⁠ reemplazando el separador decimal de coma (⁠ , ⁠) por *punto (⁠ . ⁠)*, lo cual es esencial para que RML lo interprete correctamente como un literal numérico (⁠ xsd:decimal ⁠).
•⁠  ⁠*Decodificación de Sentido:* Los códigos alfanuméricos (⁠ 1- ⁠, ⁠ 1= ⁠, etc.) en la columna ⁠ sentido_codigo ⁠ fueron reemplazados por sus nombres completos (⁠ Norte ⁠, ⁠ Sur ⁠, ⁠ Este ⁠, ⁠ Oeste ⁠) para mejorar la *legibilidad semántica* del grafo resultante.
•⁠  ⁠*Ajuste de Encabezados:* Se renombraron las columnas identificadoras (⁠ FDIA ⁠, ⁠ FEST ⁠, ⁠ FSEN ⁠) a nombres claros (⁠ fecha_dia ⁠, ⁠ codigo_estacion ⁠, ⁠ sentido_codigo ⁠) para simplificar las plantillas RML.

## 2. Conclusión y Entregables de la Tarea 3

La limpieza y transformación estructural de datos en OpenRefine se ha completado. Los entregables generados son:

•⁠  ⁠*⁠ operations.json ⁠*: Contiene la secuencia de todas las operaciones realizadas, garantizando la trazabilidad del proceso.
•⁠  ⁠*⁠ datos_estacion_marzo-updated.csv ⁠*: El dataset final, transformado a formato "largo", listo para ser utilizado como fuente de datos para el Mapeo RML.
