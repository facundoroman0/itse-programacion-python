"""
DESAFÍO 3
Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor.
Considerar el caso en que ambos números son iguales.
"""
numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))

if numero_1 == numero_2:
    print(f"Ambos numeros son iguales!")
else:
    if numero_1 < numero_2:
        print(f"El numero {numero_1} es menor que el segundo {numero_2}")
    else:
        print(f"El numero {numero_2} es menor que el primero {numero_1}")
