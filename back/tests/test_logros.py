# tests/test_logros.py
from logros import verificar_logros, LOGROS

class TestLogros:
    def test_primer_juego(self):
        usuario = {'logros': {'logros_obtenidos': []}}
        logros = verificar_logros(usuario, 'primer_juego')
        assert 'Primer juego' in logros
        assert len(usuario['logros']['logros_obtenidos']) == 1

    def test_blackjack(self):
        usuario = {'logros': {'logros_obtenidos': []}}
        logros = verificar_logros(usuario, 'blackjack', [10, 1])
        assert 'Blackjack' in logros