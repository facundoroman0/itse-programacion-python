class Hotel():
    def __init__(self):
        self.reservas = []

    @property
    def reservas(self):
        return self.reservas

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
    
    
    