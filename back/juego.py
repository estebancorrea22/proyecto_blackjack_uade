from tirada_dados import tirar_dado, evaluar_mano
from apuestas import realizar_apuesta, doblar_apuesta
from calcular_pago import calcular_pago  
from logros import verificar_logros
from recompensas import aplicar_recompensa, mostrar_logros
from datetime import datetime, timedelta

def mostrar_reglas():
    """
    Muestra por pantalla las reglas básicas del Blackjack con dados.
    Parámetros: ninguno.
    Retorna: None.
    """    
    print("\n--- REGLAS DEL BLACKJACK ---")
    print("1. Ganas si sacas 21 con tus dos primeros dados (Blackjack)")
    print("2. Pierdes si te pasas de 21")
    print("3. Si no, gana quien tenga más puntos")

def turno_jugador(usuario,apuesta):
    """
    Ejecuta el turno del jugador: permite tirar otro dado, doblar la apuesta o plantarse.
    Parámetros:
        usuario (dict): Datos del jugador, incluido su saldo.
        apuesta (int): Monto apostado al inicio del turno.
    Retorna:
        tuple: (estado, total, mano, apuesta) donde:
               estado (str)  "jugando", "blackjack", "pasado" o "plantado";
               total (int)   suma de los dados del jugador;
               mano (list)   lista de valores de los dados;
               apuesta (int)  apuesta final tras posibles cambios.
    """
    mano = tirar_dado(2)
    print(f"\nTus dados: {mano[0]} y {mano[1]} - Total: {sum(mano)}")
    
    while True:
        print("1.Tirar otro dado\n2.Doblar la apuesta\n3.Plantarse")
        opcion = input("Ingrese su opción:").lower()       
        
        if opcion == '1':
            nuevo_dado = tirar_dado(1)[0]
            mano.append(nuevo_dado)
            total = sum(mano)
            print(f"Nuevo dado: {nuevo_dado} - Total: {total}")  
            estado, total = evaluar_mano(mano)
            if estado != "jugando":
                return estado, total, mano, apuesta

        elif opcion == '2':
            mano, nueva_apuesta, total, estado, usuario = doblar_apuesta(mano, apuesta, usuario)
            apuesta = nueva_apuesta
            if estado == "saldo_insuficiente":
                print("No se pudo doblar la apuesta. Elige otra opción.")
                continue
            estado, total = evaluar_mano(mano)
            if estado != "jugando":         
                return estado, total, mano, apuesta
            
        elif opcion == '3':
            total = sum(mano)           
            return "plantado", total, mano , apuesta
               
        else:
            print("Opción inválida. Ingresa '1', '2' o '3'.")  

def turno_crupier():
    """
    Ejecuta el turno del crupier: lanza dados hasta alcanzar un total mínimo de 17.
    Parámetros: ninguno.
    Retorna:
        tuple: (estado, total) donde:
        estado (str) "jugando", "blackjack" o "pasado" según la suma de los dados;
        total (int) suma de los valores obtenidos por el crupier.
    """
    mano = tirar_dado(2)
    print(f"\nCrupier muestra: {mano[0]} y [*]")
    
    while sum(mano) < 17:
        mano.extend(tirar_dado(1))
    print(f"Crupier revela su mano: {', '.join(map(str, mano))} - Total: {sum(mano)}")
    return evaluar_mano(mano), sum(mano)

