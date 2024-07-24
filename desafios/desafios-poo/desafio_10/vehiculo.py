
class Vehiculo():
    def __init__(self, marca, modelo, velocidad):
        self.__marca = marca;
        self.__modelo = modelo;
        self.__velocidad = velocidad;
    
    # Getters
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    #Setters
    @marca.setter
    def marca(self, nueva_marca):
        self.__marca = nueva_marca

    @modelo.setter
    def modelo(self, nueva_modelo):
        self.__modelo = nueva_modelo
    
    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        self.__velocidad = nueva_velocidad

    # Metodos
    def encender(self):
        print("Encendido")
    
    def frenar(self):
        print(f"Frenando...")
    
    def acelear(self):
        print(f"Acelerando...")
    
    def apagar(self):
        print("Apagado")