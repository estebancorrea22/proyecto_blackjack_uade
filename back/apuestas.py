
def realizar_apuesta(usuario):
    """Realiza apuesta con validación de saldo"""
    saldo = usuario['saldo']
    
    while True:
        try:
            apuesta = int(input(f"Saldo: ${saldo:,}\nApuesta (0 para salir): $"))
            if apuesta == 0:
                return None, None
            if apuesta < 0 or apuesta > saldo:
                print("Apuesta inválida")
                continue
            return apuesta, {**usuario, 'saldo': saldo - apuesta}
        except ValueError:
            print("Ingrese número válido")

def calcular_resultado(apuesta, res_jug, res_crup, usuario):
    """
    Calcula resultado usando diccionario de condiciones.

    Returns:
        tuple: (resultado_str, usuario_dict) donde resultado_str es un string con el resultado
               y usuario_dict es el diccionario del usuario actualizado.
    """
    condiciones = [
        ('blackjack', lambda: res_jug[0] == "blackjack" and res_crup[0] != "blackjack", int(apuesta * 2.5)),
        ('pasado', lambda: res_jug[0] == "pasado", 0),
        ('crupier_pasado', lambda: res_crup[0] == "pasado", apuesta * 2),
        ('ganador', lambda: res_jug[1] > res_crup[1], apuesta * 2),
        ('perdedor', lambda: res_jug[1] < res_crup[1], 0)
    ]

    for nombre, condicion, valor in condiciones:
        if condicion():
            resultado = (nombre, valor)
            break
    else:
        resultado = ('empate', apuesta)

    usuario['saldo'] += resultado[1]
    return f"Resultado: {resultado[0]}", usuario




#CAROLINA
# def double_bet(hand, current_bet):
#     """
#     El jugador decide duplicar la apuesta y lanzar un dado adicional.
#     El crupier debe aceptar la apuesta automáticamente.
#     Parámetros: hand (list): Mano actual de dados.
#         current_bet (int o float): Monto actual apostado.
#     Retorna:tuple: (mano_actualizada, nueva_apuesta, total_tras_tirada, estado)
#             estado: 'bust' si el total supera 21, de lo contrario 'continue'
#     """
#     try:
#         new_bet = current_bet * 2
#         new_die = roll_dice(1)[0]
#         hand.append(new_die)
#         total = sum_dice(hand)
#         status = "bust" if total > 21 else "continue"
#         return hand, new_bet, total, status
#     except Exception as e:
#         print(f"Error doubling bet: {e}")
#         return hand, current_bet, sum_dice(hand), "error"



