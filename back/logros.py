from notificar_redes import notificar_discord

LOGROS = {
    'primer_juego': {
        'id': 1,
        'nombre': 'Primer juego',
        'descripcion': 'Jugar por primera vez',
        'recompensa': 500
    },
    'ganador_nato': {
        'id': 2,
        'nombre': 'Ganador nato',
        'descripcion': 'Ganar 3 partidas consecutivas',
        'recompensa': 1000
    },
    'blackjack': {
        'id': 3,
        'nombre': 'Blackjack',
        'descripcion': 'Obtener un blackjack (21 exacto)',
        'recompensa': 800
    },
    'arriesgado': {
        'id': 4,
        'nombre': 'Arriesgado',
        'descripcion': 'Apostar más de 1000 en una jugada',
        'recompensa': 700
    }
}

def verificar_logros(usuario, evento, contexto=None):
    """
    Verifica si el usuario ha alcanzado algún logro basado en el evento
    """
    logros_desbloqueados = []

 
    if evento == 'primer_juego':
        logro = LOGROS[evento]

        if 'logros' not in usuario:
            usuario['logros'] = {
                'logros_obtenidos': [],
                'logros_disponibles': []
            }

        ya_obtenido = any(l['id'] == logro['id'] for l in usuario['logros']['logros_obtenidos'])

        if not ya_obtenido:
            usuario['logros']['logros_obtenidos'].append(logro)
            logros_desbloqueados.append(logro['nombre'])
            if notificar_discord(usuario, logro['nombre'], logro['recompensa']):
                print(f"Logro notificado a Discord: {logro['nombre']}")
            else:
                print(f"Error al notificar logro a Discord: {logro['nombre']}")


    elif evento == 'ganador_nato':
        
        if 'logros' not in usuario:
            usuario['logros'] = {
                'logros_obtenidos': [],
                'logros_disponibles': []
            }
        
        logro = LOGROS[evento]
        victorias_consecutivas = usuario.get('victorias_consecutivas', 0) + 1
        usuario['victorias_consecutivas'] = victorias_consecutivas
        if victorias_consecutivas >= 3:
            ya_obtenido = any(l['id'] == logro['id'] for l in usuario['logros']['logros_obtenidos'])
            if not ya_obtenido:
                usuario['logros']['logros_obtenidos'].append(logro)
                logros_desbloqueados.append(logro['nombre'])
            if notificar_discord(usuario, logro['nombre'], logro['recompensa']):
                    print("Notificación enviada a Discord")
            else:
                print("No se pudo notificar a Discord")
      

    elif evento == 'blackjack':
        
        if 'logros' not in usuario:
            usuario['logros'] = {
                'logros_obtenidos': [],
                'logros_disponibles': []
            }
        
        logro = LOGROS[evento]
        if contexto and isinstance(contexto, list) and sum(contexto) == 21 and len(contexto) == 2:
            ya_obtenido = any(l['id'] == logro['id'] for l in usuario['logros']['logros_obtenidos'])
            if not ya_obtenido:
                usuario['logros']['logros_obtenidos'].append(logro)
                logros_desbloqueados.append(logro['nombre'])
            if notificar_discord(usuario, logro['nombre'], logro['recompensa']):
                    print("Notificación enviada a Discord")
     

    elif evento == 'arriesgado':
        if 'logros' not in usuario:
            usuario['logros'] = {
                'logros_obtenidos': [],
                'logros_disponibles': []
            }
        logro = LOGROS[evento]

        ya_obtenido = any(l['id'] == logro['id'] for l in usuario['logros']['logros_obtenidos'])
        if not ya_obtenido:
            usuario['logros']['logros_obtenidos'].append(logro)
            logros_desbloqueados.append(logro['nombre'])
            if notificar_discord(usuario, logro['nombre'], logro['recompensa']):
                    print("Notificación enviada a Discord")


    
    return logros_desbloqueados