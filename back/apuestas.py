from tirada_dados import sumar_dados, tirar_dado

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
            return apuesta, {**usuario, 'saldo': saldo}
        except ValueError:
            print("Ingrese número válido")


def doblar_apuesta(mano, apuesta_actual, usuario):
    """
    El jugador decide duplicar la apuesta y lanzar un dado adicional.
    El crupier debe aceptar la apuesta automáticamente.
    """
    saldo_restante = usuario['saldo']
    if saldo_restante < apuesta_actual:
        print("No tienes saldo suficiente para doblar la apuesta.")
        return mano, apuesta_actual, sumar_dados(mano), "saldo_insuficiente", usuario

    try:
        nueva_apuesta = apuesta_actual * 2
        usuario['saldo']
        print(f"Apuesta duplicada a ${nueva_apuesta}")        
        nuevo_dado = tirar_dado(1)[0]
        mano.append(nuevo_dado)
        total = sumar_dados(mano)
        estado = "pasado" if total > 21 else "jugando"
        print(f"\nDado adicional: {nuevo_dado} - Total: {total}")
        return mano, nueva_apuesta, total, estado, usuario
    except Exception as e:
        print(f"Error al doblar la apuesta: {e}")
        return mano, apuesta_actual, sumar_dados(mano), "error", usuario


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