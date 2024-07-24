"""
Desafío 31
Dado un numero entero informar la suma de sus dígitos.
"""

numero_entero = int(input("Ingrese un numero entero: "))
numero_a_texto = str(numero_entero)

suma = 0;

for i in numero_a_texto:
    j = int(i)
    suma = suma + j

print(f"La suma de los digitos es: {suma}")