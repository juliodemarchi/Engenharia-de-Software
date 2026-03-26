# Métodos de classe
#servem para manipular os atributos de classe, ou seja, os atributos que são compartilhados por todas as instâncias da classe. Eles são definidos usando o decorador @classmethod e recebem a classe como primeiro argumento, geralmente nomeado como cls.

class Circulo2:
    __totalCirculos = 0 # Atributo privado

    def __init__(self, pontox, pontoy, raio):
        self.__pontox = pontox
        self.__pontoy = pontoy
        self.__raio = raio
        Circulo2.__totalCirculos += 1

        #@classmethod criar o método de classe
        @classmethod
        def get_total_circulos(cls):
            return cls.__totalCirculos
