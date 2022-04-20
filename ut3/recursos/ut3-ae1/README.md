# PRO-UT3-AE1. Prueba práctica

## Recursos

* Podrás usar los apuntes de la unidad colgados en la plataforma en el apartado **Contenidos** de la unidad.
* Abre los mismos y cuando hayas terminado esconecta el cable de red del equipo. 


## Criterios de evaluación

* El programa o función **funciona correctamente** y realiza todas las acciones solicitadas
* Los **nombres** de variables y funciones son significativos sin ambigüedad la información que almacenan o la funcionalidad que realizan.
* El código es **claro**, **eficiente** y **legible**
* Si es necesario, se crean **funciones intermedias** que hacen el código más legible o refactorizan tareas que se hacen de forma repetitiva en diferentes apartados

## Enunciado

### Parte 1

En la cocina de restaurante se informatizan las recetas de los platos que se preparan. En la versión inicial del programa se usa como estructura de datos para almacenar una receta un diccionario con los elementos principales de la receta. Un ejemplo de la misma es la siguiente:

```python
receta = {
    "nombre" : "tortilla papas",                                        # Nombre de la receta
    "tiempo" : 30,                                                      # Tiempo en minutos de elaboración
    "ingredientes" : ["papas", "huevos", "cebolla", "aceite", "sal"]
}
``` 

En un fichero de nombre `recetas_v1.txt` se incluyen en cada línea del mismo y en formato `json` diferentes recetas. Crea el fichero desde el sistema operativo e inserta en el mismo el siguiente contenido:

```
{"nombre": "pollo verduras", "tiempo": 45, "ingredientes": ["pollo", "cebollas", "zanahorias", "calabacines"]}
{"nombre": "tortilla papas", "tiempo": 30, "ingredientes": ["papas", "huevos", "cebolla", "aceite", "sal"]}
{"nombre": "tortilla francesa", "tiempo": 10, "ingredientes": ["huevos", "aceite", "sal"]}
{"nombre": "arroz cubana", "tiempo": 30, "ingredientes": ["arroz", "huevos", "papas", "salchichas", "aceite", "sal"]}
```

Crea un fichero de nombre `recetas_v1.py` e inserta en el mismo las siguientes funciones:

#### `mostrar_receta()` **1p**

Le pasamos el **nombre de una receta** y muestra por pantalla la información de la misma de la forma:

```
Nombre: Tortilla papas
Tiempo: 30 minutos
Ingredientes:
* papas
* huevos
* cebolla
* aceite
* sal
```

Solución:

```python
import json

FILE_RECETAS = "recetas_v1.txt"

def mostrar_receta(nombre_receta):
    with open(FILE_RECETAS, "r") as file:
        for receta_json in file:
            receta = json.loads(receta_json)
            if receta["nombre"] == nombre_receta:
                print(f"Nombre: {receta['nombre']}")
                print(f"Tiempo: {receta['tiempo']} minutos")
                print("Ingredientes:")
                for ingrediente in receta["ingredientes"]:
                    print(f"* {ingrediente}")
                return
            print("La receta no existe")

mostrar_receta("tortilla francesa")
```

Se podría refactorizar extrayendo el código en el que se muestra la receta a otra función:

```python
import json

FILE_RECETAS = "recetas_v1.txt"

def print_receta(receta):
    print(f"Nombre: {receta['nombre']}")
    print(f"Tiempo: {receta['tiempo']} minutos")
    print("Ingredientes:")
    for ingrediente in receta["ingredientes"]:
        print(f"* {ingrediente}")

def mostrar_receta(nombre_receta):
    with open(FILE_RECETAS, "r") as file:
        for receta_json in file:
            receta = json.loads(receta_json)
            if receta["nombre"] == nombre_receta:
                print_receta(receta)
                return

mostrar_receta("tortilla francesa")
```

También podemos usar el método `readlinnes()` para cargar las líneas del fichero en una lista y luego recorrerlas:

```python
def mostrar_receta(nombre_receta):
    with open(FILE_RECETAS, "r") as file:
        recetas = file.readlines()                  # Leemos líneas a lista
        for receta_json in recetas:                 # la líneas del fichero contienen texto en formato json
            receta = json.loads(receta_json)        # pasamos la línea a diccionario
            if receta["nombre"] == nombre_receta:
                print_receta(receta)
                return
        print("Receta no encontrada")
```

#### `mostrar_receta_ingredientes()` **1,5p**

Se le pasa a la función un lista de ingredientes y muestra todas las recetas que incluyen **todos los ingredientes** de la lista.

solución:

```python
def mostrar_receta_ingredientes(lista_ingredientes):
    with open(FILE_RECETAS,"r") as file:
        recetas = file.readlines()
        for receta_json in recetas:                 
            receta = json.loads(receta_json)
            ingredientes_receta = receta["ingredientes"]   # Extraemos los ingredientes de la receta que estamos recorriendo
            
            # Comprobamos si todos los ingredientes que buscamos están en la receta
            contiene_ingredietes = True
            for ingrediente in lista_ingredientes:
                if ingrediente not in ingredientes_receta:
                    contiene_ingredietes = False
            
            if contiene_ingredietes:
                mostrar_receta(receta["nombre"])
                
mostrar_receta_ingredientes(["aceite", "sal", "huevos"])
```

Se podría refactorizar con una función a la que le pasamos dos listas y devuelve verdadero en caso de que todos los elementos de la primera lista estén contenidos en la segunda lista:

