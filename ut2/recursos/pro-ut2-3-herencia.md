# PRO-UT2-A3. Herencia Simple
## Herencia en OOP

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

### Supuesto

Definir la clase `Vehiculo` que tiene:

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
    * `descripcion()` devuelve texto con la descripción. Por ejemplo: "Coche con motor de combustión, matrícula 1234ABC, de color rojo y 4 ruedas"

Crea la clase `CocheElectrico` que hereda de la clase `Vehículo` y tiene las propiedad añadida:

* métodos:
    * `descripcion()` devuelve texto con la descripción. Por ejemplo: "Coche con motor eléctrico, matrícula 4321ABC, de color rojo y 4 ruedas"

Crea la clase `Moto` que hereda de la clase `Vehículo` y tiene las propiedad añadida:

* métodos:
    * `descripcion()` devuelve texto con la descripción. Por ejemplo: "Moto con matrícula 1234GRD, de color rojo y 2 ruedas"

Crea un objeto de ejemplo de cada clase y prueba todos los métodos disponibles de cada uno.

Inserta resultado aquí:

```python
class Vehiculo:
    def __init__(self, matricula, color, num_ruedas):
        self._matricula = matricula
        self._color = color
        self._num_ruedas = num_ruedas

    def get_matricula(self):
        return self._matricula
    
    def __str__(self):
        return f"Vehículo con matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

class CocheCombustion(Vehiculo):
    def descripcion(self):
        return f"Coche con motor de combustión, matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

class CocheElectrico(Vehiculo):
    def descripcion(self):
        return f"Coche con motor eléctrico, matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

class Moto(Vehiculo):
    def descripcion(self):
        return f"Moto, matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

v = Vehiculo("1234ABC", "verde", 4)
print(v)

c = CocheCombustion("TF7984G", "beige", 4)
print(c.descripcion())
print(c)

ce = CocheElectrico("8765JVZ", "blanco", 4)
print(ce.descripcion())
print(ce)

m = Moto("8763GRD", "amarilla", 2)
print(m.descripcion())
print(m)
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

### Supuesto 2

Si modificamos las clases definidas en el supuesto anterior de forma que:

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

El resultado es:

```python
class Vehiculo:
    def __init__(self, matricula, color, num_ruedas):
        self._matricula = matricula
        self._color = color
        self._num_ruedas = num_ruedas

    def get_matricula(self):
        return self._matricula
    
    def __str__(self):
        return f"Vehículo con matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

class CocheCombustion(Vehiculo):
    def __init__(self, matricula, color, num_ruedas, cilindrada):
        self._matricula = matricula
        self._color = color
        self._num_ruedas = num_ruedas
        self._cilindrada = cilindrada
    
    def get_cilindrada(self):
        return self._cilindrada

    def descripcion(self):
        return f"Coche con motor de combustión de {self.get_cilindrada()} cc, matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

class CocheElectrico(Vehiculo):
    def __init__(self, matricula, color, num_ruedas, potencia):
        self._matricula = matricula
        self._color = color
        self._num_ruedas = num_ruedas
        self._potencia = potencia

    def get_potencia(self):
        return self._potencia

    def descripcion(self):
        return f"Coche con motor eléctrico de {self.get_potencia()}CV, matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

class Moto(Vehiculo):
    def descripcion(self):
        return f"Moto, matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

v = Vehiculo("1234ABC", "verde", 4)
print(v)

c = CocheCombustion("TF7984G", "beige", 4, 1100)
print(c.descripcion())
print(c)

ce = CocheElectrico("8765JVZ", "blanco", 4, 180)
print(ce.descripcion())
print(ce)

m = Moto("8763GRD", "amarilla", 2)
print(m.descripcion())
print(m)
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

### Supuesto 3

Vamos a utilizar  `super()` en las clases `CocheCombustion`, `CocheElectrico` y `Moto` en todos los casos posibles.

