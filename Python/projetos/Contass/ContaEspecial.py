from Contass.Conta import Conta
import datetime

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite < valor:
            print(f"Saldo insuficiente {self.numero}")
            return False
        else:
            self.saldo -= valor
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(["saque", valor, datetime.datetime.today()])
            return True
        
# Método depositar precisa ser reescrito para a conta especial
def depositar(self, valor):
    pass