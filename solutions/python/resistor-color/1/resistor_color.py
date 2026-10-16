def color_code(color):
    """Devuelve el valor de resistencia segun los colores
        Args:
           color(str): color de la franja
        Returns:
            int: Valor de la resistencia
    """
    resistor_colors=colors()
    return resistor_colors.index(color)


def colors():
    """Devuelve una lista de los colores que tienen una resistencia"""
    
    colors=["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey",
            "white"]
    return colors
