import datetime

class Poupanca:
    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracaoMes = taxa_remuneracao
        self.dataAbertura = datetime.datetime.today()

    def remuneraConta(self):
        self.saldo += self.saldo * self.taxa_remuneracaoMes