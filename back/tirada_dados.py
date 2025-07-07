import random

sumar_dados = lambda dados: sum(dados) + 10 if (1 in dados and sum(dados) + 10 <= 21) else sum(dados)

def tirar_dado(veces=1):
    """
    Lanza un dado de 10 caras (D10) una cantidad de veces determinada.
    Parámetros: veces (int): Cantidad de dados a lanzar. Por defecto es 1.
    Retorna: list: Lista con los resultados obtenidos en cada tirada.
    """
    try:
        return [random.randint(1, 10) for i in range(veces)]
    except Exception as e:
        print(f"Error al tirar el dado: {e}")
        return []

def evaluar_mano(mano):
    """
    Evalúa el estado actual de la mano: si se pasó, logró blackjack o sigue jugando.
    Parámetros: mano (list): Lista de dados tirados.
    Retorna: tuple: (estado, total)
            estado: 'pasado', 'blackjack', 'jugando'
            total: suma de la mano según las reglas del juego
    """
    total = sumar_dados(mano)
    if total > 21:
        return "pasado", total
    if total == 21:
        return ("blackjack" if len(mano) == 2 else "jugando"), total
    return "jugando", total