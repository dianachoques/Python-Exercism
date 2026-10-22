"""Módulo  para obtener respuestas de Bob ante distintas entradas de texto"""
  
def response(hey_bob):
    """
    Devuelve una resuepa predeterminada de Bob segun el patron de texto
    Arg:
        hey_bob (str): pregunta o texto paraBob
    Returns:
        srt: Respuesta segun el patron del texto
            "Sure."                             : para texto que terminen en ?
            "Whoa, chill out!"                  : Para texto en mayusculas
            "Calm down, I know what I'm doing!" : para texto en mayusculas que terminen en ?
            "Fine. Be that way!"                : Para un texto  vacio.
            "Whatever."                         : para cualquier otro texto
    """
    hey_bob = hey_bob.strip()
    is_question = hey_bob.endswith("?")
    is_shout = hey_bob.isupper()
    
    if  not hey_bob:
        return "Fine. Be that way!"
    if is_question and is_shout:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_shout:
        return  "Whoa, chill out!"
    return  "Whatever."
    
