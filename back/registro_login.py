
usuarios = []
def registro_usuario():
    mayor_edad = 18
    edad = int(input("ingresa tu edad"))
    if edad < mayor_edad:
        print("No puedes registrarte, eres menor de edad")
        return
    nombre = input("nombre: ")
    correo = input("correo @hotmail.com: ")
    contrasena = input("ingressa contrasena: ")
    saldo = 1000  

    nuevoUsuario = [contrasena, correo, nombre, saldo]
    usuarios.append(nuevoUsuario)
    print("Usuario registrado con exito !!")

def login_usuario():
    correo = input("correo @hotmail.com:")
    contrasena = input("ingressa contrasena:")
    for usuario in usuarios:
        if usuario[1] == correo and usuario[0] == contrasena:
            print("Bienvenido", usuario[2])
            return
    print("Usuario o contrasena incorrectos")
   