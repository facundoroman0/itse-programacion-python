from caballo import Caballo
from carrera import Carrera

def run():
    caballo_1 = Caballo("Relámpago")
    caballo_2 = Caballo("Velóz")
    mi_carrera = Carrera(caballo_1, caballo_2)
    mi_carrera.iniciar()

if __name__ == "__main__":
    run()