def jugar_blackjack(usuario):
    """
    Inicia y gestiona una o más rondas de Blackjack con dados para el usuario.
    Durante el juego se administran las apuestas, turnos, logros y recompensas.
    Parámetros:
        usuario (dict): Contiene la información del jugador (nombre, saldo, logros).
    Retorna:
        dict: Usuario actualizado con su nuevo saldo y logros obtenidos tras jugar.
    """
    
    print(f"\n¡Bienvenido al Blackjack, {usuario['nombre']}!")
    print(f"Saldo actual: ${usuario['saldo']:,}")
    mostrar_reglas()

    
    ahora = datetime.now()
    saldo_actual = usuario['saldo']
    
    if saldo_actual <= 100:
        if usuario.get('ultima_recarga_diaria'):
            tiempo_transcurrido = ahora - usuario['ultima_recarga_diaria']
            if tiempo_transcurrido >= timedelta(hours=24):
                if saldo_actual < 1000:
                    usuario['saldo'] += 1000
                    usuario['ultima_recarga_diaria'] = ahora
                    print(f"\n¡Recarga diaria de +1000 aplicada! Nuevo saldo: ${usuario['saldo']:,}")
            else:
                tiempo_restante = timedelta(hours=24) - tiempo_transcurrido
                horas = tiempo_restante.seconds // 3600
                minutos = (tiempo_restante.seconds % 3600) // 60
                
                if saldo_actual <= 0 or saldo_actual < 100:
                    print("\n¡Fondos insudicientes!")
                    print(f"Prueba nuevamente en {horas} horas y {minutos} minutos.")
                    return usuario
        else:
            
            if saldo_actual < 100:
                usuario['saldo'] += 1000
                usuario['ultima_recarga_diaria'] = ahora
                print("\n¡Recarga diaria de $1000 aplicada!")
                print(f"Nuevo saldo: ${usuario['saldo']:,}")

    # Si después de verificar recarga sigue con $0 o menos
    if usuario['saldo'] <= 0:
        print("\n¡No tienes fondos suficientes para jugar!")
        return usuario

    print(f"\n¡Bienvenido al Blackjack, {usuario['nombre']}!")
    print(f"Saldo actual: ${usuario['saldo']:,}")
    
    logros_desbloqueados = verificar_logros(usuario, 'primer_juego')
    for logro_id in logros_desbloqueados:
        aplicar_recompensa(usuario, logro_id)
        print(f"\n¡Logro desbloqueado: {logro_id}!")

    while True:
        apuesta, usuario = realizar_apuesta(usuario)
        if apuesta is None:
            break
        
        if apuesta >= 1000:
            logros_desbloqueados = verificar_logros(usuario, 'arriesgado', apuesta)
            for logro_id in logros_desbloqueados:
                aplicar_recompensa(usuario, logro_id)
                print(f"\n¡Logro desbloqueado: {logro_id}!")

        estado_jugador, total_jugador, mano_jugador, apuesta = turno_jugador(usuario, apuesta)

        if estado_jugador == "blackjack":
            logros_desbloqueados = verificar_logros(usuario, 'blackjack', mano_jugador)
            for logro_id in logros_desbloqueados:
                aplicar_recompensa(usuario, logro_id)
                print(f"\n¡Logro desbloqueado: {logro_id}!")

        if estado_jugador != "pasado":
            (estado_crupier, total_crupier) = turno_crupier()
        else:
            estado_crupier, total_crupier = "sin_jugar", 0

        # Determinar resultado del juego
        if estado_jugador == "pasado" or total_jugador > 21:
            resultado = "derrota"
        elif estado_crupier == "pasado" or total_crupier > 21:
            resultado = "victoria"
        elif total_jugador > total_crupier:
            resultado = "victoria"
        elif total_jugador < total_crupier:
            resultado = "derrota"
        elif estado_jugador == "blackjack" and estado_crupier != "blackjack":
            resultado = "blackjack"
        elif estado_jugador == "blackjack" and estado_crupier == "blackjack":
            resultado = "empate"
        else:
            resultado = "empate"

        ganancia = calcular_pago(resultado, apuesta, usuario)

        print(f'Ganancia: {ganancia}')
        print(f"Saldo: {usuario['saldo']}")
        usuario["saldo"] += ganancia

        print(f"\nResultado de la ronda: {resultado.upper()} (Saldo: {'+' if ganancia > 0 else '-' if ganancia < 0 else ''}${abs(ganancia)})")
        print(f"Nuevo saldo: ${usuario['saldo']:,}")

        if resultado in ["victoria", "blackjack"]:
            logros_desbloqueados = verificar_logros(usuario, 'ganar_juego')

        if usuario['saldo'] <= 0:
            print("\n¡Te quedaste sin fondos!")

        opcion_extra = input("\n¿Ver logros? (s/n): ").lower()
        if opcion_extra == 's':
            mostrar_logros(usuario)

        while True:
            otra_ronda = input("\n¿Otra ronda? (s/n): ").lower()
            if otra_ronda == 's':
                break
            elif otra_ronda == 'n':
                return usuario
            else:
                print("Opción inválida. Ingresa 's' o 'n'.")
    
    return usuario

   
