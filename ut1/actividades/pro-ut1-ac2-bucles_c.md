# PRO-UT1-AC2. Actividad complementaria. Sentencias de repetición

## Criterios de calificación

* El programa realiza lo que se solicita
* El nombre de las variables expresa lo que van a contener las mismas
* Si se van a utilizar valores constantes estos se inicializan al principio del programa
* Dado que el tamaño de los programas va a ir siendo cada vez mayor, es importante que se comente el código.

## Tareas

Realizar los siguientes programas. En ningún caso se deberán emplear elementos de Python que no hayamos visto en clase o que no se ofrezcan como recursos.

### 1. Tabla de multiplicar en HTML

Escribe un programa que muestre la tabla de multiplicar de los números del 1 al 10 y lo muestre en una tabla HTML. En cada celda se mostrará la operación y el resultado 

Inserta el programa:

```python=

```

### 2. Mostrar tabla de multiplicar en el navegador

En el siguiente [código de ejemplo](https://gist.github.com/ichigar/a20c01263dfd1eb7e06097e88583485c#file-show_html_browser-py) se muestra como mostrar una cadena de texto que contiene código HTML en el navegador. Modifica el programa del apartado anterior para que se muestre en el navegador.

Inserta el programa:

```python
```

### 3. Numeros primos

Un numero es primo si solo es divisible por 1 y por si mismo, o  lo que es lo mismo, un múmero es primo si el resto de dividir dicho número por los valores que hay entre 2 y el número - 1 siempre da distinto de 0. 

Escribe un programa que lea un número de teclado positivo y nos diga si es primo o no:

Inserta el programa:

```python
```

### 4. Primeros números primos

Escribe un programa que muestre por pantalla los 100 primeros números primos

Inserta el programa:

```python
```

### 5. Duración cálculo números primos

El siguiente [bloque de código](https://gist.github.com/ichigar/30064947e548126dab336e0d482f58b4#file-time_spent-py) permite calcular el tiempo empleado en ejecutar un programa. Modifica el programa del apartado anterior de forma que calcule el tiempo empleado en ejecutar el programa.

Inserta el programa:

```python

```

### 6. Tabla con duracion de cálculos

Escribe un programa que calcule los 500, 1000, 1500 y 2000 primeros números primos. 

El programa deberá mostrar en el navegador una tabla HTML con el último número primo y el tiempo empleado en ejecutar cada uno de los casos . 

El tiempo se mostrará en segundos (sin decimales). La tabla tendrá un encabezado que indique que valores se muestran en cada columna.

El resultado se debería parecer a lo siguiente al mostrarlo en el navegador:

| Cantidad numeros primos | Último número primo | Tiempo empleado (s) |
| :---------------------: | :-----------------: | :-----------------: |
|           500           |        3559         |          4          |
|          1000           |        7907         |         23          |
|          1500           |         ...         |         ...         |
|          2000           |         ...         |         ...         |

Inserta el programa:

```python

```

**Nota:** como no hemos visto funciones la longitud del programa va a ser bastante larga. El ejercicio siguiente optimiza la longitud del programa utilizando funciones

### 7. Mejora de tabla de duración cálculos con funciones

Investiga cómo se declara una función en Python. Modifica el programa anterior de forma que:

* Crees una función de nombre `primeros_primos()` a la que le pases la cantidad de números primos que quieres calcular y devuelva el valor del último calculado.
* Utilices dicha función en el programa para obtener el resultado similar al anterior, pero la cantidad de números primos irá de 100 en 100 hasta 1000.

El resultado se debería parecer a lo siguiente al mostrarlo en el navegador:

| Cantidad numeros primos | Último número primo | Tiempo empleado (s) |
| :---------------------: | :-----------------: | :-----------------: |
|           100           |         523         |          0          |
|           200           |        1217         |          0          |
|           300           |        1979         |          1          |
|           ...           |         ...         |         ...         |
|          1000           |        7907         |         23          |

Inserta el programa:

```python

```
