# Testando métodos com retorno

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
    valor_saque = 400
    resultado_saque = c1.sacar(valor_saque)

    # validando o retorno para verificar se o saque foi realizado com sucesso
    if resultado_saque:
        print(f'Saque de R${valor_saque} realizado com sucesso!')
        print(f'Saldo atual: R${c1.saldo}')
    else:
        print("Saldo insuficiente para realizar o saque.")

if __name__ == "__main__":
    main()