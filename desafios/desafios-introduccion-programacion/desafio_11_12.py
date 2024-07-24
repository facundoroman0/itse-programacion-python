"""
Desafío 11
Imprimir todos los dígitos decimales, del 0 al 9, utilizando una repetición. ERROR! Son infinitos

DESAFIO 12
Imprimir todos los números entre el 100 y el 199.
"""

i = 100
while i<=199:
    print(f"{i} ", end="")
    i+=1 
print(f"\n")

# Usando for y range(desde, hasta, de cuanto en cuanto (defecto: 1))

for i in range(100, 200):
    print(f"{i} ", end="")
print(f"\n")