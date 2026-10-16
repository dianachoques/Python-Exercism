"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2
def bake_time_remaining(elapsed_bake_time):
    """Calcular el tiempo restante de preparación.
    
    Parámetros:
        elapsed_bake_time (int): El número de minutos ya transcurridos.
        
    Devuelve:
        int: Tiempo total restante.  
    """
    tiempo_restante=EXPECTED_BAKE_TIME-elapsed_bake_time
    return tiempo_restante

def preparation_time_in_minutes(number_of_layers):
    """Calcula el tiempo de preparación según el número de capas que tenga la receta
    
    Parámetros:
        número_de_capas (int): El número de capas de la lasaña.
    
    Devuelve:
        int: El tiempo total transcurrido (en minutos) por cada capa.
    """
    tiempo_preparacion=number_of_layers*PREPARATION_TIME
    return tiempo_preparacion

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calcula el tiempo de cocción transcurrido.
    
    Parámetros:
        número_de_capas (int): El número de capas de la lasaña.
        tiempo_de_horneado_transcurrido (int): Tiempo que la lasaña lleva horneándose en el horno.
    
    Devuelve:
        int: El tiempo total transcurrido (en minutos) entre la preparación y el horneado.   
    """
    total_minutos=preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
    return total_minutos
