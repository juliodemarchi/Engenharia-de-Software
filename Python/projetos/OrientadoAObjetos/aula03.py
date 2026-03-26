# A CLASSE (O molde)
class Celular:
    # Construtor e Atributos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    # Métodos (Comportamentos)
    def ligar(self):
        self.ligado = True
        print(f"O {self.modelo} está ligado.")

# O OBJETO (A instância)
meu_celular = Celular("Apple", "iPhone 15")
seu_celular = Celular("Samsung", "S24")

meu_celular.ligar() # Ação realizada pelo objeto