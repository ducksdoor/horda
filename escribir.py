from os import system


def print_red(text):
    # Secuencia de escape ANSI para color de texto rojo
    red_text = f"\033[91m{text}\033[0m"
    print(red_text)

def print_green(text):
    # Secuencia de escape ANSI para color de texto verde
    green_text = f"\033[92m{text}\033[0m"
    print(green_text)

def print_yellow(text):
    # Secuencia de escape ANSI para color de texto amarillo
    yellow_text = f"\033[93m{text}\033[0m"
    print(yellow_text)

def print_blue(text):
    # Secuencia de escape ANSI para color de texto azul
    blue_text = f"\033[94m{text}\033[0m"
    print(blue_text)

def limpiar():
    system("clear")
    #system("cls")

