#Chamando método privado dentro de um método público
class MinhaClasse:
    def __init__(self, valor):
        self.atributo_privado = 42

    def metodo_privado1(self):
        print("Este é um método privado.")
        

    def metodo_publico1(self):
        print("Este é um método público1.")
        self._metodo_privado1()

    def _metodo_privado2(self):
        print("Este é outro método fortemente privado.")
        self._metodo_privado2()

    def metodo_publico2(self):
        print("Este é um método público2.")
        self._metodo_privado2()


obj = MinhaClasse()
obj.metodo_publico1() # Chama o método publico que por sua vez chama o método privado
# Saida:
# Este é um método público1.
# Este é um método privado.

#Embora não seja recomendado, voce ainda pode chamar diretamente o método privado, mas isso é considerado uma má prática e deve ser evitado.
obj._metodo_privado1() # Funciona, mas vai contra a convenção de privacidade e pode levar a problemas de manutenção no futuro.

#Acessar diretamente o método fortemente privado não funciona:
#obj.__metodo_fortemente_privado() # Isso gera um AttributeError, pois o método fortemente privado não é acessível diretamente fora da classe.
obj._MinhaClasse__metodo_fortemente_privado2() # Funciona, mas não é recomendado
#Saida:
# Este é um método fortemente