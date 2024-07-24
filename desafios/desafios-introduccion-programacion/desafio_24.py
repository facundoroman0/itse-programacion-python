"""
Desafío 24
Desarrollar un programa que permita al usuario ingresar dos años y luego imprima
todos los años en ese rango, que sean bisiestos y múltiplos de 10. Nota: para que un
año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que
también sea divisible por 400.
"""

anio_1 = int(input("Ingrese un año: "))
anio_2 = int(input("Ingrese otro año: "))


anio_entre_rango = anio_1

print("Listado de años entre los ingresados")
while anio_entre_rango <= anio_2:

    if (anio_entre_rango % 4 == 0 and anio_entre_rango % 100 != 0) or anio_entre_rango % 400 == 0:
        print(anio_entre_rango," ")

    anio_entre_rango+=1
