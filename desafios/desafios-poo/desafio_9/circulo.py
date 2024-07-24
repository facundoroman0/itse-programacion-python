"""
Desafío 9
Desarrollar una clase Circulo que contenga un radio, con un método que retorne el área y otro que retorne el perímetro del Circulo

"""
import math
class Circulo():
    def __init__(self, radio):
        self.__radio = radio
    
    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, nuevo_radio):
        self.__radio = nuevo_radio

    def area_circulo(self):
        # pi por radio al cuadrado
        return math.pi * math.pow(self.radio, 2)
    
    def perimetro_circulo(self):
        return 2 * math.pi * self.radio
    

    
    
    
