import random

def sumar_dados(mano):
    """ 
    Calcula el total optimizando el valor del As (1)
    parametros: mano (list): Lista de dados tirados.
    Retorna: int: Suma total de la mano, considerando Ases como 11 o 1 según sea necesario."""
    total = 0
    num_ases = 0
    
    for dado in mano:
        if dado == 1:  # Es un As
            total += 11
            num_ases += 1
        else:
            total += dado
    
    # Ajustar Ases de 11 a 1 si nos pasamos de 21
    while total > 21 and num_ases > 0:
        total -= 10  # Cambiamos un As de 11 a 1
        num_ases -= 1
    
    return total

def tirar_dado(veces=1):
    """Lanza un dado de 10 caras (valores 1-10)
    parametros: veces (int): Cantidad de dados a lanzar. Por defecto es 1.
    Retorna: list: Lista con los resultados obtenidos en cada tirada."""
    
    return [random.randint(1, 10) for _ in range(veces)]

def evaluar_mano(mano):
    """
    Evalúa el estado de la mano:
    - 'blackjack': 21 exacto con 2 cartas (un 10 y un As)
    - 'pasado': > 21
    - 'jugando': cualquier otro caso
    parametros: mano (list): Lista de dados tirados.
    Retorna: tupla: (estado, total)
    """
    total = sumar_dados(mano)
    
    if total > 21:
        return "pasado", total
    elif total == 21 and len(mano) == 2:
        return "blackjack", total
    else:
        return "jugando", total