```python
def lista_en_lista(lista, lista_buscar):
    """Comprueba si todos los elementos de lista están en lista_buscar """
    
    for item in lista:
        if item not in lista_buscar:
            return False
    return True

def mostrar_receta_ingredientes(lista_ingredientes):
    with open(FILE_RECETAS,"r") as file:
        recetas = file.readlines()
        for receta_json in recetas:                 
            receta = json.loads(receta_json)
            ingredientes_receta = receta["ingredientes"]   # Extraemos los ingredientes de la receta que estamos recorriendo
            
            # Comprobamos si todos los ingredientes que buscamos están en la receta
            if lista_en_lista(lista_ingredientes, ingredientes_receta):
                mostrar_receta(receta["nombre"])
                
mostrar_receta_ingredientes(["aceite", "sal", "huevos"])
```

#### `nueva_receta()` **1,5p**

Se le pasa como parámetros:
* El nombre de la receta
* El tiempo de preparación
* La lista de ingredientes

Añade la receta al fichero.

Importante tener en cuenta que a la hora de añadir la receta al fichero:
* Debemos abrirlo en modo append
* Hemos de convertir el diccionario a `json` antes de escribirlo
* Se debe añadir un salto de línea al principio para que se escriba en una nueva línea:

```python
def nueva_receta(nombre_receta, tiempo, lista_ingredientes): 
    with open(FILE_RECETAS,"a") as file:    # Abrimos el fichero en modo append
        receta = {
            "nombre":nombre_receta, 
            "tiempo":tiempo, 
            "ingredientes":lista_ingredientes
        }
        
        file.write("\n" + json.dumps(receta))   # Escribimos el diccionario en formato json

nueva_receta("arbejas", 15, ["arbejas", "zanahoria", "aceite", "sal"])
```

**Nota:** para evitar problemas de codificación de carácteres no utilices caracteres que no sean del alfabeto inglés en las recetas. (No usar ñ, á, é, í, ó, ú)

#### `anadir_ingrediente()` **1,5p**

Se le pasa como parámetro el nombre de la receta y el nombre de un ingrediente y se modifica la receta en el fichero añadiendo el nueva ingrediente a la lista de ingredientes de la misma.

#### `eliminar_receta()` **1,5p**

Se le pasa como parámetro el nombre de la receta y la elimina del fichero

### Parte 2

Con el fin de tener más información de las recetas se modifica la estructura de datos de forma que en la receta se indica para cuantas personas es y se dan más detalles de los ingredientes inluyendo aparte del nombre, la cantidad y la unidad de medida de los mismos. Un ejemplo sería el siguiente:

```python
receta = {
    "nombre" : "tortilla papas",                                    # Nombre de la receta
    "tiempo" : 30,                                                     # Tiempo en minutos de elaboración
    "personas" : 2,
    "ingredientes" : {
        "papas" : {"cantidad" : 300, "unidad" : "gramos"},
        "huevos" : {"cantidad" : 2, "unidad" : "unidades"},
        "cebolla" : {"cantidad" : 50, "unidad" : "gramos"},
        "aceite" : {"cantidad" : 100, "unidad" : "mililitros"},
        "sal" : {"cantidad" : 1, "unidad" : "pizca"}
    }
}
``` 

Ten en cuenta, que en el ejemplo anterior, si queremos mostrar la cantidad de `cebolla` a utilizar lo podríamos hacer ejecutando: 

```python
print(receta["ingredientes"]["cebolla"]["cantidad"])
```

Para esta segunda parte, crea un fichero de nombre `recetas_v2.txt` e inserta en el mismo el siguiente contenido:

```
{"nombre": "tortilla papas", "tiempo": 30, "personas": 2, "ingredientes": {"papas": {"cantidad": 300, "unidad": "gramos"}, "huevos": {"cantidad": 2, "unidad": "unidades"}, "cebolla": {"cantidad": 50, "unidad": "gramos"}, "aceite": {"cantidad": 100, "unidad": "mililitros"}, "sal": {"cantidad": 1, "unidad": "pizca"}}}
{"nombre": "tortilla francesa", "tiempo": 10, "personas": 1, "ingredientes": {"huevos": {"cantidad": 1, "unidad": "unidades"}, "aceite": {"cantidad": 10, "unidad": "mililitros"}, "sal": {"cantidad": 1, "unidad": "pizca"}}}
{"nombre": "espaguetis carbonara", "tiempo": 35, "personas": 4, "ingredientes": {"espaguetis": {"cantidad": 400, "unidad": "gramos"}, "queso parmesano": {"cantidad": 100, "unidad": "gramos"}, "huevos": {"cantidad": 2, "unidad": "unidades"}, "beicon": {"cantidad": 150, "unidad": "gramos"}}}
```

Crea un fichero de nombre `recetas_v2.py` e inserta en el mismo las siguientes funciones:


#### `mostrar_receta_personas()` **1,5p**

Le pasamos el nómbre de una receta y el número de personas para la que se quiere preparar y muestra la receta con las cantidades ajustadas al número de personas. 

Así, por ejemplo, se llamamos a la función `mostrar_receta_personas("tortilla papas", 3)` debería mostrar:

```
Nombre: Tortilla papas
Tiempo: 30 minutos
Personas: 3
Ingredientes:
* papas: 450 gramos
* huevos: 3 unidades
* cebolla: 75 gramos
* aceite: 150 mililitros
* sal: 1.5 pizca
```

#### `anadir_ingrediente()` **1,5p**

Se le pasa como parámetro el nombre de la receta y el nombre de un ingrediente, la cantidad y la unidad y se modifica la receta en el fichero añadiendo el nuevo ingrediente a la lista de ingredientes de la misma.

