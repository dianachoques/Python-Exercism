"""Funcion que devuelve True o false si es un Año bisiesto"""
def leap_year(year):
    """
    parametros (int):
        year: el año que sera evaluado
    resultado (bool):
         True o False
    """
    if year%4==0:
        if year%100==0:
            return year%400==0
        return True
    return False
        
