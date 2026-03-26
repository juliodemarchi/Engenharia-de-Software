# Somente pode ser alterado por um método da classe
# O método é o único responsável por alterar o estado do objeto

class Conta:
    def __init__(self, numero, saldo):
        self.numero = numero # Atributo privado
        self.saldo = saldo # Atributo privado

    def main():
        conta = Conta(1, 1000)
        saldo = conta.saldo
        print(saldo)