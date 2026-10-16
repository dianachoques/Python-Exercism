"""Modulo que devuelve el valor de una resitencia segun el color"""
COLORS=["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey",
            "white"]
def value(colors):
    value = int(COLORS.index(colors[0]))*10 + int(COLORS.index(colors[1]))
    return value
