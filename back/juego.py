""" from tirada_dados import tirar_dado, evaluar_mano
from apuestas import realizar_apuesta, calcular_resultado
from collections import namedtuple
from logros import verificar_logros
from recompensas import aplicar_recompensa, mostrar_logros


def mostrar_reglas():
    print("\n--- REGLAS DEL BLACKJACK ---")
    print("1. Ganas si sacas 21 con tus dos primeros dados (Blackjack)")
    print("2. Pierdes si te pasas de 21")
    print("3. Si no, gana quien tenga más puntos")
    print("4. El crupier debe pedir dados hasta llegar a 17\n")

def turno_jugador():
    mano = tirar_dado(2)
    print(f"\nTus dados: {mano[0]} y {mano[1]} - Total: {sum(mano)}")
    
    while True:
        estado, total = evaluar_mano(mano)
        if estado != "jugando":
            return estado, total
        
        opcion = input("¿Quieres otro dado? (s/n): ").lower()
        if opcion == 's':
            nuevo_dado = tirar_dado(1)[0]
            mano.append(nuevo_dado)
            print(f"Nuevo dado: {nuevo_dado} - Total: {sum(mano)}")
        elif opcion == 'n':
            return "plantado", total
        else:
            print("Opción inválida. Ingresa 's' o 'n'.")

def turno_crupier():
    mano = tirar_dado(2)
    print(f"\nCrupier muestra: {mano[0]} y [*]")
    
    while sum(mano) < 17:
        mano.extend(tirar_dado(1))
    print(f"Crupier revela su mano: {', '.join(map(str, mano))} - Total: {sum(mano)}")
    return evaluar_mano(mano)

def jugar_blackjack(usuario):
    print(f"\n¡Bienvenido al Blackjack, {usuario['nombre']}!")
    print(f"Saldo actual: ${usuario['saldo']:,}")
    mostrar_reglas()

    # Verificar si es el primer juego del usuario
    logros_desbloqueados = verificar_logros(usuario, 'primer_juego')
    for logro_id in logros_desbloqueados:
        aplicar_recompensa(usuario, logro_id)
        print(f"\n¡Logro desbloqueado: {logro_id}!")

    Resultado = namedtuple('Resultado', ['estado', 'total'])
    
    while True:
        apuesta, usuario = realizar_apuesta(usuario)
        if apuesta is None:  # Si eligió salir
            break
            
        # Verificar logro por apuesta alta
        if apuesta >= 1000:
            logros_desbloqueados = verificar_logros(usuario, 'apuesta_alta', apuesta)
            for logro_id in logros_desbloqueados:
                aplicar_recompensa(usuario, logro_id)
                print(f"\n¡Logro desbloqueado: {logro_id}!")
            
        # Turnos
        resultado_jugador = turno_jugador()
        if resultado_jugador[0] == "blackjack":
            logros_desbloqueados = verificar_logros(usuario, 'blackjack', resultado_jugador[1])
            for logro_id in logros_desbloqueados:
                aplicar_recompensa(usuario, logro_id)
                print(f"\n¡Logro desbloqueado: {logro_id}!")
        
        if resultado_jugador[0] != "pasado":
            resultado_crupier = turno_crupier()
            print(f"\nCrupier final: {resultado_crupier[1]} ({resultado_crupier[0]})")
        else:
            resultado_crupier = Resultado(estado="sin_jugar", total=0)
        
        # Resultado
        mensaje, usuario = calcular_resultado(apuesta, resultado_jugador, resultado_crupier, usuario)
        print(f"\n{mensaje}")
        print(f"Nuevo saldo: ${usuario['saldo']:,}")
        
        # Verificar logros por victorias
        if "ganador" in mensaje or "blackjack" in mensaje:
            logros_desbloqueados = verificar_logros(usuario, 'ganar_juego')
            for logro_id in logros_desbloqueados:
                aplicar_recompensa(usuario, logro_id)
                print(f"\n¡Logro desbloqueado: {logro_id}!")
        
        if usuario['saldo'] <= 0:
            print("\n¡Te quedaste sin fondos!")
        
        # Mostrar opción de ver logros
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
    
    return usuario """


