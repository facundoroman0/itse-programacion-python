"""
Desafío 37
Una Chocolatería tiene a la venta bombones en cajas de 5, 8 y 13 unidades.
Desarrollar una función que reciba el dato de la cantidad de bombones pedida por el
cliente, luego, calcular e informar si es posible entregar el pedido y con cuantas cajas
de cada tamaño o no es posible armar una entrega con esa cantidad pedida.
Utilice varias estrategias para realizar el calculo. Luego, testear cada estrategia con 13
cantidades generadas aleatoriamente de un rango de entre 1 a 1000.
"""

def es_posible_entregar_bombones(cantidad):
    for x in range(int(cantidad / 13 + 1)):
        for y in range(int((cantidad - 13 * x) / 8) + 1):
            z = int((cantidad - 13 * x - 8 * y) / 5)
            if 13 * x + 8 * y + 5 * z == cantidad:
                return x, y, z
    return None

import random

cantidades = [random.randint(1, 1000) for i in range(13)]
resultado = []

for cantidad in cantidades:
    resultado = es_posible_entregar_bombones(cantidad)
    if resultado:
        print(f"{cantidad} bombones: {resultado[0]} cajas de 13, {resultado[1]} cajas de 8, {resultado[2]} cajas de 5")
    else:
        print(f"{cantidad} bombones: No es posible entregar")
