from auto import Auto
from vehiculo import Vehiculo

class App():
    def __init__(self):
        self.lista_vehiculos = []

    def mostrar_menu(self):
        print(f"="*15)
        print(f"Calculadora")
        print(f"="*15)
        print("\n1 - Ingresar datos\n2 - Mostrar datos\n0 - Salir\n")

    def ingresar_datos(self):
        auto = Auto("volkwagen","Golf GTI", "300km", 4, "Negro")
        self.lista_vehiculos.append(auto)
        lancha = Vehiculo("lanchita 1", "DFT-007", "400km")
        self.lista_vehiculos.append(lancha)

    def mostrar_datos(self):
        pass
    
    def menu_opciones(self):
        op = -1;
        se_ingreso_datos = False
        while op != 0:
            self.mostrar_menu()
            op = int(input("Ingrese una opcion: "))
            if op == 1:
                self.ingresar_datos()
                se_ingreso_datos = True
            if op == 2 and se_ingreso_datos:
                self.mostrar_datos()
            elif op == 0 and se_ingreso_datos:
                print(f"Programa finalizado")
            else:
                if not se_ingreso_datos:
                    print(f"\nDebe ingresar los datos primero!\n")
                else:
                    print(f"\nOpcion errónea. Trate nuevamente!\n")
            

    def execute(self):
        self.menu_opciones()
    

app = App()
app.execute()
    

    

    

