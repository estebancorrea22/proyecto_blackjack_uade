from logros import verificar_logros
from notificar_redes import notificar_discord
from tirada_dados import evaluar_mano

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

def test_verificar_logros_primer_juego():
    usuario = {'nombre': 'Jugador1', 'saldo': 1000}
    logros = verificar_logros(usuario, 'primer_juego')  
    assert len(logros) == 1
    assert logros[0] == 'Primer juego'  
def test_verificar_logros_ganador_nato():
    usuario = {'nombre': 'Jugador2', 'saldo': 2000, 'logros': {'logros_obtenidos': [], 'logros_disponibles': []}}
   
    usuario['victorias_consecutivas'] = 3
    logros = verificar_logros(usuario, 'ganador_nato')
    assert len(logros) == 1
    assert logros[0] == 'Ganador nato'
    
def test_verificar_logros_blackjack(estado='blackjack'):
    usuario = {'nombre': 'Jugador3', 'saldo': 3000, 'logros': {'logros_obtenidos': [], 'logros_disponibles': []}}
    mano = [10, 11]  
    estado, _ = evaluar_mano(mano)
    logros = verificar_logros(usuario, 'blackjack', mano)
    assert len(logros) == 1
    assert logros[0] == 'Blackjack'
def test_verificar_logros_arriesgado():
    usuario = {'nombre': 'Jugador4', 'saldo': 4000, 'logros': {'logros_obtenidos': [], 'logros_disponibles': []}}
    apuesta = 1500 
    logros = verificar_logros(usuario, 'arriesgado', apuesta)
    assert len(logros) == 1
    assert logros[0] == 'Arriesgado'