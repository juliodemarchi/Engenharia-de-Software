class Conta:

    def __init__(self, numero, saldo):
        self.__numero = numero # Atributo privado
        self.__saldo = saldo # Atributo privado
        
        def sacar(self, valor):
            if self.__saldo < valor:
                return False
            else:
                self.__saldo -= valor
                self.extrato.transacoes.append(["SACAR VALOR"])
                return True