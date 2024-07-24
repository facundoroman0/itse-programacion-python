"""
Desafío 40
Desarrollar un algoritmo en donde se informe el volumen, en litros, de un contenedor de
tipo prisma rectangular, esfera o cilíndrico.
Para realizar dichos cálculos se requerirá al usuario que primero seleccione el tipo de
contenedor ingresando la opción correspondiente y luego se pidan los datos requeridos
para el cálculo de ese contenedor en particular.
Tips: se sugiere, que se presente un Menú de Opciones que luzca de la siguiente
forma:
Menú de Opciones
-----------------------------------------------------------
1 - Calcular volumen contenedor prisma rectangular - V = largo × ancho × altura
2 - Calcular volumen contenedor esférico - V = 4/3 pi * r^3
3 - Calcular volumen contenedor cilíndrico - V = Π h r²,
s - Salir
"""
import math

def calcular_volumen_prisma_rectangular(largo, ancho, altura):
    return largo*ancho*altura;

def calcular_volumen_contenedor_esferico(radio):
    return ((4/3)*(math.pi)) * math.pow(radio,3)

def calcular_volumen_contenedor_cilindrico(radio, altura):
    return math.pi * altura * math.pow(radio,2)

def mostrar_menu_de_opciones():

    print(f"\nMenú de Opciones\n")
    print(f"-----------------------------------------------------------\n")
    print(f"1 - Calcular volumen contenedor prisma rectangular\n2 - Calcular volumen contenedor esférico\n3 - Calcular volumen contenedor cilíndrico\ns - Salir")
    
    return None

def opcion_prisma_rectangular():
    print(f"\nCalcular el volumen del prisma rectangular")
    largo = float(input("Largo: "))
    ancho = float(input("Ancho: "))
    altura = float(input("Altura: "))
    volumen = calcular_volumen_prisma_rectangular(largo, ancho, altura);
    print(f"El volumen del prisma rectangular es: {volumen:.2f}cm²")

    return None

def opcion_contenedor_esferico():
    print(f"\nCalcular el volumen del contenedor esférico")
    radio = float(input("Radio: "))
    volumen = calcular_volumen_contenedor_esferico(radio);
    print(f"El volumen del contendor esférico es: {volumen:.2f}cm³")

    return None

def opcion_contenedor_cilindrico():
    print(f"\nCalcular el volumen del contenedor cilíndrico")    
    radio = float(input("Radio: "))
    altura = float(input("Altura: "))
    volumen = calcular_volumen_contenedor_cilindrico(radio, altura);
    print(f"El volumen del contendor esférico es: {volumen:.2f} cm²")

    return None

def menu_de_opciones():

    op = " "

    while op!= "s":
        mostrar_menu_de_opciones()
        print("\nIngrese una Opcion: ",end="")
        op = input()
        if op == "1":
            opcion_prisma_rectangular()
        elif op == "2":
            opcion_contenedor_esferico()
        elif op == "3":
            opcion_contenedor_cilindrico()
        elif op == "s":
            continue
        else:
            print(f"\nOpcion no contemplada. Elija una de las mostradas por favor")
    
    return None


# Principal
menu_de_opciones()