#Agregar un contacto
#Eliminar Contactos
#Actualizar un Contacto
#Ver un Contacto
#Ver toos nuestros contactos

agenda_telefonica = dict()



def imprimir_operacion(nombre_operacion):
    print()
    print("------------Agenda Telefónica------------")
    print(nombre_operacion)
    print("-------------------------------------------")
    print()

def agregar_contacto():
    # print("agregar contacto")
    nombre = input("Nombre del nuevo contacto: ")
    numero = input("Numero del nuevo contacto: ")
    agenda_telefonica[nombre] = numero
    imprimir_operacion("Contacto Agregado")

    # print()
    # print("------------Agenda Telefónica------------")
    # print("Contacto Agregado")
    # print("-------------------------------------------")
    # print()

def eliminar_contacto():
    # print("eliminar contacto")
    nombre = input("Nombre del contacto que desea borrar: ")
    try:
        del agenda_telefonica[nombre]
    except KeyError:
        imprimir_operacion("Ese contacto no existe")
    else:
        imprimir_operacion("Contacto Eliminado")

def actualizar_contacto():
    # print("actualizar contacto")
    nombre = input("Nombre del contacto que deseas actualizar: ")
    numero = input("Nuevo numero de este contacto: ")

    agenda_telefonica[nombre] = numero

    imprimir_operacion("Contacto Actualizado")
def ver_contacto():
    # print("ver contacto")
    nombre = input("Nombre del contacto: ")
    nombre_operacion = None

    try:
        # nombre_operacion = print(nombre + " - " + agenda_telefonica[nombre])
        nombre_operacion = "{} - {}".format(nombre,agenda_telefonica[nombre])
    except KeyError:
       nombre_operacion = print("Ese contacto no existe")

    imprimir_operacion(nombre_operacion)


def ver_contactos():
    # print("ver contactos")
    nombre_operacion = None

    if len(agenda_telefonica) == 0:
        nombre_operacion = print("No existe ningún contacto")
    else:
        for contacto in agenda_telefonica:
           # nombre_operacion = print(contacto + "-" + agenda_telefonica[contacto])
            if nombre_operacion == None:
                nombre_operacion = "{} - {}".format(contacto,agenda_telefonica[contacto])
            else:
                nombre_operacion += "\n{} - {}".format(contacto,agenda_telefonica[contacto])
    imprimir_operacion(nombre_operacion)
def iniciar_agenda():
    print("Bienvenido a la Agenda Telefónica de Juan")

    while True:
        print("1 - Agregar Contacto")
        print("2 - Eliminar Contacto")
        print("3 - Actualiza Contacto")
        print("4 - Ver un Contacto")
        print("5 - Ver todos los Contacto")
        print("6 - Salir")

        try:
            operacion = int(input(": "))
        except ValueError:
            print()
            print("Porfavor selecciona un numero del 1 al 6")
            print()
        else:
            if operacion == 1:
                agregar_contacto()
            elif operacion ==2:
                eliminar_contacto()
            elif operacion == 3:
                actualizar_contacto()
            elif operacion == 4:
                ver_contacto()
            elif operacion == 5:
                ver_contactos()
            elif operacion == 6:
                break
            else:
                print("operación desconnocida")


def dar_despedida():
    print()
    print("Gracias por usar nuestra agenda telefónica")
    print()


iniciar_agenda()
dar_despedida()

