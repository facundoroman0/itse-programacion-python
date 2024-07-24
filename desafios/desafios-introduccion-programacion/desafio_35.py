"""
Desafío 35
Intercambia los valores de dos variables de tipo entero sin utilizar una tercera variable.
"""

def intercambiar(variable_1, variable_2):
    return variable_2, variable_1;

variable_1 = 3
variable_2 = 6

print(f"\nPrimera valor: {variable_1}\nSegundo valor: {variable_2}")

variable_1, variable_2 = intercambiar(variable_1, variable_2)

print(f"\nPrimera valor: {variable_1}\nSegundo valor: {variable_2}")