"""Modulo que evalua si los corchetes, las llaves y los paréntesis de un texto están equilibrados"""
PAIRS={']':'[','}':'{',')':'('}

def is_paired(input_string):
    """Indica si los delimitadores del texto están emparejados y bien anidados.
     
    Args:
        input_string (str): Texto a evaluar.
    Returns:
        bool: True si todos los delimitadores están emparejados y anidados
            correctamente; False en caso contrario.
    """
    stack = []
    opening_chars = frozenset(PAIRS.values())
    for char in input_string:
        if char in opening_chars:
            stack.append(char)
        elif char in PAIRS:
            if not stack or PAIRS[char] != stack.pop():
                return False
                
    return not stack
