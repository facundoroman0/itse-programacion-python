import os # Modulo usado para usar la funcion que limpia la pantalla
import time # Modulo usado para usar la funcion que retrasa la impresion por consola
class Carrera():
    def __init__(self, caballo_1, caballo_2):
        self.__caballo_1 = caballo_1
        self.__caballo_2 = caballo_2 
        self.__distancia_meta = 100
    
    """getters"""
    @property
    def caballo_1(self):
        return self.__caballo_1
    
    @property
    def caballo_2(self):
        return self.__caballo_2
    
    @property
    def distancia_meta(self):
        return self.__distancia_meta
    
    """setters"""
    @caballo_1.setter
    def caballo_1(self, nuevo_caballo_1):
        self.caballo_1 = nuevo_caballo_1

    @caballo_2.setter
    def caballo_2(self, nuevo_caballo_2):
        self.caballo_2 = nuevo_caballo_2
    
    """inicia la carrera de caballos y la muestra"""
    def iniciar(self):
        while self.caballo_1.posicion < self.distancia_meta or self.caballo_2.posicion < self.distancia_meta:
            # os.system("clear") # Limpia la terminal - Si tienes Linux, usá este
            os.system("cls") # Limpia la terminal - Si tienes Windows, usá este
            print("-"*40, "CARRERA DE CABALLOS", "-"*40)
            print("-"*100)
            self.caballo_1.correr()
            self.caballo_1.mostrar_caballo(self.caballo_1.posicion)
            self.caballo_2.correr()
            self.caballo_2.mostrar_caballo(self.caballo_2.posicion)
            print("-"*100)
            time.sleep(0.1) # Tiempo de espera para mostrar los caballos y la pista
            if self.caballo_1.posicion > self.distancia_meta or self.caballo_2.posicion > self.distancia_meta:
                break # corto el bucle a cualquier caballo que rebase la meta
            
        if self.caballo_1.posicion == self.caballo_2.posicion:
            print(f"Hubo empate")
        elif self.caballo_1.posicion > self.caballo_2.posicion:
            print(f"{self.caballo_1.nombre} ganó la carrera")
        else:
            print(f"{self.caballo_2.nombre} ganó la carrera")
    
        