from random import choice
class Enemigo:
    def __init__(self, nombre, puntos_vida, puntos_ataque, puntos_defensa):
        self.nombre = nombre
        self.puntos_vida = puntos_vida
        self.puntos_ataque = puntos_ataque
        self.puntos_defensa = puntos_defensa

    def esta_vivo(self):
        return self.puntos_vida > 0

    def __str__(self):
        return f"Nombre: {self.nombre}\nPuntos de Vida: {self.puntos_vida}\nPuntos de Ataque: {self.puntos_ataque}\nPuntos de Defensa: {self.puntos_defensa}"


posibles_nombres = ["Patata Rancia", "Queso apestoso", "Cabra que tira piedras mientras escalas", "Persona que sonrie demasiado",
           "Hombre lobo en Paris", "Helado de chocolate y menta", "Pirata sin piernas", "Toxicomano que necesita dinero"]
def crear_enemigo():
    nombre = choice(posibles_nombres)
    enemigo = Enemigo(f"{nombre}", 100, 20, 10)
    return(enemigo)