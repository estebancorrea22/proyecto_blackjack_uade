import requests
from datetime import datetime



DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1391902889840087142/Crf5Z-Ln6MzLrokPWAEN31wfptdPFPBONL_v3c5x_kCq9oWgAMN4lXVmDdT2yYqNbW3H"

def notificar_discord(usuario, logro_nombre, recompensa=None):
    """
    Envía una notificación a Discord cuando se desbloquea un logro
    
    Args:
        usuario (dict): Diccionario con datos del usuario
        logro_nombre (str): Nombre del logro desbloqueado
        recompensa (int, optional): Cantidad de recompensa recibida
    """
    embed = {
        "title": f" ¡Nuevo logro desbloqueado!",
        "description": f"**{usuario['nombre']}** ha desbloqueado:",
        "color": 0x00ff00,  # Color verde
        "fields": [
            {
                "name": "Logro",
                "value": logro_nombre,
                "inline": True
            },
            {
                "name": "Recompensa",
                "value": f"${recompensa}" if recompensa else "Sin recompensa",
                "inline": True
            },
            {
                "name": "Saldo actual",
                "value": f"${usuario.get('saldo', 0):,}",
                "inline": False
            }
        ],
        "timestamp": datetime.now().isoformat(),
        "footer": {
            "text": "Sistema de Logros - Blackjack"
        }
    }

    payload = {
        "username": "Notificador de Logros",
        "avatar_url": "https://i.imgur.com/J5qwe1o.png",  
        "embeds": [embed]
    }

    try:
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=5  
        )
        
        if response.status_code == 204:
            print("Notificación enviada exitosamente a Discord")
            return True
        else:
            print(f" Error al enviar a Discord. Código: {response.status_code}")
            print(f"Respuesta: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f" Error de conexión con Discord: {str(e)}")
        return False
    except Exception as e:
        print(f" Error inesperado: {str(e)}")
        return False
    