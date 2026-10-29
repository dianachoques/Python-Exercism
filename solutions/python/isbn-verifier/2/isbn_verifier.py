"""Evalua si el texto es un ISBN-10 válido."""
DIGITOS = "0123456789"

def is_valid(isbn):
    """Indica si el texto es un ISBN-10 válido.
        Ignora los guiones en el texto
        Args:
            isbn(str): texto a evaluar:
        Return:
            bool: True si cumple con la formula del ISBN-10,
            False en caso contrario.
    """
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    body, control = isbn[:9], isbn[9]
    if not all(char in DIGITOS for char in body):
        return False
    if control in DIGITOS:
        values = [int(char) for char in body] + [int(control)]
    elif control == "X":
        values = [int(char) for char in body] + [10]
    else:
        return False

    return  sum(value * weight for value, weight  in zip(values, range(10,0,-1))) % 11 == 0
 
    
