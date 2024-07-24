"""
Desafío 14
Solicitar al usuario que ingrese un número entero positivo e imprimir todos los números
correlativos entre el ingresado por el usuario y uno menos del doble del mismo.
"""

numero = int(input("Ingrese un numero: "))
correlativo_numero = numero * 2 - 1

print("Numeros entre el ingresado y el doble del mismo menos 1\n")
for i in range(numero,correlativo_numero):
    print(f"{i} ")

print("")
