"""
Desafío 34
Calcular el dato estadístico mediana de una lista dada. Si la lista es de longitud impar,
retorna el valor mediana de la misma. Si la lista es de longitud par, retorna el promedio
de los dos valores mediana. Si la lista está vacía lanzar una excepción ValueError
"""

def calcular_mediana(lista):
    if len(lista) == 0:
        raise ValueError("La lista está vacía")
    
    lista_ordenada = sorted(lista)
    longitud = len(lista)
    indice_medio = int(longitud / 2)
    
    if longitud % 2 == 1: 
        return lista_ordenada[indice_medio]
    else:  
        return (lista_ordenada[indice_medio - 1] + lista_ordenada[indice_medio]) / 2

try:
    lista = [5, 2, 1, 3, 4]
    print("La mediana es:", calcular_mediana(lista))
    
    lista_vacia = []
    print("La mediana es:", calcular_mediana(lista_vacia))
except ValueError as e:
    print(e)