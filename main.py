from escribir import *
from os import system
from quejas import *
from presentacion import ft_start
from menu import ft_menu_principal
from heroe import *

from heroe import Heroe

if __name__ == "__main__":
    nombre = ""
    x = 0
    juego = 0
    game = True
    while game == True:
        if juego == 0:
            nombre = ft_start(x)
            juego+=1
        jugador = crear_heroe(nombre)

        if juego != 0:
            juego = ft_menu_principal(jugador)
        if juego == 42:
            #system("clr")
            system("clear")
            print(jugador)
            print_blue("GRACIAS POR JUGAR!")
            game = False
    #subprocess.run("clear")
