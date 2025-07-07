# tests/test_apuestas.py
import pytest 
from apuestas import realizar_apuesta, doblar_apuesta

class TestApuestas:
    def test_realizar_apuesta_valida(self, monkeypatch):
        usuario = {'saldo': 1000}
        monkeypatch.setattr('builtins.input', lambda _: '500')
        apuesta, _ = realizar_apuesta(usuario)
        assert apuesta == 500

    def test_realizar_apuesta_invalida(self, monkeypatch):
        usuario = {'saldo': 1000}
        inputs = iter(['1500', '500'])  # Primero inválida, luego válida
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        apuesta, _ = realizar_apuesta(usuario)
        assert apuesta == 500

    def test_doblar_apuesta_saldo_suficiente(self):
        usuario = {'saldo': 1000}
        mano = [10, 5]
        nueva_mano, nueva_apuesta, total, estado, _ = doblar_apuesta(
            mano, 500, usuario
        )
        assert nueva_apuesta == 1000
        assert len(nueva_mano) == 3