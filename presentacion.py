from escribir import *
from os import system
from quejas import *

def ft_start(x):
    presentacion = True
    while presentacion == True:
        #print(x)
        if x < 10:
            print_green("Bienvenido a esta nueva partida.")
        if x > 10:
            print_red("¿No crees que te he preguntado el nombre muchas veces...? lo intentare otra vez..")
        print_green("¿como te llamas?")
        nombre = input("")
        if nombre =="":
            x+=3
            if x < 10:
                print_red("Eres mudo?")
            if x > 10:
                print_red("No eres mudo. Esta claro que te falta verano o te sobra tiempo")
            continue

        if (len(nombre) >= 10):
            x+=1
            print_red("PERO QUE TE HAS CREIDO! LOS NOMBRES TAN LARGOS ROMPEN LAS BUENAS FORMAS DE LOS JUEGOS! ")
            ft_estandar(x)
            continue
        if x > 10:
            print_green(f"pues {nombre}, no me gusta tu nombre, pero no todo el mundo puede tener un nombre tan guay como el mio...")
        if x < 10:
            print_green(f"Encantadisimo de conocer {nombre}")
        print_yellow("SE BIENVENIDO A LA ONIONQUEST! una aventura con muchas capas, un olor extraño y que por supuesto. Te va a hacer llorar!")
        buliano = "no"
        while (buliano != "si"):
            print_yellow("Si estas preparado puedes escribir si. Sin embargo, si quieres volver a hablar conmigo puedes escribir no")
            buliano = input(" ")
            if buliano == "si":
                return(nombre)
            if buliano == "no":
                x+=2
                ft_estandar(x)
                break
            else:
                #to do --- que esto no empiece desde el priincipi
                if x < 20:
                    print_blue("No te he entendido la verdad...")
                if x > 20:
                    print_red("Dios mio. Aqui tambien vas a molestarme... Porfavor escribe 'si' y empieza a jugar... te lo suplico")
                continue