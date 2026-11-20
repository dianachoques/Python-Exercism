"""Convierte los dígitos de un número entre dos bases."""
def rebase(input_base, digits, output_base):
    """ Convierte una lista de dígitos de una base a otra
        Args:
            input_base (int): Base de los dígitos de entrada.
            digits (list[int]): Digitos del numero.
            output_base: Base de los dígitos de salida.
            
        Returns:
            list[int]: : Dígitos convertidos a la base output_base
            
        Raises:
            ValueError: Si alguna base es menor que 2 o si algún dígito no
            cumple 0 <= d < input_base.
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    valor = sum(digit * (input_base ** index) 
                        for index, digit in enumerate(reversed(digits)))
    if valor == 0:
        return [0]
    digits_output = []
    
    while valor:
        valor, residuo = divmod(valor, output_base)
        digits_output.append(residuo)

    digits_output.reverse()
    return digits_output
        
        
    
