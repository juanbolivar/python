import random
def rango_dificultad(dificultad):
    if dificultad == 1:
        print("Estoy pensando un número del 1 al 10")
    else:
        print("Estoy pensando un número del 1 al 40")

def num_intentos(dificultad):
    if dificultad == 1 or dificultad == 2:
        print("Solamente tienes 5 intentos")
    else:
        print("Solamente tienes 3 intentos")


def jugar():
    intentos = 0

    print("Bienvenido a Adivina el Numero")
    while True:
        try:
            dificultad = int(input("Introduca número para elegir dificultad: \n 1-Fácil \n 2-Medio \n 3-Difícil"))
            break
        except ValueError:
            print("No ha introducido un número, introduce un número")
    if dificultad == 1:
        numero_aleatorio = random.randint(1, 10)
    else:
        numero_aleatorio = random.randint(1, 40)
    # print("Estoy pensando un número del 1 al 10")
    rango_dificultad(dificultad)
    # print(rango_dificultad)
    print("Adivinia cual es")
    # print("Solamente tiene 5 intentos")
    num_intentos(dificultad)
    # print(mensaje(num_intentos))
    if dificultad == 1 or dificultad == 2:
        vidas = 5
    else:
        vidas = 3
    while intentos < vidas:
        try:
            adivinanza = int(input("El numero es: "))
        except ValueError:
            print("Ese no es un número válido")
        else:
            if adivinanza == numero_aleatorio:
                print("Adivinaste en "+ str(intentos+1) + " intentos.")
                jugar_nuevamente = input("Quieres juagar de nuevo? si/no: ")
                if jugar_nuevamente.lower() == "si":
                    jugar()
                else:
                    print("Fin del juego.")
                break

            elif adivinanza > numero_aleatorio:
                print("Fallaste, el número es menor")
            else:
                print("Fallaste, el número es mayor")

            intentos += 1
            print("Intento {}/{}".format(intentos,vidas))
    else:
        print("Se te acabaron los intentos")
        print("Gracias por jugar")
        print()
        jugar_nuevamente= input("Quieres juagar de nuevo? si/no: ")
        if jugar_nuevamente.lower() == "si":
            jugar()
        else:
            print("Fin del juego.")

jugar()