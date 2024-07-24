"""
Desafío 39
Desarrollar un algoritmo en donde se requiera al usuario que ingrese un texto largo y
luego a ese mismo dato se le cuenten la cantidad de ocurrencias de cada una de las
vocales. Tener en cuenta que cada vocal puede presentarse en mayúscula, minúscula
o acentuada, de tal manera que se obtenga la siguiente información:

cantidad de ocurrencias de la vocal a: ...
cantidad de ocurrencias de la vocal e: ...
cantidad de ocurrencias de la vocal i: ...
cantidad de ocurrencias de la vocal o: ...
cantidad de ocurrencias de la vocal u: ...
cantidad total de vocales: ...
"""

def ocurrencias_vocales(texto):
    ocurrencias_a, ocurrencias_e, ocurrencias_i, ocurrencias_o, ocurrencias_u = 0, 0, 0, 0, 0
    for i in texto:
        if i == "a" or i == "á":
            ocurrencias_a += 1
        elif i == "e" or i == "é":
            ocurrencias_e += 1
        elif i == "i" or i == "í":
            ocurrencias_i += 1
        elif i == "o" or i == "ó":
            ocurrencias_o += 1
        elif i == "u" or i == "ú":
            ocurrencias_u += 1
        else:
            continue

    return ocurrencias_a, ocurrencias_e, ocurrencias_i, ocurrencias_o, ocurrencias_u;

texto = input("Ingrese un texto: ").lower()

ocurrencias_a, ocurrencias_e, ocurrencias_i, ocurrencias_o, ocurrencias_u = ocurrencias_vocales(texto)

print(f"Cantidad de ocurrencia de vocales\n'a' aparece {ocurrencias_a} veces\n'e' aparece {ocurrencias_e} veces\n'i' aparece {ocurrencias_i} veces\n'o' aparece {ocurrencias_o} veces\n'u' aparece {ocurrencias_u} veces")
