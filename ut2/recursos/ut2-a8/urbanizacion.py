
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