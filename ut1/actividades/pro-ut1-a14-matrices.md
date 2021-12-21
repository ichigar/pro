# PRO - UT1-A14. Matrices

* [Pair programming tips](https://duckly.com/blog/7-tips-for-successful-pair-programming/)

### Operciones sobre listas de varias dimensiones
Dada la siguiente lista

```python
a = [ 
    [2, 4, 6, 8],  
    [1, 3, 5, 7],  
    [8, 6, 4, 2],  
    [7, 5, 3, 1] 
    ] 
```

a) Escribe una función que reciba dicha lista como parámetro y un número y devuelva `True` si el elemento se encuentra en la misma

Inserta el resultado:

```python

```

b) Escribe una función que reciba dicha lista como parámetro y devuelva una tabla HMTL con cada elemento en una celda

Inserta el resultado:

```python

```

c) Escribe una función que reciba dicha lista como parámetro y el número de una columna (un número del 1 al 4) y devuelva la suma de todos los números de dicha columna

Inserta el resultado:

```python

```

## Suma de matrices
Implementa una función a la que se le pasan dos mátrices y devuelve la suma de las mismas

Para comprobar su funcionamiento se leerán de teclado las dos matrices y se llamará a la función.

Una vez obtenido el resultado se mostrará por pantalla.

**NOTA**: No todas las matrices se pueden sumar o restar entre sí. La condición necesaria para sumar o restar dos matrices es que tengan la **misma dimensión**, es decir, que tengan el **mismo número de filas y de columnas**. Para sumar matrices de la misma dimensión se suman entre sí los elementos que ocupan el mismo lugar en cada matriz.

![](https://i.imgur.com/B5SlF9I.png)

Inserta el programa:

```python

```

## Encuentra al sospechoso

Debido a la gran cantidad de crímenes y casos sin resolver, la policía local ha decidido implementar su propio sistema de reconocimiento de sospechosos con la técnica basada en el uso del DNA.

Para esto la policía mantiene dos listas de información; la primera contiene el nombre de las personas registradas en la región (nombre y apellido), la otra, un cromosoma representativo del DNA de cada una de esas personas.

Por simplicidad, un cromosoma se considera como una cadena de 0 (ceros) y 1 (unos), de largo 20.

El método para determinar el sospechoso, es el siguiente:

* Se obtiene una muestra del cromosoma del autor del delito (20 caracteres)
* Se busca en la lista de cromosomas, aquel cromosoma que es más parecido a la muestra. El más parecido se define como el cromosoma que tiene más genes (caracteres) iguales a la muestra.
* Al terminar la búsqueda, se muestra el nombre de la persona cuyo cromosoma es sospechoso, con el porcentaje de parentesco.

La informacíon inicial del programa se debe inicializar en variables en el código, es decir, nombres y cromosomas, en cambio la secuencia encontrda en la escena del crimen, debe ser ingresada por el usuario por teclado.

Desarrolle un programa que lleve a cabo la búsqueda descrita a partir de una muestra de entrada.

Recuerde que como se trata de dos listas, la información del nombre como la de los cromosomas, deben estar en la misma posición en ambas listas.

Consideremos, personas como Pedro Álvarez, Juan Costa y Diego Simeone. Sus secuencias serán

```
00000101010101010101
00101010101101110111
00100010010000001001
```

Ejemplo de ejecución del programa:
```
Ingrese secuencia: 01010101000011001100
El culpable es Pedro Álvarez con un parentezco de 60%
```

**Nota**: se valorará el uso de funciones para las diferentes partes del programa


Inserta el resultado:

```python

```


###### tags: `pro` `ut1` `actividad` `matrices`