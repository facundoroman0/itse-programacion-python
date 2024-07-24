"""
  En un Banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El Banco requiere también al final del día 
calcular la cantidad de dinero que se ha depositado. Se deberán instanciar dos clases, la clase Cliente y la clase Banco. La clase 
Cliente tendrá los atributos nombre, cantidad y los métodos __init__, depositar, extraer, get_total. La clase Banco tendrá como 
atributos 3 objetos de la clase Cliente y los métodos __init__, operar y deposito_total.
"""

class Cliente():
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def cantidad(self):
        return self.cantidad
    
    def nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def depositar(self, monto_deposito):
        self.cantidad += monto_deposito
    
    def get_total(self):
        return
        
    def extraer(self, monto_extraer):
        extraccion_hecha = False
        if self.cantidad != 0:
            self.cantidad -= monto_extraer
            extraccion_hecha = True
        return extraccion_hecha

