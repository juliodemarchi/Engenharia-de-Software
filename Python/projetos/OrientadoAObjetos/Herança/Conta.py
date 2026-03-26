# Criando uma Conta Corrente
from OrientadoAObjetos.Herança import ContaCorrente


minha_cc = ContaCorrente
("Maria", 1000, 200)
minha_cc.consultar_saldo() # Herdado do pai
minha_cc.sacar(1150)       # Usa a lógica específica da filha
minha_cc.consultar_saldo()

print("-" * 20)

# Criando uma Conta Poupança
minha_poupanca = ContaCorrente.ContaPoupanca("João", 5000)
minha_poupanca.aplicar_rendimento(0.05) # Método exclusivo da Poupança
minha_poupanca.consultar_saldo()