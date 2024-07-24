"""
Desafío 38
Desarrollar un algoritmo en donde se requiera al usuario que ingrese un nombre y
luego a ese mismo dato se lo presente, separado por un espacio en blanco, 30 veces
repetido en una misma línea de la pantalla.
"""

nombre = input("Por favor, ingresa tu nombre: ")
resultado = (nombre + " ") * 30
print(resultado)
