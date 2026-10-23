"""Módulo que convierte números en sonidos de lluvia."""

SOUNDS= ((3,'Pling'), ( 5,'Plang'), (7,'Plong'))
def convert(number):
    """
    Convierte un entero en su "sonido de lluvia".
    Args: 
        number (int): Número a procesar.
    Returns:
        str: Concatenacion en este orden:
             'Pling' (divisible entre 3)
             'Plang' (divisible entre 5)
             'Plong' (divisible entre 7)
             Si no es divisible entre ninguno, devuelve el número como cadena.
    """
    sound_rain=''.join(sonido for factor,sonido in SOUNDS if number % factor == 0) 
        
    return sound_rain or str(number)
