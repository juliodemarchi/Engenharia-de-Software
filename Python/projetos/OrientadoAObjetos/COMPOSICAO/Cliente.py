# Construtores e metodo init e self
# Self é a forma da classe se referir a ela mesma
# --init-- é o método construtor que criar o objeto da classe

class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

        