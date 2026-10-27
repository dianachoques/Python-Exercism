"""Modulo para determinar si un texto es un PANGRAMA"""

ALFABET = frozenset('abcdefghijklmnopqrstuvwxyz')

def is_pangram(sentence):
    """Indica si el texto contiene todas las letras del alfabeto inglés.
        Args:
            sentence (str): texto para evaluar.
        Returns: 
            bool: True si cada letra de la a a la z aparece al menos una vez;
            False en caso contrario.
        """
    return ALFABET.issubset(sentence.lower())
