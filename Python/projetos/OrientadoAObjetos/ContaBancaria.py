class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial # Este é o 'estado' que o objeto guarda

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor  # O objeto subtrai do seu próprio saldo atual
            conta_destino.saldo += valor # O objeto destino soma ao seu saldo atual
            print(f"Transferência de R${valor} realizada: {self.titular} -> {conta_destino.titular}")
        else:
            print(f"Erro: {self.titular} tentou enviar R${valor}, mas o saldo é insuficiente.")

    def gerar_extrato(self):
        print(f"Extrato -> {self.titular}: R${self.saldo}")

# --- EXECUÇÃO PASSO A PASSO ---

# 1. Criando as contas
conta1 = ContaBancaria("Conta 1", 1000)
conta2 = ContaBancaria("Conta 2", 500)

# 2. Primeira transferência (Conta 1 perde 200, fica com 800)
conta1.transferir(200, conta2)

# 3. Segunda transferência (Conta 1 perde mais 300, deve levar em conta os 800)
conta1.transferir(300, conta2)

# 4. Agora Conta 2 devolve um valor (Conta 2 tinha 500 + 200 + 300 = 1000)
conta2.transferir(100, conta1)

print("\n--- Resultado Final ---")
conta1.gerar_extrato() # Deve mostrar 600 (1000 - 200 - 300 + 100)
conta2.gerar_extrato() # Deve mostrar 900 (500 + 200 + 300 - 100)