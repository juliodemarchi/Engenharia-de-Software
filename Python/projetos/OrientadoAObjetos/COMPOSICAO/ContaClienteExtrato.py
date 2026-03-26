# A composição é uma forma mais forte de associação, onde um objeto é parte de outro objeto.


import datetime

from Extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(('Depósito', valor, "Data", datetime.datetime.today()))

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(('Saque', valor, "Data", datetime.datetime.today()))
            return True
        
    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return 'Não existe saldo suficiente'
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(('Transferência', valor, "Data", datetime.datetime.today()))
            return 'Transferência realizada com sucesso!'
    
    def gerarsaldo(self):
        print(f'numero: {self.numero} saldo: {self.saldo} clientes: {self.clientes}')