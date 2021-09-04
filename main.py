from unittest import main
from conta2 import ContaDestino

class Conta (ContaDestino):
    def __init__(self, conta, titular, saldo, limite):
      super().__init__(conta, titular, saldo, limite)

    def depositar(self, valor):
      if valor > 0:
        self._saldo += valor
        print ("Foi depositado o valor de %s reais na sua conta. O saldo agora é R$%s,00" % (valor, self._saldo))
        return self._saldo

    def sacar(self, valor):
      if self._saldo < valor or self.limite < valor:
        print ("Não é possível sacar este valor")
        return None

      else:
        self._saldo -= valor
        print("Foi sacado o valor de %s reais da sua conta. O saldo agora é de R$%s,00" % (valor, self._saldo))
        return self._saldo

    def transferir (self, destino, valor):
      destino = destino
      if self._saldo > valor or self.limite > valor:
        self._saldo -= valor
        destino._saldo += valor
        print ("Valor transferido foi R$%s,00. Saldo da conta destino: R$%s,00. Seu saldo atual: R$%s,00" % (valor, destino._saldo, self._saldo))
        return self._saldo
      
      else:
        print("Valor inválido para transferir")
        return None


    def extrato (self):
      return self._saldo       


if __name__ == '__main__':
    main()
