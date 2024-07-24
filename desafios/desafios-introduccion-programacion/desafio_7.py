"""
DESAFÍO 7
Desarrollar un programa que permita al usuario elegir un candidato por el cual votar.
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde,
candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe
imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato
elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los
candidatos disponibles, indicar “Opción errónea”.
"""

print(f"- - - - - - - Candidatos- - - - - - -")
print(f"Candidato A - Partido Rojo\nCandidato B - Partido Verde\nCandidato C - Partido Azul")
opcion_candidato = input("\nElija una opcion: ").lower()


if opcion_candidato == "a":
    print("Usted ha votado por el partido Rojo")
elif opcion_candidato == "b":
    print("“Usted ha votado por el partido Verde")
elif opcion_candidato == "c":
    print("“Usted ha votado por el partido Azul")
else:
    print("Opcion errónea")