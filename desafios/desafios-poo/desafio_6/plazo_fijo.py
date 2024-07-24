from cuenta import Cuenta

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, tipo_cuenta, plazo, interes):
        super().__init__(titular, cantidad, tipo_cuenta)
        self.plazo = plazo
        self.interes = interes
    
    @property
    def plazo(self):
        return self.plazo
    
    def plazo(self, nuevo_plazo):
        self.plazo = nuevo_plazo
    
    @property
    def interes(self):
        return self.interes
    
    def plazo(self, nuevo_interes):
        self.interes = nuevo_interes 

    def importe_interes(self):
        return (self.cantidad * self.interes)/100
    
    def datos_titular(self):
        pass

    def total_interes(self):
        pass
    