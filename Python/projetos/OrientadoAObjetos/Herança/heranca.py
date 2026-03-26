# Classe Pai (Base)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo...")

# Classe Filha (Herda de Animal)
class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} diz: Au Au!")

# Classe Filha (Herda de Animal)
class Gato(Animal):
    def miar(self):
        print(f"{self.nome} diz: Miau!")

# Criando os objetos
dog = Cachorro("Rex")
cat = Gato("Felix")

# Usando métodos herdados e métodos próprios
dog.comer()  # Herdado de Animal
dog.latir()  # Próprio de Cachorro

cat.comer()  # Herdado de Animal
cat.miar()   # Próprio de Gato

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome) # Chama o __init__ do pai
        self.raca = raca       # Adiciona um atributo novo