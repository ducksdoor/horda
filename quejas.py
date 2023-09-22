from escribir import *
from os import system

def ft_estandar(x):
    if x < 3 and x > 12:
        print_red("¡CEBOLLA MIA! NO PUEDES SER TAAAN MALO PULSANDO TECLAS.")
    elif x > 3:
        print_red("Eres un poco pesadito...")

    print_blue("pulsa enter y empieza otra vez anda...")
    input(" ")
    #system("cls")
    system("clear")
