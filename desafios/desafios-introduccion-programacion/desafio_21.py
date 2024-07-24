"""
Desafío 21
Desarrollar un algoritmo que muestre los primeros 10 números de la sucesión de
Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada
elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8,
13, 21, 34, 55...
"""

anterior = 0
siguiente = 1
suma_fibonacci = 0
print(f"Sucesion Fibonacci")

for i in range(0,10):
    print(f"{anterior}  ",end="")
    suma_fibonacci = anterior + siguiente
    anterior = siguiente
    siguiente = suma_fibonacci

print("")