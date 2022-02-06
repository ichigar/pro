# PRO-UT2-3. Herencia
## Herencia

La **herencia** modela un tipo de relación llamada **es un** entre dos clases. Significa que cuando tenemos una clase **derivada** que hereda de una clase **base** se crea una relación en la que la clase `derivada` **es una** `especialización` de la clase `base`

En UML se representa de la siguiente forma:

![](https://i.imgur.com/N0wxyfl.jpg)

Las cajas representan las clases y la flecha la relación; parte de la clase derivada hacia la clase base y se suele añadir la palabra **extends** a la flecha.

En una relación de herencia:
* Las clases que heredan de otra se llaman clases **derivadas**, **subclases** o **subtipos**
* Las clases desde las que otras derivan se llaman clases **base** o **superclases**
* De una clase derivada se dice que **deriva**, **hereda** o **extiende** una clase base.

Si por ejejmplo, tenemos una clase `Animal` y derivamos de la misma una clase `Gato`, la relación de herencia indica que el `Gato` **es un** `Animal`. Esto significa que el `Gato` **hereda** las **características** de un `Animal`.

## Herencia simple en Python

### Definir clase heredada
Si tenemos dos clases en Python. Por ejemplo:

```python
class MotherClass:
    pass

class ChildClass:
    pass
```
Para establecer una relación de herencia entre ambas se hace especificando en la clase `hija` la clase `madre` como parámetro.

```python
class MotherClass:
    pass

class ChildClass(MotherClass):
    pass
```
### Miembros de clases heredadas

Su pongamos que tenemos una clase madre `Animal`:

```python
class Animal:
    def __init__(self, legs):
        self.legs = legs

    def walk(self):
        return "Animal walking..."
```

Si queremos crear las clases perro (`Dog`) y pato(`Duck`) de forma que **hereden** las características de la clase animal los hacemos de la manera siguiente:

```python
class Dog(Animal):
    def growl(self):
        return "A dog can growl but a duck can't. Grrr..."

class Duck(Animal):
    def quack(self):
        return "A duck can quack but a dog can't. Quack..."
```

Las clases hija cumplen con la característica de que un pato **es un** animal y un perro **es un** animal.

Al heredar, las clases hija tienen acceso a los miembros de la clase madre y por tanto incluyen:

* El atributo `legs`
* los métodos `__init__()` y `walk()` de la clase madre.

Por tanto, si creamos un objeto de una de las clases hija tiene las propiedades de la clase madre y las propiedades añadidas en la propia clase hija:

```python
toby = Dog(4)
print(toby.legs)    # 4
print(toby.walk())  # "Animal walking..."
print(toby.growl()) # "A dog can growl but a duck can't. Grrr..."

lucas = Duck(2)
print(lucas.legs)    # 4
print(lucas.walk())  # "Animal walking..."
print(lucas.quack()) # "A duck can quack but a dog can't. Quack..."
```

### Actividad 1

Crea la clase `Vehiculo` que tiene:

* atributos:
    * `_matricula`
    * `_color`
    * `_num_ruedas`
* métodos:
    * `__init__()` 
    * `get_matricula()` devuelve la matrícula
    * `__str__()` devuelve texto con descripción del vehículo de la forma: "vehículo con matrícula 1234ABC, de color rojo y 4 ruedas"

Crea la clase `CocheCombustion` que hereda de la clase `Vehículo` y tiene las propiedad añadidas:

* métodos:
    * `descripcion()` devuelve texto con la descripción. Por ejemplo: "Coche con motor de combustión con matrícula 1234ABC, de color rojo y 4 ruedas"

Crea la clase `CocheElectrico` que hereda de la clase `Vehículo` y tiene las propiedad añadida:

* métodos:
    * `descripcion()` devuelve texto con la descripción. Por ejemplo: "Coche con motor eléctrico con matrícula 1234ABC, de color rojo y 4 ruedas"

Crea la clase `Moto` que hereda de la clase `Vehículo` y tiene las propiedad añadida:

* métodos:
    * `descripcion()` devuelve texto con la descripción. Por ejemplo: "Moto con matrícula 1234ABC, de color rojo y 2 ruedas"

Crea un objeto de ejemplo de cada clase y prueba todos los métodos disponibles de cada uno.

Inserta resultado aquí:

```python

```

### Sobreescritura de métodos heredados

Si en una clase hija se crea un método con el mismo nombre que la clase madre el nuevo método **sobreescribe** el método de la clase madre.

```python
class Animal:
    def __init__(self, legs):
        self.legs = legs

    def walk(self):
        return "Animal walking..."

class Dog(Animal):
    def __init__(self, legs, color):
        self.legs = legs
        self.color = color
        
    def walk(self):
        return "Dog walking..."
```

### Actividad 2

Modifica las clases definidas en el ejemplo anterior de forma que:

Clase `CocheCombustion` se añade:

* atributo 
    * `_cilindrada` -> valor entero, representa cc, centímetros cúbicos del motor
* métodos a añadir/modificar para incluir la información de la cilindrada
    * `__init__()`
    * `__str__()`
    * `get_cilindrada`
    * `descripcion()` 


Clase `CocheElectrico` se añade:

* atributo 
    * `_potencia` -> valor entero, representa CV, caballos del motor
* métodos a añadir/modificar para incluir la información de la cilindrada
    * `__init__()`
    * `__str__()`
    * `get_potencia`
    * `descripcion()` 

Inserta resultado:

```python

```

### Accediendo a los métodos de la clase madre con super()

El método **super()** permite reutilizar el código de la clase madre en las clases hija. Veámoslo con un ejemplo.

```python
class Animal:
    def __init__(self, legs):
        self.legs = legs

    def walk(self):
        return "Animal. Walking..."

class Dog(Animal):
    def __init__(self, legs, color):
        super().__init__(legs)
        self.color = color

    def growl(self):
        return "A dog can growl but a duck can't. Grrr..."

class Duck(Animal):
    def quack(self):
        print("Duck child class. A duck can quack but a dog can't. Quack...")

fluffy = Dog(4, "grey")
print(fluffy.legs)      # 4
print(fluffy.color)     # "grey" 
```

### Actividad 3

Utiliza `super()` en las clases `CocheCombustion`, `CocheElectrico` y `Moto` en todos los casos posibles.

Inserta resultado:

```python

```
## Herencia múltiple

Python permite herencia múltiple. Se utiliza cuando la clase hija tiene características de **más de una clase madre**. En este caso, la clase hija hereda los miembres de más de una clase madre:

```python
class MotherClass1:
    pass

class MotherClass2:
    pass

class ChildClass(MotherClass1, MotherClass2):
    pass
```

Ejemplo:

```python
class SeaAnimal:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return "Swimming"

class LandAnimal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return "Walking..."

class Penguin(SeaAnimal, LandAnimal):
    def __init__(self, name):
        super().__init__(name)
```

En el caso anterior un Pingüino **es un** animal marino y **es un** animal terrestre y puede, por tanto, nadar y caminar.

```python
linux = Penguin("Tux")
print(linux.walk())     # Walking...
print(linux.swim())     # Swimming
```

## Orden de resolución

Al heredar de más de una clase madre se puede dar el caso de que dichas clases madres tengan un mismo métodos:

```python
class B:
    def x(self):
        print('x: B')


class C:
    def x(self):
        print('x: C')


class D(B, C):
    pass


d = D()
d.x()
```
El resultado de ejecutar el programa anterior es:

```
x: B
```

Python resuelve este caso siguiendo las siguientes reglas:

* Si el método ha sido sobreescrito en la clase hija, este es el que se ejecuta.
* Si el método no existe en la clase hija pero si en más de una de las clases madres se ejecuta el de aquella que se haya especificado antes a la hora de heredar.

Lo mismo pasa si usamos para llamar usando `super()` un método que existe en más de una clase madre, se resuelve ejecutando el de aquella que se haya indicando que hereda en primer lugar:

```python
class B:
    def x(self):
        print('x: B')


class C:
    def x(self):
        print('x: C')


class D(B, C):
    def x(self):
        super().x()
    pass


d = D()
d.x()        # 'x: B'
```

## Usando métodos de más de una clase madre

Cómo vimos, el método `super()` nos perminte acceder a métodos de la clase madre, pero si tenemos más de un antecesor con métodos con el mismo nombre, debemos disponer de una forma de discriminar de cuál de ellos queremos reutilizar un miembro. Para ello reemplazamos el método `super()` por el nombre de la clase de la que queremos reutilizar el método:

```python
class B:
    def x(self):
        print('x: B')


class C:
    def x(self):
        print('x: C')


class D(B, C):
    def x(self):
        C.x(self)   # Se ha de pasar self al método
    pass


d = D()
d.x()    # x: C
```
Además, cuando invocamos de esta forma un método de una de las clases madres hemos pasar como primer parámetro del mismo `self` para que la clase madre disponga del objeto sobre el que aplicar el método.

El funcionamiento es el mismo para cualquier método, en particular también para el constructor:

```python
class SeaAnimal:
    def __init__(self, name):
        print("SeaAnimal INIT")
        self.name = name

    def swim(self):
        return "Swimming..."

class LandAnimal:
    def __init__(self, age):
        print("LandAnimal INIT")
        self.age = age

    def walk(self):
        print("Walking...")

class Penguin(SeaAnimal, LandAnimal):
    def __init__(self, name, age):
        SeaAnimal.__init__(self, name=name)
        LandAnimal.__init__(self, age=age)

penguin = Penguin("Kowalski", 3)
print(penguin.name, penguin.age)
```

### Actividad 4

Crea la clase `CocheHibrido` que hereda de las clases `CocheCombustion` y `CocheElectrico`

Reescribe los métodos de la clase `CocheHibrido` de forma que el resultado de los mismos sea coherente. Aprovecha los métodos de las clases madre siempre que sea posible.

Inserta el resultado:

```python

```


## Recursos

* [Herencia y Composición en Python - Realpython](https://realpython.com/inheritance-composition-python/)
* [Herencia en OOP con Python - Jack Dong - medium.com](https://medium.com/analytics-vidhya/python-oop-inheritance-20f973fe9096)
* [OOP inheritance](https://www.koderhq.com/tutorial/python/oop-inheritance/)
* [https://realpython.com/python-super/ - RealPython](https://realpython.com/python-super/)
* [OOP in Python - RealPython](https://realpython.com/python3-object-oriented-programming/#inherit-from-other-classes-in-python)
* [OOP in Python vs Java - RealPython](https://realpython.com/oop-in-python-vs-java/#inheritance-and-polymorphism)

###### tags: `pro` `ut2` `poo` `oop` `herencia`