class Triangulo():
    """Desafío 2. documentación del codigo"""

    def __init__(self, cateto_opuesto, cateto_adyacente, hipotenusa):
        self.__cateto_opuesto = cateto_opuesto
        self.__cateto_adyacente = cateto_adyacente
        self.__hipotenusa = hipotenusa

    @property
    def cateto_opuesto(self):
        return self.__cateto_opuesto

    @property
    def cateto_adyacente(self):
        return self.__cateto_adyacente

    @property
    def hipotenusa(self):
        return self.__hipotenusa

    def magnitud_lado_mayor(self):
        return max([self.__cateto_opuesto, self.__cateto_adyacente, self.__hipotenusa])

    def tipo_triangulo(self):
        if self.__cateto_opuesto == self.__cateto_adyacente and self.__cateto_opuesto == self.__hipotenusa:
            return "Equilátero" # tiene los 3 lados iguales
        elif self.__cateto_opuesto == self.__cateto_adyacente or self.__cateto_opuesto == self.__hipotenusa or self.__cateto_adyacente == self.__hipotenusa:
            return "Isósceles" # tiene dos lados iguales
        else:
            return "Escaleno" # tiene todos los lados distintos


def execute():
    # inicializar un triángulo
    triangulo = Triangulo(5, 3, 7)

    # consultar magnitud de mayor lado
    print(
        f" el mayor lado del triángulo es: {triangulo.magnitud_lado_mayor()}")

    # consultar tipo de triángulo
    print(f" el tipo de triángulo es: {triangulo.tipo_triangulo()}")


if __name__ == "__main__":
    # permite ejecutar el script como modulo y como libreria
    execute()
