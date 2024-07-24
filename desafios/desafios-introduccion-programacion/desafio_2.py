"""
DESAFÍO 2
Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. No
considerar el caso en que ambos números son iguales
"""

numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))

if numero_1 < numero_2:
    print(f"El numero {numero_1} es menor que el numero {numero_2}")
else:
    if numero_2 < numero_1:
        print(f"El numero {numero_2} es menor que el numero {numero_1}")
