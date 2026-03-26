class Circulo:
    totalCirculos = 0

    def __init__(self, pontox, pontoy, raio):
        self.__pontox = pontox
        self.__pontoy = pontoy
        self.__raio = raio
        Circulo.totalCirculos += 1

#Primeiro teste
circ1 = Circulo(1, 1, 10)
print(circ1.totalCirculos) 

#Segundo teste
circ2 = Circulo(2, 2, 20)
print(circ2.totalCirculos)
#print(circ1.totalCirculos)


