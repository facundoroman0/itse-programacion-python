"""
Desafío 36
Desarrollar la función cuadrado_perfecto que reciba un numero entero positivo en una
variable de nombre numero. Luego la función debe retornar la lista de los numero
cuadrado perfectos que no sean números pares
"""

def cuadrado_perfecto(numero):
    if numero <= 0:
        raise ValueError("El número debe ser un entero positivo")
    
    cuadrados_impares = []

    for i in range(1, numero + 1):
        cuadrado = i * i
        if cuadrado > numero:
            break
        if cuadrado % 2 != 0:
            cuadrados_impares.append(cuadrado)
    
    return cuadrados_impares

numero = 50
print(f"Los cuadrados perfectos impares hasta {numero} son: {cuadrado_perfecto(numero)}")

