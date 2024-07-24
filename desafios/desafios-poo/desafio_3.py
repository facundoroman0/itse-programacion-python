"""
Desarrollar un programa el cual el Usuario ingrese dos valores enteros
por teclado. Utilizar el metodo __init__. Incluir el calculo de la suma,
resta, multiplcacion y division. Utiiza un metodo para cada una de las
operaciones. Nombrar a la clase Calculadora.
"""


class Calculadora:
    # Método Contstructor
    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    # Getters, Setters y Deleters
    @property
    def numero_1(self):
        return self.numero_1
            
    def numero_1(self, nuevo_numero_1):
        self.numero_1 = nuevo_numero_1

    @property
    def numero_2(self):
        return self.numero_2
            
    def numero_2(self, nuevo_numero_2):
        self.numero_2 = nuevo_numero_2  

    # Metodos definidos
    def sumar(self):
        return self.numero_1 + self.numero_2;

    def restar(self):
        return self.numero_1 - self.numero_2;

    def multiplicar(self):
        return self.numero_1 * self.numero_2;

    def dividir(self):
        return self.numero_1 / self.numero_2

class App:
    def __init__(self):
        pass

    def ingresar_datos(self):
        print(f"-"*15)
        numero_1 = int(input("Ingrese un numero: "))
        numero_2 = int(input("Ingrese otro numero: "))
        print(f"-"*15)
        return numero_1, numero_2

    def mostrar_menu(self):
        print(f"="*15)
        print(f"Calculadora")
        print(f"="*15)
        print("\n1 - Ingresar datos\n2 - Sumar\n3 - Restar\n4 - Multiplicar\n5 - Dividir\n0 - Salir\n")

    def menu_opciones(self):
        op = -1;
        se_ingreso_datos = False
        while op != 0:
            self.mostrar_menu()
            op = int(input("Ingrese una opcion: "))
            if op == 1:
                numero_1, numero_2 = self.ingresar_datos()
                calculadora = Calculadora(numero_1, numero_2)
                se_ingreso_datos = True
            if op == 2 and se_ingreso_datos:
                print(f"Resultado:{calculadora.sumar():>9}")
            elif op == 3 and se_ingreso_datos:
                print(f"Resultado:{calculadora.restar():>9}")
            elif op == 4 and se_ingreso_datos:
                print(f"Resultado:{calculadora.multiplicar():>9}")
            elif op == 5 and se_ingreso_datos:
                if numero_2 == 0:
                    print(f"No se puede dividir por cero. Trate nuevamente!")
                else:
                    print(f"Resultado: {calculadora.dividir():>10}")
            elif op == 0:
                print(f"Programa finalizado")
            else:
                if not se_ingreso_datos:
                    print(f"\nDebe ingresar los datos primero!\n")
                else:
                    print(f"\nOpcion errónea. Trate nuevamente!\n")
            
            

       
# Programa principal
mi_app = App()
mi_app.menu_opciones()
        