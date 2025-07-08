#funciones para darle opciones al usuario de en que mesa va a jugar 
def mesa1(usuario):
    if usuario['saldo'] >= 1000:
        print("Mesa 1: Apuesta mínima de 1000")
        return True
    else:
        print("No tienes suficiente saldo para jugar en la Mesa 1.")
        return False
def mesa2(usuario):
    if usuario['saldo'] >= 5000:
        print("Mesa 2: Apuesta mínima de 5000")
        return True
    else:
        print("No tienes suficiente saldo para jugar en la Mesa 2.")
        return False
def mesa3(usuario):
    if usuario['saldo'] >= 10000:
        print("Mesa 3: Apuesta mínima de 10000")
        return True
    else:
        print("No tienes suficiente saldo para jugar en la Mesa 3.")
        return False
    
#usuario elije la mesa
def elegir_mesa(usuario):
    print("Elige una mesa para jugar:")
    print("1. Mesa 1 (Apuesta mínima de 1000)")
    print("2. Mesa 2 (Apuesta mínima de 5000)")
    print("3. Mesa 3 (Apuesta mínima de 10000)")
    
    opcion = input("Ingresa el número de la mesa que deseas elegir: ")
    
    if opcion == '1':
        return mesa1(usuario)
    elif opcion == '2':
        return mesa2(usuario)
    elif opcion == '3':
        return mesa3(usuario)
    else:
        print("Opción no válida. Por favor, elige una mesa válida.")
        return False