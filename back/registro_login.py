import os
from datetime import datetime
import json
import re

usuarios = []
usuario_actual = None

def generar_id():
    """Genera un ID único usando comprensión de listas y operador in"""
    ids_existentes = [u['id'] for u in usuarios]
    return max(ids_existentes) + 1 if ids_existentes else 1

def validar_contrasena(contrasena):
    """
    Valida la contraseña usando expresiones regulares y operador in.
    Requiere:
    - 8+ caracteres
    - 1 mayúscula   
    - 1 carácter especial
    """
    caracteres_especiales = "!@#$%^&*(),.?\":{}|<>"
    return (len(contrasena) >= 8 and 
            any(c.isupper() for c in contrasena) and 
            any(c in caracteres_especiales for c in contrasena))

def registro_usuario():
    """Registro de usuario con validación de matriz de datos"""
    # Matriz de validaciones: [(condición, mensaje_error)]
    validaciones = [
        (lambda e: e >= 18, "Debes ser mayor de edad"),
        (lambda n: len(n) > 0, "Nombre no válido"),
        (lambda c: re.match(r'^.+@.+\..+$', c) is not None, "Correo no es valido. Intentelo nuevamente"),
        (lambda c: not any(u['correo'] == c for u in usuarios), "Correo ya existe")
    ]
    
    # Usando map y filter para validaciones
    edad = int(input("Edad: "))
    if not validaciones[0][0](edad):
        print(validaciones[0][1])
        return

    nombre = input("Nombre: ")
    correo = input("Correo: ")
    
    # Validación con operador in
    if any(not v[0](correo) for v in validaciones[2:]):
        print(next(v[1] for v in validaciones[2:] if not v[0](correo)))
        return

    contrasena = input("Contraseña: (La contraseña debe incluir 1 mayuscula, 1 caracter especial y debe ser de por lo menos 8 caracteres)")
    if not validar_contrasena(contrasena):
        print("Contraseña no cumple requisitos")
        return

    # Diccionario con datos del usuario
    nuevo_usuario = {
        "id": generar_id(),
        "nombre": nombre,
        "correo": correo,
        "contrasena": contrasena,
        "saldo": 1000,
        "edad": edad,
        "ultima_recarga": datetime.now(),
        "ultimo_login": None,
        "historial": [],  # Lista para historial de juegos
        "logros": []
    }
    
    usuarios.append(nuevo_usuario)
    # guardar_usuarios()
    guardar_usuarios_json()
    print("¡Registro exitoso!")

def eliminar_usuario():
    """Elimina un usuario después de confirmación"""
    mostrar_usuarios()
    if not usuarios:
        return
    
    try:
        id_eliminar = int(input("Ingrese el ID del usuario a eliminar: "))
        usuario = next((u for u in usuarios if u['id'] == id_eliminar), None)
        
        if usuario:
            confirmacion = input(f"¿Está seguro que desea eliminar al usuario {usuario['nombre']}? (s/n): ").lower()
            if confirmacion == 's':
                usuarios.remove(usuario)
                print("Usuario eliminado con éxito.")
                # guardar_usuarios()
                guardar_usuarios_json()
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró un usuario con ese ID.")
    except ValueError:
        print("ID inválido. Ingrese un número.")

def login_usuario():
    """
    Inicia sesión de usuario y verifica si ha pasado 1 día desde la última recarga.
    Si la fecha de última recarga es anterior a hoy, añade 1000 al saldo.
    """
    correo = input("Ingrese su correo: ")
    contrasena = input("Ingrese su contraseña: ")
    
    usuario = next((u for u in usuarios if u['correo'] == correo and u['contrasena'] == contrasena), None)
    
    if usuario:
        ahora = datetime.now()
        usuario['ultimo_login'] = ahora
        
        # Verificar si la última recarga fue antes de hoy
        fecha_ultima_recarga = usuario['ultima_recarga'].date()
        fecha_hoy = ahora.date()
        
        if fecha_ultima_recarga < fecha_hoy:
            usuario['saldo'] += 1000
            usuario['ultima_recarga'] = ahora
            guardar_usuarios_json()  # Guarda los cambios en el saldo
            print(f"¡Recarga diaria de +1000 aplicada! Nuevo saldo: {usuario['saldo']}")
        
        print(f"Bienvenido {usuario['nombre']}")
        return usuario
    else:
        print("Correo o contraseña incorrectos.")
        return None


def logout():
    """Cierra la sesión del usuario actual"""
    global usuario_actual
    if usuario_actual:
        print(f"¡Hasta pronto, {usuario_actual['nombre']}!")
        usuario_actual = None
    else:
        print("No hay ninguna sesión activa.")


def mostrar_usuarios():
    """Muestra todos los usuarios registrados con sus datos principales"""
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    print("\nUsuarios registrados:")
    print("ID | Nombre | Correo | Saldo | Última recarga")
    print("-" * 70)
    for u in usuarios:
        fecha_recarga = u['ultima_recarga'].strftime("%d-%m-%Y - %H:%M")
        print(f"{u['id']} | {u['nombre']} | {u['correo']} | {u['saldo']} | {fecha_recarga}")

