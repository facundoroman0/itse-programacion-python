"""
  Desarrollar un programa que conste de una clase Cuenta y dos subclases PlazoFijo y CajaAhorro. 
Definir los atributos titular, cantidad, tipo de cuenta y métodos para consultar los datos en la clase 
Cuenta. La clase CajaAhorro hereda los datos y consulta el tipo de cuenta. La clase PlazoFijo tendrá 
atributos propios, plazo e interés. Tendrá métodos para obtener el importe del interés 
(cantidad * interés / 100), datos del titular, plazo, interés, tipo de cuenta y total de interés. 
Instanciar al menos dos objeto de cada subclase.
"""

class Cuenta():
    def __init__(self, titular, cantidad, tipo_cuenta):
        self.titular = titular
        self.cantidad = cantidad
        self.tipo_cuenta = tipo_cuenta
    
    @property
    def titular(self):
        return self.titular
    
    @property
    def cantidad(self):
        return self.cantidad
    
    @property
    def tipo_cuenta(self):
        return self.tipo_cuenta
    
    @titular.setter
    def titular(self, nuevo_titular):
        self.titular = nuevo_titular
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    @tipo_cuenta.setter
    def tipo_cuenta(self, nuevo_tipo_cuenta):
        self.tipo_cuenta = nuevo_tipo_cuenta
    
