"""
Desafío 27
Solicitar al usuario que ingrese los nombres de los estudiantes de primer año,
finalizando al ingresar “S”. Luego, solicitar al usuario que ingrese los nombres de los
estudiantes de segundo año, finalizando al ingresar “S”.
A continuación informar:

- la lista de todos los nombres de los estudiantes de primer año y de segundo año,
sin repeticiones.

- La lista de todos los nombres de los estudiantes de primer año y de segundo
año que se repiten.

- la lista de todos los nombres de los estudiantes de primer año que no se repiten
en segundo año.
"""
# Genera una lista con nombres de estudiantes
def generarListaNombresEstudiantes():
    lista = []
    nombre = ""

    while nombre != "s":
        nombre = input("Ingresar nombre: ")
        if nombre != "s":
            lista.append(nombre)
    return lista

# Determina si una lista está vacia o no
def verificarListaVacia(lista):
    if len(lista)==0:
        return True;
    else:
        return False;

# Genera una lista sin repeticiones
def generarSinRepeticiones(lista):
    sin_repeticiones = []
    for i in lista:
        if i not in sin_repeticiones:
            sin_repeticiones.append(i)    
    return sin_repeticiones

# Genera una lista con los nombres repetidos de una lista de nombres
def generarRepetidos(lista):
    repetidos = []
    for i in lista:
        if lista.count(i)>1 and i not in repetidos:
            repetidos.append(i)      
    return repetidos

# Genera una lista con los nombres unicos
def generarNoRepetidos(lista):
    sin_repetir = []
    for i in lista:
        if lista.count(i) == 1:
            sin_repetir.append(i)
    return sin_repetir

# Muestra una lista
def mostrarLista(lista):
    for i in range(0,len(lista)):
        print(lista[i])
    
# Muestra los listados de nombres de primer y segundo año sin repeticiones
def mostrarListadoPrimerSegundoAnio(lista_1, lista_2):
    mi_lista = generarSinRepeticiones(lista_1)
    print(f"- - - - - - -Listado de alumnos de primer año - - - - - - -")
    mostrarLista(mi_lista)
    mi_lista = generarSinRepeticiones(lista_2)
    print(f"- - - - - - -Listado de alumnos de segundo año - - - - - - -")
    mostrarLista(mi_lista)
    return None
    
# Muesta listado de los alumnos con nombres repetidos en primer y segundo año
def mostrarListadoDeRepetidos(lista_1,lista_2):
    lista_repetidos = generarRepetidos(lista_1);
    print(f"- - - - - - -Listado de alumnos con nombres repetidos de primer año - - - - - - -")
    mostrarLista(lista_repetidos)

    lista_repetidos = generarRepetidos(lista_2);
    print(f"- - - - - - -Listado de alumnos con nombres repetidos de seguno año - - - - - - -")
    mostrarLista(lista_repetidos)
    return None

# Muestra listado de nombres unicos en primer y segundo año
def mostrarListadoNombresUnicos(lista_1, lista_2):
    print(f"- - - - - - -Listado de alumnos con nombres que no se repiten de primer año - - - - - - -")
    nombres_unicos = generarNoRepetidos(lista_1)
    mostrarLista(nombres_unicos)
    print(f"- - - - - - -Listado de alumnos con nombres que no se repiten de segundo año - - - - - - -")
    nombres_unicos = generarNoRepetidos(lista_2)
    mostrarLista(nombres_unicos)
    return None


# PROGRAMA PRINCIPAL
if __name__ == '__main__':
# Llamado para generar listas
    print(f"Generar lista de primer año: ")
    lista_primer_anio = generarListaNombresEstudiantes()
    print(f"Generar lista de segundo año: ")
    lista_segundo_anio = generarListaNombresEstudiantes()


    if not(verificarListaVacia(lista_primer_anio) and verificarListaVacia(lista_segundo_anio)):
        # Mostrar listados de nombres de primer y segundo año sin repeticiones
        print(f"\nConsigna 1)")
        mostrarListadoPrimerSegundoAnio(lista_primer_anio, lista_segundo_anio)
        print(f"\nConsigna 2)")
        mostrarListadoDeRepetidos(lista_primer_anio,lista_segundo_anio)
        print(f"\nConsigna 3)")
        mostrarListadoNombresUnicos(lista_primer_anio,lista_segundo_anio)
    else:
        print(f"Listas vacias!")




