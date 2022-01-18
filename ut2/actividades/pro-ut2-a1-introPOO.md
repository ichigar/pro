# PRO - UT2-A1- Introducción POO

## Paradigmas de programación
En programación, un **paradigma** es un enfoque concreto de desarrollar y
estructurar el desarrollo de programas

En la unidad anterior hemos aprendido a programar utilizando el paradigma **imperativo**

No es el único paradigma que existe:

* Funcional
* Orientado a objetos

### Paradigma de la programación imperativa o estructurada

Consiste en una secuencia de instrucciones que el ordenador debe ejecutar.

Los elementos más importantes en esta forma de programar son:
1. **Variables**: zonas de memoria donde guardamos información.
2. **Tipos de datos**: son los valores que se pueden almacenar.
3. **Expresiones**: corresponde a operaciones entre variables (del mismo o distinto tipo)
4. **Estructuras de control**: 
* **Secuenciales**: ejecución de instrucciones de forma consecutiva
* **Bucles**: permiten ejecutar un conjunto de instrucciones varias veces
* **Condicionales**: ejecutar una parte del código u otra en función de que se cumpla una condición o abortar la ejecución del programa.

### Paradigma de la programación orientada a objetos

Se basa en la idea de agrupación de datos y funciones relacionados en "unidades" de información.

El tipo de datos nuevo que permite agrupar datos y funciones se llama **clase**

A cada variable de tipo clase se le denomina **objeto**

## Ventajas de la POO

La OOP no es mejor ni peor que otros paradigmas. Cada paradigma es más o menos útil en función del tipo de problema que queremos solucionar.

Algunas ventajas de la OOP son:


* **Encapsulación de datos**: los datos y las operaciones para modificarlos pertenecen al objeto y solo son accesibles desde el mismo.  
* **Simplicidad**: la creación de grandes sistemas es una tarea compleja, con muchos problemas que resolver. La capacidad de dividir la complejidad en problemas más pequeños, en **objetos** permite simplificar la tarea global.

* **Facilidad de modificación**: cuando se basa en objetos y modela el sistema con ellos, es más fácil realizar el seguimiento de qué partes del sistema se deben modificar. Todo esto facilita la corrección de errorers o agregar una característica nueva.
* **Capacidad de mantenimiento**: en general, el mantenimiento del código es difícil y con el tiempo se complica más. Requiere disciplina en forma de una nomenclatura correcta y una arquitectura clara y coherente, entre otros aspectos. El uso de **objetos** facilita la **búsqueda de un área concreta** del código que necesita mantenimiento.
* **Reusabilidad**: la definición de un objeto se puede usar muchas veces en muchas partes del sistema o, potencialmente, también en otros sistemas. 

## Clases

Una **clase** es una entidad que define una serie de elementos que determinan un estado (datos) y un comportamiento (operaciones sobre los datos que modifican su estado).

Hemos visto que python define una serie de tipos de datos **primitivos** incluidos con el lenguaje. Los hemos utilizado al definir variables (int, float, str, list, tuple, ....)

Cuando creamos una clase estamos definiendo un nuevo tipo de dato.

Para crear una clase en Python usamos la palabra reservada `class`

Una clase básica la podemos crear en Python de la siguiente forma:

```python
class Coche:    # Declaración de la clase
    pass        # Código de la clase
```

> Por convención se usa notación **CamelCase** a la hora de asignar nombres a las clases. Esta notación consiste en poner en mayúscula el primer caracter del nombre de la clase. Si el nombre tiene varias palabras se ponen juntas sin espacios y con el primer caracter de cada palabra en mayúscula (Ejemplo `CocheCarrerasFormula1`)

**Actividad 1**

Crea la clase vacia `Perro`

```python

```

## Creación de objetos

Una clase es un molde, una plantilla, un tipo de dato definido por el programador.

Un objeto es una variable del tipo de la clase que hemos definido.

En Python creamos un objeto asignando a una variable la clase que hemos definido:

