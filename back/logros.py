from datetime import datetime

# Definición de logros disponibles
LOGROS = {
    'primer_juego': {
        'nombre': 'Primer juego',
        'descripcion': 'Jugar por primera vez',
        'recompensa': 500
    },
    'ganador_nato': {
        'nombre': 'Ganador nato',
        'descripcion': 'Ganar 3 partidas consecutivas',
        'recompensa': 1000
    },
    'blackjack': {
        'nombre': 'Blackjack',
        'descripcion': 'Obtener un blackjack (21 exacto)',
        'recompensa': 800
    },
    'arriesgado': {
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
        if 'logros' not in usuario or 'primer_juego' not in usuario['logros']:
            logros_desbloqueados.append('primer_juego')
    
    elif evento == 'ganar_juego':
        victorias_consecutivas = usuario.get('victorias_consecutivas', 0) + 1
        usuario['victorias_consecutivas'] = victorias_consecutivas
        if victorias_consecutivas >= 3 and 'ganador_nato' not in usuario.get('logros', {}):
            logros_desbloqueados.append('ganador_nato')
    
    elif evento == 'blackjack':
        if contexto and sum(contexto) == 21 and len(contexto) == 2:
            if 'blackjack' not in usuario.get('logros', {}):
                logros_desbloqueados.append('blackjack')
    
    elif evento == 'apuesta_alta':
        if contexto and contexto >= 1000:
            if 'arriesgado' not in usuario.get('logros', {}):
                logros_desbloqueados.append('arriesgado')
    
    return logros_desbloqueados