Inserta resultado:

```python
class Vehiculo:
    def __init__(self, matricula, color, num_ruedas):
        self._matricula = matricula
        self._color = color
        self._num_ruedas = num_ruedas
        self.revisiones = []

    def get_matricula(self):
        return self._matricula
    
    def __str__(self):
        return f"Vehículo con matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

class CocheCombustion(Vehiculo):
    def __init__(self, matricula, color, num_ruedas, cilindrada):
        super().__init__(matricula, color, num_ruedas)
        self._cilindrada = cilindrada
    
    def get_cilindrada(self):
        return self._cilindrada

    def descripcion(self):
        return f"Coche con motor de combustión de {self.get_cilindrada()} cc, matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

class CocheElectrico(Vehiculo):
    def __init__(self, matricula, color, num_ruedas, potencia):
        super().__init__(matricula, color, num_ruedas)
        self._potencia = potencia

    def get_potencia(self):
        return self._potencia

    def descripcion(self):
        return f"Coche con motor eléctrico de {self.get_potencia()}CV, matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

class Moto(Vehiculo):
    def descripcion(self):
        return f"Moto, matrícula {self.get_matricula()}, de color {self._color} y {self._num_ruedas} ruedas."

v = Vehiculo("1234ABC", "verde", 4)
print(v)

c = CocheCombustion("TF7984G", "beige", 4, 1100)
print(c.descripcion())
print(c)

ce = CocheElectrico("8765JVZ", "blanco", 4, 180)
print(ce.descripcion())
print(ce)

m = Moto("8763GRD", "amarilla", 2)
print(m.descripcion())
print(m)
```

## Supuesto 4

Validación de campos de entrada

La clase `Validate` define atributos y métodos comunes para validar el valor de campos de entrada de formularios web. Su definición es la siguiente:

```python
class Validate:
    special_chars = "@#$%&/()=*{}[]-+"
    numbers = "0123456789"
    
    def __init__(self, input):
        self._input = input
    
    def _validate_length(self, min_length):
        if len(self._input) < min_length:
            return False
        else:
            return True
    
    def _is_numeric(self):
        """
        Pasamos una cadena de texto y devuelve True si todos los caracteres de la misma son números y False en caso contrario
        """
        pass  # Eliminar línea y completar código
    
    def _has_upper(self):
        """
        Pasamos una cadena de texto y devuelve True si contiene, al menos, un carácter en mayúscula.  Devuelve False en caso contrario.
        """
        pass  # Eliminar línea y completar código
    
    def _has_special_char(self):
        """
        Pasamos una cadena de texto y devuelve True si contiene, al menos un carcter especial. Devuelve False en caso contrario.
        """
        pass  # Eliminar línea y completar código
    
        
```
Completar la definición de las siguientes clases hijas para validar campos específicos:

