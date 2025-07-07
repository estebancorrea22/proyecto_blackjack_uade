def calcular_pago(resultado, apuesta, usuario, api=False, saldo=0):
    """Calcula el pago basado en el resultado del juego y la apuesta realizada. 
        Parametros:
        resultado (str): Resultado del juego ('victoria', 'blackjack', 'empate', 'derrota').
        apuesta (int): Monto apostado por el jugador.
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
        if api == True:
            return -min(apuesta, saldo)
        return -min(apuesta, usuario['saldo'])

    return total_ganado
