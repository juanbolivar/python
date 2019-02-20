# s.union(t)	s | t	new set with elements from both s and t
# s.intersection(t)	s & t	new set with elements common to s and t
# s.difference(t)	s - t	new set with elements in s but not in t
# s.symmetric_difference(t)	s ^ t	new set with elements in either s or t but not both

# Obtener los Sets del usuario, los llamaremos A y B
# Debemos hacer función de unión
# Debemos hacer función de intersección
# Debemos hacer función de diferencia
# Debemos hacer función de diferencia simétrica

# con la función set, casteamos el valor del input en set
# utilizamos la función split para que separe nuestra cadena,
# como no le indicamos nada, coge el espacio como delimitador

# print(conjunto_a)
# print(conjunto_b)
mensaje_inicio = "Bienvenido a los Conjuntos"
mensaje_actualizacion = "Actualización de conjuntos"


def union_conjuntos(conjunto_a, conjunto_b):
    # conjunto_a | conjunto_b

    print("\nLa union de A y B es {}\n".format(conjunto_a.union(conjunto_b)))

    # conjunto_a.union(conjunto_b)


def interseccion_conjuntos(conjunto_a, conjunto_b):
    print("\nLa interseccion de A y B es {}\n".format(conjunto_a.intersection(conjunto_b)))


def diferencia_conjuntos(conjunto_a, conjunto_b):
    print("Elije la diferencia que quieres realizar:")
    print("1. A - B")
    print("2. B - A")
    try:
        operacion = int(input(": "))
    except ValueError:
        print("\nDebes introducir 1 o 2\n")
        diferencia_conjuntos(conjunto_a, conjunto_b)
    else:
        if operacion == 1:
            print("\nLa diferencia de A - B es {}\n".format(conjunto_a.difference(conjunto_b)))
        elif operacion == 2:

            print("\nLa diferencia de B - A es {}\n".format(conjunto_b.difference(conjunto_a)))
        else:
            print("No reconozco esa operacion. Inttenta de nuevo")
            diferencia_conjuntos(conjunto_a, conjunto_b)


def diferencia_simetrica_conjuntos(conjunto_a, conjunto_b):
    print("\nLa diferencia simetrica de A y B es {}\n".format(conjunto_a.symmetric_difference(conjunto_b)))


def ver_instrucciones():
    print("Operaciones que puedes realizar:")
    print("1 Union")
    print("2 Interseccion")
    print("3 Diferencia")
    print("4 Diferencia simetrica")
    print("5 Ver instrucciones")
    print("6 Insertar nuevos conjuntos")
    print("7 Salir")


def calculadora_conjuntos(mensaje):
    print(mensaje)
    print("Introduce los elementos de los conjunto separados por espacios")
    print("Ejemplo: 1 3 5 8 0 2")

    conjunto_a = set(input("Conjunto A: ").split())
    conjunto_b = set(input("Conjunto B: ").split())

    ver_instrucciones()

    while True:
        try:
            operacion = int(input("Elige el número de operación que deseas realizar"))
        except ValueError:
            print("Introduce un número del 1 al 6")
        else:
            if operacion == 1:
                union_conjuntos(conjunto_a, conjunto_b)
            elif operacion == 2:
                interseccion_conjuntos(conjunto_a, conjunto_b)
            elif operacion == 3:
                diferencia_conjuntos(conjunto_a, conjunto_b)
            elif operacion == 4:
                diferencia_simetrica_conjuntos(conjunto_a, conjunto_b)
            elif operacion == 5:
                ver_instrucciones()
            elif operacion == 6:
                calculadora_conjuntos(mensaje_actualizacion)
            elif operacion == 7:
                print("\nGracias por usar nuestra aplicación. Te esperamos pronto\n")
                break
            else:
                print("No reconozco esa operacion. Intenta de nuevo")


calculadora_conjuntos(mensaje_inicio)
