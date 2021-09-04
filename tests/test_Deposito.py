from unittest import TestCase
from main import Conta

class TestesDeposito(TestCase):
  def test_deposito1(self):
    teste = Conta (222, "Maria", 200,500)
    resultado = teste.depositar(50)
    esperado = 250

    self.assertEqual(resultado, esperado)

  def test_deposito2(self):
    teste = Conta (914, "Jisung", 1000,500)
    resultado = teste.depositar(7)
    esperado = 1001

    self.assertEqual(resultado, esperado) 
