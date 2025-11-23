Self-Assessment GROUP14

En esta fase del trabajo nos hemos organizado por parejas para realizar la limpieza y procesamiento de los dos archivos CSV en OpenRefine. Cada pareja se ha encargado de uno de los datasets.

Para el primer CSV, 'AccidentesBicicletas_2024', comenzamos eliminando las filas duplicadas que coorespondían a un mismo individuo. Posteriormente, nos ocupamos de los valores que figuraban como espacios en blanco, rellenándolos con el valor 'Desconocido'.

Después, realizamos la conversión de las columnas 'coordenadas_x_utm' y 'coordenadas_y_utm' a un formato estándar de longitud y latitud, creando las nuevas columnas 'longitud' y 'latitud' respectivamente. Finalmente, cambiamos el tipo de datos de las columnas 'positiva_droga' y 'positiva_alcohol' a booleanos.
Cabe destacar que para la transformación de coordenadas utilizamos un código proporcionado por ChatGPT que posteriormente adaptamos a las necesidades de nuestro documento CSV.

Respecto al segundo archivo, 'cabezas_semáforo_bici', eliminamos la columna de 'fecha', y al igual que con el primer dataset, convertimos las coordenadas GPS al formato estándar de longitud y latitud. Finalmente, cambiamos los tipos de semáfoforo que había para asegurarnos de que coincidieran con los términos especificados en la ontología.

Cuando obtuvimos los datasets definitivos, los guardamos como documentos nuevos CSV y exportamos los cambios realizados en dos documentos JSON.
