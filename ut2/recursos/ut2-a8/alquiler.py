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