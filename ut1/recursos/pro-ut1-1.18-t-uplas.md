# UT1-1.18-T-UPLAS

## Introducción

El concepto de tupla es muy similar al de lista. Aunque hay algunas diferencias menores, lo fundamental es que, mientras una lista es **mutable** y se puede modificar, una **tupla** no admite cambios y, por lo tanto, es **inmutable.**

## Creando tuplas

Podemos pensar en crear tuplas tal y como lo hacíamos con listas, pero usando como delimitador paréntesis en lugar de corchetes:

```python
>>> empty_tuple = ()

>>> gc_geoloc = (28.46824, -16.89546)

>>> three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')
```

### Tuplas de un elemento

Hay que prestar especial atención cuando vamos a crear una tupla de un único elemento. La intención primera sería hacerlo de la siguiente manera:

```python
>>> one_item_tuple = ('Papá Noel')

>>> one_item_tuple
'Papá Noel'

>>> type (one_item_tuple)
str
```



Realmente, hemos creado una variable de tipo **str** (cadena de texto). Para crear una tupla de un elemento debemos añadir una coma al final:



```python
>>> one_item_tuple = ('Papá Noel',)

>>> one_item_tupl
('Papá Noel',)

>>> type (one_item_tuple)
tuple
```



### Tuplas sin paréntesis
Según el caso, hay veces que nos podemos encontrar con tuplas que no llevan paréntesis. Quizás no está tan extendido, pero a efectos prácticos tiene el mismo resultado. Veamos algunos ejemplos de ello:



```python
>>> one_item_tuple = 'Papá Noel',

>>> gc_geoloc = 28.46824, -16.89546

>>> three_wise_men = 'Melchor', 'Gaspar', 'Baltasar'
```



## Modificar una tupla

Como ya hemos comentado previamente, las tuplas con estructuras de datos inmutables. Una vez que las creamos con un valor, no podemos modificarlas. Veamos qué ocurre si lo intentamos:

```python
>>> three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')

>>> three_wise_men[0] = 'Bruce Willis'
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```



## Conversión
Para convertir otros tipos de datos en una tupla podemos usar la función `tuple()`:



Esta conversión es válida para aquellos tipos de datos que sean iterables: cadenas de caracteres, listas, diccionarios, conjuntos, etc. Un ejemplo que no funciona es intentar convertir un número en una tupla:
El uso de la función tuple() sin argumentos equivale a crear una tupla vacía:
2.4 Operaciones con tuplas
Con las tuplas podemos realizar todas las operaciones que vimos con listas salvo las que conlleven una modificación «in-situ» de la misma:
o reverse()
o append()
o extend()
o remove()
o clear()
o sort()
4
2.5 Desempaquetado de tuplas
El desempaquetado es una característica de las tuplas que nos permite asignar una tupla a variables independientes:
Figura 1: Desempaquetado de tuplas
Veamos un ejemplo con código:
Intercambio de valores
A través del desempaquetado de variables podemos llevar a cabo el intercambio de los valores de dos variables de manera directa:
Nota: A priori puede parecer que esto es algo «natural», pero en la gran mayoría de lenguajes de programación no es posible hacer este intercambio de forma «directa» ya que necesitamos recurrir a una tercera variable «auxiliar» como almacén temporal en el paso intermedio de traspaso de valores.
5
Contenidos creados por: Sergio Delgado Quintero
Maquetado por: