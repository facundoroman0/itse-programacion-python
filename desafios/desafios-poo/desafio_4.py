"""
Desarrollar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el e-mail. 
Además se deberá presentar un Menú de Opciones con las siguientes opciones:
    • Crear contacto
    • Borrar contacto
    • Editar contacto
    • Lista de contactos
    • Buscar contacto
    • Cerrar agenda
"""
class Contacto():
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    @property
    def nombre(self):
        return self.nombre

    def nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    @property
    def telefono(self):
        return self.telefono

    def telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    @property
    def email(self):
        return self.email

    def email(self, nuevo_email):
        self.email = nuevo_email
    

class Agenda():
    def __init__(self):
        self.lista_contactos = []
    
    def crear_contacto(self):
        print(f"="*25)
        print(f"    Crear contacto")
        print(f"="*25)
        nombre = input("Nombre del contacto: ")
        telefono = int(input("Teléfono: "))
        email = input("E-mail: ")
        contacto = Contacto(nombre, telefono, email)
        self.lista_contactos.append(contacto)
    
    def buscar(self, nombre):
        for i in range(0, len(self.lista_contactos)):
            if self.lista_contactos[i].nombre == nombre:
                pos = i
        return pos

    def agenda_vacía(self):
        esta_vacia = False
        if len(self.lista_contactos)==0:
            esta_vacia=True
        return esta_vacia
    
    def buscar_contacto(self):
        if not self.agenda_vacía():

            print(f"="*25)
            print(f"\tBuscar contacto")
            print(f"="*25)
            pos = -1
            nombre = input("Nombre del contacto: ")
            pos = self.buscar(nombre)
            if pos != -1:
                print("\nInfo. del contacto")
                self.mostrar_contacto(self.lista_contactos[pos])
            else:
                print(f"Contacto inexistente\n")
        else:
            print(f"No hay contactos disponibles")

    def mostrar_contacto(self, contacto):
        print(f"Nombre: {contacto.nombre}")
        print(f"Teléfono: {contacto.telefono}")
        print(f"E-mail: {contacto.email}")

    def mostrar_lista_contactos(self):
        print(f"="*25)
        print(f"    Lista de contactos")
        print(f"="*25)
        if not self.agenda_vacía():
            for i in range(0, len(self.lista_contactos)):
                print(f"Contacto [{i}]")
                self.mostrar_contacto(self.lista_contactos[i])
        else:
            print(f"No hay contactos disponibles")

    def borrar_contacto(self):
        print(f"="*25)
        print(f"\tBorrar contacto")
        print(f"="*25)
        if not self.agenda_vacía():
            print(f"Borrar contacto")
            x_nombre = input("Ingrese el nombre del contacto para borrar: ")
            pos = self.buscar(x_nombre)
            if pos != -1:
                print(f"{self.lista_contactos[pos].nombre} fue eliminado con éxito")
                self.lista_contactos.pop(pos)
                pass
            else:
                print(f"Contacto inexistente")
        else:
            print(f"No hay contactos disponibles")

    def actualizar_campo(self, contacto, op):
        if op == 1:
            contacto.nombre = input("Ingrese el nuevo nombre: ")
        elif op == 2:
            contacto.telefono = int(input("Ingrese el telefono: "))
        elif op == 3:
            contacto.email = input("Ingrese el nuevo email: ")
        else:
            pass
        return contacto

    def editar_contacto(self):
        print(f"="*25)
        print(f"\tEditar contacto")
        print(f"="*25)
        pos = -1
        if not self.agenda_vacía():
            nombre = input("Nombre del contacto para editar: ")
            pos = self.buscar(nombre)
            if pos!= -1:
                print(f"\nElija que campo editar:\n1-Nombre\n2-Telefoo\n3-Email\n")
                opcion = int(input("Ingrese su opcion: "))
                self.lista_contactos[pos] = self.actualizar_campo(self.lista_contactos[pos], opcion)
                print(f"Contacto actualizado")
            else:
                print("Contacto inexistente")
        else:
            print(f"Sin contactos disponibles")

    def mostrar_menu(self):
        print(f"="*25)
        print(f"\tAgenda")
        print(f"="*25)
        print("\n1 - Crear contacto\n2 - Borrar contacto\n3 - Editar contacto\n4 - Lista de contactos\n5 - Buscar contacto\n0 - Cerrar agenda\n")

    def menu_opciones(self):
        op = -1
        while op != 0:
            self.mostrar_menu()
            op = int(input("Ingrese una opcion: "))
            if op == 1:
                self.crear_contacto()
            if op == 2:
                self.borrar_contacto()
            if op == 3:
                self.editar_contacto()
            if op == 4:
                self.mostrar_lista_contactos()
            if op == 5:
                self.buscar_contacto()
                
            if op == 0:
                print(f"Programa finalizado")



agenda = Agenda()
agenda.menu_opciones()
    