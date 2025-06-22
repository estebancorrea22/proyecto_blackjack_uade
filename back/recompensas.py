from logros import LOGROS
from datetime import datetime

def aplicar_recompensa(usuario, logro_id):
    """
    Aplica la recompensa por un logro desbloqueado
    """
    if logro_id not in LOGROS:
        return False
    
    if 'logros' not in usuario:
        usuario['logros'] = {}
    
    if logro_id not in usuario['logros']:
        recompensa = LOGROS[logro_id]['recompensa']
        usuario['saldo'] += recompensa
        usuario['logros'][logro_id] = {
            'fecha': datetime.now().isoformat(),
            'reclamado': True
        }
        return True
    
    return False

def mostrar_logros(usuario):
    """
    Muestra los logros del usuario y los disponibles
    """
    print("\n--- TUS LOGROS ---")
    if 'logros' in usuario and usuario['logros']:
        for logro_id, detalle in usuario['logros'].items():
            logro = LOGROS.get(logro_id, {})
            print(f"{logro.get('nombre', 'Desconocido')}: {logro.get('descripcion', '')}")
            print(f"Obtenido el: {detalle['fecha']}\n")
    else:
        print("Aún no has desbloqueado logros.")
    
    print("\n--- LOGROS DISPONIBLES ---")
    for logro_id, logro in LOGROS.items():
        if 'logros' not in usuario or logro_id not in usuario['logros']:
            print(f"{logro['nombre']}: {logro['descripcion']} - Recompensa: ${logro['recompensa']}")