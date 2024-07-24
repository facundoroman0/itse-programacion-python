"""
DESAFÍO 4
Solicitar al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes,
otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si
el día ingresado no es ninguno de esos, imprimir otro mensaje distinto.
"""

dia_semana = input("Ingrese un dia de la semana: ")
dia_semana_minusculas = dia_semana.lower()
if dia_semana_minusculas == "lunes":
    print(f"Primer dia de la semana")
elif dia_semana_minusculas == "viernes":
    print(f"¡Buen fin de semana!")
elif dia_semana_minusculas == "sabado":
    print(f"¡Disfrute su dia!")
elif dia_semana_minusculas == "domingo":
    print(f"¡Ultimo dia de la semana!")
elif dia_semana_minusculas == "martes" or dia_semana_minusculas == "miercoles" or dia_semana_minusculas == "jueves":
    print("Buen día!")
else:
    print("El dia ingresado es erróneo")