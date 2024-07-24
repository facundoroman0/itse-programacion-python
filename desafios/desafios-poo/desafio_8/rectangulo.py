"""
Desafío 8
  Desarrollar una clase Rectangulo que contenga una base y una altura y un método que retorne el área del 
rectángulo.
"""

class Rectangulo():
    def __init__(self, base, altura):
        self.__base = base
        self.__altura  = altura
    
    """Getters"""    
    @property
    def base(self):
        return self.__base
    
    @property
    def altura(self):
        return self.__altura

    """Setters"""
    @base.setter
    def base(self, nueva_base):
        self.__base = nueva_base
    
    @altura.setter
    def base(self, nueva_altura):
        self.__altura = nueva_altura

    """Retorna el area del rectangulo"""
    def area_rectangulo(self):
        return self.__base * self.__altura

    