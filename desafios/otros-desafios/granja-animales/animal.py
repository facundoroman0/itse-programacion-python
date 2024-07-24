
class Animal():
    """Tipo Abstracto de Dato Animal"""

    def __init__(self, nombre, onomatopeya):
        # atributo privado con __
        self.__nombre = nombre
        self.__onomatopeya = onomatopeya

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def onomatopeya(self):
        return self.__onomatopeya

    @onomatopeya.setter
    def onomatopeya(self, onomatopeya):
        self.__onomatopeya = onomatopeya
