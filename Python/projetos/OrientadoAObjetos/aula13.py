class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R$ {valor} realizada com sucesso de {self.titular} para {conta_destino.titular}!")
        else:
            print("Saldo insuficiente para realizar a transferência.")

    def gerar_extrato(self):
        print(f"Titular: {self.titular} | Saldo Atual: R$ {self.saldo}")

# 1. Criando as contas com os saldos iniciais solicitados
conta1 = ContaBancaria("Conta 1", 1000)
conta2 = ContaBancaria("Conta 2", 500)

print("--- Saldo Inicial ---")
conta1.gerar_extrato()
conta2.gerar_extrato()
print("-" * 30)

# 2. Conta1 envia 200 para a Conta 2
conta1.transferir(200, conta2)

print("\n--- Extrato Final ---")
# 3. Gerando extrato com o saldo atual
conta1.gerar_extrato()
conta2.gerar_extrato()