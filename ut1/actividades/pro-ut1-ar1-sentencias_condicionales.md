# PRO - UT1-AR1. Ejercicios refuerzo. Sentncias condicionales.
## Años que faltan
Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

Ejemplos de ejecución:
```
Año actual: 2021
Introduce el año de referencia: 2010

Han pasado 11 años desde el año 2010
```

```
Año actual: 2021
Introduce el año de referencia: 2030

Faltan 9 años para el año 2030
```

Inserta a continuación el programa:

```python

```
## Años que faltan

Modifica el programa para que en lugar de leer el año actual de teclado  lo obtenga usando la librería `datetime`. 

A continuación se muestra un ejemplo de uso:

```python
from datetime import date
current_year = date.today().year
```

ejemplo de ejecución:
```
Introduce el año de referencia: 2012

Han pasado 9 años desde el año 2010
```

Inserta a continuación el programa:

```python

```
## Precio de la entrada
Escribir un programa para una empresa que tiene parques acuáticos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 

El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 10 años puede entrar gratis, si tiene entre 10 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

Inserta a continuación el programa:

```python

```

## Edad e ingresos para tributar
Para tributar un determinado impuesto se debe ser mayor de 25 años y tener unos ingresos iguales o superiores a 1100 € mensuales. En caso de tener que pagar el tributo es un 5% de los ingresos obtenidos a partir de 1100€.

Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no. Y en caso de tener que tributar que muestre la cantidad a tributar.

Ejemplos de ejecución:

```
Introduce la edad: 23
Introduce los ingresos: 1890

No tiene que pagar impuesto
```

```
Introduce la edad: 26
Introduce los ingresos: 1200

Debe pagar un impuesto de 5€
```

Inserta a continuación el programa:

```python

```
## Menú pizzeria

La pizzería DaCanio ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

* Ingredientes vegetarianos: pimiento y champiñones.
* Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 

Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

Ejemplos de ejecución:

```
Introduce 1 si quieres una pizza vegetariana o 2 para no vegetariana: 2
Puedes elegir entre:
1 - Peperoni
2 - Jamón
3 - Salmóm
Elije por su número el ingrediente que deseas: 3

Has elegido una pizza no vegetariana con mozzarella, tomate y salmón
```

Inserta a continuación el programa:

```python

```


###### tags: `pro` `ut1` `repaso` `if` `condicionales`