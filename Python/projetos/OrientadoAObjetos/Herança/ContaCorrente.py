from OrientadoAObjetos import ContaBancaria01


class ContaCorrente(ContaBancaria01):
    def __init__(self, titular, saldo_inicial=0, limite=500):
        # O super() traz o construtor da classe pai
        super().__init__(titular, saldo_inicial)
        self.limite = limite

    # Sobrescrevemos o método sacar para considerar o limite
    def sacar(self, valor):
        if 0 < valor <= (self._saldo + self.limite):
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado (usando limite).")
        else:
            print("Limite excedido!")

class ContaPoupanca(ContaBancaria01):
    def aplicar_rendimento(self, taxa):
        rendimento = self._saldo * taxa
        self._saldo += rendimento
        print(f"Rendimento de R${rendimento:.2f} aplicado!")