"""Desafio 1. Como utilizar una librería creada por nosotros. """
from estudiante import Estudiante

# inicialización del objeto
estudiante = Estudiante("Mariano", 5)

# consulta de sus atributos
print(f" nombre: {estudiante.nombre}")
print(f" nota del estudiante: {estudiante.nota_evaluacion}")

# consultar si el estudiante ha aprobado
print(f" el estudiante aprobó  ?: {estudiante.is_aprobado()}")
