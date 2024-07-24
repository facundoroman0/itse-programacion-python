"""
Desafío 30
Sumar dos numeros enteros sin utilizar el operador de suma.
"""

def sumar(numero_1, numero_2):
    numero_1 *= -1
    return (numero_1-numero_2)*-1

numero_1 = -5;
numero_2 = 10;

print(f"Resultado: {sumar(numero_1,numero_2)}")