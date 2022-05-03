# PRO-UT3-AER1. Recuperación. Prueba práctica
## Recursos

* Podrás usar los apuntes de la unidad colgados en la plataforma en el apartado **Contenidos** de la unidad.
* Abre los mismos y cuando hayas terminado esconecta el cable de red del equipo. 


## Criterios de evaluación

* Después del código de cada función se incluye un ejemplo de ejecución de la misma
* El programa o función **funciona correctamente** y realiza todas las acciones solicitadas
* Los **nombres** de variables y funciones son significativos sin ambigüedad la información que almacenan o la funcionalidad que realizan.
* El código es **claro**, **eficiente** y **legible**
* Si es necesario, se crean **funciones intermedias** que hacen el código más legible o refactorizan tareas que se hacen de forma repetitiva en diferentes apartados

## Enunciado

### Parte 1

En un videoclub se informatiza la información de las películas de su catálogo.En la versión inicial del programa se usa como estructura de datos para almacenar una película un diccionario con los elementos principales de la película. Un ejemplo de la misma es la siguiente:

```python
pelicula = {
    "nombre" : "Aterriza como puedas",                                  # Nombre de la receta
    "duracion" : 88,                                                    # Tiempo en minutos de la película
    "reparto" : ["Robert Hays", "Julie Hagerty", "Leslie Nielsen", "Lloyd Bridges"]
}
``` 

En un fichero de nombre `peliculas_v1.txt` se incluyen en cada línea del mismo y en formato `json` diferentes recetas. Crea el fichero desde el sistema operativo e inserta en el mismo el siguiente contenido:

```
{"nombre": "Aterriza como puedas", "duracion": 88, "reparto": ["Robert Hays", "Julie Hagerty", "Leslie Nielsen", "Lloyd Bridges"]}
{"nombre": "Los Cazafantasmas", "duracion": 107, "reparto": ["Bill Murray", "Dan Aykroyd", "Sigourney Weaver"]}
{"nombre": "Avatar", "duracion": 137, "reparto": ["Sam Worthington", "Sigourney Weaver", "Zoe Saldana"]}
{"nombre": "Lost in traslation", "duracion": 105, "reparto": ["Bill Murray", "Scarlett Johansson"]}
```

Crea un fichero de nombre `peliculas_v1.py` e incluye en el mismo las funciones que se enumeran a continuación y ejemplos de uso de las mismas:

**Nota:** para evitar que las funciones funcionen correctamente asegúrate de:
* Convertir a json las películas antes de escribirlas en el fichero
* Convertir a diccionario al leerlas para poder acceder a la información de las mismas.
* Que las funciones no dejen líneas en blanco ni al final ni entre la información de una película y otra.

¡¡¡Mucha suerte!!!

#### `mostrar_pelicula()` **1p**

Le pasamos el **nombre** de una pelicula y **muestra por pantalla** la información de la misma de la forma:

```
Nombre: Aterriza comopuedas
Duración: 88 minutos
Reparto:
* Robert Hays
* Julie Hagerty
* Leslie Nielsen
* Lloyd Bridges"
```



#### `mostrar_pelicula_actor()` **1,5p**

Se le pasa a la función el nombre de un **actor** y la función devolvera una **lista** con el **nombre** de las peliculas en las que dicho actor participa. En caso de no haber ninguna película que cumpla el criterio la función devolverá `False`


#### `nueva_pelicula()` **1,5p**

Se le pasa como parámetros:
* El nombre de la película
* La duración en minutos
* La lista de actores principales

Si la película ya está en el archivo no debe añadirse al mismo y la función debe devolver `False`. Devolverá `True` en caso contrario.

**Nota:** para evitar problemas de codificación de carácteres no utilices caracteres que no sean del alfabeto inglés en las recetas. (No usar ñ, á, é, í, ó, ú). 

#### `anadir_actor()` **1,5p**

