
from decoradores import ft_nombre_espacio
from escribir import *
from heroe import *

#combate
def write_combate_menu(jugador):
    print("*" * 23 + "Combate" + "*" * 24)
    #print_blue("*" + " " * 21 + f"  {jugador.pun}" + " " * 19 + "*")
    print("*" + " " * 19 + "[1] - Atacar" + " " * 21 + "*")
    print("*" + " " * 19 + "[9] - Nuevo enemigo" + " " * 14 + "*")
    print("*" + " " * 52 + "*")
    print("*" + " " * 19 + "[0] - volver" + " " * 21 + "*")
    print("*" * 23 + "Combate" + "*" * 24)
    print("\n")
    print(jugador)
def print_enemigo(enemigo, x):
    if x == 1:
        print_red("Tu enemigo es:")
    if x == 2:
        print_red("Tu  nuevo enemigo es:")
    print(enemigo)
    print("\n")

def write_estadistica_menu(jugador):
    nombre = ft_nombre_espacio(jugador.nombre)
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