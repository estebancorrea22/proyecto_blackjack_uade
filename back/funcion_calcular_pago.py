def calcular_pago(resultado, apuesta, blackjack=False, seguro_apostado=0, crupier_tiene_blackjack=False):
    total_ganado = 0

    if resultado == 'victoria':
        total_ganado = apuesta
    elif resultado == 'blackjack':
        total_ganado = int(apuesta * 1.5)
    elif resultado == 'empate':
        total_ganado = 0
    elif resultado == 'derrota':
        total_ganado = -apuesta

    if seguro_apostado > 0:
        if crupier_tiene_blackjack:
            total_ganado += seguro_apostado * 2
        else:
            total_ganado -= seguro_apostado

    return total_ganado