Se le pasa como parámetro el nombre de la película y el nombre de un actor y se modifica la película en el fichero añadiendo el nuevo actore a la lista con el reparto de la misma. Si el actor ya está en la lista no debe ser añadido a la misma y la función debe devolver `False`. Devolverá `True` en caso contrario.

#### `eliminar_receta()` **1,5p**

Se le pasa como parámetro el nombre de la película y la elimina del fichero. En caso de no existir la película la función debe devolver `False`



### Parte 2

Con el fin de tener más información de los alquileres de cada película se modifica la estructura de datos de forma que en la misma se guarda también la información de los alquileres realizados en forma de lista de diccionarios en los que la clave es el número de socio y el valor es, a su vez, otro diccionario con las fechas de alquiler y devolución de la película.

```python
pelicula = {
    "nombre" : "Aterriza como puedas",
    "duracion" : 88,
    "reparto" : ["Robert Hays", "Julie Hagerty", "Leslie Nielsen", "Lloyd Bridges"],
    "alquileres": {
        "002" : {"f_alquiler": "2022-02-03", "f_devolucion": "2022-02-07"},
        "011" : {"f_alquiler": "2022-03-11", "f_devolucion": "2022-03-17"},
        "033" : {"f_alquiler": "2022-04-15", "f_devolucion": ""},
    }
}
``` 
Ten en cuenta, que en el ejemplo anterior, si queremos mostrar la de alquiler de la película realizado por el socio "011" lo haríamos ejecutando: 

```python
print(pelicula["alquileres"]["011"]["f_alquiler"])
```

Para esta segunda parte, crea un fichero de nombre `peliculas_v2.txt` e inserta en el mismo el siguiente contenido:

```
{"nombre": "Aterriza como puedas", "duracion": 88, "reparto": ["Robert Hays", "Julie Hagerty", "Leslie Nielsen", "Lloyd Bridges"], "alquileres": {"002": {"f_alquiler": "2022-02-03", "f_devolucion": "2022-02-07"}, "011": {"f_alquiler": "2022-03-11", "f_devolucion": "2022-03-17"}, "033": {"f_alquiler": "2022-04-15", "f_devolucion": ""}}}
{"nombre": "Los Cazafantasmas", "duracion": 107, "reparto": ["Bill Murray", "Dan Aykroyd", "Sigourney Weaver"], "alquileres": {"102": {"f_alquiler": "2021-09-30", "f_devolucion": "2021-10-07"}, "033": {"f_alquiler": "2022-02-11", "f_devolucion": "2022-02-18"}}}
{"nombre": "Avatar", "duracion": 137, "reparto": ["Sam Worthington", "Sigourney Weaver", "Zoe Saldana"], "alquileres": {"012": {"f_alquiler": "2022-02-11", "f_devolucion": ""}}}
{"nombre": "Lost in traslation", "duracion": 105, "reparto": ["Bill Murray", "Scarlett Johansson"], "alquileres": {"124": {"f_alquiler": "2020-12-21", "f_devolucion": "2020-12-25"}}}
```

Crea un fichero de nombre `peliculas_v2.py` e inserta en el mismo las siguientes funciones y ejemplos de uso de las mismas:


#### `obtener_peliculas_no_devueltas()` **1,5p**

Las películas no devueltas son aquellas cuya **fecha de devolución** esta **vacia** (""). De cada película no devuelta, la función mostrará el **nombre** de las película y el **número de socio** que la ha alquilado. En caso de que **todas** las películas hayan sido devueltas la función devolverá `False`.

Suponer que solo puede haber un alquiler sin devolver en toda la lista de alquileres de una película.

#### `devolver_pelicula()` **1,5p**

Se le pasa como parámetro el **nombre de la película**, el **número de socio** que la tenía alquilada y la **fecha de devolución** y se modifica en el fichero dicha información y la función devuelve `True`. La función devolverá `False` en caso de:
* No existir la película
* La película existe pero no haya ningún alquiler de dicho socio
* La película haya sido alquilada por el socio pero ya esté devuelta.
