





from Contass.Conta import Conta
from Contass.Poupanca import Poupanca


class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, taxa_remuneracao, clientes, numero, saldo):
        #inicializar os atributos herdados da classe conta
        Conta.__init__(self, clientes, numero, saldo)
        #Inicializar os atributos herdados da classe poupança
        Poupanca.__init__(self, taxa_remuneracao)


    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxa_remuneracaoMes / 30)