# PRO-UT2-AE8. Simulacro examen

## Proyecto urbanización de viviendas vacacionales

### Descripción

Se desea crear un programa para gestionar la urbanización de viviendas de alquiler vacacional SOL.

La urbanización está compuesta de una serie de **viviendas** cada una de las cuales se identifica por su **nombre**. Cada vivienda tiene un determinado **número de habitaciones**  y un **precio** de alquiler por día. 

Además, de cada vivienda se sabe en cada momento si está **limpia** o no.

La Urbanización Sol tiene la política de cobrar un mínimo de 3 días de alquiler (aunque se ocupe por menos tiempo)

En todo momento se guarda un listado de las casas de la urbanización y del saldo de ingresos y gastos de la urbanización. Además se guarda un listado con las viviendas ocupadas.

Cada vez que se alquila una vivienda (**checkin**) se incrementa el saldo de la urbanización con el coste del alquiler.

Cada vez que se libera una vivienda (**checkout**) se debe limpiar la vivienda y decrementar el saldo de la urbanización con el coste de la limpieza de la vivienda. El coste de limpiar una vivienda es de 10€ por habitación.

## Implementación

### Modularidad

El programa se dividirá en 4 módulos contenidos en 4 archivos distintos:

* `vivienda.py`
* `alquiler.py`
* `alquiler_vivienda.py`
* `urbanizacion.py`

Además habrá un programa principal `main.py`que será el punto de entrada a la aplicación.

### main.py

En el mismo iremos importando los archivos que necesitemos e iremos creando objetos y comprobando su funcionamiento a medida que creemos clases. 

Cuando hayamos terminado el resto de archivos probaremos la aplicación en su conjunto:

* Crearemos un conjunto de viviendas
* Las añadiremos a la urbanización
* Alquilaremos y liberaremos viviendas
* Comprobaremos el saldo de la urbanización tras las operaciones.
* Mostraremos las viviendas de la urbanización
* Mostraremos la información de los alquileres actuales

### vivienda.py

En el fichero `vivienda.py` se incluye la siguiente clase abstracta:

```python
from abc import ABC, abstractmethod

class ViviendaInterface(ABC):
    coste_limpieza_habitacion = 10
    @abstractmethod
    def __str__():
        pass
    
    @abstractmethod
    def limpiar():
        pass
    
    @abstractmethod
    def get_nombre()
        pass
    
```

Se debe completar el fichero con la definición de la clase `Vivienda` que implementa `ViviendaInterface` teniendo en cuenta que:

Al crear una vivienda se le debe pasar:

* Su **nombre** -> `_nombre`
* El **número de habitaciones** que tiene -> `_num_habitaciones`
* El **precio por día** de la vivienda -> `_precio_dia`

Cuando se crea la vivienda por defecto está **limpia**. La información anterior se guarda en atributo lógico.

El método `__str__()` devolverá la información de la vivienda y si se encuentra o no limpia.

El método `limpiar()` pasa el estado de la vivienda a limpia.

El método `get_nombre()` devuelve el nombre de la propiedad

Resultado:

```python
from abc import ABC, abstractmethod

class ViviendaInterface(ABC):
    _coste_limpieza_habitacion = 10
    @abstractmethod
    def __str__():
        pass
    
    @abstractmethod
    def limpiar():
        pass
    
    @abstractmethod
    def get_nombre():
        pass
    
class Vivienda(ViviendaInterface):

    def __init__(self, nombre, num_habitaciones, precio_dia):
        self._nombre = nombre
        self._num_habitaciones = num_habitaciones
        self._precio_dia = precio_dia
        self._limpia = True

    def __str__(self):
        if self._limpia:
            msg = "Está limpia"
        else:
            msg = "No está limpia"
        return f"Nombre: {self._nombre} - {self._num_habitaciones} habitaciones - {self._precio_dia}€ por día - {msg}"

    def limpiar(self):
        self._limpia = True

    def get_nombre(self):
        return self._nombre

    def calcular_limpieza(self):
        return self._coste_limpieza_habitacion * self._num_habitaciones

# Comprobaciones
if __name__ == "__main__":   
    v = Vivienda("101", 3, 30)
    print(v)
```

### alquiler.py

En el fichero `alquiler.py` se incluye la siguiente clase abstracta:

```python
from abc import ABC, abstractmethod

class AlquilerInterface(ABC):
    _min_dias = 3
    
    @abstractmethod
    def __str__():
        pass
```

