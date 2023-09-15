from os import system
from escribir import *

def ft_menu_estadisticas(nombre):
    system("cls")
    print("*" * 21 + "Estadisticas" + "*" * 21)
    print("*" + " " * 52 + "*")
    print("*" + " " * 21 + f"  {nombre}" + " " * 19 + "*")
    print("*" + " " * 52 + "*")
    print("*" + " " * 20 + "Nivel" + " " * 27 + "*")
    print("*" + " " * 20 + "Experiencia" + " " * 21 + "*")
    print("*" + " " * 20 + "vida" + " " * 28 + "*")
    print("*" + " " * 20 + "Ataque" + " " * 26 + "*")
    print("*" + " " * 20 + "Defensa" + " " * 25 + "*")
    print("*" + " " * 52 + "*")
    print("*" + " " * 19 + "[0] - volver" + " " * 21 + "*")
    print("*" * 21 + "Estadisticas" + "*" * 21)
    accion = input()
    if accion == "0":
        return
    else:
        print_yellow("no te entiendo, ¡seguro que puedes indicarmelo mejor!")
        accion = input("")
        ft_menu_estadisticas(nombre)
def ft_menu_principal(nombre):
    system("cls")
    print("*" * 20 + "MENU PRINCIPAL" + "*" * 20)
    print("*" + " " * 12 + "[1]  - Nuevo combate" + " " * 20 + "*")
    print("*" + " " * 12 + "[2]  - Estadisticas" + " " * 21 + "*")
    print("*" + " " * 12 + "[3]  - Tienda" + " " * 27 + "*")
    print("*" + " " * 12 + "[4]  - Objetos" + " " * 26 + "*")
    print("*" + " " * 12 + "[42] - Salir del juego" + " " * 18 + "*")
    print("*" * 20 + "MENU PRINCIPAL" + "*" * 20)
    turno = input()

    if turno == "1":
        print_yellow("Los enemigos aun no llegan, habla con Lucas para saber mas")
        nada = input("")
        return
    elif turno == "2":
        ft_menu_estadisticas(nombre)
        return
    elif turno == "3":
        print_yellow("La tienda esta cerrada... Vuelve mas tarde")
        nada = input("")
        return
    elif turno == "4":
        print_yellow("Mira a tu alrededor, eso es todo lo que tienes, no leas tanto y sal a jugar a la calle...")
        nada = input("")
        return
    elif turno == "42":
        return(42)
    else:
        print_yellow("no te entiendo, ¡seguro que puedes indicarmelo mejor!")
        nada = input("")
        return

