# Alternativa desafio 1
# Añadiendo intentos

# intentos = 3
# cliente = 0
# while True and intentos != 0:
#     try:
#         cliente = int(input("ingrese un numero de cliente: "))
#         break
#     except ValueError:
#         print("Valor erroneo")
#         intentos -= 1
#         if intentos != 0:
#             print(f"Te quedan {intentos} intentos")
#         continue

# if cliente != 0 and intentos!= 0:
#     if cliente == 1000:
#         print("Ganaste un premio")
#     else:
#         print("No tienes premios asignados")
# else:
#     print("\nNo tienes intentos")

# Altertnativa al desafio 3
# numero_1 = int(input("Ingrese un numero: "))
# numero_2 = int(input("Ingrese otro numero: "))

# if numero_1 < numero_2:
#     print(f"El numero {numero_1} es menor que el numero {numero_2}")

# elif numero_2 < numero_1:
#         print(f"El numero {numero_2} es menor que el numero {numero_1}")

# else:
#      print("Los dos numeros son iguales")

# Alternativa al desafio 6
print("Ingresa el primer nombre:")
nombre1 = input()
print("Ingresa el segundo nombre:")
nombre2 = input() 
if nombre1[0] == nombre2[0] or nombre1[len(nombre1)-1] == nombre2[len(nombre1)-1]:
    print("Coincidencia")
else:
    print("No hay coincidencia")
