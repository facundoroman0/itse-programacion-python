"""
Desafío 22
Desarrollar un programa que permita al usuario ingresar 6 números enteros, que
pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números
negativos y el promedio de los positivos.
No olvides que no es posible dividir por cero, por lo que es necesario evitar que el
programa arroje un error si no se ingresaron números positivos.

"""
suma_positivos = 0
suma_negativos = 0
cantidad_positivos = 0

for i in range(0,6):

    numero_entero = int(input("Numero entero: "))

    if numero_entero != 0:
        if numero_entero < 0:
            suma_negativos += numero_entero
        else:
            suma_positivos += numero_entero
            cantidad_positivos += 1

if suma_negativos != 0:
    print(f"Sumatoria de los negativos: {suma_negativos}")
else:
    print(f"No se ingresaron numeros negativos")

if cantidad_positivos != 0:
    print(f"Promedio de numeros positivos: {suma_positivos/cantidad_positivos}")
else:
    print("No se ingresaron numeros positivos")

