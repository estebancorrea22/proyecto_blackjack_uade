from functools import reduce

"""
    La funcion recargar_saldo_tarjeta permite a un usuario recargar su saldo
    ingresando su correo y el numero de su tarjeta de credito (teniendo en cuenta que la tarjeta tiene un minimo de 16 digitos) y si el monto que se quiere recargar es menor o igual a 0 no se recarga el salddo y esto se informa al usuario, en caso de que la recarga sea exitosa se informa al usuario el nuevo saldo
    
    Se utiliza la funcion built-in de python "next()" y la funcion iterable "filter()" para buscar el usuario en la lista de usuarios
    
    Despues de validar que el monto a ingresar es mayor a 0 se convierte a float y se suma al saldo del usuario
"""

def recargar_saldo_tarjeta(usuarios):
    correo = input("Ingrese correo al que se le va a recargar saldo: ")
    usuario = next(filter(lambda u: u['correo'] == correo, usuarios),None)
    
    if not usuario:
        print("Usuario no encontrado")
        return

    tarjeta = input("Ingrese el numero de su tarjeta de credito (16 dígitos): ")
    while len(tarjeta) != 16 or not tarjeta.isdigit():
        print("El numero de tarjeta es invalido. Debe tener minimo 16 digitos.")
        tarjeta = input("Ingrese el numero de su tarjeta de credito (16 dígitos): ")

    monto = input("Ingrese el monto a recargar: ")
    while not monto.isdigit() or float(monto) <= 0:
        print("Monto invalido. Debe ser un numero mayor a 0")
        monto = input("Ingrese el monto que desea recargar: ")

    monto = float(monto) 
    usuario["saldo"] += monto
    print(f"Saldo recargado exitosamente! Nuevo saldo de {usuario['nombre']}: {usuario['saldo']}")
  
  
"""
    La funcion calcular_saldo_total nos deja saber cual es el saldo total de los usuarios registrados, usando "reduce" de la libreria "functools" para iterar sobre la lista de usuarios y sumar el saldo de cada uno, devolviendo el saldo total al final
"""  
def calcular_saldo_total(usuarios):
    saldo_total = reduce(lambda acc, u: acc + u["saldo"], usuarios, 0)
    print(f"El saldo total de todos los usuarios es: {saldo_total}")
    return saldo_total
