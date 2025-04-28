from proyecto_blackjack_uade.back.tirada_dados import tirar_dado

def sumar_dados(mano):
    return sum(mano)

def iniciar_jugada(jugador, crupier):
    jugador['mano'] = []
    jugador['estado'] = 'jugando'

    crupier['mano'] = []
    crupier['estado'] = 'jugando'

def turno_jugador(jugador):
    print(f"Turno del Jugador")

    while True:
        decision = input("¿Querés empezar la ronda? (Y/N): ").strip().upper()
        if decision == 'Y':
            break
        elif decision == 'N':
            jugador['estado'] = 'saltear'
            print("Decidiste no jugar esta ronda. El Crupier gana la ronda automáticamente")
            return
        else:
            print("Error. Ingresá 'Y' para sí o 'N' para no.")
    
    jugador['mano'].extend(tirar_dado(2))

    while True:
        print(f"Dados tirados:{jugador['mano']}")
        total_suma_dados_tirados=sumar_dados(jugador['mano'])
        print(f"El total de los dados tirado es:{total_suma_dados_tirados}")

        if total_suma_dados_tirados > 21:
            print("Te has pasado de 21. ¡Perdiste!")
            break
        elif total_suma_dados_tirados == 21:
            print("¡Felicidades, Blackjack!")
            break
        
        while True:
            decision = input("¿Quieres tirar otro dado? (Y/N): ").strip().upper()
            if decision == 'Y':
                jugador['mano'].extend(tirar_dado(1))
                break
            elif decision == 'N':
                print(f"Te quedaste con un total de {total_suma_dados_tirados}.")
                return
            else:
                print("Error. Ingresá 'Y' para sí o 'N' para no.")
    
    print(f"Dados tirados:{jugador['mano']} , Resultado:{total_suma_dados_tirados}")

def turno_crupier(crupier):
    print(f"Turno del Crupier")
    crupier['mano'].extend(tirar_dado(2))
    while sumar_dados(crupier['mano']) < 17:
        crupier['mano'].extend(tirar_dado(1))
    print(f"Dados tirados:{crupier['mano']} , Resultado:{sumar_dados(crupier['mano'])}")

jugador = {'nombre': 'Jugador'}
crupier = {'nombre': 'Crupier'}

turno = 'jugador'

for ronda in range(1, 7):
    iniciar_jugada(jugador, crupier)

    print(f"Ronda {ronda}")
    turno_jugador(jugador)

    if jugador['estado'] == 'saltear':
        print(f"\n¡El Crupier gana ronda {ronda}!\n")
        continue

    turno_crupier(crupier)
    

    total_jugador = sumar_dados(jugador['mano'])
    total_crupier = sumar_dados(crupier['mano'])

    if total_jugador > 21:
        print(f"\n¡El Jugador se pasó de 21, el Crupier gana ronda {ronda}!")
    elif total_crupier > 21:
        print(f"\n¡El Crupier se pasó de 21, el Jugador gana ronda {ronda}!")
    elif total_jugador > total_crupier and total_jugador <= 21:
        print(f"\n¡El Jugador gana ronda {ronda}!")
    elif total_crupier > total_jugador and total_crupier <= 21:
        print(f"\n¡El Crupier gana ronda {ronda}!")
    else:
        print(f"\n¡Empate en la ronda {ronda}!")