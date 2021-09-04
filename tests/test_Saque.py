from unittest import TestCase
from main import Conta


class TestesSaca(TestCase):
    def test_saca1(self):
        teste = Conta(885, "Han", 700, 500)
        resultado = teste.sacar(100)

        self.assertEqual(resultado, 600)

    def test_saca2(self):
        teste = Conta(325, "Iriany", 1500, 500)
        resultado = teste.sacar(900)

        self.assertEqual(resultado, 600)
