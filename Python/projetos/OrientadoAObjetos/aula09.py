# Método com retorno
# O método com retorno serve para validar o estado de um objeto

class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
    def gerar_extrato(self):
        print(f'numero: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}')

def main():
    c1 = Conta(1, 1, "João", 1000)
    c1.depositar(9000) # cahamando o método depositar
    c1.gerar_extrato() # chamando o método gerar_extrato
    c1.sacar(500) # chamando o método sacar
    c1.gerar_extrato() # chamando o método gerar_extrato final

if __name__ == "__main__":
    main()