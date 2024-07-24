"""
Desafío 25
Dada una lista no vacía de numeros enteros, cada numero aparece dos veces, excepto
uno de ellos. El algoritmo debe encontrar cual de ellos no se repite.
"""

lista_numeros_enteros = [10, 80, 25, 25, 30, 35, 35, 80, 10] #Eliminar los repetidos, una variante
sin_duplicar = set([])

for i in lista_numeros_enteros:
    if i not in sin_duplicar:
        sin_duplicar.add(i)

    
print(f"Numero sin duplicado: {sin_duplicar}")



