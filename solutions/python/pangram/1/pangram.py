"""Modulo para determinar si un texto es un PANGRAMA"""

ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
ALFABETO =frozenset(ALFABETO)

def is_pangram(sentence):
    """Indica si el texto contiene todas las letras del alfabeto inglés.
        Args:
            sentence (str): texto para evaluar.
        Returns: 
            bool: True si cada letra de la a a la z aparece al menos una vez;
            False en caso contrario.
        """
    return ALFABETO.issubset(sentence.lower())
