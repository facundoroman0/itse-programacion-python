from vehiculo_terrestre import VehiculoTerrestre

class Auto(VehiculoTerrestre):
    def __init__(self, marca, modelo, velocidad, cantidad_ruedas, color):
        super().__init__(marca, modelo, velocidad, cantidad_ruedas)
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, nuevo_color):
        self.__color = nuevo_color

    
