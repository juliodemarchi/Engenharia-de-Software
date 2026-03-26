class Relogio:
    def mostrar_hora(self):
        return "14:30"

class Calendario:
    def mostrar_data(self):
        return "12/02/2026"

# O Smartwatch herda de ambas as classes
class Smartwatch(Relogio, Calendario):
    def resumo_do_dia(self):
        hora = self.mostrar_hora()
        data = self.mostrar_data()
        print(f"Hoje é {data} e agora são {hora}.")

# Testando
meu_relogio = Smartwatch()
meu_relogio.resumo_do_dia()