```python
coche = Coche()
```
Con la asignación anterior hemos creado una **objeto** de la clase **Coche**. A este proceso se ledenomina **instanciar** o crear una **instancia**

Podemos crear todos los objetos de una clase que queramos:

```python
c1 = Coche()
c2 = Coche()
```

**Actividad 2**

Crea dos objetos de la clase `Perro` de nombre `toby` y `kaiko`

```python

```

## Añadir atributos a una clase

Los atributos o datos encapsulados en un objeto se crean cuando se crea una instancia de un objeto.

Hay una función especial a la que se llama en el momento de la creación, denominada **constructor**.

### Constructor

Un **constructor** es una función especial que solo se invoca al crear por primera vez el objeto. Por tanto, el constructor solo se llamará una vez. 

En este método, se crean los **atributos** que debe tener el objeto. Además, se asignan **valores iniciales** a los atributos creados.

Por tanto, este método es el encargado de crear el **estado inicial** de un objeto,

En Python, el constructor tiene el nombre `__init__()`. 

A `__init__()` le podemos dar el número de parámetros que queramos, pero el primer parámetro de `__init__()` debe ser siempre una variable especial de nombre `self` que hace referencia al **propio** objeto y permite que le añadamos atributos al objeto:

```python
class Coche:
    def __init__(self, color, velocidad):
        self.color = color
        self.velocidad = velocidad
```

> La indentación de `def` es la que permite saber a Python que el método `__init__()` pertenece a la clase `Coche`.

En el cuerpo de `__init__()` hay dos instrucciones que usan la variable `self`:
* `self.color = color` crea el atributo de nombre `color` y asigna al mismo el valor del parámetro `color`
* `self.velocidad = velocidad` crea el atributo de nombre `velocidad` y asigna al mismo el valor del parámetro `velocidad`

Si ahora queremos crear un objeto de la clase Coche de la misma forma:

```python
coche = Coche()
Se produjo una excepción: TypeError       (note: full exception trace is shown but execution is paused at: <module>)
__init__() missing 2 required positional arguments: 'color' and 'velocidad'
  File "/home/ivan/mega/clases/pro/proyectos/test/test_objetos.py", line 6, in <module> (Current frame)
    coche = Coche()
```

Python devuelve un error indicando que debemos pasar dos parámetros al crear el objeto.

```python
coche_rojo = Coche("rojo", 20)
coche_blanco = Coche("blanco", 30)
```

Acabamos de crear dos instancias de la clase `Coche` el objeto `coche_rojo` un coche rojo que circula a 20Kmh y el objeto `coche_verde` que representa a un coche de color verde que circula a 30Kmh

> Fíjate que aunque `__init__()` tiene 3 parámetros solo hemos pasado 2 al crear el objeto; Python se encarga de pasar de forma automática `self` en el momento de llamar al constructor y no debemos pasarlo como parámetro.

Después de crear un objeto podemos acceder a sus atributos usando  **notación punteada**

```python
>>> coche_rojo.color
'rojo'
>>> coche_blanco.velocidad
30
```

**Actividad 3**

Modifica la clase `Perro` de forma que los objetos de dicha clase tengan nombre y edad y raza

```python
class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self. raza = raza
```

**Actividad 4**

Crea los objetos:
* `toby` que será un Perro de nombre **Toby**, de 4 años y raza **Pastor alemán**
* `kaiko` que será un Perro de nombre **Kaiko**, de 6 años y raza **Chihuahua**

```python
toby = Perro("Toby", 4, "Pastor Alemán")
kaiko = Perro("Kaiko", 6, "Chihuahua")
```

### Atributos de clase

Los atributos que acababamos de definir se llaman **atributos de instancia** y son especificos de cada objeto en el momento de crearlos.

Python permite definir también **atributos de clase**, son atributos que tienen el mismo valor en todos los objetos que creemos en una determina clase.

Se crean asignando valor a una variable fuera del método `__init__()`. Dichas variables deben estar indentadas y ubicadas al principio de la definición de la clase. Ademas deben inicializarse.

Por ejemplo, todos los coches tienen en común tener 4 ruedas:

