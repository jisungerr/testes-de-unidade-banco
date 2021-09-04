class ContaDestino:
  def __init__(self, conta, titular, saldo, limite):
    self.conta = conta
    self.titular = titular
    self._saldo = saldo
    self.limite = limite