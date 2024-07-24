"""
Desafio 1
Solicitar al usuario que ingrese su número de cliente. Si el número es el 1000, imprimir
"Ganaste un premio".
"""
numero_cliente = int(input("Ingrese el numero de cliente: "))
if numero_cliente == 1000:
    print(f"Ganaste un premio")
else:
    print(f"Seguí participando!!!")