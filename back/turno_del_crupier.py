from tirada_dados import tirar_dado

"""

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
