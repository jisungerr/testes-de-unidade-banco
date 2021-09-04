from unittest import  TestCase
from main import Conta

class TesteExtrato(TestCase):
  def test_extrato(self):
    teste = Conta (6574, "Edwiges", 450, 500)
    resultado = teste.extrato()

    self.assertEqual(resultado, 450)
