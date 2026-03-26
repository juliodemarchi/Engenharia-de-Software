# HERANÇA: Definindo a classe pai
class Passaro:
    def voar(self):
        print("O pássaro está voando...")

    def emitir_som(self):
        print("Som genérico de pássaro")

# HERANÇA: Falcao herda de Passaro
class Falcao(Passaro):
    def emitir_som(self): # POLIMORFISMO: Sobrescrevendo o método
        print("Som de Falcão: Kreeee!")

# HERANÇA: Pinguim herda de Passaro
class Pinguim(Passaro):
    def voar(self): # POLIMORFISMO: Mudando o comportamento de voar
        print("Pinguins não voam, eles nadam!")
    
    def emitir_som(self):
        print("Som de Pinguim: Honk!")

# Testando o Polimorfismo
aves = [Falcao(), Pinguim()]

for ave in aves:
    ave.emitir_som() # O mesmo comando gera resultados diferentes