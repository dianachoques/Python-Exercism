"""Módulo que devuelve el número de pasos de la Conjetura de Collatz."""
def steps(number):
    """
    Devuelve el número de pasos que necesita un número para llegar a 1.
    Args:
        number (int): entero positivo a procesar con la conjetura de Collatz.
    Returns:
        int: número de iteraciones necesarias para llegar a 1.
    Raises:
        ValueError: si number no es un entero positivo.
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed") 
    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = (number * 3) +1
            
        count += 1
        
    return count