"""Validación de números con el algoritmo Luhn."""

DIGITOS = frozenset("0123456789")

class Luhn:
    """Valida un número de tarjeta con el algoritmo de Luhn."""
    def __init__(self, card_num:str):
        self.card_num = card_num

    def valid(self):
        """Indica si el número cumple el algoritmo de Luhn.
             Solo permite caracteres que sean dígitos y espacios.
             Si tiene un dígito o menos es inválido
        Returns:
            bool: True si la suma de dígitos es múltiplo de 10;
                False en caso contrario

        """
        digitos = self.card_num.replace(" ", "")
        if len(digitos) <= 1 or not DIGITOS.issuperset(digitos):
            return False
        suma = 0
        for indice, caracter in enumerate(reversed(digitos)):
            numero = int(caracter)
            if indice % 2 :
                numero *= 2
                if numero > 9:
                    numero -= 9
            suma += numero

        return suma % 10 == 0
