# Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar sus atributos
# , consultar la magnitud del tamaño del lado mayor y consultar el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo:
    def __init__(self, tipo, lado_a, lado_b, lado_c):
        self.tipo = tipo;
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
    
    @property
    def tipo(self):
        return self.tipo  
    
    def tipo(self, nuevo_tipo):
        self.tip = nuevo_tipo

    @property
    def lado_a(self):
        return self.lado_a  
    
    def lado_a(self, nuevo_lado_a):
        self.lado_a = nuevo_lado_a

    @property
    def lado_b(self):
        return self.lado_b  
    
    def lado_b(self, nuevo_lado_b):
        self.lado_b = nuevo_lado_b

    @property
    def lado_c(self):
        return self.lado_c  
    
    def lado_c(self, nuevo_lado_c):
        self.lado_c = nuevo_lado_c

    def consultar_tipo(self):
        return self.tipo

    def magnitud_lado_mayor(self):
        lado_mayor = self.lado_a
        if self.lado_a >= self.lado_b and self.lado_a >= self.lado_c:
            lado_mayor = self.lado_a
        else:
            if self.lado_b >= self.lado_c:
                lado_mayor = self.lado_b
            else:
                lado_mayor = self.lado_c
        return lado_mayor

def cargar_datos_triangulo():
    triangulo = Triangulo(" ", 0, 0, 0)
    triangulo.tipo = input("Tipo: ")

    lado = 0

    if triangulo.tipo == "equilatero":
        lado = float(input("Valor de sus lados: "))
        triangulo.lado_a = lado
        triangulo.lado_b = lado
        triangulo.lado_c = lado
    elif triangulo.tipo == "isoseles":
        lado = float(input("Lados iguales: "))
        triangulo.lado_a = lado
        triangulo.lado_b = lado
        lado = float(input("Lado desigual: "))
        triangulo.lado_c = lado
    else:
        lado = float(input("Primer lado: "))
        triangulo.lado_a = lado
        lado = float(input("Segundo lado: "))
        triangulo.lado_b = lado
        lado = float(input("Tercer lado: "))
        triangulo.lado_c = lado

    return triangulo

def consultar_magitud(triangulo):
    print(f"La magnitud del triangulo es {triangulo.magnitud_lado_mayor()}")
    return None

def consultar_tipo(triangulo):
    print(f"Es un triángulo {triangulo.consultar_tipo()}")

def menu_opciones():
    triangulo = Triangulo(" ", 0, 0, 0)
    op = -1
    while op != 0:
        print(f"\nMenu de Opciones: \n1-Cargar datos de triangulo\n2-Consultar magnitud del lado mayor\n3-Consultar tipo\n0-Salir\nElija una opcion: ",end="")
        op = int(input())
        if op == 1:
            triangulo = cargar_datos_triangulo()
        elif op == 2:
            consultar_magitud(triangulo)
        elif op == 3:
            consultar_tipo(triangulo)
        else:
            if op != 0:
                print(f"Opcion erronea. Trate nuevamente!")

menu_opciones()
