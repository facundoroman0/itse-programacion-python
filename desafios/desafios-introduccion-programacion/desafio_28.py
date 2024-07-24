"""
Desafío 28
Encriptar un mensaje utilizando el método de “la cifra del césar”, que consiste en correr
cada letra del mensaje (considerando la posición de cada una en el alfabeto) una
determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra
“HOLA” se transforma en “JQNC”.
Si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se
vuelve a comenzar desde la letra “a”.
"""

def correr_letra(letra, alfabeto, corrimiento):
    letra_encriptada = ""

    for i in range(0, len(alfabeto)):
        if alfabeto[i] == letra:
            posicion = int((i + corrimiento) % 27)
            letra_encriptada = alfabeto[posicion]

    return letra_encriptada

alfabeto = ["a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l",
            "m", "n", "ñ", "o", "p", "q",
            "r", "s", "t", "u", "v", "w",
            "x", "y", "z"]

codificado = []
corrimiento = int(input("Corrimiento: "))
mensaje = input("Mensaje: ")

for i in range(0,len(mensaje)):
    letra = correr_letra(mensaje[i], alfabeto, corrimiento)
    codificado.append(letra)
print(codificado)
