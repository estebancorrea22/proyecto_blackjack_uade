from tirada_dados import tirar_dados

import time

def manejar_tiempo(jugador, tiempo_max=6):
    print(f"\n{jugador['nombre']} tiene {tiempo_max} segundos para tirar los dados.")

    start = time.time()
    inicio_jugada = input("Presioná ENTER para tirar los dados")
    end = time.time()

    if end - start > tiempo_max:
        print("Se pasó el tiempo.")
        jugador['mano'].append(tirar_dados())