Se debe completar el fichero con la definición de la clase `Alquiler` que implementa `AlquilerInterface` teniendo en cuenta que:

Al crear un alquiler se le pasa el **número de días** del alquiler

El método `__str__()` devolverá la información del alquiler

EL contenido completo del archivo sería:

```python
from abc import ABC, abstractmethod

class AlquilerInterface(ABC):
    _min_dias = 3
    
    @abstractmethod
    def __str__():
        pass

class Alquiler(AlquilerInterface):

    def __init__(self, num_dias):
        self._num_dias = num_dias

    def __str__(self):
        
        return f"El alquiler es de {self._num_dias} día(s)"
```


###  alquiler_vivienda.py

En el fichero se importan las clases `Alquiler` y `Vivienda` y se crea la clase `AlquilerVivienda` que hereda de las anteriores. El contenido inicial del mismo será:

```python
from alquiler import *
from vivienda import *

class AlquilerVivienda(Alquiler, Vivienda):
```

Se debe completar el fichero con la definición de la clase teniendo en cuenta que:

Al crear el alquiler de una vivienda:

*  Se le pasa al constructor:
    *   el número de días del alquiler -> `_num_dias`
    *   un objeto con los datos de una vivienda -> `_vivienda` 


El método `calcular_total_alquiler()` devolverá el importe total del alquiler

El metodo `calcular_limpieza()` devolverá el coste de limpiar la habitación. 

El método `__str__()` mostrará las características de la vivienda, el coste de limpieza de la misma y por cuantos días está ocupada y el total del mismo.

comprobaciones:

```python
v = Vivienda("101", 3, 30)
a = AlquilerVivienda(5, v) # Se alquila la vivienda por 5 dias

print(a)
print(a.calcular_total())
print(a.calcular_limpieza())
```
EL contenido completo del archivo sería:

```python
from alquiler import *
from vivienda import *

class AlquilerVivienda(Alquiler, Vivienda):
    def __init__(self, num_dias, vivienda):
        Alquiler.__init__(self, num_dias)
        self._vivienda = vivienda

    def __str__(self):
        msg += super().__str__() + "\n"
        msg += self._vivienda.__str__()
        return msg

    def calcular_total_alquiler(self):
        n_dias = self._num_dias
        if n_dias < self._min_dias:
            n_dias = self._min_dias
        return n_dias * self._vivienda._precio_dia

    
# Comprobaciones
if __name__ == "__main__":
    v = Vivienda("101", 3, 30)
    a = AlquilerVivienda(5, v) # Se alquila la vivienda por 5 dias

    print(a)
    print(a.calcular_total_alquiler())

```


### urbanizacion.py

Se importa la clase `AlquilerVivienda` y se define en el la clase `UrbanizacioSolInterface`. El contenido inicial del fichero será:

```python
from alquiler_vivienda import *
from abc import ABC, abstractmethod


class UrbanizacionSolInterface(ABC):
    
    def __init__(self):
        self._viviendas = []
        self._alquileres = []
        self._saldo = 0
        
    def _existe_vivienda(self, nombre_vivienda)
        for vivienda in self._viviendas:
            if vivienda.get_nombre() == nombre_vivienda:
                return True
        return False
    
    def _esta_alquilada(self, nombre_vivienda)
        for alquiler in self._alquileres:
            if alquiler._vivienda.get_nombre() == nombre_vivienda:
                return True
        return False
    
    def _obtener_vivienda(self, nombre_vivienda):
        for vivienda in self._viviendas:
            if vivienda.get_nombre() == nombre_vivienda:
                return vivienda
        return False
    
    def _get_index_alquiler(self, nombre_vivienda):
        l = len(self._alquileres)
        for i in range(l):
            alquiler = self._alquileres[i]
            if alquiler._vivienda.get_nombre() == nombre_vivienda:
                return i
        return -1
    
    @abstractmethod   
    def nueva_vivienda(self):
        pass
    
    @abstractmethod
    def viviendas_libres(self, num_personas):
        pass   
    
    @abstractmethod
    def checkin(self, nombre_vivienda, num_dias, num_personas):
        pass
    
    @abstractmethod
    def limpiar_vivienda(self, nombre_vivienda):
        pass
    
    @abstractmethod
    def _quitar_alquiler(self, nombre_vivienda):
    
    @abstractmethod
    def checkout(self, nombre_vivienda):
        pass
       
    @abstractmethod
    def mostrar_vivienda(self, nombre_vivienda):
        pass
    
    @abstractmethod
    def mostrar_saldo(self)
     
```

