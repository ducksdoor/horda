class Heroe:
    def __init__(self, nombre, puntos_vida, puntos_ataque, puntos_defensa):
        self.nombre = nombre
        self.puntos_vida = puntos_vida
        self.puntos_ataque = puntos_ataque
        self.puntos_defensa = puntos_defensa

    def esta_vivo(self):
        return self.puntos_vida > 0

    def __str__(self):
        return f"Nombre: {self.nombre}\nPuntos de Vida: {self.puntos_vida}\nPuntos de Ataque: {self.puntos_ataque}\nPuntos de Defensa: {self.puntos_defensa}"


def crear_heroe(nombre):
    nombre = nombre
    jugador = Heroe(nombre, 100, 20, 10)
    return(jugador)