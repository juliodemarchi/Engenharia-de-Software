import datetime
from Contass.Extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(f"DEPOSITO", valor, datetime.datetime.today())

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente {self.numero}")
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(f"SAQUE", valor, datetime.datetime.today())
            return True
        
    def transfere_valor(self, conta_destino, valor):
        if self.sacar < valor:
            return "Não existe saldo suficiente para realizar a transferência"
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(f"TRANSFERENCIA", valor, datetime.datetime.today())
            return "Transferência realizada com sucesso"
        
    def gerar_saldo(self):
        print(f'Conta: {self.numero}')
        print(f'Saldo: R${self.saldo:10.2f}')