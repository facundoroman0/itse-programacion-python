from animal import Animal


class Granja():
    """Tipo Abstracto de Dato Granja"""

    def __init__(self):
        # atributo privado con __
        self.__animales = []
        self.cargar()

    def add_animal(self, un_animal):
        self.__animales.append(un_animal)

    def como_dicen_animales(self):
        for animal in self.__animales:
            print(f" El Animal {animal.nombre} hace {animal.onomatopeya}")

    def cargar(self):
        un_animal = Animal("Vaca", "Mouhu")
        self.add_animal(un_animal)
        un_animal = Animal("Gato", "Miahu")
        self.add_animal(un_animal)
        un_animal = Animal("Perro", "Guahu")
        self.add_animal(un_animal)
        un_animal = Animal("Pollito", "PioPio")
        self.add_animal(un_animal)

    def execute(self):
        self.como_dicen_animales()
