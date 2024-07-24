"""
Desafío 15
Desarrollar un programa que solicite al usuario una cantidad y luego itere la cantidad de
veces dada. En cada iteración, solicitar al usuario que ingrese un número. Al finalizar,
mostrar la suma de todos los números ingresados.
"""

cantidad = int(input("Ingrese una cantidad: "))
suma = 0
if cantidad > 0:
    for i in range(0,cantidad):
        numero = int(input("Ingrese un numero: "))
        suma += numero

    print(f"La suma de los numeros es: {suma}")
else:
    print("Cantidad erronea")
