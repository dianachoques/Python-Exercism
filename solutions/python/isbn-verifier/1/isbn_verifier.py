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
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    cuerpo, control = isbn[:9], isbn[9]
    if not all(c in DIGITOS for c in cuerpo):
        return False
    if control in DIGITOS:
        valores = [int(c) for c in cuerpo] + [int(control)]
    elif control == "X":
        valores = [int(c) for c in cuerpo] + [10]
    else:
        return False

    return  sum(valor * peso for valor, peso  in zip(valores, range(10,0,-1))) % 11 == 0
 
    
