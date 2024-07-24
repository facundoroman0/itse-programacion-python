"""
DESAFÍO 6 [Usar slice()]
Solicitar al usuario que ingrese los nombres de dos personas, los cuales se
almacenarán en dos variables. A continuación, imprimir “coincidencia” si los nombres
de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Si
no es así, imprimir “no hay coincidencia”.
"""

nombre_1 = input("Ingrese el nombre de la primera persona: ")
nombre_2 = input("Ingrese el nombre de la segunda persona: ")

if nombre_1[0] == nombre_2 [0] and nombre_1[len(nombre_1) - 1] == nombre_2[len(nombre_2) - 1]: 
    print("Hay coincidencia. Empiezan y terminan con la misma letra")

elif nombre_1[0] == nombre_2[0]:
    print("Hay coincidencia. Empiezan con la misma letra")

elif nombre_1[len(nombre_1) - 1] == nombre_2[len(nombre_2) - 1]:
    print("Hay coincidencia. Terminan con la misma letra")

else:
    print("No hay coincidencia")