Se debe completar el fichero creando la clase `UrbanizacionSol` que implementa `UrbanizacionSolInterface`teniendo en cuenta que:

Al crear un objeto de esta clase:
* se crea una lista vacia `_viviendas` que se utilizará para almacenar objetos de la clase `Vivienda`
* Se crea una lista vacia `_alquileres` que guardará los datos de los alquilers como objetos de la clase `AlquilerVivienda`
* Se inicializa el `_saldo` de la urbanización a 0

Al método `_existe_vivienda()` se le pasa el nombre de una vivienda y si existe en el listado devuelve `True` y en caso contrario devuelve `False`

Al método `_esta_alquilada()` se le pasa el nombre de una vivienda y si existe en el listado de alquileres devuelve `True` y en caso contrario devuelve `False`

Al método `_obtener_vivienda()` se le pasa el nombre de una vivienda y si existe devuelve el objeto con la vivienda. En caso contrario devuelve `False`

Al método `_get_index_alquiler` se le pasa el nombre de una vivienda y devuelve la posición que ocupada el objeto en la lista de alquileres. Si no está devuelve **-1**

Al método `nueva_vivienda()` se lee de teclado los datos de una vivienda, se crea un objeto de la clase `Vivienda` y lo añade a la **lista de viviendas** de la urbanización. Antes de añadir la vivienda se comprueba que no exista otra con el mismo nombre (`_existe:vivienda()`). De ser así se muestra un mensaje de error y no se crea la vivienda.

El método `viviendas_libres()` muesta por pantalla un listado con la descripción de las viviendas que están libres (usa `__str__()` para objetos de la clase vivienda)

El método `limpiar_vivienda()` se le pasa el nombre de una vivienda y cambia el estado de la misma a limpio y actualiza el saldo de la urbanización quitando el coste de limpiar la vivienda.

El método `checkin()` se le pasa el nombre de una vivienda y el número de dias y
* Comprueba si la vivienda existe y no está alquilada. En caso contrario muestra un mensaje de error.
* Si existe y no está alquilada se crea un objeto de la clase `AlquilerVivienda` y se añade a la lista de alquileres de la Urbanizacion
* Se actualiza el saldo de la urbanización incrementándolo con el coste del alquiler


Al método `_quitar_alquiler()` se le pasa el nombre de una vivienda. Usando `_get_index_alquiler()` la posición que ocupa en la lista de alquileres el objeto y si lo encuentra lo elimina de la lista.

El método `checkout()` comprueba que la vivienda está ocupada (`_esta_aqluilada()`). Y si es así:

* Quita el objeto de la clase `AlquilerVivienda` de la lista de alquileres de la urbanizacion usando `_quitar_alquiler()`
* llama a `limpiar_vivienda()` para cambiar el estado de la vivienda y el saldo de la urbanización

El método `mostrar_vivienda` se le pasa el nombre de una vivienda y si está en la lista se usa el método `__str__()` del objeto de tipo vivienda para mostrar su descripción. Si no existe se muestra un mensaje indicándolo.

El método `mostrar_saldo()` muestra por pantalla el saldo actual de la urbanización.

EL contenido completo del archivo sería:

