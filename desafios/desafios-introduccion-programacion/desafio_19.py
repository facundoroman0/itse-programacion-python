"""
Desafío 19
Desarrollar un programa que muestre la sumatoria de todos los múltiplos de 3
encontrados entre el 0 y el 100.
"""

sumatoria_multiplos_3 = 0
for i in range(0,100):
    if i % 3 == 0:
        sumatoria_multiplos_3 += i;

print(f"La sumatoria de los numeros multiplos de 3 entre 0 y 100 es: {sumatoria_multiplos_3}")

