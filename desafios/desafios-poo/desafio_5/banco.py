from cliente import Cliente

class Banco():
    def __init__(self, cliente_1, cliente_2, cliente_3):
        self.cliente_1 = cliente_1
        self.cliente_2 = cliente_2
        self.cliente_3 = cliente_3

    @property
    def cliente_1(self):
        return self.cliente_1

    def cliente_1(self, nuevo_cliente_1):
        self.cliente_1 = nuevo_cliente_1
    
    @property
    def cliente_2(self):
        return self.cliente_2

    def cliente_2(self, nuevo_cliente_2):
        self.cliente_2 = nuevo_cliente_2

    @property
    def cliente_3(self):
        return self.cliente_3

    def cliente_3(self, nuevo_cliente_3):
        self.cliente_3 = nuevo_cliente_3
    
    def mostrar_menu(self):
        print(f"="*25)
        print(f"\tBanco")
        print(f"="*25)
        print("\n1 - Operar\n2 - Deposito total\n0 - Salir")
    
    def mostrar_sub_menu(self):
        print(f"="*25)
        print(f"\tOperar")
        print(f"="*25)
        print("\n1 - Depositar\n2 - Extraer\n3 - Total actual\n0- Volver al menu principal")
    
    def buscar_cliente(self, nombre_cliente):
        cual_cliente = -1
        if self.cliente_1.nombre == nombre_cliente:
            cual_cliente = 1
        elif self.cliente_2.nombre == nombre_cliente:
            cual_cliente = 2
        elif self.cliente_3.nombre == nombre_cliente:
            cual_cliente = 3
        else:
            pass
        return cual_cliente
    
    def mostrar_ticket(self, nombre, monto, cantidad_disponible):
        print(f"="*15, end="Ticket")
        print(f"="*15)
        print(f"Nombre: {nombre}\nMonto: {monto}\nCantidad disponible: {cantidad_disponible}")
        
    def depositar_monto(self):
        nombre = input("Nombre el cliente: ")
        monto_disponible = 0
        if self.buscar_cliente(nombre)!= -1:
            monto_depositar = float(input("Monto a depositar: "))
            if self.buscar_cliente(nombre) == 1:
                self.cliente_1.depositar(monto_depositar)
                monto_disponible = self.cliente_1.cantidad 
            pass
            if self.buscar_cliente(nombre) == 2:
                self.cliente_2.depositar(monto_depositar)
                monto_disponible = self.cliente_2.cantidad
            else:
                self.cliente_3.depositar(monto_depositar)
                monto_disponible = self.cliente_3.cantidad
            
            self.mostrar_ticket(nombre, monto_depositar, monto_disponible)
            
        else:
            print(f"Cliente inexistente!")

    def extraer_monto(self):
        nombre = input("Nombre el cliente: ")
        monto_disponible = 0
        if self.buscar_cliente(nombre)!= -1:
            monto_extraer = float(input("Monto a extraer: "))
            if self.buscar_cliente(nombre) == 1:
                self.cliente_1.extraer(monto_extraer)
                monto_disponible = self.cliente_1.cantidad 
            elif self.buscar_cliente(nombre) == 2:
                self.cliente_2.extraer(monto_extraer)
                monto_disponible = self.cliente_2.cantidad
            else:
                self.cliente_3.extraer(monto_extraer)
                monto_disponible = self.cliente_3.cantidad
    
            self.mostrar_ticket(nombre, monto_extraer, monto_disponible)
            
        else:
            print(f"Cliente inexistente!")

    def total_disponible(self):
        nombre = input("Nombre el cliente: ")
        print(f"="*15, end=" Datos del cliente ")
        print(f"="*15)
        if self.buscar_cliente(nombre)!= -1:
            if self.buscar_cliente(nombre) == 1:
                print(f"Nombre: {self.cliente_1.nombre}")
                print(f"Cantidad: {self.cliente_1.cantidad}")
                
            elif self.buscar_cliente(nombre) == 2:
                print(f"Nombre: {self.cliente_2.nombre}")
                print(f"Cantidad: {self.cliente_2.cantidad}")
            else:
                print(f"Nombre: {self.cliente_3.nombre}")
                print(f"Cantidad: {self.cliente_3.cantidad}")
        else:
            print(f"Cliente inexistente!")

    def deposito_total(self):
        print(f"="*15, end=" Total reacudado por el Banco ")
        print(f"="*15)
        total_recaudado = self.cliente_1.cantidad + self.cliente_2.cantidad + self.cliente_3.cantidad
        print(f"Depósito total: {total_recaudado}")
        
    def operar(self):
        op = -1
        while op!= 0:
            self.mostrar_sub_menu()
            op = int(input("Elegí una opcion: "))
            if op == 1:
                self.depositar_monto()
            elif op == 2:
                self.extraer_monto()
            elif op == 3:
                self.total_disponible()
            elif op == 0:
                break;
            else:
                print(f"Opcion erronea. Trate nuevamente!")
    
    def menu_opciones(self):
        op = -1
        while op!= 0:
            self.mostrar_menu()
            op = int(input("Introduce una opcion: "))
            if op == 1:
                self.operar()
            elif op == 2:
                self.deposito_total()
            elif op == 0:
                print(f"Programa finalizado")
            else:
                print(f"Opcion erronea. Trate nuevamente!")
    
def ejecutar():
    cliente_1 = Cliente("Pedro",50000.0)
    cliente_2 = Cliente("Manuel", 100.0)
    cliente_3 = Cliente("Lucas", 500.0)

    mi_app_banco = Banco(cliente_1, cliente_2, cliente_3)
    mi_app_banco.menu_opciones()

ejecutar()