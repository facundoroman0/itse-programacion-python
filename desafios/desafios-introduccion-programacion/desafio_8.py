"""
DESAFIO 8
Desarrollar un programa que solicite al usuario una letra y, si es una vocal, muestre el
mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa
un String de más de un carácter, informarle que no se puede procesar el dato.
"""

letra = input("Ingrese una letra: ").lower()
longitud = len(letra)

if longitud == 1:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print(f"Es vocal")
    else:
        print(f"No es vocal")
else:
    print(f"No se puede procesar el dato")

"""
if longitud == 1:
    if letra in ["a", "e", "i", "o", "u"]:
        print(f"Es vocal")
    else:
        print(f"No es vocal")
else:
    print(f"No se puede procesar el dato")
"""