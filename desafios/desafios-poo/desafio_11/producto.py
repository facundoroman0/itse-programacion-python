class Productor():
    def __init__(self, codigo, nombre, precio, cantidad):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters
    @property
    def codigo(self):
        return self.codigo
    
    @property
    def nombre(self):
        return self.nombre
    
    @property
    def precio(self):
        return self.precio
    
    @property
    def cantidad(self):
        return self.cantidad
    
    # Setters
    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @cantidad.setter
    def cantidad(self, nuevo_cantidad):
        self.__cantidad = nuevo_cantidad

    
