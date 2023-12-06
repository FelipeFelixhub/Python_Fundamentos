class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def exibir_saldo(self):
        return self._saldo
conta = Conta(100)
conta.depositar(200)
conta.sacar(50)

print(conta.exibir_saldo())

