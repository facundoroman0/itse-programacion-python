"""
DESAFIO 9
Desarrollar un programa que permita saber si un año es bisiesto. Para que un año sea
bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también
sea divisible por 400.
"""
anio = int(input("Ingrese el año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"El año es bisiesto")
else:
    print(f"El año no es bisiesto")