from gestion_saldo import calcular_saldo_total, recargar_saldo_tarjeta
from datetime import datetime



usuarios = []

def registro_usuario():
    """
    Se utiliza una lista global para almacenar los usuarios registrados
    Registra un nuevo usuario en el sistema y verifica que la contrasena tenga al menos 8 caracteres y que el correo termine en '@hotmail.com' y que el usuario sea mayor de edad tambien se usa datetime para guardar la fecha en la que se hizo la ultima recarga y el saldo con en el que el jugador empieza es de 1000
    
    """
    mayor_de_edad = 18
    edad = int(input("Ingresa tu edad: "))
    while edad < mayor_de_edad:
        print("Debes ser mayor de edad para registrarte.")
        edad = int(input("Ingresa tu edad: "))
    
    nombre = input("Ingresa tu nombre: ")
    saldo = 1000
    ultima_recarga = datetime.now()

    correo = input("Ingresa correo (@hotmail.com): ")
    while not correo.endswith("@hotmail.com"):
        print("El correo debe terminar con @hotmail.com.")
        correo = input("Ingresa correo (@hotmail.com): ")
        
    contrasena = input("Ingresa contrasena (minimo 8 caracteres): ")
    while len(contrasena) < 8:
        print("La contrasena debe tener al menos 8 caracteres.")
        contrasena = input("Ingresa contrasena (minimo 8 caracteres): ")

    """
        Se crea un usuario como diccionario y se hace un append a la lista global de usuarios
    """

    nuevo_usuario = {
        "id": len(usuarios) + 1, 
        "contrasena": contrasena,
        "correo": correo,
        "nombre": nombre,
        "saldo": saldo,
        "ultima_recarga": ultima_recarga
    }
    usuarios.append(nuevo_usuario)  
    print("Usuario registrado con exito!!")


    """
    La funcion de login_usuario permite a un usario iniciar sesion verificando si su correo y contrasena son validos, usando next() y filter() para buscar el usuario en la lista 
    si el usuario es valido se imprime un mensaje de bienvenida
    
    """
def login_usuario():

    correo = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraseña: ")

    # Usar filter para buscar el usuario
    usuario = next(filter(lambda u: u['correo'] == correo and u['contrasena'] == contrasena, usuarios),None)
    
    if usuario:
        print(f"Bienvenido {usuario['nombre']}")
        return usuario
    else:
        print("Correo o contraseña incorrectos.")
        return None

"""
    la funncion perimite mostrar los usuarios registrados en el sistema e imprime su id, nombre,correo y saldo actual
"""

def mostrar_usuarios():
    
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    print("Usuarios registrados:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Correo: {usuario['correo']}, Saldo: {usuario['saldo']}")

registro_usuario()
login_usuario()
mostrar_usuarios()
recargar_saldo_tarjeta(usuarios)
calcular_saldo_total(usuarios)