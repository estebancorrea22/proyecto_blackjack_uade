from funcion_tirar_dados_inicio import tirar_dados

max_jugadores = 6
min_jugadores = 1

def iniciar_jugada(jugadores, crupier):
    if not (min_jugadores <= len(jugadores) <= max_jugadores):
        return

    for jugador in jugadores:
        jugador['mano'] = tirar_dados()
        jugador['estado'] = 'jugando'

    crupier['mano'] = tirar_dados()
    crupier['estado'] = 'jugando'