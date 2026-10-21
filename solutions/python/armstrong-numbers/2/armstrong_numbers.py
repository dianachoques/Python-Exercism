"""Modulo para determinar si un numero es Armstrong"""
def is_armstrong_number(number):
    """Devuelve True or False si number es o no un numero Armstrong
    Args:
        number(int): numero a ser evaluado
    Returns:
        (Booleano): True si es Armstrong y False si no
    """
    numero = list(str(number))
    suma=0
    for digito in numero:
        suma+=(int(digito))**(len(numero))

    return number == suma