from tirada_dados import tirar_dado, evaluar_mano
from apuestas import realizar_apuesta
from funcion_calcular_pago import calcular_pago  
from logros import verificar_logros
from recompensas import aplicar_recompensa, mostrar_logros

def mostrar_reglas():
    print("\n--- REGLAS DEL BLACKJACK ---")
    print("1. Ganas si sacas 21 con tus dos primeros dados (Blackjack)")
    print("2. Pierdes si te pasas de 21")
    print("3. Si no, gana quien tenga más puntos")
    print("4. El crupier debe pedir dados hasta llegar a 17\n")

# def turno_jugador():
#     mano = tirar_dado(2)
#     print(f"\nTus dados: {mano[0]} y {mano[1]} - Total: {sum(mano)}")
    
#     while True:
#         estado, total = evaluar_mano(mano)
#         if estado != "jugando":
#             return estado, total, mano
        
#         opcion = input("¿Quieres otro dado? (s/n): ").lower()
#         if opcion == 's':
#             nuevo_dado = tirar_dado(1)[0]
#             mano.append(nuevo_dado)
#             print(f"Nuevo dado: {nuevo_dado} - Total: {sum(mano)}")
#         elif opcion == 'n':
#             return "plantado", total, mano
#         else:
#             print("Opción inválida. Ingresa 's' o 'n'.")

def turno_jugador(usuario,apuesta):
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
                return estado, total, mano, apuesta, usuario     

        elif opcion == '2':
            mano, nueva_apuesta, total, estado, usuario = doblar_apuesta(mano, apuesta, usuario)
            apuesta = nueva_apuesta
            if estado == "saldo_insuficiente":
                print("No se pudo doblar la apuesta. Elige otra opción.")
                continue
            estado, total = evaluar_mano(mano)
            if estado != "jugando":         
                return estado, total, mano, apuesta, usuario
            
        elif opcion == '3':
            total = sum(mano)           
            return "plantado", total, mano, apuesta, usuario 
               
        else:
            print("Opción inválida. Ingresa '1', '2' o '3'.")  

def turno_crupier():
    mano = tirar_dado(2)
    print(f"\nCrupier muestra: {mano[0]} y [*]")
    
    while sum(mano) < 17:
        mano.extend(tirar_dado(1))
    print(f"Crupier revela su mano: {', '.join(map(str, mano))} - Total: {sum(mano)}")
    return evaluar_mano(mano), mano

def jugar_blackjack(usuario):
    print(f"\n¡Bienvenido al Blackjack, {usuario['nombre']}!")
    print(f"Saldo actual: ${usuario['saldo']:,}")
    mostrar_reglas()

    logros_desbloqueados = verificar_logros(usuario, 'primer_juego')
    for logro_id in logros_desbloqueados:
        aplicar_recompensa(usuario, logro_id)
        print(f"\n¡Logro desbloqueado: {logro_id}!")

    while True:
        apuesta, usuario = realizar_apuesta(usuario)
        if apuesta is None:
            break
        
        if apuesta >= 1000:
            logros_desbloqueados = verificar_logros(usuario, 'apuesta_alta', apuesta)
            for logro_id in logros_desbloqueados:
                aplicar_recompensa(usuario, logro_id)
                print(f"\n¡Logro desbloqueado: {logro_id}!")

        estado_jugador, total_jugador, mano_jugador = turno_jugador()

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
        if estado_jugador == "pasado":
            resultado = "derrota"
        elif estado_crupier == "pasado":
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

        ganancia = calcular_pago(resultado, apuesta)
        usuario["saldo"] += ganancia

        print(f"\nResultado de la ronda: {resultado.upper()} (+{ganancia} saldo)")
        print(f"Nuevo saldo: ${usuario['saldo']:,}")

        if resultado in ["victoria", "blackjack"]:
            logros_desbloqueados = verificar_logros(usuario, 'ganar_juego')
            for logro_id in logros_desbloqueados:
                aplicar_recompensa(usuario, logro_id)
                print(f"\n¡Logro desbloqueado: {logro_id}!")

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

   
   
