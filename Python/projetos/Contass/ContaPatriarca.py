class ContaPatriarca:
    def __init__(self, titular, saldo_total):
        self.titular = titular
        self._saldo = saldo_total
        self.historico = []

    def exibir_patrimonio(self):
        print(f"Patrimônio total de {self.titular}: R${self._saldo:,.2f}")

class ContaHerdeiro(ContaPatriarca):
    def __init__(self, titular, parentesco):
        # O herdeiro começa com saldo 0, pois a herança ainda será recebida
        super().__init__(titular, saldo_total=0)
        self.parentesco = parentesco

    def receber_heranca(self, conta_pai, valor):
        if valor <= conta_pai._saldo:
            # Lógica da transferência
            conta_pai._saldo -= valor
            self._saldo += valor
            
            # Gerando o extrato de transferência
            extrato = (
                f"\n--- EXTRATO DE TRANSFERÊNCIA DE HERANÇA ---\n"
                f"Doador: {conta_pai.titular}\n"
                f"Beneficiário: {self.titular} ({self.parentesco})\n"
                f"Valor Recebido: R${valor:,.2f}\n"
                f"Novo Saldo do Herdeiro: R${self._saldo:,.2f}\n"
                f"------------------------------------------"
            )
            print(extrato)
        else:
            print(f"Erro: O patrimônio de {conta_pai.titular} é insuficiente para esta transferência.")

# --- Execução do Exemplo ---

# 1. Criamos a conta do Pai com um saldo de 1 milhão
pai = ContaPatriarca("Carlos Silva", 1000000)
pai.exibir_patrimonio()

# 2. Criamos a conta da Filha (que herda a estrutura de ContaPatriarca)
filha = ContaHerdeiro("Julia Silva", "Filha")

# 3. Realizamos a transferência da herança
filha.receber_heranca(pai, 250000)

# 4. Verificamos os saldos finais
pai.exibir_patrimonio()
filha.exibir_patrimonio()