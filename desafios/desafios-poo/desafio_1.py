# Desarrollar un programa que defina el Tipo de Dato Abstracto (TDA) Estudiante que tenga como
# atributos el nombre y nota de evaluación. Incluir los métodos para inicialización y consulta 
# de sus atributos y consulta si ha aprobado o no ha aprobado la evaluación.

class Estudiante:
    # Método constructor
    def __init__(self, nombre, nota_evaluacion):
        self.nombre = nombre
        self.nota_evaluacion = nota_evaluacion

    # Getters y Setters
    @property # getter: obtener valor del atributo
    def nombre(self):
        return self.nombre
                
     #setter: modificar valor del atributo
    def nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    @property # @property es un decorador que hace que el metodo se tome como atributo
    def nota_evaluacion(self):
        return self.nota_evaluacion
        
    def nota_evaluacion(self, nueva_nota_evaluacion):
        self.nota_evaluacion = nueva_nota_evaluacion
    
    # Métodos definidos
    def informar_nota_evaluacion(self):
        if self.nota_evaluacion > 6:
            print(f"El alumno {self.nombre} aprobó con {self.nota_evaluacion}")

    
estudiante = Estudiante("Manuel", 9.0)
estudiante.informar_nota_evaluacion()