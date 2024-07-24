"""
DESAFÍO 5
Desarrollar un programa que, dado un número entero, muestre su valor absoluto. Nota:
para los números positivos su valor absoluto es igual al número (el valor absoluto de 52
es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado
por -1 (el valor absoluto de -52 es 52).
"""

numero = int(input("Ingrese un numero entero: "))
if numero >= 0:
    print(f"El valor absoluto del numero ingresado es: {numero}")
else:
    print(f"El valor absoluto del numero ingresado es: {numero*-1}")