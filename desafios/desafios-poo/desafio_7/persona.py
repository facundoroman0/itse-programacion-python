class Persona():

    """Defino atributos por defecto"""
    def __init__(self):
        self.__nombre = " "
        self.__edad = 0
        self.__dni = 0

    """Getters"""
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def dni(self):
        return self.__dni
    
    """Setters"""
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni
    
    """Metodos definidos"""
    def es_mayor_edad(self):
        es_mayor_de_edad = False
        if self.__edad > 18:
            es_mayor_de_edad = True
        
        return es_mayor_de_edad