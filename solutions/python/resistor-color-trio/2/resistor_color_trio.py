"""Modulo con una funcion que calcula el valor de la resistencia"""
colores=['black','brown','red','orange','yellow','green','blue','violet','grey','white']

def label(colors):
    """Calcula el valor de la resistencia basado en el codigo de colores
    Args :  
        colors (str): secuencia de string de los colores ("brown", "black", "red")
    returns :
        str : El valor de la resistencia con su unidad ("33 ohms" o "33 kiloohms")
    """
    valor = f'{colores.index(colors[0])}{colores.index(colors[1])}'
    valor_duo=int(valor)
    valor_completo = valor_duo * (10**int(colores.index(colors[2])))
    if 1000 <= valor_completo < 1000000:
        return f'{valor_completo//1000} kiloohms'
    if 1000000 <= valor_completo < 1000000000:
        return f'{valor_completo//1000000} megaohms'
    if  valor_completo>=1000000000:
        return f'{valor_completo//1000000000} gigaohms'
    return f'{valor_completo} ohms'
    
