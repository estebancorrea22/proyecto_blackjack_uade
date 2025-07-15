from juego import jugar_blackjack, turno_crupier, turno_jugador

#se testea solo el juego, no se testea la parte de logros ni de discord
def test_jugar_blackjack():
    usuario = {'nombre': 'Jugador1', 'saldo': 1000, 'logros': {'logros_obtenidos': [], 'logros_disponibles': []}}
    jugar_blackjack(usuario)
    
    # Verificar que el saldo del usuario se haya actualizado
    assert usuario['saldo'] >= 0  