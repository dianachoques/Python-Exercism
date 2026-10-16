"""Modulo que devuelve el valor de una resitencia segun el color"""

RESISTOR_COLORS=["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey",
            "white"]
def value(colors):
    value = int(RESISTOR_COLORS.index(colors[0]))*10 + int(RESISTOR_COLORS.index(colors[1]))
    return value
