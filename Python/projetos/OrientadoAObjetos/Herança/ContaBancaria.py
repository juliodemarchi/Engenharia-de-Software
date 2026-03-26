class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial  # Usamos '_' para indicar que é um atributo protegido

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self._saldo:.2f}")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
            return True
        else:
            print("Saldo insuficiente ou valor inválido.")
            return False