```python
class Coche:
    # Atributos de clase
    ruedas = 4
    
    def __init__(self, color, velocidad):
        # Atributos de instancia
        self.color = color
        self.velocidad = velocidad
```

Con la notación punteada podemos acceder también a los atributos de clase

```python 
>>> coche_rapido = Coche("azul", 120)
>>> coche_rapido.ruedas
4
```

**Actividad 5**

Modifica la clase `Perro` añadiendo el atributo de clase `especie` inicializa su valor a "Canis familiaris"

Inserta el código completo de la clase
```python

```

## Métodos de instancia

Los métodos de instancia son funciones definidas dentro de una clase y qué solo pueden ser llamados desde un objeto de la clase.

El primer parámetro de un método, igual que en el constructor `__init__()` debe ser siempre `self`

```python
class Coche:
    ruedas = 4
    
    def __init__(self, color, velocidad):
        self.color = color
        self.velocidad = velocidad
        
    # métodos de instancia
    def descripcion(self):
        return f"El coche tiene color {self.color} y una velocidad de {self.velocidad} Kmh"
    
    def acelera(self, incremento):
        self.velocidad += incremento
        return f"Nueva velocidad: {self.velocidad} Kmh"
    
```

Hemos añadido a la clase dos métodos de instancia:

* `descripcion()` que devuelve una cadena mostrando el color y la velocidad del coche
* `acelera()` que incrementa la velocidad del coche con el parámetro que le pasemos y devuelve una cadena de texto que informa de la nueva velocidad.

Para ejecutar los métodos de instancia usamos notación punteada.

```python=
>>> coche_rojo = Coche("rojo", 80)

>>> coche_rojo.descripcion()
'El coche tiene color rojo y una velocidad de 80 Kmh'

>>> coche_rojo.acelera(20)
'Nueva velocidad: 100 Kmh'
```

**Actividad 6*+

Añade a la clase Perro los métodos:

* `caracteristicas()` devuelve cadena de texto con todas las características del objeto.
* `cumpleanos()` añade un año a la edad del perro.
* `ladrar()` se le pasa una cadena de texto (ejemplo: si ha Kaiko le pasamos el método ladrar con "Guau guau" de parámetro) devuelve la cadena "Kaiko dice Guau guau"

Inserta el código completo de la clase
```python
class Perro:
    especie = "Canis familiaris"
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    def caracteristicas(self):
        return f"El perro se llama {self.nombre} tiene {self.edad} años y es de raza {self.raza}"
    def cumpleanos(self):
        self.edad += 1
        
    def ladrar(self, sonido):
        return f"{self.nombre} dice ¡{sonido}!"


toby = Perro("Toby", 4, "Pastor Alemán")
kaiko = Perro("Kaiko", 6, "Chihuahua")
print(kaiko.caracteristicas())
kaiko.cumpleanos()
print(kaiko.caracteristicas())
print(toby.ladrar("auuuuuuuuuuuu"))
```

**Actividad 7**

Investiga qué son los métodos **dunder** en Python. Inserta la respuesta:

> R: 

## El método `__str__()`

Cuando creamos una clase es buena idea disponer de un método que permita mostrar la información relevante del objeto. En el caso anterior hemos creado un método de nombre `descripcion()` que realiza dicha función, pero está no es la forma más "Pythonica" de hacerlo

Por ejemplo, si creamos una lista Python muestra una representación de la misma si usamos `print()` para mostrarla.

```python
>>> names = ["Fletcher", "David", "Dan"]
>>> print(names)
['Fletcher', 'David', 'Dan']
```

Sin embargo, si llamamos con `print()` un objeto que hayamos creado de la clase Coche obtenemos algo como:

```python=
>>> print(coche_rojo)
<__main__.Coche object at 0x00aeff70>
```

Obtenemos un mensaje críptico que indica que `coche_rojo` es un objeto de la clase `Coche` y a continuación su dirección de memoria.

Podemos cambiar el resultado de `print()` sobre un objeto creando un método especial de nombre `__str__()`.

