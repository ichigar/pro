# UT1-A2. Ejercicos de introducción a Python

## Elementos curriculares
**RA1** Reconocer la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje de programación utilizado.
### Criterios de evaluación
1.a) Identificar los bloques que componen la estructura de un programa informático.

1.c) Utilizar entornos integrados de desarrollo.

1.d) Identificar los distintos tipos de variables y la utilidad específica de cada uno.

1.e) Modificar el código de un programa para crear y utilizar variables.

1.g) Clasificar, reconocer y utilizar en expresiones los operadores del lenguaje.

1.i) Introducir comentarios en el código.

## actividad 1

Calcula sin utilizar el intérprete el resultado de cada una de los prints. Escríbelo al lado como comentario:

```python
a = False
b = False
x = not(a)
y = not(b)
print(a or b)
print(x or y)
print(a or x)
print(x or b)
print(a and b)
print(x and y)
print(a and x)
print(x and b)
print(a ^ b)
print(x ^ y)
print(a ^ x)
print(x ^ b)

```

## actividad 2

Determina mentalmente (sin programar) el resultado que aparecerá por pantalla en las siguientes operaciones lógicas. Escríbelo a lado como comentario

```python
bool(25.0) or bool("")          
not bool(25.0) or bool("")
bool(1) ^ bool(0) and bool (not 0)
bool(1) and not(false) or True

```

## actividad 3

Calcula sin utilizar el intérprete el resultado de cada una de los prints. Escríbelo al lado como comentario:

```python
a = 1
b = 20
print(a < 10)
print(b > -5)
print(not b != 20)
print(a < 10 or b == 20)
print(a < 10 ^ b == 20)
print(a < 10 and not(b == 20))
print(a = 10 or b >= 20)
print(a == 2 - 1 and b > 20)
```
## actividad 4

A partir del siguiente programa, sin quitar nada de lo existente. Solo añadiendo nuevos argumentos a las funciones `print` 

```python
print("FICHA DEL")
print("CLIENTE")
print("=")
print("Nombre:" + "EDAD:" + "NIF:")
print("Datos de contacto" + "\temail:")
print("telefono:")
print("=")
```
De forma que la salida por pantalla del programa sea:

```
FICHA DEL CLIENTE
========================================================================
Nombre:
Edad:
NIF:  
    
Datos de contacto:
    email: 
    teléfono: 

Otros "datos de interes" del 'cliente':    
========================================================================
```

Inserta aquí el programa modificado

```python
```

## actividad 5

Completa el siguiente programa:

```python
apellidos = "Suarez Gonzalez"
nombre =  "Antonio"
nif = "41123321p"
edad = 25.0
email = "asuagar@example.com"
n_telefono = "656661122"
datos_interes = "Carnet conducir B2"
print("FICHA DEL")
print("CLIENTE")
print("=")
print("Nombre:" + "EDAD:" + "NIF:")
print("Datos de contacto" + "\temail:")
print("telefono:")
print("=")
```

De forma que genere la siguiente salida por pantalla

```
FICHA DEL CLIENTE
========================================================================
Nombre: Suarez Gonzalez, Antonio
Edad: 25
NIF: 41123321p
    
Datos de contacto:
    email: asuagar@example.com
    teléfono: 656661122

Otros "datos de interes" del 'cliente': Carnet conducir B2  
========================================================================
```

## actividad 6

Escribe un programa que lea de teclado 3 números y muestre el valor medio de los tres con un decimal de precisión. 

Ejemplo de ejecución:

```
Primer número: 1.234
Segundo número: 2.2222
Tercer número: 10

El promedio de los tres es 4.5
```



Inserta aquí el programa:

```python

```

## Actividad 7

Implementar un programa que usa cuatro variables **(firstname, lastname, age y email)** para almacenar tu nombre, tu apellido, tu edad y correo electrónico.

Ejemplo de ejecución: 

```
Introduzca su nombre: Antonio
Introduzca sus apellidos: Suárez García
Antonio, indique su edad: 25
¿Cuál es su correo electrónico?: asuagar@example.com
Estos son los datos leídos:
Antonio Suárez González, de 25 años de edad y puedes contactar con él enviando un correo a la dirección asuagar@example.com
```

Inserta aquí el programa:

```python

```

## Actividad 8

Escriba un programa que pida un número de días, horas, minutos y segundos y calcule cuántos segundos son en total.

Ejemplo de ejecución:

```
Convertidor a segundos
Dígame un número de días: 365
Dígame un número de horas: 5
Dígame un número de minutos: 48
Dígame un número de segundos: 45
365 días, 5 horas, 48 minutos y 45 segundos son 31556925 segundos
```

Inserta aquí el programa:

```python

```

## Actividad 9

Escribir un programa que solicite por teclado un importe en euros y devuelva su conversión en las siguientes divisas:

- Dólares (EEUU)
- Libras (GB)
- Liras turcas. (TK)

Inserta aquí el programa:

```python

```

## Actividad 10

Escribe un programa en el que se lea de teclado el capital inicial, el tipo de interés anual y los años de la inversión y muestre por pantalla el capital obtenido y el rendimiento de la inversión con 2 decimales de precisión

Ejemplo de ejecución:

```
El capital obtenido para 30000€ al 4.1% de interés durante 5 años es de 36675.40€ y el rendimiento de la inversión es de 6675.40€
```

Inserta aquí el programa:

```python

```

## Actividad 11

Modifica la **actividad 5** de forma que todos los valores a mostrar sean leídos por pantalla

Inserta aquí el programa:

```python

```
