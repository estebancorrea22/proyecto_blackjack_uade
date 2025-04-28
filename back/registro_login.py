
usuarios = []

def registro_usuario():
    mayor_edad = 18
    edad = int(input("Ingresa tu edad"))
    if edad < mayor_edad:
        print("No puedes registrarte, eres menor de edad")
        return
    nombre = input("Nombre: ")
    correo = input("Correo @hotmail.com: ")
    contrasena = input("Ingresa contrasena: ")
    saldo = 1000  

    nuevoUsuario = [contrasena, correo, nombre, saldo]
    usuarios.append(nuevoUsuario)
    print("Usuario registrado con exito !!")

def login_usuario():
    correo = input("Correo @hotmail.com:")
    contrasena = input("Ingresa contrasena:")
    for usuario in usuarios:
        if usuario[1] == correo and usuario[0] == contrasena:
            print("Bienvenido", usuario[2])
            return
    print("Usuario o contrasena incorrectos")
   