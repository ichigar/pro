# Valores aleatorios: la biblioteca random

## La biblioteca **random**

La biblioteca **random** contiene una serie de funciones relacionadas con los valores aleatorios. El [listado completo de funciones de esta biblioteca](https://docs.python.org/3/library/random.html) se describe en el manual de Python.

------

Como ocurre con todas las bibliotecas, antes de utilizar una función se debe importar la función o la biblioteca entera.

- Si se importa la biblioteca entera, se debe escribir el nombre de la biblioteca y el de la función separada por un punto, como muestra el siguiente ejemplo:         

  ```python
  import random
  print(random.randrange(10))
  ```
  
  ```
  4
  ```
  
- Si se importa únicamente una función, se debe escribir simplemente el nombre de la función, como muestra el siguiente ejemplo:         

  ```python
  from random import randrange
  print(randrange(10))
  ```
  
  ```
  1
  ```
  
- Si se importan varias funciones, los nombres de las funciones deben separarse como comas (,), como muestra el siguiente ejemplo:         

  ```python
  from random import randrange, choice
  print(randrange(10))
  print(choice(["uno", "dos", "tres"]))
  ```
  
  ```
  5
  dos
  ```

## Generar números enteros: la función **randint()**

La función **randint(\*a\*, \*b\*)** genera un número entero entre *a* y *b*, ambos incluidos. *a* debe ser inferior o igual a *b*.

```python
import random
print(random.randint(10, 20))
12
```

## Generar números enteros: la función **randrange()**

La función **randrange(\*a\*, \*b\*, \*c\*)** genera un número entero entre los valores generados por range(*a*, *b*, *c*). Como ocurre con range(), la función **randrange()** admite uno, dos o tres argumentos. El tercer argumento indica el incremento de los valores a seleccionar.

```python
import random
print(random.randrange(10))
9
```
```python
import random
print(random.randrange(10, 110))
61
```
```python
import random
print(random.randrange(10, 110, 10))   # los número se seleccionan al azar de 10 en 10
80
```



## Generar números reales: la función **random()**

La función **random()** genera un número decimal entre 0 y 1 (puede generar 0, pero no 1).

```python
import random
print(random.random())
0.5310449231726346
```

## Generar números reales: la función **uniform()**

La función **uniform(\*a\*, \*b\*)** genera un número real entre *a* y *b* (puede generar *a* y, debido a la forma de redondear de Python, puede que genere *b* o no).

```python
import random

print(random.uniform(5, 8))
6.216950987513291
```

## Seleccionar un elemento al azar: la función **choice()**

La función **choice(\*secuencia\*)** elige un  valor al azar en un conjunto de elementos. Cualquier tipo de datos  enumerable (tupla, lista, cadena, range) puede utilizarse como conjunto  de elementos.

```python
import random
print(random.choice((14, 15, 20, 150)))
14
```
```python
import random
print(random.choice(["alfa", "beta", "gamma"]))
gamma
```
```python
import random
print(random.choice("AEIOU"))
E
```
```python
import random
print(random.choice(range(10)))
4
```

## Referencias

Apuntes generados a partir del curso [Introducción a la programación con Python](http://www.mclibre.org/consultar/python/) que se distribuye bajo una [Licencia Creative Commons Reconocimiento-CompartirIgual 4.0 Internacional (CC BY-SA 4.0).](https://creativecommons.org/licenses/by-sa/4.0/deed.es_ES)

![CC-BY-SA](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)

