"""Modulo que traduce un texto a lenguaje Pig Latin"""
VOWELS='aeiou'

def _split_index(word):
    """Devuelve el índice donde termina el prefijo consonántico."""
    for i, char in enumerate(word):
        if char in VOWELS or (char == 'y' and i > 0):
            if char == 'u' and  i > 0 and word[i - 1] == 'q':
                return i + 1
            return i
    return len(word)

def translate_word(word):
    """Devuelve la palabra reconstruida"""
    if word.startswith(('xr', 'yt')):
        return word + 'ay'
    i = _split_index(word)
    return word[i:] + word[:i] + 'ay'

def translate(text):
    """Devuelve el texto reconstruido"""
    return ' '.join(translate_word(word) for word in text.split())

        
