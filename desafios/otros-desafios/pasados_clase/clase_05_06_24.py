class Estudiante():
    """Aquí va la documentacion de la clase"""
    curso = "Programacion 1"
    #Método constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def informar_estudiante(self):
        return [self.nombre, self.apellido, self.curso]


estudiante_1 = Estudiante("Alberto", "Castillo")
estudiante_2 = Estudiante("Maxi", "Robles")
print(f"El estudiante {estudiante_1.nombre} {estudiante_1.apellido} cursa {estudiante_1.curso}")
print(f"El estudiante {estudiante_2.nombre} {estudiante_2.apellido} cursa {estudiante_2.curso}")


 