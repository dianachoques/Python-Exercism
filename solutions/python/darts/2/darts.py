"""Devuelve el puntaje del jugador segun la region donde cayo el dardo"""
def score(x, y):
    """Devuelve el puntaje segun las coordenadas del dardo
    Args:
        x, y (int): Coordenadas a procesar
    Returns:
        int: Puntaje segun el circulo donde se encuentra las coordenadas
    """
    distancia = (x ** 2 + y ** 2) ** 0.5

    if distancia > 10:
        return 0
    if distancia > 5:
        return 1
    if distancia > 1:
        return 5
    return 10
    
