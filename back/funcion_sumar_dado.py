from funcion_tirar_dados_inicio import tirar_dados

def sumar_dados(mano):
    total_dados = sum(mano)
    if 1 in mano and total_dados + 10 <= 21:
        return total_dados + 10
    return total_dados

mano = tirar_dados()
print(f"Tirada: {mano}")
print(f"Total mano: {sumar_dados(mano)}")