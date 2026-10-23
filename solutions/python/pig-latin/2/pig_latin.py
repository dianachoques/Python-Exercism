"""Modulo que traduce un texto a lenguaje Pig Latin"""
VOWELS='aeiou'

def _split_index(word):
    """Devuelve el índice donde termina el prefijo consonántico."""
    for index, char in enumerate(word):
        if char in VOWELS or (char == 'y' and index > 0):
            if char == 'u' and  index > 0 and word[index - 1] == 'q':
                return index + 1
            return index
    return len(word)

def translate_word(word):
    """Devuelve la palabra reconstruida"""
    if word.startswith(('xr', 'yt')):
        return word + 'ay'
    index = _split_index(word)
    return word[index:] + word[:index] + 'ay'

def translate(text):
    """Devuelve el texto reconstruido"""
    return ' '.join(translate_word(word) for word in text.split())

        
