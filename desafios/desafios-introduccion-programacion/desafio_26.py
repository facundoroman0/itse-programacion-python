"""
Desafío 26
Desarrolle una función para invertir un dato alfanumérico. Pruebe si el código funciona
correctamente.
"""

# Invierte un alfanumerico y lo retorna en una lista
def invertirDatoAlfanumerico(dato):
    invertido = []
    i = len(dato)

    while i>0:
        #invertido += dato[i-1]
        invertido.append(dato[i-1])
        i -= 1
    return invertido

# PROGRAMA PRINCIPAL
dato_alfanumerico = input("Ingresar dato alfanumerico: ")
print(f"{invertirDatoAlfanumerico(dato_alfanumerico)}")
