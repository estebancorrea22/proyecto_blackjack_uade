import os
from datetime import datetime, timedelta
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
    parametros: contrasena (str): Contraseña a validar.
    Retorna: bool: True si la contraseña es válida, False en caso contrario.
    """
    caracteres_especiales = "!@#$%^&*(),.?\":{}|<>"
    return (len(contrasena) >= 8 and 
            any(c.isupper() for c in contrasena) and 
            any(c in caracteres_especiales for c in contrasena))

def registro_usuario():
    """Registro de usuario con validación de matriz de datos
    Parametros: validaciones (list): Lista de validaciones a aplicar.
    Cada validación es una tupla con (condición, mensaje_error).
    Retorna: el usuario registrado o None si se cancela."""
    # Matriz de validaciones: [(condición, mensaje_error)]
    validaciones = [
        
        (lambda e: e >= 18, "Debes ser mayor de edad"),
        (lambda e: e <= 100, "Edad no válida"),
        (lambda e: isinstance(e, int), "Edad debe ser un número entero"),
        (lambda n: isinstance(n, str) and len(n) > 0, "Nombre no puede estar vacío"),
        (lambda n: re.match(r'^[a-zA-Z\s]+$', n) is not None, "Nombre solo puede contener letras y espacios"),
        (lambda n: len(n) <= 50, "Nombre no puede exceder 50 caracteres"),
        (lambda n: isinstance(n, str), "Nombre debe ser una cadena de texto"),
        (lambda n: n.strip() != "", "Nombre no puede estar vacío"),
        (lambda n: n.strip() != " ", "Nombre no puede ser solo espacios"),
        (lambda n: len(n) > 0, "Nombre no válido"),
        (lambda c: len(c) > 0, "Correo no puede estar vacío"),
        (lambda c: re.match(r'^.+@.+\..+$', c) is not None, "Correo no es valido. Intentelo nuevamente"),
        (lambda c: not any(u['correo'] == c for u in usuarios), "Correo ya existe")
        
    ]
    
    while True:
        # Validación de edad
        while True:
            edad_input = input("Edad: ")
            if edad_input.lower() == 'cancelar':
                print("Registro cancelado.")
                return
            
            try:
                edad = int(edad_input)
                if not validaciones[0][0](edad):
                    print(validaciones[0][1])
                elif not validaciones[1][0](edad):
                    print(validaciones[1][1])
                else:
                    break
            except ValueError:
                print("La edad debe ser un número entero.")

        # Validación de nombre
        while True:
            nombre = input("Nombre: ")
            if nombre.lower() == 'cancelar':
                print("Registro cancelado.")
                return
            
            if not validaciones[3][0](nombre):
                print(validaciones[3][1])
            elif not validaciones[4][0](nombre):
                print(validaciones[4][1])
            elif not validaciones[5][0](nombre):
                print(validaciones[5][1])
            else:
                break

        # Validación de correo
        while True:
            correo = input("Correo: ")
            if correo.lower() == 'cancelar':
                print("Registro cancelado.")
                return
            
            if not validaciones[10][0](correo):
                print(validaciones[10][1])
            elif not validaciones[11][0](correo):
                print(validaciones[11][1])
            elif not validaciones[12][0](correo):
                print(validaciones[12][1])
            else:
                break

        # Validación de contraseña
        while True:
            contrasena = input("Contraseña (debe incluir 1 mayúscula, 1 carácter especial y 8+ caracteres): ")
            if contrasena.lower() == 'cancelar':
                print("Registro cancelado.")
            else:
                if not validar_contrasena(contrasena):
                    print("Contraseña no válida. Debe tener al menos 8 caracteres, 1 mayúscula y 1 carácter especial.")
                else:
                    confirmacion = input("Confirme su contraseña: ")
                    if confirmacion != contrasena:
                        print("Las contraseñas no coinciden. Intente nuevamente.")
                    else:
                        print("Contraseña válida.")
                        break
        break
    # Creación del usuario
    nuevo_usuario = {
        "id": generar_id(),
        "nombre": nombre,
        "correo": correo,
        "contrasena": contrasena,
        "saldo": 1000,
        "edad": edad,
        "ultima_recarga": datetime.now(),
        "ultima_recarga_diaria": None,
        "ultimo_login": None,
        "historial": [],
        "logros": {"logros_obtenidos": []}
    }
    
    usuarios.append(nuevo_usuario)
    guardar_usuarios_json(nuevo_usuario)
    print("\n¡Registro exitoso!")
    
def modificar_saldo_usuario(id_usuario, nuevo_saldo, guardar=True):
    """
    Modifica el saldo de un usuario con el ID dado.
    
    Parámetros:
        id_usuario (int): ID del usuario a modificar
        nuevo_saldo (int): Nuevo saldo a asignar
        guardar (bool): Si se debe guardar el usuario en el JSON inmediatamente
    Retorna:
        bool: True si se modificó correctamente, False en caso contrario
    """
    cargar_usuarios_json()  # Asegura que la lista de usuarios esté actualizada

    usuario = next((u for u in usuarios if u['id'] == id_usuario), None)

    if usuario:
        usuario['saldo'] = nuevo_saldo
        if guardar:
            guardar_usuarios_json(usuario)
        print(f"Saldo actualizado para el usuario {usuario['nombre']}. Nuevo saldo: {nuevo_saldo}")
        return True
    else:
        print(f"No se encontró un usuario con ID {id_usuario}.")
        return False

    
def eliminar_usuario(id_eliminar, api = False):
    """
    Elimina un usuario después de confirmación.
    parametros: 
        id_eliminar (int): ID del usuario a eliminar (Para llamada por API).
        api (bool): Booleano que indica si la funcion sera llamada por la API o por consola
    """
    mostrar_usuarios()
    if not usuarios:
        return
    
    try:
        if not api:
            id_eliminar = int(input("Ingrese el ID del usuario a eliminar: "))
        usuario = next((u for u in usuarios if u['id'] == id_eliminar), None)
        
        if usuario:
            confirmacion = input(f"¿Está seguro que desea eliminar al usuario {usuario['nombre']}? (s/n): ").lower()
            if confirmacion == 's':
                usuarios.remove(usuario)
                print("Usuario eliminado con éxito.")
                # guardar_usuarios()
                guardar_usuarios_json(usuario)
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró un usuario con ese ID.")
    except ValueError:
        print("ID inválido. Ingrese un número.")

def login_usuario(correo, contrasena, api = False):
    """
    Inicia sesión de usuario y verifica si ha pasado 1 día desde la última recarga.
    Si la fecha de última recarga es anterior a hoy, añade 1000 al saldo.
    Parámetros:
        correo (str): Correo del usuario a loguear (Para API).
        contrasena (str): Contraseña del usuario a loguear (Para API)
        api (bool): Indica si la funcion sera llamada desde la API o no para cambio de logica
    Retorna:
        usuario: Devuelve el usuario si se pudo loguear, None si no pudo
    """
    cargar_usuarios_json()
    
    if not api:
        correo = input("Ingrese su correo: ")
        contrasena = input("Ingrese su contraseña: ")

    usuario = next((u for u in usuarios if u['correo'] == correo and u['contrasena'] == contrasena), None)
    if api: 
        return usuario
    
    if usuario:
        ahora = datetime.now()
        usuario['ultimo_login'] = ahora
        
        print(f"Bienvenido {usuario['nombre']}")
        return usuario
    else:
        print("Correo o contraseña incorrectos.")
        return None


def logout():
    """
        Cierra la sesión del usuario actual
    """
    global usuario_actual
    if usuario_actual:
        print(f"¡Hasta pronto, {usuario_actual['nombre']}!")
        usuario_actual = None
    else:
        print("No hay ninguna sesión activa.")


def mostrar_usuarios():
    """
        Muestra todos los usuarios registrados con sus datos principales
    """
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    print("\nUsuarios registrados:")
    print("ID | Nombre | Correo | Saldo | Última recarga")
    print("-" * 70)
    for u in usuarios:
        fecha_recarga = u['ultima_recarga'].strftime("%d-%m-%Y - %H:%M")
        print(f"{u['id']} | {u['nombre']} | {u['correo']} | {u['saldo']} | {fecha_recarga}")

def guardar_usuarios_json(usuario=None, filename='./usuarios/usuarios.json'):
    """
    Guarda un usuario en el archivo JSON, actualizándolo si ya existe por ID.
    Convierte datetime a string para serialización.
    """
    # Validación de usuario
    if usuario is None:
        print("Error: No se proporcionó usuario para guardar")
        return False
    
    try:
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(filename), exist_ok=True)  

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                usuarios = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            usuarios = []
    
        usuario_serializable = usuario.copy()
        
        for key, value in usuario_serializable.items():
            if isinstance(value, datetime):
                usuario_serializable[key] = value.isoformat()
            elif key == 'logros' and isinstance(value, dict):
                # Serializar fechas en logros si las hubiera
                for logro in value.get('logros_obtenidos', []):
                    if 'fecha' in logro and isinstance(logro['fecha'], datetime):
                        logro['fecha'] = logro['fecha'].isoformat()

        # Actualizar o añadir usuario
        actualizado = False
        for i, u in enumerate(usuarios):
            if u.get('id') == usuario_serializable['id']:
                usuarios[i] = usuario_serializable
                actualizado = True
                break
        
        if not actualizado:
            usuarios.append(usuario_serializable)

        # Guardar cambios
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
        
        print("Usuario guardado correctamente.")
        return True

    except Exception as e:
        print(f"Error crítico al guardar usuario: {str(e)}")
        return False

def cargar_usuarios_json():
    """Carga usuarios desde archivo JSON"""
    global usuarios
    try:
        if os.path.exists('./usuarios/usuarios.json'):
            with open('./usuarios/usuarios.json', 'r', encoding='utf-8') as f:
                usuarios = json.load(f)
                for u in usuarios:
                    # Convertir strings ISO de vuelta a datetime
                    if 'ultima_recarga' in u:
                        u['ultima_recarga'] = datetime.fromisoformat(u['ultima_recarga'])
                    if 'ultima_recarga_diaria' in u and u['ultima_recarga_diaria']:
                        u['ultima_recarga_diaria'] = datetime.fromisoformat(u['ultima_recarga_diaria'])
                    if 'ultimo_login' in u and u['ultimo_login']:
                        u['ultimo_login'] = datetime.fromisoformat(u['ultimo_login'])
                    if 'logros' in u:
                        for logro in u['logros'].get('logros_obtenidos', []):
                            if 'fecha' in logro and logro['fecha']:
                                logro['fecha'] = datetime.fromisoformat(logro['fecha'])
        else:
            usuarios = []
    except Exception as e:
        print(f"Error al cargar usuarios: {str(e)}")

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
# while True:
  
#     print("\n--- Sistema de Usuarios ---")
#     if usuario_actual:
#         print(f"Usuario actual: {usuario_actual['nombre']} (Saldo: {usuario_actual['saldo']})")
#     mostrar_menu()
        
#     opcion = input("\nSeleccione una opción: ")
        
#     if opcion == "1":
#         registro_usuario()
#     elif opcion == "2":
#         if usuario_actual:   
#             print("\n--- Mi Perfil ---")
#             print(f"Nombre: {usuario_actual['nombre']}")
#             print(f"Correo: {usuario_actual['correo']}")
#             print(f"Edad: {usuario_actual['edad']}")
#             print(f"Saldo: {usuario_actual['saldo']}")
#             from recompensas import mostrar_logros
#             mostrar_logros(usuario_actual)
#             input("\nPresione Enter para continuar...")
#         else:
#             usuario = login_usuario('', '', False)
#             if usuario:
#                 usuario_actual = usuario
#                 print(f"Tu saldo actual es: {usuario_actual['saldo']}")
#                 input("\nPresione Enter para continuar...")
#     elif opcion == "3":
#         mostrar_usuarios()
        
#         input("\nPresione Enter para continuar...")
#     elif opcion == "4":
#         eliminar_usuario()
#         if usuario_actual and usuario_actual not in usuarios:  
#             usuario_actual = None
#         input("\nPresione Enter para continuar...")
#     elif opcion == "5":
#         if usuario_actual:
#             if usuario_actual['saldo'] < 100:
#                 print("\nNo tienes saldo suficiente para jugar (mínimo $100).")
#                 input("Presione Enter para volver al menú principal...")
#                 continue
#             from juego import jugar_blackjack
#             usuario_actual = jugar_blackjack(usuario_actual)
#             guardar_usuarios_json(usuario_actual)
#             input("\nPresione Enter para continuar...")
#         else:
#             print("Saliendo del sistema...")
#             break
#     elif opcion == "6" and usuario_actual:
        
#         logout()
#         input("\nPresione Enter para continuar...")
#     elif opcion == "7" and usuario_actual:
        
#         print("Saliendo del sistema...")
#         break
#     else:
#         print("Opción no válida. Intente de nuevo.")
#         input("\nPresione Enter para continuar...")