from datetime import date

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

@classmethod
def apartiranonasc(cls, nome, ano):
    return cls(nome, date.today().year - ano)
#metodo estático para verificar se é maior de idade
@staticmethod
def ehmaior(idade):
    return idade >= 18
pessoa1 = pessoa (nome='Ventury', idade=62)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa.ehmaior(pessoa1.idade))
pessoa2 = pessoa.apartiranonasc(nome='Maria', ano=1990)
print(pessoa2.nome)
print(pessoa2.idade)
print(pessoa.ehmaior(pessoa2.idade))
