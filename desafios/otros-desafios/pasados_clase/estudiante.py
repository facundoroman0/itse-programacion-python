
class Estudiante():
    """Desafío 1. documentación del codigo"""

    def __init__(self, nombre, nota_evaluacion):
        # atributo privado con __
        self.__nombre = nombre
        self.__nota_evaluacion = nota_evaluacion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def nota_evaluacion(self):
        return self.__nota_evaluacion

    @nota_evaluacion.setter
    def nota_evaluacion(self, nota_evaluacion):
        self.__nota_evaluacion = nota_evaluacion

    def is_aprobado(self):
        """se evalúa si el Estudiante aprobó con nota de 6 o mas"""
        return self.nota_evaluacion >= 6

