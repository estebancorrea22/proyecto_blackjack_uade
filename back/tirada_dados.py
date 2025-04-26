import random

dados_tirados=[]

sumar_dados= lambda dados: sum(dados)+(10 if 1 in dados and sum(dados) + 10 <= 21 else 0)

def tirar_dado(veces=1):
    nuevos_dado=[]
    for _ in range(veces):
        dado=random.randint(1, 10)
        nuevos_dado.append(dado)
    dados_tirados.extend(nuevos_dado)
    return nuevos_dado

tirar_dado(2)
