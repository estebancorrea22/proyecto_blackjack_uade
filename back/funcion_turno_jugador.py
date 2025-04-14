from funcion_pedir_tirar_dado import pedir_tirar_dado
from funcion_sumar_dado import sumar_dados

def turno_jugador(jugador):
    while jugador['estado'] == 'jugando':
        total = sumar_dados(jugador['mano'])
        print(f"\n{jugador['nombre']} - Mano: {jugador['mano']} (Total: {total})")

        if total > 21:
            print("Te pasaste de 21. ¡PERDISTE!")
            jugador['estado'] = 'PERDIÓ'
            break
        elif total == 21:
            print("¡BLACKJACK!")
            jugador['estado'] = 'PLANTADO'
            break

        opcion = input("Elegí: (1)PEDIR(HIT), (2)PLANTARSE(STAND), (3)IGUALAR DINERO, (4)DOBLAR(DOUBLE), (5)DIVIDIR(SPLIT), (6)RENDIRSE: ").strip()

        if opcion == "1":
            nuevo_dado = pedir_tirar_dado()
            jugador['mano'].append(nuevo_dado)
            print(f"Tiraste un dado y obtuviste: {nuevo_dado}")
        elif opcion == "2":
            print("Te plantaste.")
            jugador['estado'] = 'plantado'
            print(f"Total en mano:{}")

            #nose como hacer para que vaya sumando las manos


        elif opcion == "3":
            print("")
        #resolver tema apuesta


        elif opcion == "4":
            print("Doblando apuesta y tirando un dado más.")
            nuevo_dado = pedir_tirar_dado()
            jugador['mano'].append(nuevo_dado)
            print(f"Tiraste un dado y obtuviste: {nuevo_dado}")
            jugador['estado'] = 'doblando apuesta'
            #nose como hacer para que vaya sumando las manos
            #hay que hacer funcion para la apuesta

        elif opcion == "5":
            if len(jugador['mano']) == 2 and jugador['mano'][0] == jugador['mano'][1]:
                print("Dividiendo mano..")
            else:
                print("No se puede dividir: los dados no son iguales.")
        #nose como hacer para dividir la mano y luego sumarlo para el mismo jugador
        #hay que poner en claro como es la regla esta
        #cuando se dividi la mano se hace de una misma apuesta o se hace dos apuestas separadas?
        #nose como hacer para que vaya sumando las manos
        #hay que hacer funcion para la apuesta

        elif opcion == "6":
            print("Te rendiste.")
            jugador['estado'] = 'se rindió'
            break
        else:
            print("Opción inválida.")