from cuenta import Cuenta

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad, tipo_cuenta):
        super().__init__(titular, cantidad, tipo_cuenta)
    
    