# PRO-UT1-A13. Ejercicios cadenas caracteres

## Actividades

### 1. Intercambio de carácteres extremos

Escribe un programa en el que dada una cadena se genera una de salida en la que se intercambian el primer y último carácter de la misma. Usar subcadenas.

```
`vestimenta` -> 'aestimentv' 
```

Solución:

```python
cadena = input("Introduce texto: ")
resultado = cadena[-1] + cadena[1:-1] + cadena[0] 
print(resultado)
```

### 2. Sustituir repeticiones del primer carácter
Escribe un programa en el que leamos una cadena de texto y devuelva cadena igual a la original, pero todas las repeticiones del primer carácter sean sustituidas por una "#" excepto el primer carácter. Usar subcadenas.
 
 ```
 'anónimamente' -> anónim#mente
 ```

Solución:
```python
cadena = input("Introduce texto: ")

primero = cadena[0]
l = len(cadena)

resultado = cadena

for i in range(1,l):
    if cadena[i] == primero:
        resultado = resultado[:i] + "#" + resultado[i + 1:]

print(resultado)
```

### 3. Caracteres que ocupan posiciones pares
Escribe un programa que genere una cadena con todos los carácteres que ocupan la posición par de una cadena y otra con los que ocupan la posición impar:

```
'cadena perpetua' -> 'aeapreu', 'cdn epta'
```

Solución:

```python

```



### 4. Intercambio de palabras

Escribe un programa en Python al que le pasamos una cadena formada por dos palabras separadas por un espacio y genere una cadena en la que se intercambien las palabras
 
```
'uno dos'  -> 'dos uno'
```
Solución:

```python
cadena = "primera segunda"
aux = cadena.split()

reversed = aux[::-1]

cadena = " ".join(reversed)
print(cadena)
```

### 5. Separar y ordenar alfabéticamente

Escribe un programa en el que leemos una cadena que contiene palabras separadas por comas y las muestra ordenadas alfabéticamente

```
`uno, dos, tres, cuatro` -> 'cuatro, dos, tres, uno'
```

Solución:

```python
cadena = 'uno, dos, tres, cuatro'
aux = cadena.split(", ")
aux.sort()
cadena = ", ".join(aux)
print(cadena)
```

### 6. Palabras que empiezan por a

Escribe un programa al que le pasamos una cadena de caracterers y muestra las palabras que comiencen con la letra 'A'. Por ejemplo, si recibe 'Antes de ayer' debe devolver 'Antes ayer'.

Solución: 
```python
cadena = 'Antes de ayer y despues de mañana ahora'
aux1 = cadena.split()
aux2 = []
for palabra in aux1:
    if palabra.startswith("a") or palabra.startswith("A"):
        aux2.append(palabra)
cadena = " ".join(aux2)
print(cadena)
```

### 7. Caracteres distintos
Escribe un programa en python al que le pasemos una cadena y muestre los caracteres distintos que incluye y cuantas veces se repite cada uno

Solución:

```python
cadena = 'Antes de ayer y despues de mañana ahora'
aux = cadena.lower()
l_encontrados = []
for caracter in aux:
    if caracter not in l_encontrados:
        print(f"{caracter} aparece {aux.count(caracter)} veces")
        l_encontrados.append(caracter)
```

### 7.2. Capitalizar frases

Escribir programa que pase a mayúscula la primera letra de cada frase de un texto. Las frases están separadas por puntos "."
```python
cadena = '''
the Zen of Python, by Tim Peters. beautiful is better than ugly. explicit is better than implicit. simple is better than complex.
'''
```

Solución:

```python

```

### 8. Función sin puntuación

Escribe una función en Python a la que le pasamos una cadena de texto y devuelve la misma cadena, pero sin ningún signo de puntuación

Solución:

```python

```
### 9. Palabras distintas

Escribe un programa al que le pasamos una cadena de caracteres que contiene una o varias frases y nos muestra todas las palabras que contiene y cuantas veces se repite cada una.

**Nota:** las palabras pueden estar separadas por espacios o por signos de puntuación (',', '.', ';').

Solución:

```python

```


### 10. Palíndroma

Escribir una función que reciba una cadena y devuelva `True` si es palíndroma



'Daba la sal al abad' es palíndroma porque si eliminamos todos los espacios y pasamos todos los carácteres a minúsculas se lee igual de derecha a izquierda que de izquierda a derecha.

'dabalasalalabad'

Solución:

```python

```

### 11. Extraer número de teléfono
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-928724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

Solución:

```python

```
## Complementarios

### 12. Transformar cadena

Transformar una cadena de texto en función de unas reglas:
* El primer carácter indica el número de veces que se repite la primera subcadena. Puedes suponer sólo números del 1 al 9.
* El último carácter indica el número de veces que se repite la última subcadena. Puedes suponer sólo números del 1 al 9.
* Las dos subcadenas de entrada están separadas siempre por un guión medio.
* Las dos subcadenas de salida deberán estar separadas por una almohadilla.
* No se puede usar el método `split()`

```
2car-bike3' -> 'carcar#bikebikebike'
```

Solución:
```python

```

### 13. Estraer fecha

Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el nombre del mes ('enero' por ejemplo) y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

Solución
```python

```
### 14. Informaciones de cadena
Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:

* La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe devolver 'USB'.
* Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe 'república argentina' debe devolver 'República Argentina'.


Solución
```python

```


## Recursos

* [https://www.w3resource.com/python-exercises/string/](https://www.w3resource.com/python-exercises/string/)
* [https://pynative.com/python-string-exercise/](https://pynative.com/python-string-exercise/)
* [https://www.geeksforgeeks.org/python-string-exercise/](https://www.geeksforgeeks.org/python-string-exercise/)
* [https://www.pythonprogramming.in/strings.html](https://www.pythonprogramming.in/strings.html)
* [https://www.codesdope.com/practice/python-string/](https://www.codesdope.com/practice/python-string/)
* [https://exercism.org/tracks/python/exercises](https://exercism.org/tracks/python/exercises)
###### tags: `pro` `ut1` `cadenas` `ejercicios`