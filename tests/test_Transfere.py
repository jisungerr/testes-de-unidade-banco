from unittest import TestCase
from main import Conta
from conta2 import ContaDestino

class TestesTransferir(TestCase):
  def test_transferir1(self):
      teste = Conta (5464, "Beatriz", 600,500)
      c2 = ContaDestino (4647, "IFPB", 4000, 800)
      resultado = teste.transferir(c2, 30)
      esperado = 570

      self.assertEqual(resultado, esperado)

  def test_transferir2(self):
      teste = Conta (3782, "Inês Brasil", 30,500)
      c2 = ContaDestino (94893, "Inês Portugal", 700, 1000)
      resultado = teste.transferir(c2, 50)
      esperado = 0

      self.assertEqual(resultado, esperado) 
