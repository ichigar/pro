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


if __name__ == "__main__":   
    v = Vivienda("101", 3, 30)
    print(v)