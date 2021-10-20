# UT1-A6-Bucles (I) 

## Tareas

### Factorial

El factorial de un número entero `n` es una operación matemática que consiste en multiplicar todos los factores `n x (n-1) x (n-2) x ... x 1`. Así, el factorial de `5` (escrito como `5!`) es igual a: `5! = 5 x 4 x 3 x 2 x 1 = 120`

Elabora un programa que permita calcular el factorial de un número entero indicado por el usuario.

Inserta aquí el programa:

```python
```

### Pares impares

Escriba un programa que pregunte cuántos números va a introducir, pida esos  números y escriba la cantidad de números pares e impares que ha escrito.

Ejemplo:

```
Dígame cuántos números va a escribir: 5
Dígame el número 1: 17
Dígame el número 2: 5
Dígame el número 3: 7
Dígame el número 4: 22
Dígame el número 5: 19
Ha escrito 1 número(s) par(es)Ha escrito 4 número(s) impar(es)
```

Inserta aquí el programa:

```python
```



### Número mayor

Desarrollar una aplicación que pregunte inicialmente cuantos números se van a  introducir por teclado, los solicite y devuelva por pantalla el número  mayor y el menor. 

**Ayuda**: Utilizar una variable “mayor” y otra "menor"  que almacene en cada instante el número más grande y el más pequeño  encontrado respectivamente. En cada iteración, se comprobará si el  número introducido es más grande que el que tenemos almacenado en  “mayor” y en caso afrmativo, se actualizará su valor. Para el menor, en  cada iteración se comprobará si el número introducido es más pequeño que el que tenemos almacenado en “menor” y en caso afrmativo, se  actualizará su valor.

Ejemplo de ejecución:

```
¿Cuántos números va a introducir? 4
Introduzca número 1: 4
Introduzca número 2: 7
Introduzca número 3: 6
Introduzca número 4: 1

El mayor es el 7 y el menor es el 1
```

Inserta aquí el programa:

```python

```

### Suma y promedio

Escribir un programa que permita al usuario ingresar 5 números enteros,  que pueden ser positivos o negativos. Al finalizar, mostrar la suma de los números negativos y el promedio de los positivos. 

No olvides que no es posible dividir por cero, por lo que es  necesario evitar que el programa arroje un error si no se lee ningún  números positivo.

Inserta aquí el programa:

```python

```

### Vocales en frase

Solicitar al usuario que ingrese una frase y luego imprimir un listado  de las vocales que aparecen en esa frase (sin repetirlas).

Inserta aquí el programa:

```python

```

### Fibonacci

Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de  éstos, cada elemento es la suma de los dos números anteriores en la  secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

Inserta aquí el programa:

```python

```

### Bisiestos en rango

Escribir un programa que permita al usuario ingresar dos años y luego  imprima todos los años en ese rango, que sean bisiestos y múltiplos de  10. 

**Nota**: para que un año sea bisiesto debe ser divisible por 4 y no debe  ser divisible por 100, excepto que también sea divisible por 400.

Inserta aquí el programa:

```python

```

## Complementario
### Reloj digital

El siguiente programa muestra los números del 0 al 99 por pantalla con un retraso de 1 segundo entre uno y otro.

```python
import time
import os
for i in range(100):
    os.system("clear")  # limpiamos la pantalla
    print(i)            # mostramos el número
    time.sleep(1)       # aplicamos un retraso de 1seg
```

A partir del programa anterior muestra por pantalla un reloj que en formato digital muestre horas:minutos:segundos, teniendo en cuenta que la hora, minuto iniciales se generarán de forma aleatoria.

Inserta aquí el programa:

```python
```

