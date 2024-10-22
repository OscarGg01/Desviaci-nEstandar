# Cálculo de Media y Desviación Estándar

Este proyecto permite calcular el promedio y la desviación estándar de 
una lista de números proporcionados por el usuario. También incluye una 
funcionalidad interactiva donde el usuario ingresa los números 
manualmente, y el programa calcula y muestra los resultados.

##Explicación de ejecución y pruebas

Al ejecutar el main, el usuario podrá ingresar la cantidad de elementos que
desea ingresar, posteriormente se le pide al usuario que ingrese los elementos
para que la aplicación le retorne la media y la desviación estandar de los 
elementos ingresados

Pruebas de la Función calcular_media

test_media_lista_vacia:
Verifica que la función calcular_media lance la excepción personalizada 
NoSePuedeCalcular cuando la lista de elementos está vacía.
Esto asegura que no se pueda calcular la media de una lista sin valores.

test_media_un_elemento:
Valida que la media de una lista con un solo elemento sea el valor del único elemento.
Ejemplo: Para [5], la media es 5.

test_media_dos_elementos:
Verifica el cálculo de la media para una lista con dos elementos.
Ejemplo: Para [5, 15], la media es (5 + 15) / 2 = 10.

test_media_varios_elementos_positivos:
Prueba el cálculo de la media para una lista con varios números positivos.
Ejemplo: Para [1, 2, 3, 4, 5], la media es 3.

test_media_varios_elementos_ceros:
Verifica que la media de una lista con varios ceros sea 0.
Ejemplo: Para [0, 0, 0, 0], la media es 0.

test_media_elementos_positivos_y_negativos:
Prueba el cálculo de la media para una lista con números positivos y negativos.
Ejemplo: Para [-3, -1, 1, 3], la media es 0.

test_media_elementos_no_numericos:
Verifica que la función lance una excepción TypeError si la lista contiene elementos no numéricos.
Ejemplo: Para [1, 2, "a", 3], se debe lanzar un TypeError.

Pruebas de la Función calcular_desviacion_estandar

test_desviacion_lista_vacia:
Verifica que la función calcular_desviacion_estandar lance la excepción NoSePuedeCalcular si la lista está vacía.
Esto asegura que no se pueda calcular la desviación estándar de una lista sin valores.

test_desviacion_un_elemento:
Valida que la desviación estándar de una lista con un solo elemento sea 0, ya que no hay variación.
Ejemplo: Para [5], la desviación estándar es 0.0.

test_desviacion_dos_elementos:
Prueba el cálculo de la desviación estándar para una lista con dos elementos.
Ejemplo: Para [5, 15], la desviación estándar es 5.0.

test_desviacion_varios_elementos_positivos:
Verifica el cálculo de la desviación estándar para una lista con varios elementos positivos.
Ejemplo: Para [1, 2, 3, 4, 5], la desviación estándar es aproximadamente 1.414.

test_desviacion_varios_elementos_ceros:
Valida que la desviación estándar de una lista con varios ceros sea 0.
Ejemplo: Para [0, 0, 0, 0], la desviación estándar es 0.0.

test_desviacion_elementos_positivos_y_negativos:
Prueba el cálculo de la desviación estándar para una lista con números positivos y negativos.
Ejemplo: Para [-3, -1, 1, 3], la desviación estándar es aproximadamente 2.236.

test_desviacion_elementos_no_numericos:
Verifica que la función calcular_desviacion_estandar lance una excepción TypeError si la lista contiene 
elementos no numéricos.
Ejemplo: Para [1, 2, "a", 3], se debe lanzar un TypeError.
