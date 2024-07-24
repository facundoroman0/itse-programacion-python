"""
Autor: Facundo Nahuel Romano
"""

"""Importar libreria random para numeros aleatorios"""
from random import *

"""Genera un numero aleatorio entre 0 y 99"""
def generar_aleatorio_entre_0_y_99():
    numero_aleatorio = randint(0,99)
    return numero_aleatorio

"""Genera una lista con numeros enteros entre 0 y 99, segun la cantidad pasada como parámetro"""
def generar_universo(cantidad_elementos):
    universo = []
    for i in range(0, cantidad_elementos):
        universo.append(generar_aleatorio_entre_0_y_99())
    return universo
    
"""Muestra una etapa de simulacion del universo"""
def mostrar_simulacion_universo(universo):
    for i in range(0, len(universo)):
        print(f"{universo[i]:>3}",end="")
    return None

"""Determina si un numero pasado como parámetro es par"""
def numero_par(numero):
    es_par = False
    if numero%2==0:
        es_par = True
    return es_par

"""Busca y reemplaza un numero impar por un numero aleatorio"""
def reemplazar_impar_por_aleatorio(universo):
    for i in range(0, len(universo)):
        if not numero_par(universo[i]):
            universo[i] = generar_aleatorio_entre_0_y_99()
    return universo

"""Determina si el universo contiene un numero impar. Si tiene, retorna True; caso contrario, retorna False"""
def buscar_numeros_aleatorios_impares(universo):
    hay_numero_impar = False
    for i in range(0,len(universo)):
        if not numero_par(universo[i]):
            hay_numero_impar = True
    return hay_numero_impar


"""PROGRAMA PRINCIPAL"""
"""Defino el universo como lista; muestro el titulo y realizo el ingreso de la cantidad de elementos"""
mi_universo = []
print(f"-------------------------------\n Un Universo de números pares\n-------------------------------")
cantidad_elementos = int(input("Ingrese la cantidad de elementos: "))
print(" ")

"""Genero la simulacion del universo"""
mi_universo = generar_universo(cantidad_elementos)

"""Muestro el estado inicial del universo"""
print(f"Estado inicial del Universo...")
print(f"",end="")
mostrar_simulacion_universo(mi_universo)
print("")

"""Defino las etapas de simulacion"""
etapa = 0

"""Mostrar las etapas de simulacion hasta que no haya numeros impares"""
while buscar_numeros_aleatorios_impares(mi_universo):

    """Reemplazo el aleatorio por el numero impart encontrado"""
    mi_universo = reemplazar_impar_por_aleatorio(mi_universo)

    """Incremento y muestro la etapa de simulacion"""
    etapa = etapa + 1   
    print(f"\nEtapa de simulacion numero {etapa}:")
        
    """Si aun quedan impares, muestro la simulacion. Sino, muestra el estado en equilibrio"""
    if buscar_numeros_aleatorios_impares(mi_universo):
        print(f"",end="")
        mostrar_simulacion_universo(mi_universo)  
    else:
        print(f"El Universo en Estado de Equilibrio...")
        print(f"",end="")
        mostrar_simulacion_universo(mi_universo)
    print(f" ")

"""Si no hubo etapas de simulacion, incrementa y muestra el estado en equilibrio"""
if etapa == 0:
    etapa = etapa + 1   
    print(f"\nEtapa de simulacion numero {etapa}:")
    print(f"El Universo en Estado de Equilibrio...")
    print(f"",end="")
    mostrar_simulacion_universo(mi_universo)
    print(f"")

    

