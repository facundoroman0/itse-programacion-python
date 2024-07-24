"""
Desafío 32
Desarrollar la función potencia sin utilizar los operadores de multiplicación o división.
"""
def suma_repetitiva(a, b):
    producto = 0
    for i in range(b):
        producto += a
    return producto

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        raise ValueError("Este método no soporta exponentes negativos.")
    
    resultado = base
    for i in range(1, exponente):
        resultado = suma_repetitiva(resultado, base)
    
    return resultado

# Ejemplo de uso
print(f"- - - - - - - Calcular de potencia- - - - - - - -")
base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"El resultado de {base} ^ {exponente} es {potencia(base, exponente)}")
