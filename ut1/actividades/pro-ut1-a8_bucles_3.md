# UT1-A8. Estructuras de repetición III

## Tareas

### 1. Suma de numeros pares

Escribe un programa que lea valores de teclado y calcule la suma de todos los números pares que leídos. El programa terminará cuando leamos un valor negativo o cuando leamos un valor mayor de 1000

Inserta aquí el  programa:

```python
```

### 2. Suma de multiplos de 5

Escribe un programa que lea un valor y calcule la suma de todos los números múltiplos de 5 que hay entre 0 y dicho valor

Inserta aquí el  programa:

```python

```

### 3. Número de negativos y más cercano a 10

Escribe un programa que lea números de teclado y muestre cuántos de los valores leídos son negativos y cual es el valor más cercano a 10. El programa terminará cuando leamos un 0

Inserta aquí el  programa:

```python

```

### 4. Movimientos bancarios

Escribe un  programa que lea el saldo inicial de un cliente. A continuación leerá los datos de los movimientos del cliente (cantidad y concepto). La cantidad será positiva si es un ingreso y negativa si es un gasto. El programa terminará cuando la cantidad leída sea 0.

Cuando termine, el programa mostrará el número de movimientos y el saldo final

Ejemplo de ejecución:

```
Lectura de movimientos en la cuenta
Introduce el saldo inicial: 700
Cantidad: -100
Concepto: reparación bici

Cantidad: -35.50
Concepto: bono bus

Cantidad: 80
Concepto: venta go-pro

Cantidad: 0

Haz realizado 3 movimientos. El saldo actual es de 644.50€ 
```

Inserta aquí el  programa:

```python

```

### 5. Adivina el número

Escribe un programa en el que el ordenador genere un número al azar entre 0 y 9. A continuación el programa me pedirá que adivine el número. El programa me irá dando pistas diciéndome si el número es mayor o menor que el que he introducido. El programa terminará cuando adivine el número e indicará cuántos intentos he necesitado.

Ejemplo de ejecución:

```
ADIVINA EL NÚMERO ENTRE 0 Y 9
Introduce un valor: 5
El valor es menor. Introduce un número: 3
El valor es menor. Introduce un número: 1
El valor es mayor. Introduce un número: 2
¡Correcto! has necesitado 4 intentos
```

Inserta aquí el  programa:

```python

```

### 6. Movimientos bancarios. Extracto

Modifica el programa anterior de forma que cuando el programa termine mostrará todos los movimientos en filas. En cada fila se mostrará, además de los datos leídos, el número del movimiento y el saldo después de dicho movimiento.

Ejemplo de ejecución:

```
Lectura de movimientos en la cuenta
Introduce el saldo inicial: 700
cantidad: -100
concepto: reparación bici
cantidad: -35.50
concepto: bono bus
cantidad: 80
concepto: venta go-pro
cantidad: 0

Extracto de movimientos en la cuenta:
=====================================
1 | reparación bici | -100.00 | 600
2 | bono bus | -35.50 | 564.5
3 | venta go-pro | +80.00 | 644.5
=====================================

```

Inserta aquí el  programa:

```python

```

### 7. Fichas de clientes

Escribe un programa que lea los datos de clientes (nombre, apellidos, email y edad). Después de leer los datos de 1 cliente el programa nos preguntará si queremos leer los datos de otro cliente. Si introducimos "s" leera los datos, si introducimos cualquier otra cadena el programa terminará y nos mostrará el código HTML que permita generar una tabla con los datos de los clientes. La tabla mostrada en el navegador debería ser similar a:

| Nombre | Apellidos     | email            | edad |
| ------ | ------------- | ---------------- | ---- |
| Juan   | Valdez Suárez | caracol@cafe.com | 68   |
| Jhon   | Travolta      | pulp@fiction.net | 59   |

Inserta aquí el  programa:

```python

```

## Tareas complementarias

### 8. El ordenador adivina el número

Escribe un programa en el que el ordenador te pedirá que pienses un número entre 0 y 100. El ordenador generará un número al azar entre 0 y 100 y te preguntará si es el número correcto o si es menor o si es mayor. Deberemos introducir:

* "=" si hemos acertado
* "<" si el número es menor que el que ha generado
* ">" si el número es mayor que el que ha generado

Si le indicamos que es menor el programa generará un número al azar entre 0 y el número anterior y nos volvera a preguntar.

Si el número es mayor el programa generará un número al azar entre el número generado y 100 y nos volvera a preguntar

Si el número es correcto nos dará la enhorabuena y nos dirá cuantos intentos ha necesitado.

De forma sucesiva el ordenador irá preguntándonos generando números al azar en función de las respuesta que le vayamos dando hasta que obtenga la respuesta correcta.

Ejemplo de ejecución:

```
Vamos a jugar. Piensa un número
Cuando lo tengas pulsa enter
¿El número es el 34? Introduce '=', '<' o '>': >
¿El número es el 46? Introduce '=', '<' o '>': >
¿El número es el 89? Introduce '=', '<' o '>': <
¿El número es el 56? Introduce '=', '<' o '>': >
¿El número es el 70? Introduce '=', '<' o '>': =
He adivinado en 5 intentos
```

### 9. Movientos bancarios en tabla HTML con cantidades con 2 decimales

Modifica el programa de los movimientos bancarios de forma que el resultado se muestre en una tabla HTML. Muestra todas las cantidades y saldos con dos decimales. En el [siguiente ejemplo](https://gist.github.com/ichigar/1ddf0350546debf232d92d7d32a6f4e8) puedes ver cómo hacerlo.

Inserta aquí el  programa:

```python

```



