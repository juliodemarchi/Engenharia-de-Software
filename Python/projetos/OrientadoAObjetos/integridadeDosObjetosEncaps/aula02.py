# burlando atributos privados em Python
# Em Python não possui atributos verdadeiramente privados

from Classes.Conta import Conta

conta = Conta(1, 1000)
saldo1 = conta._Conta__saldo  # Acessando atributo privado (não recomendado)
print(saldo1)

saldo2 = conta.saldo  # Acessando atributo público
print(saldo2)