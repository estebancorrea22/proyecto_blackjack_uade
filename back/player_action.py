from dice_logic import roll_dice, sum_dice

def roll_another_die(hand):
    """
    El jugador o crupier lanza un dado adicional y actualiza su mano.
    Parámetros: hand (list): Mano actual de dados.
    Retorna: tuple: (mano_actualizada, total_tras_tirada, estado)
            estado: 'bust' si el total supera 21, de lo contrario 'continue'
    """
    try:
        new_die = roll_dice(1)[0]
        hand.append(new_die)
        total = sum_dice(hand)
        status = "bust" if total > 21 else "continue"
        return hand, total, status
    except Exception as e:
        print(f"Error rolling dice: {e}")
        return hand, sum_dice(hand), "error"

def double_bet(hand, current_bet):
    """
    El jugador decide duplicar la apuesta y lanzar un dado adicional.
    El crupier debe aceptar la apuesta automáticamente.
    Parámetros: hand (list): Mano actual de dados.
        current_bet (int o float): Monto actual apostado.
    Retorna:tuple: (mano_actualizada, nueva_apuesta, total_tras_tirada, estado)
            estado: 'bust' si el total supera 21, de lo contrario 'continue'
    """
    try:
        new_bet = current_bet * 2
        new_die = roll_dice(1)[0]
        hand.append(new_die)
        total = sum_dice(hand)
        status = "bust" if total > 21 else "continue"
        return hand, new_bet, total, status
    except Exception as e:
        print(f"Error doubling bet: {e}")
        return hand, current_bet, sum_dice(hand), "error"

def stand(hand):
    """
    El jugador o crupier decide plantarse (no tirar más dados).
    Parámetros: hand (list): Mano actual de dados.
    Retorna: tuple: (mano, total, 'stand')
    """
    total = sum_dice(hand)
    return hand, total, "stand"