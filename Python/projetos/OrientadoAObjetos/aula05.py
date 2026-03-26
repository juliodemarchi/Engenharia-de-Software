class Lampada:
    # Atributos de classe (valores padrão para todos os objetos)
    estado = "desligada"
    cor = "branca"

    # Métodos que alteram ou exibem o estado
    def ligar(self):
        self.estado = "ligada"
        print("A lâmpada foi acesa!")

    def exibir_info(self):
        print(f"Status: {self.estado} | Cor: {self.cor}")

# Criando o objeto (instanciando sem passar argumentos)
minha_lampada = Lampada()

# Acessando e modificando atributos diretamente
minha_lampada.exibir_info()
minha_lampada.ligar()
minha_lampada.exibir_info()