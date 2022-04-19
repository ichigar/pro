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
