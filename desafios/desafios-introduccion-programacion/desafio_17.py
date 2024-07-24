"""
Desafío 17
Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se
encuentran en dicha frase.

"""
frase = input("Ingrese una frase: ").lower()

cantidad_vocales = 0
for i in range(0,len(frase)):
    if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        cantidad_vocales += 1

if cantidad_vocales != 0:
    print(f"Cantidad de vocales en la frase ingresada: {cantidad_vocales}")
else:
    print("No hay vocales en la frase ingresada!")

# Otra Alternativa
for letra in frase:
    if letra in "aeiouáéíóú": #Relacion con un conjunto
        cantidad_vocales+=1

print(f"Cantidad de vocales en la frase ingresada: {cantidad_vocales}")