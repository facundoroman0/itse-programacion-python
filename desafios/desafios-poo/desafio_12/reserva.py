class Reserva():
    def __init__(self, nombre, tipo_habitacion, precio, duracion):
        self.__nombre= nombre;
        self.__tipo_habitacion = tipo_habitacion
        self.__precio = precio
        self.__duracion = duracion

    @property
    def nombre(self):
        return self.__nombre 
    
    @property
    def tipo_habitacion(self):
        return self.__tipo_habitacion 

    @property
    def precio(self):
        return self.__precio 

    @property
    def duracion(self):
        return self.__duracion
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @tipo_habitacion.setter
    def tipo_habitacion(self, nuevo_tipo_habitacion):
        self.__tipo_habitacion = nuevo_tipo_habitacion

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio
    
    @duracion.setter
    def duracion(self, nueva_duracion):
        self.__duracion = nueva_duracion;



    