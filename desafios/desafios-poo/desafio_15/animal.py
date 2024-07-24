class Animal():
    def __init__(self, nombre, onomatopeya):
        self.__nombre  = nombre
        self.__onomatopeya = onomatopeya

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def onomatopeya(self):
        return self.__onomatopeya
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @onomatopeya.setter
    def onomatopeya(self, nuevo_onomatopeya):
        self.__onomatopeya = nuevo_onomatopeya
        
    

        