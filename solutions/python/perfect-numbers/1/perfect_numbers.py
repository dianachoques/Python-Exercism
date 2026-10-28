"""Clasifica un entero positivo como perfecto, abundante o deficiente."""
from math import isqrt

def sum_factores(number):
    """Devuelve la suma de los factores de un numero"""
    suma = 0
    for digit in range(1, isqrt(number) + 1 ):
        if number % digit == 0:
            suma += digit
            par = number // digit
            if par != digit:
                suma += par

    return suma - number


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int):
        raise TypeError("El número debe ser un tipo de dato entero (int).")
        
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
        
    suma_factores = sum_factores(number)
    if suma_factores == number:
        return "perfect"
    if suma_factores > number:
        return "abundant"
    return "deficient"
