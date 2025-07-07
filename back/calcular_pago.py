def calcular_pago(resultado, apuesta, usuario, blackjack=False, seguro_apostado=0, crupier_tiene_blackjack=False):
    """Calcula el pago basado en el resultado del juego y la apuesta realizada. 
        Parametros:
        resultado (str): Resultado del juego ('victoria', 'blackjack', 'empate', 'derrota').
        apuesta (int): Monto apostado por el jugador.
        blackjack (bool): Indica si el jugador tiene blackjack.
        seguro_apostado (int): Monto apostado en el seguro.
        crupier_tiene_blackjack (bool): Indica si el crupier tiene blackjack.
    Retorna: 
        int: Monto total ganado o perdido por el jugador.
    """
    total_ganado = 0

    if resultado == 'victoria':
        total_ganado = apuesta
    elif resultado == 'blackjack':
        total_ganado = int(apuesta * 1.5)
    elif resultado == 'empate':
        total_ganado = 0
    elif resultado == 'derrota':
        return -min(apuesta, usuario['saldo'])
    if seguro_apostado > 0:
        if crupier_tiene_blackjack:
            total_ganado += seguro_apostado * 2
        else:
            total_ganado -= seguro_apostado

    return total_ganado
