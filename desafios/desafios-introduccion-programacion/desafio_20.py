"""
Desafío 20
Dado un número entero positivo, mostrar su Factorial. El Factorial de un número se
obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese
número.
"""

factorial = 1
numero= int(input("Ingrese un numero: "))

if numero == 0:
    print(f"El factorial de cero es: {factorial}")
else:
    aux = numero
    while numero != 1:
        factorial = factorial * numero
        numero -=1
    print(f"El factorial de {aux} es: {factorial:}".replace(",","."))