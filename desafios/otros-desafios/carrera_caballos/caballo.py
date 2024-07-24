import random
class Caballo():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__posicion = 0
        
    """getters"""
    @property
    def posicion(self):
        return self.__posicion
    
    @property
    def nombre(self):
        return self.__nombre

    """setters"""
    @posicion.setter
    def posicion(self, nueva_posicion):
        self.__posicion = nueva_posicion

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    """muestra el recorrido de caballo segun la cantidad de espacios"""
    def mostrar_caballo(self, cantidad_espacios):
        print(cantidad_espacios*" ","*")
    
    """retorna la distancia en 0, 1, o 2 pasos"""
    def correr(self):
        self.posicion += random.randint(0,2)
        
    

        