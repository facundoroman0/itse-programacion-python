from rectangulo import Rectangulo

def ingresar_datos():
    print(f"="*35)
    print(f"\tArea del rectangulo")
    print(f"="*35)
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    return base, altura

def execute():
    base, altura = ingresar_datos()
    mi_rectangulo = Rectangulo(base, altura)
    print(f"El area del rectangulo es: {mi_rectangulo.area_rectangulo():.2f}")

if __name__ == "__main__":
    execute()




    