from escribir import *
from os import system
from quejas import *
from decoradores import ft_nombre_espacio
from presentacion import ft_start
from menu import ft_menu_principal
nombre = ""
x = 0
juego = 0
game = True
while game == True:
    if juego == 0:
        nombre = ft_start(x)
        nombre = ft_nombre_espacio(nombre)
        juego+=1
    else:
        juego = ft_menu_principal(nombre)
    if juego == 42:
        system("cls")
        print_blue("GRACIAS POR JUGAR!")
        game = False
    #subprocess.run("clear")
