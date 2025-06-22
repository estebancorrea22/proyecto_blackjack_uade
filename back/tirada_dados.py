import random

dados_tirados=[]

sumar_dados= lambda dados: sum(dados)+(10 if 1 in dados and sum(dados) + 10 <= 21 else 1)

def tirar_dado(veces=1):
    nuevos_dado=[]
    for _ in range(veces):
        dado=random.randint(1, 10)
        nuevos_dado.append(dado)
    dados_tirados.extend(nuevos_dado)
    return nuevos_dado

def evaluar_mano(mano):
    total = sumar_dados(mano)
    if total > 21:
        return "pasado", total
    elif total == 21:
        return "blackjack", total
    else:
        return "jugando", total
