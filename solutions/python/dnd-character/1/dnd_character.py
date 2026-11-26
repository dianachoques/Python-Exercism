import random

class Character:
    """Personaje de D&D con habilidades generadas al azar
    Attributes:
        strength, dexterity, constitution,
        intelligence, wisdom, charisma (int): Puntaje de cada habilidad (3 - 18)
        hitpoints (int): Puntaje de cada habilidad (10 - modificador de constitucion)

    """
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution =  self.ability()
        self.intelligence =  self.ability()
        self.wisdom =  self.ability()
        self.charisma =  self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        """Genera el puntaje de una habilidad
        Lanza 4 dados de 6 lados, descarta el menor y suma los tres restantes.
        Returns:
            int: Puntaje entre 3 y 18
        """
        resultados = []
        for i in range(4):
            resultados.append(random.randint(1, 6))
        resultados.remove(min(resultados))
        return sum(resultados)

def modifier(value):
    """Calcula el modificador de una habilidade
    Args:
        value (int): Valor de la constitucion
    Returns:
        int: Modificador de la constitucion
    """
    return (value - 10)//2
