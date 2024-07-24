from persona import Persona

def es_mayor_de_edad(persona):
    if persona.es_mayor_edad():
        print(f"La persona {persona.nombre} es mayor de edad")
    else:
         print(f"La persona {persona.nombre} no es mayor de edad")

def generar_persona(persona):
    print(f"="*30)
    print(f"\tGenerar datos persona")
    persona.nombre = input("Nombre: ")
    persona.edad = int(input("Edad: "))
    persona.dni = int(input("DNI: "))
    return persona

def mostrar_menu():
    print(f"="*30)
    print(f"\tMenu de Opciones")
    print(f"="*30)
    print("\n1 - Crear Persona\n2 - Ver si es mayor de edad\n0 - Salir")

def menu_opciones(persona):
    op = -1
    while op!= 0:
        mostrar_menu()
        op = int(input("Introduce una opcion: "))
        if op == 1:
            persona = generar_persona(persona)
        elif op == 2:
            es_mayor_de_edad(persona)
        elif op == 0:
            print(f"Programa finalizado")
        else:
            print(f"Opcion erronea. Trate nuevamente!")

def ejecutar():           
    mi_persona = Persona()
    menu_opciones(mi_persona)

ejecutar()

    
