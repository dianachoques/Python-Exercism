"""Módulo que evalúa si un triangulo es equilátero, isósceles o escaleno."""

def is_triangle(sides):
    """Devuelve True  si los lados son de un triangulo, False si no."""
    side1, side2, side3 = sides
    return ( min(sides)>0
           and side1 + side2 >= side3
           and side2 + side3 >= side1
           and side1 + side3 >= side2)
    
def equilateral(sides):
    """
        Devuelve True si los tres lados son iguales.
        Args:
            sides(list): lista con los tres lados del triángulo.
        Returns:
            bool: True si es un triángulo equilatero, False si no.
    """
    
    return (is_triangle(sides) and len(set(sides))==1)
    
def isosceles(sides):
    """ 
        Devuelve True si al menos dos lados son iguales.
        Args:
            sides(list): lista con los tres lados del triángulo.
        Returns:
            bool: True si es un triángulo isósceles, False si no.
    """
     
    return (is_triangle(sides) and len(set(sides)) <= 2)
         


def scalene(sides):
    """ 
        Devuelve True si los tres lados son distintos.
        Args:
            sides(list): lista con los tres lados del triángulo.
        Returns:
            bool: True si es un triángulo escaleno, False si no.
    """
     
    return (is_triangle(sides) and len(set(sides)) == 3)
