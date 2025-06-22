import random

sum_dice= lambda dice: sum(dice)+ 10 if (1 in dice and sum(dice) + 10 <= 21 ) else sum(dice)

def roll_dice(times=1):
    """
    Lanza un dado de 10 caras (D10) una cantidad de veces determinada.
    Parámetros: times (int): Cantidad de dados a lanzar. Por defecto es 1.
    Retorna: list: Una lista con los resultados obtenidos en cada tirada.
    """
    try:
        return [random.randint(1, 10) for i in range(times)]
    except Exception as e:
        print(f"Error rolling dice: {e}")
        return []
