# Cadenas de texto(2)

## Introducción

En el apartado 4 de los apuntes vimos:

*  En que consisten las cadenas de texto
* El uso de comillas simples, dobles y triples para delimitarlas
* El uso de secuencias de escape para mostrar caracteres especiales
* Las operaciones `+`y `*` que permiten concatenar y repetir cadenas respectivamente
* Las cadenas en bruto (raw)
* Y posteriormente vimos las cadenas con formato o formateadas

En este apartado vermos la funciión `len()` que nos permite obtener la longitud de una cadena, cómo acceder a una caracter determinado en una cadena y la sentencia `in` para comprobar si un caracter o caracters aparecen en una cadena de texto

## Longitud de una cadena. La función `len()`

La función `len()`nos devuelve el número de caracteres de una cadena que le pasemos como parámetro. 

**Ejemplos**:

```python
>>> print(len("hola"))
4
>>> print(len("\n"))
1
>>> nombre = "Antonio"
>>> print(len(nombre))
7

```

## Accediendo a un determinado carácter o carácteres de una cadena

### Usando indexación de cadenas

Podemos acceder a un determinado caracter de una cadena usando el operador de indexado. Cada letra, espacio o símbolo en una cadena tiene una posición, también denominada índice. La forma de especificar dicha posición es usando corchetes `[]` con el número de la posición dentro de los mismos. El índice siempre empieza a contar por `0` por lo que para acceder a la primera posición debemos  usar el índice 0.

```python
>>> word = "POKEMON"
>>> print(word[0])
P
>>> print(word[3])
E
>>> print(word[6])
N
```



![](https://teachen.info/cspp/_images/strindex.svg)

Si intentamos acceder que es mayor que la longitud de la cadena obtendremos un mensaje de error:

```python
>>> word = "POKEMON"
>>> print(word[10])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    print(word[10])
IndexError: string index out of range
```

### Indexado con números negativos

También podemos usar números negativos para acceder a los caracteres de una cadena de tal forma que si usamos como índice `-1` accederemos al último carácter, `-2` al penúltimo y así sucesivamente.

```python
>>> word = "POKEMON"
>>> print(word[-1])
N
>>> print(word[-2])
O
>>> print(word[-3])
M
>>> print(word[-7])
P

```

### Subcadenas con recorte de cadenas

En ocasiones se puede dar el caso de que queremas obtener varios caracteres de una cadena; una parte de ella o subcadena. Para poder hacerlo Python nos ofrece la posibilidad de que en lugar de poner entre corchetes un único valor poner un rango de la forma `[a:b]`donde:

* `a` es la posición en la que se inicia la subcadena (incluyendo este índice)
* `b` es la posición en la que termina la subcadena (**excluyendo** este índice)

**Ejemplos**:

```python
>>> frase = "qué bien lo pasamos!"
>>> print(frase[0:3])
qué
>>> print(frase[4:8])
bien
>>> print(frase[8:13])
 lo p

```

Es importante que al recortar no se incluye el índice del segundo número.


## Referencias

* [CSP Python - Indexado de caracteres](https://teachen.info/cspp/unit2/u0202-strindex.html)

