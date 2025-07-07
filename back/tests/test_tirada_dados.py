# tests/test_tirada_dados.py
import pytest
from tirada_dados import sumar_dados, evaluar_mano, tirar_dado

class TestTiradaDados:
    @pytest.mark.parametrize("mano,esperado", [
        ([1, 10], 21),       # Blackjack
        ([1, 5, 5], 21),     # As flexible (11 + 5 + 5 = 21)
        ([10, 10, 1], 21),   # As ajustado (10 + 10 + 1)
        ([7, 7, 7], 21),     # 21 normal
        ([1, 1, 1], 13),     # Múltiples Ases
        ([10, 10], 20)       # Sin Ases
    ])
    def test_sumar_dados(self, mano, esperado):
        assert sumar_dados(mano) == esperado

    @pytest.mark.parametrize("mano,estado_esperado", [
        ([1, 10], "blackjack"),
        ([10, 10, 1], "jugando"),
        ([10, 10, 10], "pasado"),
        ([5, 5], "jugando")
    ])
    def test_evaluar_mano(self, mano, estado_esperado):
        estado, _ = evaluar_mano(mano)
        assert estado == estado_esperado

    def test_tirar_dado(self):
        dados = tirar_dado(3)
        assert len(dados) == 3
        assert all(1 <= dado <= 10 for dado in dados)