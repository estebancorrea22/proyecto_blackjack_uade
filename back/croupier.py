import random

croupier_dice = []

threshold = 17
bust_limit = 21
croupier_busted = False
croupier_stand = False


def calculate_croupier_total():
    croupier_total = 0

    for number in croupier_dice:
        croupier_total += number
    
    return croupier_total

def first_turn_croupier():
    if len(croupier_dice) == 0:
        croupier_dice.append(roll_dice())
        croupier_dice.append(roll_dice())

def check_croupier_dice():
    croupier_total = calculate_croupier_total()
    if croupier_total > bust_limit:
        croupier_busted = True
        return True
    elif croupier_total < threshold:
        croupier_dice.append(roll_dice())
    else:
        croupier_stand = True

def roll_dice():
    return random.randint(1, 10)
    
def return_croupier_data():
    return {
        "croupier_dice": croupier_dice,
        "croupier_busted": croupier_busted,
        "croupier_stand": croupier_stand,
        "croupier_total": calculate_croupier_total()
    }