# Instanciando um objeto conta
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo


# Observe os parametros passados na criação do objeto

def main():
    c1 = Conta(1, 1, "Joao", 1000) # Objeto criado a partir da classe conta
    print(f'Nome do titular da conta: {c1.nomeTitular}')
    print(f'Número da conta: {c1.numero}')
    print(f'CPF do titular: {c1.cpf}')
    print(f'Saldo da conta: {c1.saldo}')

# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será true e a função main() será executada.
# Se esse script for importado por outro script, a variável NAME referente a ele terá valor igual ao nome do arquivo (sem extensão) e a função main() não será executada.
if __name__ == "__main__":
    main()
    