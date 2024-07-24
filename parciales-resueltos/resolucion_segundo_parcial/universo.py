from simulacion import Simulacion
class Universo():
    def __init__(self):
        self.__simulacion = None
        self.__etapa = 0
    
    """getters"""
    @property
    def simulacion(self):
        return self.__simulacion
    
    @property
    def etapa(self):
        return self.__etapa

    """setters"""
    @simulacion.setter
    def simulacion(self, nueva_simulacion):
        self.__simulacion = nueva_simulacion
    
    @etapa.setter
    def etapa(self, nueva_etapa):
        self.__etapa = nueva_etapa

    """ingresa la cantidad de filas y columas de la matriz del universo"""
    def ingresar_datos(self):
        cantidad_filas = int(input("Ingrese la cantidad de filas: "))
        cantidad_columnas = int(input("Ingrese la cantidad de filas: "))
        self.__simulacion = Simulacion(cantidad_filas, cantidad_columnas)

    """muestra las etapas de la simulaciones del universo"""
    def mostrar_etapas(self):
        self.etapa = 0
        while self.__simulacion.buscar_numeros_aleatorios_impares():
            self.__simulacion.reemplazar_impar_por_aleatorio()
            self.etapa += 1
            print(f"\nEtapa de simulacion numero {self.etapa}:")
            if self.__simulacion.buscar_numeros_aleatorios_impares():
                print(f"",end="")
                self.__simulacion.mostrar_simulacion()  
            else:
                print(f"El Universo en Estado de Equilibrio...")
                print(f"",end="")
                self.simulacion.mostrar_simulacion()
            print(f" ")
        """Si no hubo etapas de simulacion, incrementa y muestra el estado en equilibrio"""
        if self.etapa == 0:
            self.etapa = self.etapa + 1   
            print(f"\nEtapa de simulacion numero {self.etapa}:")
            print(f"El Universo en Estado de Equilibrio...")
            print(f"",end="")
            self.__simulacion.mostrar_simulacion()
            print(f"")
    
    """muestra el universo y sus simulaciones"""
    def mostrar_universo(self):
        print(f"-------------------------------\n Un Universo de números pares\n-------------------------------")
        self.ingresar_datos()
        print(f" ")
        self.__simulacion.generar_simulacion();
        self.__simulacion.mostrar_simulacion();
        print(" ")
        self.mostrar_etapas()