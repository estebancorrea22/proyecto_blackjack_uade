def check_if_player_can_bet(player_coins, minimum_bet):
    if player_coins < minimum_bet:
        return False
    else:
        return True

def initial_bet(player_coins, minimum_bet, currentBet):
    player_coins = player_coins - minimum_bet
    currentBet = minimum_bet
    return player_coins, currentBet

def double_bet(playerCoins, currentBet):
    playerCoins = playerCoins - currentBet
    currentBet = currentBet * 2
    return playerCoins, currentBet

def check_end_of_hand(playerCoins, currentBet, croupier_busted, player_busted, player_points, croupier_points, player_did_blackjack, croupier_did_blackjack):
    if player_did_blackjack and croupier_did_blackjack:
        playerCoins += currentBet
        currentBet = 0
    elif player_did_blackjack:
        playerCoins += currentBet * 2.5
        currentBet = 0
    elif croupier_busted:
        playerCoins += currentBet * 2
        currentBet = 0
    elif player_busted:
        currentBet = 0
    elif player_points > croupier_points:
        playerCoins += currentBet * 2
        currentBet = 0
    elif player_points < croupier_points:
        currentBet = 0
    elif player_points == croupier_points:
        playerCoins += currentBet
        currentBet = 0
    else:
        currentBet = 0
    return playerCoins, currentBet
