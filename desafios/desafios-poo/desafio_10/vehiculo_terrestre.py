from vehiculo import Vehiculo

class VehiculoTerrestre(Vehiculo):
    def __init__(self, marca, modelo, velocidad, cantidad_ruedas):
        super().__init__(marca, modelo, velocidad)
        self.__cantidad_ruedas = cantidad_ruedas

    @property
    def cantidad_ruedas(self):
        return self.__cantidad_ruedas
    
    @cantidad_ruedas.setter
    def cantidad_ruedas(self, nueva_cantidad_ruedas):
        self.__cantidad_ruedas = nueva_cantidad_ruedas

    
    
    