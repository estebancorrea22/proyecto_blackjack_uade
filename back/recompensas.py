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

        return True
    
    return False

def mostrar_logros(usuario):
    """
    Muestra los logros del usuario y los disponibles
    """
    print("\n--- TUS LOGROS ---")

    logros_obtenidos = usuario.get('logros', {}).get('logros_obtenidos', [])

    if logros_obtenidos:
        for logro in logros_obtenidos:
            print(f"{logro['nombre']}: {logro['descripcion']}")
    else:
        print("Aún no has desbloqueado logros.")

    print("\n--- LOGROS DISPONIBLES ---")
    for clave, logro in LOGROS.items():
        ya_obtenido = any(l['id'] == logro['id'] for l in logros_obtenidos)
        if not ya_obtenido:
            print(f"{logro['nombre']}: {logro['descripcion']} - Recompensa: ${logro['recompensa']}")