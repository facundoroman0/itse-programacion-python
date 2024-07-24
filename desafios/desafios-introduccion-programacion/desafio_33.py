"""
Desafío 33
Desarrollar una función que reciba como entrada una lista y retorne otra lista con los
números sumados más uno.
"""
def retornarSiguientes(mi_lista):
    lista_siguientes = []

    for i in range(0, len(mi_lista)):
        lista_siguientes.append(mi_lista[i] + 1)
    return lista_siguientes

lista = [1,2,3,4,5,6]

print(retornarSiguientes(lista))