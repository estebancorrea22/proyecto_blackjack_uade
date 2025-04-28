from tirada_dados import tirar_dado

"""
Este código representa el turno del crupier,  el crupier tira dados uno por uno,
suma sus valores y sigue tirando mientras tenga menos de 17 puntos. Si llega a superar
los 21 puntos pierde automaticamente.Ademas muestra en pantalla cada tirada y el total
acumulado. 
"""
def dealer_turn():
    total = 0

    while total < 17:
        new_dice = tirar_dado()[0] 
        total += new_dice
        print(f"Crupier tira dado: {new_dice} (Total: {total})")

    if total > 21:
        print(f"El crupier se paso con: {total} Pierde!")
    else:
        print(f"El crupier se planto con un total de: {total}")

dealer_turn()