```python

from alquiler_vivienda import *
from abc import ABC, abstractmethod


class UrbanizacionSolInterface(ABC):
    
    def __init__(self):
        self._viviendas = []
        self._alquileres = []
        self._saldo = 0
        
    def _existe_vivienda(self, nombre_vivienda):
        for vivienda in self._viviendas:
            if vivienda.get_nombre() == nombre_vivienda:
                return True
        return False
    
    def _esta_alquilada(self, nombre_vivienda):
        for alquiler in self._alquileres:
            if alquiler._vivienda.get_nombre() == nombre_vivienda:
                return True
        return False
    
    def _obtener_vivienda(self, nombre_vivienda):
        for vivienda in self._viviendas:
            if vivienda.get_nombre() == nombre_vivienda:
                return vivienda
        return False
    
    def _get_index_alquiler(self, nombre_vivienda):
        l = len(self._alquileres)
        for i in range(l):
            alquiler = self._alquileres[i]
            if alquiler._vivienda.get_nombre() == nombre_vivienda:
                return i
        return -1
    
    @abstractmethod   
    def nueva_vivienda(self):
        pass
    
    @abstractmethod
    def viviendas_libres(self):
        pass   
    
    @abstractmethod
    def checkin(self, nombre_vivienda, num_dias):
        pass
    
    @abstractmethod
    def limpiar_vivienda(self, nombre_vivienda):
        pass
    
    @abstractmethod
    def _quitar_alquiler(self, nombre_vivienda):
        pass
    @abstractmethod
    def checkout(self, nombre_vivienda):
        pass
       
    @abstractmethod
    def mostrar_vivienda(self, nombre_vivienda):
        pass
    
    @abstractmethod
    def mostrar_saldo(self):
        pass

class UrbanizacionSol(UrbanizacionSolInterface):   
    
    def nueva_vivienda(self):
        
        nombre = input("Introduce nombre vivienda: ")
        num_habitaciones = int(input("Introduce número de habitaciones: "))
        precio_dia = int(input("Introduce precio diario: "))
        if not self._existe_vivienda(nombre):
            v = Vivienda(nombre, num_habitaciones, precio_dia)
            self._viviendas.append(v)
            return True
        else:
            return False


    def viviendas_libres(self):
        for vivienda in self._viviendas:
            nombre_vivienda = vivienda.get_nombre()
            if not self._esta_alquilada(nombre_vivienda):
                print(vivienda)
    

    def checkin(self, nombre_vivienda, num_dias):
        if self._existe_vivienda(nombre_vivienda) and not self._esta_alquilada(nombre_vivienda):
            v = self._obtener_vivienda(nombre_vivienda)
            a = AlquilerVivienda(num_dias, v)
            self._alquileres.append(a)
            total_alquiler = a.calcular_total_alquiler()
            self._saldo += total_alquiler
        else:
            print("No se pudo realizar el checkin")
    

    def limpiar_vivienda(self, nombre_vivienda):
        if self._existe_vivienda(nombre_vivienda):
            v = self._obtener_vivienda(nombre_vivienda)
            v.limpiar()
            total_limpieza = v.calcular_limpieza()
            self._saldo -= total_limpieza
        else:
            return False
    

    def _quitar_alquiler(self, nombre_vivienda):
        if self._esta_alquilada(nombre_vivienda):
            i = self._get_index_alquiler(nombre_vivienda)
            del self._alquileres[i]
        else:
            return False

    def checkout(self, nombre_vivienda):
        if self._esta_alquilada(nombre_vivienda):
            self._quitar_alquiler(nombre_vivienda)
            self.limpiar_vivienda(nombre_vivienda)
        else:
            print(f"La vivienda {nombre_vivienda} no está alquilada")
       

    def mostrar_vivienda(self, nombre_vivienda):
        
        v = self._obtener_vivienda(nombre_vivienda)
        if not v:
            print("La vivienda no existe")
        else:
            print(v)
    

    def mostrar_saldo(self):
        print(f"El saldo acutual es de {self._saldo} €")

if __name__ == "__main__":
    u = UrbanizacionSol()
    u.nueva_vivienda()
    u.mostrar_vivienda("101")
```



### main.py final

Una vez terminado el supuesto se puede comprobar la aplicación añadiendo el siguiente código al archivo `main.py`

```python
from os import system
from urbanizacion import *

u_sol = UrbanizacionSol()

opcion = 1

while opcion != 0:
    system("clear")
    print("1. Añadir propiedad")
    print("2. Checkin")
    print("3. Checkout")
    print("4. Mostrar viviendas libres")
    print("5. Mostrar vivienda")
    print("6. Mostrar saldo")
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        u_sol.nueva_vivienda()
    
    elif opcion == 2:
        nombre_vivienda = input("nombre de la vivienda: ")
        num_dias = int(input("Número de días: "))
        u_sol.checkin(nombre_vivienda, num_dias)
    
    elif opcion == 3:
        nombre_vivienda = input("nombre de la vivienda: ")
        u_sol.checkout(nombre_vivienda)
    
    elif opcion == 4:
        u_sol.viviendas_libres()
    
    elif opcion == 5:
        nombre_vivienda = input("nombre de la vivienda: ")
        u_sol.mostrar_vivienda(nombre_vivienda)
    
    elif opcion == 6:
        u_sol.mostrar_saldo()
    
    else:
        print("Opción incorrecta")
    
    input("Pulsa Enter para continuar ")

```

###### tags: `pro` `ut2` `oop` `prueba` `práctica` `simulacro`from alquiler_vivienda import *