```python
class ValidateEmail(Validate):
    min_length = 6
    def _validate_arroba(self):
        pass # completar código
    
    def _validate_domain(self):
        pass # completar código
    
    def validate(self):
        vl = self._validate_length(self.min_length)
        va = self._validate_arroba()
        vd = self._validate_domain()
        if not vl:
            return [False, "Email incorrecto"]
        if not va:
            return [False, "Email incorrecto"]
        elif not vd:
            return [False, "Email incorrecto"]
        else:
            return [True, ""]
        
class ValidatePasswd(Validate):
    min_length = 10
    pass # completar código

class ValidateCP(Validate):
    """
    Un código postal es válido si su longitud es 5 y todos los caracteres del mismo son números
    """
    length = 5
    pass # completar código

class ValidateDni(Validate):
    """
    Debe comprobar que tiene 8 números y a continuación una letra
    La letra debe ser válida para los números del DNI (busca en Internet)
    """
    length = 8
    pass # completar código

# Ejecuta a continuación comprobaciones de todos los casos posibles.
# Ejemplos
e1 = ValidateEmail("a@a")
es_valido = e1.validate()[0]
if not es_valido:
    print(e1.validate()[1]) # Devuelve 'Email incorrecto'
else:
    print("Email correcto")

e2 = ValidateEmail("a@gmail@hotmail.com")
es_valido = e2.validate()[0]
if not es_valido:
    print(e2.validate()[1]) # Devuelve 'Email incorrecto'
else:
    print("Email correcto")
    
e3 = ValidateEmail("a@example.a")
es_valido = e3.validate()[0]
if not es_valido:
    print(e3.validate()[1]) # Devuelve 'Email incorrecto'
else:
    print("Email correcto")
    
    
e4 = ValidateEmail("user@example.es")
es_valido = e4.validate()[0]
if not es_valido:
    print(e4.validate()[1]) 
else:
    print("Email correcto") 
    

p1 = ValidatePasswd('abcD*')
es_valido = p1.validate()[0]
if not es_valido:
	print(p1.validate()[1]) # Devuelve: 'Contraseña incorrecta'
else:
    print("Contraseña correcta")
    
p2 = ValidatePasswd('abcDvfghter')
es_valido = p2.validate()[0]
if not es_valido:
	print(p2.validate()[1]) # Devuelve: 'Contraseña incorrecta'
else:
    print("Contraseña correcta")
    
p3 = ValidatePasswd('abc*dftynhd')
es_valido = p3.validate()[0]
if not es_valido:
	print(p3.validate()[1]) # Devuelve: 'Contraseña incorrecta'
else:
    print("Contraseña correcta")
    
p4 = ValidatePasswd('abcD*2ytsffsq')
es_valido = p4.validate()[0]
if not es_valido:
	print(p4.validate()[1]) # Devuelve: ''
else:
    print("Contraseña correcta")
    
cp1 = ValidateCP('1234')
es_valido = cp1.validate()[0]
if not es_valido:
	print(cp1.validate()[1]) # Devuelve: 'CP incorrecto'
else:
    print("Código postal correcto")
    
cp2 = ValidateCP('12a34')
es_valido = cp2.validate()[0]
if not es_valido:
	print(cp2.validate()[1]) # Devuelve: 'CP incorrecto'
else:
    print("Código postal correcto")
    
cp3 = ValidateCP('35001')
es_valido = cp3.validate()[0]
if not es_valido:
	print(cp3.validate()[1]) # Devuelve: ''
else:
    print("Código postal correcto")
    
dni1 = ValidateDni('6232313M')
es_valido = dni1.validate()[0]
if not es_valido:
	print(dni1.validate()[1]) # Devuelve 'DNI incorrecto'
else:
    print("DNI correcto")
    
dni2 = ValidateDni('60232313A')
es_valido = dni2.validate()[0]
if not es_valido:
	print(dni2.validate()[1]) # Devuelve 'DNI incorrecto'
else:
    print("DNI correcto")
    
dni3 = ValidateDni('60232313M')
es_valido = dni3.validate()[0]
if not es_valido:
	print(dni3.validate()[1]) # Devuelve ''
else:
    print("DNI correcto")
```

## Recursos

* [Herencia y Composición en Python - Realpython](https://realpython.com/inheritance-composition-python/)
* [Herencia en OOP con Python - Jack Dong - medium.com](https://medium.com/analytics-vidhya/python-oop-inheritance-20f973fe9096)
* [OOP inheritance](https://www.koderhq.com/tutorial/python/oop-inheritance/)
* [https://realpython.com/python-super/ - RealPython](https://realpython.com/python-super/)
* [OOP in Python - RealPython](https://realpython.com/python3-object-oriented-programming/#inherit-from-other-classes-in-python)
* [OOP in Python vs Java - RealPython](https://realpython.com/oop-in-python-vs-java/#inheritance-and-polymorphism)

###### tags: `pro` `ut2` `poo` `oop` `herencia`