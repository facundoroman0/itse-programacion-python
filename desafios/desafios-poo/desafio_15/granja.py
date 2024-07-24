from animal import Animal

class Granja():
    def __init__(self):
        self.__animales = []
    
    def add_animal(self, un_animal):
        self.__animales.append(un_animal)

    def como_dicen_animales(self):
        for animal in self.__animales:
            print(f"{animal.nombre} hace: {animal.onomatopeya}")

    def cargar(self):
        un_animal = Animal()        