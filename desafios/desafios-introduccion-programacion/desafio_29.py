"""
Desafío 29
Dada un alfanumérico texto y un caracter x, retornar una lista de enteros representando
la distancia mas corta desde cada caracter en texto hasta la primer ocurrencia del
caracter x.
"""

def distancia_mas_corta(texto, x):
    n = len(texto)
    res = [0 if texto[i] == x else float("inf") for i in range(n)]
    
    prev = float("inf")
    for i in range(n):
        if texto[i] == x:
            prev = 0
        elif prev != float("inf"):
            prev += 1
        res[i] = min(res[i], prev)
    
    prev = float("inf")
    for i in range(n - 1, -1, -1):
        if texto[i] == x:
            prev = 0
        elif prev != float("inf"):
            prev += 1
        res[i] = min(res[i], prev)
    
    return res

texto = input("Ingresar un texto: ")
x = input("Ingrese un caracter: ")
print(distancia_mas_corta(texto, x))

