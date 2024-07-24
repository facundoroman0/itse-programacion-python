"""
Desafío 23
Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos
equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y
los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se
comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el
contenido de sus mensajes. Uno de los equipos decide utilizar un método antiguo de
encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje
–considerando la posición de cada una en el alfabeto– una determinada cantidad de
lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma
en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de
lugares que se correrán las letras) será dado por el usuario antes de comenzar a
encriptar. Los 5 mensajes usarán el mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se
vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se
convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo
matemático permite volver a comenzar por el principio una vez que se llegó a la “z”:
(índice de la letra a correr+corrimiento) % 27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin
modificación.
"""

def mostrar_lista(mi_lista):
    for i in range(0, len(mi_lista)):
        print(mi_lista[i],end=" ")
    return None

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
corrimiento = 3
mensaje = input("Mensaje: ")

for i in range(0,len(mensaje)):
    letra = correr_letra(mensaje[i], alfabeto, corrimiento)
    codificado.append(letra)

print(f"Mensaje Codificado: ",end="")
mostrar_lista(codificado)
