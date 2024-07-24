from circulo import Circulo

def ingresar_datos():
    radio = float(input("Radio del circulo: "))
    return radio

def execute():
    radio = ingresar_datos()
    circulo = Circulo(radio)
    print(f"El area del circulo es {circulo.area_circulo():.2f} y su perimetro es {circulo.perimetro_circulo():.2f}")

if __name__ == "__main__":
    execute()