import random
class Simulacion():
    def __init__(self, cantidad_filas, cantidad_columnas):
        self.__simulacion = []
        self.__cantidad_filas = cantidad_filas
        self.__cantidad_columnas = cantidad_columnas
    
    """Getter"""
    @property
    def simulacion(self):
        return self.__simulacion
    
    @property
    def cantidad_filas(self):
        return self.__cantidad_filas
    
    @property
    def cantidad_columnas(self):
        return self.__cantidad_columnas
    
    """Setter"""
    @simulacion.setter
    def simulacion(self, nueva_simulacion):
        self.__simulacion = nueva_simulacion
    
    @cantidad_filas.setter
    def simulacion(self, nueva_cantidad_filas):
        self.__cantidad_filas = nueva_cantidad_filas

    @cantidad_columnas.setter
    def cantidad_columnas(self, nueva_cantidad_columnas):
        self.__cantidad_columnas = nueva_cantidad_columnas

    """Genera un numero aleatorio entre 0 y 99"""
    def generar_aleatorio_entre_0_y_99(self):
        numero_aleatorio = random.randint(0,99)
        return numero_aleatorio

    """Generar una simulacion"""
    def generar_simulacion(self):
        for i in range(self.__cantidad_filas):
            fila = []
            for j in range(self.__cantidad_columnas):
                fila.append(self.generar_aleatorio_entre_0_y_99())
            self.__simulacion.append(fila)

    """Muestra una etapa de simulacion"""
    def mostrar_simulacion(self):
        for i in range(0, self.__cantidad_filas):
            for j in range(0, self.__cantidad_columnas):
                print(f"{self.__simulacion[i][j]:>3}",end="")
            print(f" ")
        return None

    """Determina si un numero pasado como parámetro es par"""
    def numero_par(self, numero):
        es_par = False
        if numero%2==0:
            es_par = True
        return es_par

    """Busca y reemplaza un numero impar por un numero aleatorio"""
    def reemplazar_impar_por_aleatorio(self):
        for i in range(0, self.__cantidad_filas):
            for j in range(0, self.__cantidad_columnas):
                if not self.numero_par(self.__simulacion[i][j]):
                    self.__simulacion[i][j] = self.generar_aleatorio_entre_0_y_99()
        
    """Determina si el universo contiene un numero impar. Si tiene, retorna True; caso contrario, retorna False"""
    def buscar_numeros_aleatorios_impares(self):
        hay_numero_impar = False
        for i in range(0, self.__cantidad_filas):
            for j in range(0, self.__cantidad_columnas):
                if not self.numero_par(self.__simulacion[i][j]):
                    hay_numero_impar = True
        return hay_numero_impar
        
    