# PRO-UT1-AER2. Recuperación. Prueba práctica
## Ejercicios
### A1. Validar código postal de la provincia de Gran Canaria

Crea **a1.py**. Su contenido inicial es el siguiente:

```python
def valid_cp_gc(cp):
    """
    validates postal code of Gran Canaria
    :cp:str
    :return:True|str
    """
    # Completar código de la función
    pass # eliminar esta línea

# Ejemplos de ejecución y resultado
print(valid_cp_gc("3501"))                  # 'longitud no válida'
print(valid_cp_gc("3B*0a"))                 # 'debe contener solo dígitos numéricos'
print(valid_cp_gc("38005"))                 # 'no empieza por 35'
print(valid_cp_gc("35201"))                 # 'debe ser menor de 35200'
print(valid_cp_gc("35105"))                 # True
```

A la función `valid_email()` le pasamos una cadena de texto con una dirección de correo electrónico y **devuelve** `True` si el email es válido o un mensaje de error si no lo es. 

En caso de que el email no sea válido el programa debe mostrar un mensaje indicando el primer criterio que no cumpla.

Las comprobaciones se harán en el siguiente orden:

* **Longitud**: 
    * Tiene longitud de exactamente 5 caracteres
    * Mensaje de error: **longitud no válida**
* **Carácteres numéricos**:
    * Los caracteres del código postal solo pueden ser números
    * Mensaje de error: **debe contener solo dígitos numéricos**
* **Empieza por**  `35`
	* Todos los códigos postales de la provincia de Gran Canaria empiezan por 35
	* Mensaje de error: **no empieza por 35**
* **Valor menor a** `35200`
	* El valor numérico debe estar entre 35000 y 35200
	* Menaje de error: **debe ser menor a 35200** 	

### A2. De snake_case a camelCase

Crea el archivo **a2.py**. Su contenido inicial es el siguiente:

```python
def sc2cc(identifier):
    """
    Converts text in snake_case format to camelCase format
    """
    # Completar código de la función
    pass # eliminar esta línea
    
print(sc2cc("nom_variable"))            # 'nomVariable'
print(sc2cc("nom_variable_compuesto"))  # 'nomVariableCompuesto'
print(sc2cc("variable"))                # 'variable'
```
Completa la función `sc2cc()` de forma que si le pasamos un identificador en formato "snake case"  **devuelve** el identificador convertido a formato "camel case".

Suponer que el identificador recibido es válido.

### A3. Juego mayor diferencia entre dados
**Marcos** y **Julio** juegan con tres dados y calculan la **diferencia** entre el dado más alto y el dado más bajo de los que tiran. 

Para cada tirada de cada jugador se muestra la puntuación obtenida. El que obtiene mayor diferencia gana.

Después de cada juego se pregunta si se desea jugar otra vez. Si la respuesta no es 's' se muestra mensaje indicando que el juego ha finalizado.

No se permite usar las funciones `max()` o `min()`


Ejemplos de ejecución:

```
JUEGO DE DADOS
Tirada de Marcos: 3 5 2 => 3 puntos
Tirada de Julio:  5 3 3 => 2 puntos
Ha ganado Marcos.
Desea jugar otra vez (s/n): s

JUEGO DE DADOS
Tirada de Marcos: 5 5 3 => 2 puntos
Tirada de Julio:  3 1 1 => 2 puntos
Han empatado.
Desea jugar otra vez (s/n): n

JUEGO FINALIZADO
```

Completar el código en el archivo **a3.py**.

### A4. Resultados baloncesto

Crear el archivo **a4.py**. Su contenido es el siguiente.

```python
def resultado(anotaciones):
    # completar función
    pass #Eliminar esta línea

def ganador(anotaciones):
    # completar función
    pass #Eliminar esta línea

def mayor_anotacion(anotaciones):
    # completar función
    pass #Eliminar esta línea

def anotacion_media_equipo(anotaciones, i_equipo):
    # completar función
    pass # Eliminar esta línea
    

bar-mad = [
    [12, 15], 
    [16, 10],
    [20, 16],
    [17, 24]
]

# Mostramos el resultado del partido
r = resultado(bar-mad)
print(f"El resultado del partido fue: Barcelona: {r[0]}, Real Madrid: {r[1]}") 
# El resultado del partido fue: Barcelona: 65, Real Madrid: 65

# Mostramos el ganador del partido
i = ganador(bar-mad)
if i == 0:
    print("El ganador fue el Barcelona")
elif i == 1
    print("El ganador fue el Real Madrid")
else:
    print("¡Empate!")
# ¡Empate!

# Mostramos el cuarto con mayor anotación total
i = mayor_anotacion(bar_mad)
print(f"El cuarto con mayor anotación fue el número {i + 1}")  
# El cuarto con mayor anotación fue el número 4

# Mostramos la anotación media del Real Madrid en cada cuarto
i_mad = 1 # el Real Madrid es el equipo visitante
p_media = anotacion_media_equipo(bar-mad, i_mad)
print(f"El Real Madrid anotó {p_media} puntos de media en cada cuarto")
# El Real Madrid anotó 16.25 puntos de media en cada cuarto

```

Las funciones anteriores nos permiten mostrar estadísticas a partir de las anotaciones en cada **cuarto** de un partido de baloncesto (tiene 4 cuartos). 

En cada fila se guardan los puntos obtenidos por cada equipo en un cuarto. El primer valor es el del equipo local y el segundo valor el del equipo visitante.

Para probar las funciones tenemos los resultados de un partido entre "Barcelona" y Real "Madrid"

Las funciones hacen los siguientes cálculos:

* La función `resultado()` a la que le pasamos las anotaciones en cada cuarto de un partido y devuelve una lista con los puntos anotados por cada equipo. El primer elemento es la suma de puntos del equipo local y el segundo la suma de puntos del equipo visitante.
* La función `ganador()` a la que le pasamos las anotaciones en cada cuarto de un partido y devuelve el índice del equipo ganador (0 si gana el equipo local, 1 si gana el visitante y -1 en caso de empate)

* La función `mayor_anotacion()` a la que le pasamos la lista con  las anotaciones en cada cuarto de un partido y devuelve el índice del cuarto en el que se anotaron mayor número de puntos.

* La función `anotacion_media_equipo()` a la que le pasamos las anotaciones en cada cuarto de un partido y el índice de uno de los equipos (`0` para el local; `1` para el visitante) devuleve la puntuación media en cada cuarto para dicho equipo. Redondear el resultado con 2 decimales.




El resultado del programa debería ser de la forma:

```
El resultado del partido fue: Barcelona: 65, Real Madrid: 65
¡Empate!
El cuarto con mayor anotación fue el número 4
El Real Madrid anotó 16.25 puntos de media en cada cuarto
```



## Puntuación

El valor de las funciones/ejercicios en el examen es de:

* `valid_cp_gc()` - **2ptos**
* `sc2cc()` - **1ptos** 
* juego mayor diferencia entre dados - **3ptos**
* `resultado()` - **1pto**
* `ganador()` - **1pto**
* `mayor_anotacion()` - **1ptos**
* `anotacion_media_equipo()` - **1pto**