Si para la clase anterior cambiamos el nombre del método `descripcion()` por `__str__()`ahora obtendremos un resultado más amigable al mostrar con `print()` el objeto:

```python
class Coche:
    ruedas = 4
    
    def __init__(self, color, velocidad):
        self.color = color
        self.velocidad = velocidad
        
    # métodos de instancia
    def __str__(self):
        return f"El coche tiene color {self.color} y una velocidad de {self.velocidad} Kmh"
    
    def acelera(self, incremento):
        self.velocidad += incremento
        return f"Nueva velocidad: {self.velocidad} Kmh"

coche_rojo = Coche("rojo", 80)

print(coche_rojo)
```

Al ejecutar obtenemos:

```
El coche tiene color rojo y una velocidad de 80 Kmh
```
**Actividad 8**
Aprovecha método existente en clase perro para crear método `__str__()`

Inserta clase:

```python

```

## Actividades de consolidación

9. Clase Alumno

Crea una clase de nombre Alumno que tendrá dos atributos de instancia `nombre` que representa el nombre del alumno y `notas` que permitira almacenar una lista de notas del alumno.

La clase tendrá el atributo de clase `centro` que inicializaremos a "IES Ana Luisa Benítez"

La clase tendrá los siguientes métodos:

* Constructor

    * Parámetros: Recibe el **nombre**. 
    * Operación: Crea una objeto de un alumno con `nombre` **nombre** y una lista vacia para sus notas.

* Representación
    * Devuelve cadena de texto con el nombre y las notas del alumno
    
* Inicialización notas al azar

    * Parámetros: n
    * Operación: crea n notas al azar entre 1 y 10 y las almacena en la lista de `notas`
    * Devuelve: nada

* Inicializar valores manualmente
    * Parámetros: ninguno
    * Devuelve: nada
    * Operación: **inicializa** la lista de `notas` con valores leido de teclado

* Encontrar nota media
    * Parámetros: ninguno
    * Devuelve: nota media del alumno
    * Operación: calcula el valor medio de las notas contenidas en la lista

* Numero de suspensos
    * Parámetros: ninguno
    * Devuelve: entero con el número de suspensos
    * Operación: calcula número de notas menores de 5 del alumno
* Añadir nota
    * Parámetros: nota
    * Devuelve: nada
    * Añade el valor **nota* al principio de la lista de notas

10. Formas geométricas del plano

Crea las clases `Cuadrado`, `Rectangulo` y `Circulo` de forma que cuando creemos un objeto de cada una de dichas clases podamos calcular para cada uno su area y perimetro.

Inserta código de las clases y ejemplos de objetos de cada una calculando el área y el perímetro

```python
```

## Objetos como parámetros de otro objeto

Un objeto puede recibir como parámetros otros objetos.

**Actividad 11**

a. Crea una clase llamada `Punto` que tendrá como atributos las coordenadas `x` e `y` del punto en cuestión. Al constructos se le pasaran las coordenadas del punto.

Al mostrar un objeto de la clase `Punto` con `print()` se devolverá un mesaje de texto con las coordenadas del mismo

b. Crea una clase llamada `Segmento`. Sus atributos serán dos objetos de la clase `Punto`. Como método tendrá longitud, que devolverá la distancia entre los dos puntos que componen el segmento. 

> distancia entre dos puntos = `math.sqrt ((x1-x2)**2 + (y1-y2)**2)`

Inserta solución:

```python

```

## Recursos
* [POO - ferestrepoca](https://ferestrepoca.github.io/paradigmas-de-programacion/poo/poo_teoria/concepts.html)
* [Tutorial POO - J2Logo](https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/)
* [python oop - curso microsoft.com](https://docs.microsoft.com/es-es/learn/modules/python-object-oriented-programming/1-introduction)
* [OOP en Python 3 - Realpython](https://realpython.com/python3-object-oriented-programming/)
* [Object Oriented Programming in Python - Usman Malik - stackabuse.com](https://stackabuse.com/object-oriented-programming-in-python/)
###### tags: `pro` `ut2` `poo` ìntroducción`