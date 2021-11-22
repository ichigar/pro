# PRO-UT1-A10. Bucles anidados

## Criterios de calificación

* El programa realiza lo que se solicita
* El nombre de las variables expresa lo que van a contener las mismas
* Si se van a utilizar valores constantes estos se inicializan al principio del programa
* Dado que el tamaño de los programas va a ir siendo cada vez mayor, es importante que se comente el código.

## Tareas

Realizar los siguientes programas. En ningún caso se deberán emplear elementos de Python que no hayamos visto en clase o que no se ofrezcan como recursos.

### Secuencias

Escribe un programa que genere utilizando bucles anidados las siguientes salida por pantalla:

#### Torre

El programa pregunta el número de filas y muestra torre de 5 asteríscos:

```
Número de filas: 7
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

#### Triángulo

El programa pregunta el número de filas y muestra tríangulo de la forma

```
Número de filas: 5
1
12
123
1234
12345
```

#### Triángulo invertido

El programa pregunta el número de filas y muestra tríangulo invertido de la forma

```
Número de filas: 6
123456
12345
1234
123
12
1
```

#### Medio árbol de navidad

Se preguntan repeticiones y filas y muestra salida de la forma

```
Número de repeticiones: 3
Número de filas: 4
#
##
###
####
#
##
###
####
#
##
###
####
```

Inserta a continuación el programa

```python
```

#### Árbol de navidad

```
Número de repeticiones: 3
Número de filas: 4
   #
  ###
 #####
#######
   #
  ###
 #####
#######
   #
  ###
 #####
#######
```

### Notas

El programa lee el nombre y las notas de 3 alumnos en 3 materias y muestra la nota media de cada uno de la forma:

```
Nombre del alumno/a 1: Juan Valdez
Nota 1: 6
Nota 2: 7
Nota 3: 9
Juan Valdez tiene de nota media: 7.33

Nombre del alumno/a 2: Marta Puerta
Nota 1: 9
Nota 2: 7
Nota 3: 9
Marta Puerta tiene de nota media: 8.33

Nombre del alumno/a 1: Jhon Doe
Nota 1: 3
Nota 2: 7
Nota 3: 5
Jhon Doe tiene de nota media: 5.00
```

 

### Listas y sublistas 1

Escribe un programa qué me pida el nombre de una tarea y la muestre, a continuación me preguntará cuantas subtareas tiene la tarea y las leeremos. Cuando termine de leerlas el programa me preguntará si quiere leer más tareas.

Al terminar de leer tareas y subtareas el programa las mostrará en listas y sublistas.

Ejemplo de ejecución:

```
Inserta la tarea 1: compra super
¿Cuantas subtares hay? 3
Inserta subtarea 1: pan
Inserta subtarea 2: leche
Inserta subtarea 3: huevos
¿Desea añadir más tareas? s

Inserta la tarea 2: limpieza
¿Cuantas subtares hay? 2
Inserta subtarea 1: habitación
Inserta subtarea 2: salón
¿Desea añadir más tareas? n

Lista de tareas
* compra super
    * pan
    * leche
    * huevos
* limpieza
    * habitación
    * salón
```

Inserta el resultado

```python
```

### Listas y sublistas 2

Modifica el programa anterior de forma que en lugar de preguntar  "¿Cuántas subtareas hay?" pregunte si quiero añadir alguna subtarea hasta que le indique que no.

Ejemplo de ejecución:

```
Inserta la tarea 1: compra super
¿quieres añadir subtarea? s
Inserta subtarea 1: pan
¿quieres añadir subtarea? s
Inserta subtarea 2: leche
¿quieres añadir subtarea? s
Inserta subtarea 3: huevos
¿quieres añadir subtarea? n

¿Desea añadir más tareas? s

Inserta la tarea 2: limpieza
¿quieres añadir subtarea? s
Inserta subtarea 1: habitación
¿quieres añadir subtarea? s
Inserta subtarea 2: salón
¿quieres añadir subtarea? n

¿Desea añadir más tareas? n

Lista de tareas
* compra super
    * pan
    * leche
    * huevos
* limpieza
    * habitación
    * salón
```

Inserta el resultado

```python

```

### 

### Listas y sublistas en HTML

Modifica el programa anterior de forma que las lista se muestre en el navegador en lugar de hacerlo por pantalla. Usa `<ul>` y `<li>`para generar la lista:

Inserta el resultado

```python

```

### 

### Datos de clientes en HTML

Escribe un programa que lea los datos de clientes (nombre, apellidos, edad, email). Después de leer los datos de un cliente nos preguntará si queremos leer los datos de otro cliente.

Cuando terminemos de leer los datos de todos los clientes se mostrará en una tabla en el navegador los datos de todos los clientes.

La tabla contendrá una fila de encabezado con el nombre de los campos de cada columna

Se valorará usar estilos para que la presentación de la tabla

Inserta a continuación el programa

```python

```
