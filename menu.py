from os import system
from generador_enemigos import *
from decoradores import ft_nombre_espacio
from acciones_de_combate import *
from carpeta_menu import texto_menu
from heroe import *
def ft_combate(jugador, enemigo):

    system("clear")
    #system("cls")
    texto_menu.write_combate_menu(jugador)
    texto_menu.print_enemigo(enemigo, 1)
    accion = input("Puedes elegir que hacer\n")
    ciclo = True
    while (ciclo == True):
        if accion == "1":
            system("clear")
            texto_menu.write_combate_menu(jugador)
            atacar(enemigo)
            texto_menu.print_enemigo(enemigo, 1)
            accion = input("")
        elif (accion == "9"):
            if (enemigo.puntos_vida <= 0):
                system("clear")
                texto_menu.write_combate_menu(jugador)
                del enemigo
                enemigo = crear_enemigo()
                texto_menu.print_enemigo(enemigo, 2)
                accion = input("")
            elif (enemigo.puntos_vida > 0):
                print_red("Hay un enemigo en la arena. No puedes llamar a mas")
                accion = input("")

        elif accion == "0":
            if (enemigo.puntos_vida > 0):
                print_red("No puedes ir al menu principal si hay enemigos...")
                accion = input("")
            else:
                ft_menu_principal(jugador)
        else:
            print_yellow("no te entiendo, ¡seguro que puedes indicarmelo mejor!")
            accion = input("")
    return
def ft_menu_estadisticas(jugador):

    system("clear")
    #system("cls")
    texto_menu.write_estadistica_menu(jugador)
    accion = input()
    bucle = True
    while (bucle == True):
        if accion == "0":
            return
        else:
            limpiar()
            texto_menu.write_estadistica_menu(jugador)
            print_yellow("\nNo te entiendo, ¡seguro que puedes indicarmelo mejor!")
            accion = input("")
def ft_menu_principal(jugador):
    system("clear")
    # system("cls")
    print("*" * 20 + "MENU PRINCIPAL" + "*" * 20)
    print("*" + " " * 12 + "[1]  - Nuevo combate" + " " * 20 + "*")
    print("*" + " " * 12 + "[2]  - Estadisticas" + " " * 21 + "*")
    print("*" + " " * 12 + "[3]  - Tienda" + " " * 27 + "*")
    print("*" + " " * 12 + "[4]  - Objetos" + " " * 26 + "*")
    print("*" + " " * 12 + "[42] - Salir del juego" + " " * 18 + "*")
    print("*" * 20 + "MENU PRINCIPAL" + "*" * 20)
    turno = input()

    if turno == "1":
        enemigo = crear_enemigo()
        ft_combate(jugador, enemigo)
        nada = input("")
        return
    elif turno == "2":
        ft_menu_estadisticas(jugador)
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

