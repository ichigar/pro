# UT1-A5. Estructuras de selección (ii)

### Completar código

Añadir las condiciones en el interior de las sentencias "if" del siguiente  programa, para que los mensajes se muestren de forma correcta: 

```python
numero1 = 5
numero2 = 8
if(...) : 
   print("numero1 no es mayor que numero2") 
if(...): 
   print("numero2 es positivo") 
if(...): 
   print("numero1 es negativo o distinto de cero") 
if(...): 
   print("Incrementar en 1 unidad el valor de numero1 no lo hace mayor o igual que numero2") 
```

Inserta aquí el programa:

```python
```

### Letra DNI

El cálculo de la letra del Documento Nacional de Identidad (DNI) es un  proceso matemático sencillo que se basa en obtener el resto de la  división entera del número de DNI y el número 23. A partir del resto de  la división, se obtiene la letra seleccionándola dentro de un array de  letras.

El array de letras es:

```
letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P',  'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
```

Por tanto si el resto de la división es `0`, la letra del DNI es la `T` y si el resto es `3` la letra es la `A`. Con estos datos, elaborar un pequeño programa que:

1. Almacene en una variable el número de DNI indicado por el usuario.
2. En primer lugar (y en una sola instrucción) se debe comprobar si el número es menor que `0` o mayor que `99999999`. Si ese es el caso, se muestra un mensaje al usuario indicando que el  número proporcionado no es válido y el programa no muestra más mensajes.
3. Si el número es válido, se calcula la letra que le corresponde según el método explicado anteriormente

Inserta aquí el programa:

```python

```

### Un segundo después

Desarrollar un programa que solicite la hora, los minutos y los segundos y calcule la hora exactamente un segundo después.

A tener en cuenta:

- Si los segundos son menores que 59, entonces incrementamos en 1 el valor de los segundos.
- Si estamos en el segundo 59 y los minutos son menores que 59,  entonces establecemos el valor de los segundos a 0 e incrementamos en 1  los minutos.
- Si estamos en el segundo 59 y en el minuto 59 puede ocurrir dos cosas:
- Si estamos en la hora 23, entonces establecemos horas, minutos y segundo a cero.
- Si la hora es menor que 23, entonces pondríamos los minutos y los segundos a 0 e incrementaríamos en 1 las horas.

Ejemplo de ejecución:

```
Introduzca la hora: 23

Introduzca los minutos: 59

Introduzca los segundos: 59

Serían las 0:0:0 exactamente un segundo después.
```

Inserta aquí el programa:

#### Mejora complementaria

Modifica el programa anterior de forma que el resultado se muestre de forma similar a un reloj digital. Si por ejemplo son las 9 horas, 5 minutos y 1 segundo se muestren como:

```
09:05:01
```

### Calcular edad a partir de la fecha de nacimiento

Desarrollar un programa que calcule la edad a partir de una fecha de nacimiento. La fecha se leerá en tres variables.

Para obtener la fecha actual nos podemos ayudar de 

A tener en cuenta:

- Para obtener el ano, mes y día actual te puedes ayudar de la [siguiente documentación](https://www.tutorialsrack.com/articles/205/how-to-get-the-year-month-and-day-from-a-datetime-in-python)
- La edad la calculamos como la diferencia entre el año actual y el año de nacimiento.
- Si el mes actual es menor que el mes de nacimiento, entonces todavía no hemos cumplido.
- Si el mes actual es igual al mes de nacimiento y el día actual es  menor que el día de nacimiento, entonces todavía no hemos cumplido.