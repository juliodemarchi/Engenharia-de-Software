# Construtores e metodo init e self
# Self é a forma da classe se referir a ela mesma
# --init-- é o método construtor que criar o objeto da classe

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

        