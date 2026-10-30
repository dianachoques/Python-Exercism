"""Cifrado de rotación César sobre el alfabeto inglés."""

TAMANO_ALFABETO = 26
def _rotar_letra(letra, base, key):
    """Devuelve una letra rotada"""
    posicion = ord(letra) - ord(base)
    return chr(ord(base) + (posicion + key) % TAMANO_ALFABETO )

def rotate(text, key):
    """Rota cada letra ASCII del texto key posiciones en el alfabeto.
    Arg:
        text (str) : Texto a procesar
        key  (int) : numero de rotacion
    Returns:
        (str) : Devuelve el texto cifrado, conserva mayúsculas y minúsculas; deja                       intactos los demás caracteres.
    """
    texto_cifrado = []
    for char in text:
        if "a" <= char <= "z":
            texto_cifrado.append(_rotar_letra(char, "a", key))
        elif "A" <= char <= "Z":
            texto_cifrado.append(_rotar_letra(char, "A", key))
        else:
            texto_cifrado.append(char)
            
    return "".join(texto_cifrado)
