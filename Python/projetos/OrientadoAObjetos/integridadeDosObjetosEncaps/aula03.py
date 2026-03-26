#Métodos decorados e atributos

class Conta:
    def __init__(self, numero):
        self.__numero = numero # Atributo privado
        self.__saldo = 0 # Atributo privado


# Ultilizando o decorator @property, podemos proteger os atributos eacessa-los somente por meio de métodos "decorados"
@property # definindo método decorado
def numero(self):
    return self._saldo

# O decorador @setter força todas alterações de valor dos atributos privados a passar por esses métodos.
@saldo.setter # definindo método setter
def saldo(self, saldo):
    if saldo < 0:
        print("Saldo inválido")
    else:
        self._saldo = saldo