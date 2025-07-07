from tirada_dados import sumar_dados, evaluar_mano, tirar_dado

#pruebas unitarias para la tirada de dados con pytest

def test_tirar_dado():
    resultados = tirar_dado(5)
    assert len(resultados) == 5  
    for resultado in resultados:
        assert 1 <= resultado <= 10 

def test_sumar_dados():
    mano = [1, 5, 10]
    total = sumar_dados(mano)
    assert total == 16  

    mano = [1, 1, 1]  
    total = sumar_dados(mano)
    assert total == 13  

    mano = [10, 10]  
    total = sumar_dados(mano)
    assert total == 20
    
def test_evaluar_mano():
    total = sumar_dados([1, 10])
    estado, total = evaluar_mano([1, 10])
    assert estado == "blackjack"
    assert total == 21
    estado, total = evaluar_mano([1, 5, 10])
    assert estado == "jugando"
    assert total == 16
    estado, total = evaluar_mano([10, 5, 7])
    assert estado == "pasado"
    assert total == 22  