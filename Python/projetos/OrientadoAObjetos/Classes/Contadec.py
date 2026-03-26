# Classe com decorador property

class Contadec:
    def __init__(self, numero):
        self.__numero = numero # Atributo privado
        self.__saldo = 0 # Atributo privado

    @property # definindo método decorado
    def saldo(self):
        return self.__saldo

    @saldo.setter # definindo método setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo inválido")
        else:
            self.__saldo = saldo