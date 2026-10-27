"""Determina si un texto es un Isograma"""
def is_isogram(phrase):
    """
    Indica si el texto no tiene letras repetidas,
    No distingue mayúsculas de minúsculas e ignora espacios y guiones.
    
    Args:
         phrase(str): Texto a evaluar
    Returns:
         bool: True si el texto no tiene letras repetidas, False en caso contrario.
    """
    cleaned_up_phrase = phrase.replace(' ','').replace('-','')
    phrase_lowercase = cleaned_up_phrase.lower()
    return len(set(phrase_lowercase)) == len(phrase_lowercase)
