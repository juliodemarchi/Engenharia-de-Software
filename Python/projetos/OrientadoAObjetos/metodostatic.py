#Método staticomethod
class MinhaClasse:
    @staticmethod
    def metodo_estatico(x, y):
        return x + y
    

# Usando o método estático
resultado = MinhaClasse.metodo_estatico(3, 5)
print(resultado)  # Saída: 8

#Note que voce não precisa criar uma isntancia da classe para chamar o método estático, basta usar o nome da classe seguido do nome do método.
obj = MinhaClasse()
resultado = obj.metodo_estatico(10, 20)
print(resultado)  # Saída: 30
