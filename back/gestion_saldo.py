from datetime import datetime, timedelta

def cargar_saldo_24hrs(usuarios):
    correo = input("Ingrese correo al que se le va a cargar saldo: ")
    usuario = next(filter(lambda u: u['correo'] == correo, usuarios), None)
    
    if not usuario:
        print("Usuario no encontrado")
        return
    
    ahora = datetime.now()
    
    if "ultima_carga_saldo" in usuario and usuario["ultima_carga_saldo"] is not None:
        ultima_carga = usuario["ultima_carga_saldo"]
        if ahora < ultima_carga + timedelta(hours=24):
            print("No han pasado 24 horas desde la ultima carga de saldo")
            return
    monto_recarga = 100  
    usuario["saldo"] += monto_recarga
    usuario["ultima_carga_saldo"] = ahora
    print(f"Saldo recargado exitosamente. Nuevo saldo: {usuario['saldo']}")

def mostrar_saldo_usuario(usuarios):
    correo = input("Ingrese correo del usuario: ")
    usuario = next(filter(lambda u: u['correo'] == correo, usuarios), None)
    
    if not usuario:
        print("Usuario no encontrado")
        return
    
    print(f"El saldo de {usuario['nombre']} es: {usuario['saldo']}")
    return usuario["saldo"]