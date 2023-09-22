from random import *
from escribir import *

def atacar(enemigo):
    x = randint(1, 6)
    x = x*10
    x = x - enemigo.puntos_defensa
    enemigo.puntos_vida = enemigo.puntos_vida - (x)
    print_green(f"has causado {x} puntos de daño")
    print("\n")