def guardar_usuarios_json(usuario, filename='back/usuarios.json'):
    """
    Guarda un usuario en el archivo JSON, actualizándolo si ya existe por ID.
    Convierte datetime a string para serialización.
    """
    os.makedirs('back', exist_ok=True)

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            usuarios = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        usuarios = []

    usuario_serializable = usuario.copy()
    if isinstance(usuario_serializable.get('ultima_recarga'), datetime):
        usuario_serializable['ultima_recarga'] = usuario_serializable['ultima_recarga'].isoformat()
    if isinstance(usuario_serializable.get('ultimo_login'), datetime):
        usuario_serializable['ultimo_login'] = usuario_serializable['ultimo_login'].isoformat()

    actualizado = False
    for i, u in enumerate(usuarios):
        if u.get('id') == usuario_serializable['id']:
            usuarios[i] = usuario_serializable
            actualizado = True
            break
    if not actualizado:
        usuarios.append(usuario_serializable)

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(usuarios, f, indent=4)
        print("Usuario guardado correctamente.")
    except Exception as e:
        print(f"Error al guardar el usuario: {str(e)}")

# def guardar_usuarios():
#     """
#     Guarda usuarios en archivo usando OS.
#     Incluye todos los campos relevantes del usuario.
#     """
#     try:
#         os.makedirs('back', exist_ok=True)
#         with open('back/usuarios.txt', 'w') as f:
#             for u in usuarios:
#                 linea = (
#                     f"{u['id']},{u['nombre']},{u['edad']},"
#                     f"{u['correo']},{u['saldo']},"
#                     f"{u['ultima_recarga'].isoformat()},"
#                     f"{u['ultimo_login'].isoformat() if u['ultimo_login'] else ''},"
#                     f"{u['contrasena']}\n"
#                 )
#                 f.write(linea)
#     except Exception as e:
#         print(f"Error al guardar usuarios: {str(e)}")

def cargar_usuarios_json():
    """Carga usuarios desde archivo JSON"""
    global usuarios
    try:
        if os.path.exists('back/usuarios.json'):
            with open('back/usuarios.json', 'r') as f:
                usuarios = json.load(f)
                for u in usuarios:
                    u['ultima_recarga'] = datetime.fromisoformat(u['ultima_recarga'])
                    if u['ultimo_login']:
                        u['ultimo_login'] = datetime.fromisoformat(u['ultimo_login'])
                    else:
                        u['ultimo_login'] = None
        else:
            usuarios = []
    except Exception as e:
        print(f"Error al cargar usuarios: {str(e)}")
# def cargar_usuarios():
#     """Carga usuarios desde archivo"""
#     if os.path.exists('back/usuarios.txt'):
#         with open('back/usuarios.txt', 'r') as f:
#             # Usando list comprehension y tuplas
#             lineas = [linea.strip().split(',') for linea in f]
#             global usuarios
#             usuarios = [{
#                 "id": int(datos[0]),
#                 "nombre": datos[1],
#                 "edad": int(datos[2]),
#                 "correo": datos[3],
#                 "saldo": float(datos[4]),
#                 "ultima_recarga": datetime.fromisoformat(datos[5]),
#                 "ultimo_login": datetime.fromisoformat(datos[6]) if len(datos) > 7 and datos[6] else None,
#                 "contrasena": datos[7] if len(datos) > 7 else datos[6],
#                 "historial": []
#             } for datos in lineas if len(datos) >= 7]

def obtener_opciones_menu():
    opciones_base = [
        "1. Registrar usuario",
        "2. Iniciar sesión" if not usuario_actual else "2. Ver mi perfil",
        "3. Mostrar usuarios",
        "4. Eliminar usuario",
        "5. Jugar Blackjack" if usuario_actual else "5. Salir",
        "6. Cerrar sesión" if usuario_actual else "",
        "7. Salir" if usuario_actual else ""
    ]
    return [op for op in opciones_base if op] 
def mostrar_menu():
    print("\n".join(obtener_opciones_menu()))

    # cargar_usuarios()
    cargar_usuarios_json()
    # Menu principal
while True:
  
    print("\n--- Sistema de Usuarios ---")
    if usuario_actual:
        print(f"Usuario actual: {usuario_actual['nombre']} (Saldo: {usuario_actual['saldo']})")
    mostrar_menu()
        
    opcion = input("\nSeleccione una opción: ")
        
    if opcion == "1":
        registro_usuario()
    elif opcion == "2":
        if usuario_actual:
               # Mostrar perfil del usuario logueado
            print("\n--- Mi Perfil ---")
            print(f"Nombre: {usuario_actual['nombre']}")
            print(f"Correo: {usuario_actual['correo']}")
            print(f"Edad: {usuario_actual['edad']}")
            print(f"Saldo: {usuario_actual['saldo']}")
            from recompensas import mostrar_logros
            mostrar_logros(usuario_actual)
            input("\nPresione Enter para continuar...")
        else:
            usuario = login_usuario()
            if usuario:
                usuario_actual = usuario
                print(f"Tu saldo actual es: {usuario_actual['saldo']}")
                input("\nPresione Enter para continuar...")
    elif opcion == "3":
        mostrar_usuarios()
        
        input("\nPresione Enter para continuar...")
    elif opcion == "4":
        eliminar_usuario()
        if usuario_actual and usuario_actual not in usuarios:  
            usuario_actual = None
        input("\nPresione Enter para continuar...")
    elif opcion == "5":
        if usuario_actual:
            from juego import jugar_blackjack
            usuario_actual = jugar_blackjack(usuario_actual)
            guardar_usuarios_json(usuario_actual)# Guarda los cambios en el saldo
            input("\nPresione Enter para continuar...")
        else:
            print("Saliendo del sistema...")
            break
    elif opcion == "6" and usuario_actual:
        
        logout()
        input("\nPresione Enter para continuar...")
    elif opcion == "7" and usuario_actual:
        
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")
