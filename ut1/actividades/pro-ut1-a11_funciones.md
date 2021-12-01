# PRO-UT1-A11. Funciones

## Criterios de calificación

* El programa realiza lo que se solicita
* El nombre de las variables expresa lo que van a contener las mismas
* Si se van a utilizar valores constantes estos se inicializan al principio del programa
* Dado que el tamaño de los programas va a ir siendo cada vez mayor, es importante que se comente el código.

## Tareas

Realizar los siguientes programas. En ningún caso se deberán emplear elementos de Python que no hayamos visto en clase o que no se ofrezcan como recursos.

### Función muestra torre
Escribe función que muestra por pantalla rectángulo de asteríscos con base como número de asteriscos de la base y altura número de asterísctos de la altura

Comprueba la función haciendo varias llamadas a la misma con diferentes argumentos.

Inserta el resultado:

```python=

```
### Funcion muestra torre de caracteres
Modifica la función del apartado anterior de forma que el caracter a mostrar sea también un parámetro. Por defecto si no pasamos ninguno se deberán mostrar asteríscos.


Comprueba la función haciendo vairas llamadas a la misma con diferentes argumentos.

Inserta el resultado:

```python

```

### Generar enlace html

Escribe una función de nombre html_enlace a la que le pasamos una url y un texto y devuelva el HTML del enlace correspondiente

Comprueba mostrando en el navegador un enlace de ejemplo

Inserta el resultado:

```python

```

### Mostrar imagen html

Escribe una función de nombre html_imagen a la que le pasamos la url de una imagen y el texto del caption y devuelva el HTML de la imagen correspondiente

Comprueba con programa que lea una url y el texto del captio, llame a la función y muestre en el navegador una imagen de ejemplo

Inserta el resultado:

```python

```

### Función valor_maximo

Escribe una función a la que le podamos pasar un número indeterminado de valores y devuelva el valor máximo de todos los argumentos.

Inserta el código de la función:

```python

```
### Cambio de divisas

Desarrolla un programa, que contendrá una función  denominada conversor que debe leer un número real y un tipo de moneda  (libra, dólar, yen) como valores de entrada. La función convertirá la  cantidad en euros al tipo de moneda correspondiente. Averigua en Internet el cambio actual entre el euro y dichas monedas.

Por ejemplo, si la  cantidad es 15 y la moneda es "dólar", se supondrá que se trata de 15 € y que hay que convertirlos a dólares y, por lo tanto, el resultado debe  ser 17,37 dólares.

Inserta el programa:

```python

```

### Salario

Desarrolla un programa que determine la cantidad de dinero que  recibirá un trabajador por concepto de las horas trabajadas en  una empresa.

Cuando las horas exceden de 40, el resto se consideran horas extras y se pagan al doble de una hora normal cuando no exceden de 8.  Sí las horas extras exceden de 8 se pagan al triple del precio de la hora normal.

Crea una función que tenga como valores de entrada el número de horas trabajadas y el precio por hora.

Inserta programa en el que se compruebe el uso de la función:

```python
```

## Tareas complementarias

### Números primos

Definir una función de nombre **es_primo()** que determine si un número entero pasado como argumento es  primo, es decir, si únicamente es divisible por si mismo y por uno. Un **número primo** es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.

**Ejemplos:**

- El número 5 **es primo**, ya que para todos aquellos números comprendidos entre 1 y 5 (1,2,3,4,5) , únicamente se obtiene **resto cero al dividir el número entre 1 o entre el propio 5.**
- El número 4 **no es primo**, ya que para todos aquellos números comprendidos entre 1 y 4 (1,2,3,4), se obtiene resto cero al  dividir el número entre 1, 2 y 4. De esta forma, el número 4 no cumple  que únicamente es divisible por sigo mismo y por uno, puesto que es  múltiplo de 2.

Inserta el código de la función:

```python
```

### Múltiplos

Escribe una función de nombre `multiplos()` a la que le pasemos como parámetros dos números y el programa mostrará todos los múltiplos que hay del segundo número entre 1 y el primer número.

Inserta el código de la función

```python
```

### Factorial

Escribe una función de nombre `factorial()` a la que le pasemos un número y nos muestre el factorial del mismo.

El factorial de un número se calcula multiplicando todos los valores que van desde 1 hasta dicho número. Ejemplo factorial de 5 = 5 x 4 x 3 x 2 x 1 = 120

Inserta el código de la función

```python

```

### Menú

Desarrolle una función `menu()` que nos presente un menú con 4 opciones.  

* Eligiendo la opción **a** nos pedirá un número y nos dirá si es primo o no (llamará a la función `es_primo()`)
* Eligiendo la opción **b** nos pedirá un número y nos mostrará todos los múltiplos de es número que hay entre 1 y 1000 (llamará a la función `multiplos()`)
* Eligiendo la opción **c** nos pedirá un número y nos mostrará el factorial de dicho número (llamará a la función `factorial()`)
* Nos mostrará también una opción **s - salir** que finalizará la función si seleccionamos cualquier opción que no sea a, b o c

Después de seleccionar una opción y mostrar el resultados se volverá a mostrar el menú a no ser que seleccionemos una opción que no sea a, b o c.

Crea un programa que llame a la función `menu()` y permita comprobar el funcionamiento. Inserta el programa:

```python
```



###### tags: `pro` `ut1` `funciones`
