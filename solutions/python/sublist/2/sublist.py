"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_sub(short_list, long_list):
    """Indica si  short_list aparece como bloque contiguo dentro de `grande`."""
    size_sublist = len(short_list)
    search_range = len(long_list) - size_sublist + 1
    
    if size_sublist == 0:
        return True
    return any(long_list[i:i + size_sublist] == short_list for i in                                    range(search_range))    
      
    
def sublist(list_one, list_two):
    """Clasifica la relación entre dos listas: igual, sublista, superlista o distintas.
        Args:
            list_one, list_two (list): Listas a comparar
        Returns:
            int: Una de las constantes del módulo:
                EQUAL si ambas listas son iguales;
                SUBLIST si list_one aparece contigua dentro de list_two;
                SUPERLIST si list_two aparece contigua dentro de list_one;
                UNEQUAL en cualquier otro caso.
    """
    if list_one == list_two:
        return EQUAL
    if is_sub(list_one,list_two):
        return SUBLIST
    if is_sub(list_two,list_one):
        return SUPERLIST
    return UNEQUAL
    
