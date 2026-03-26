# Realizando a agregação
from Conta import Conta
from Cliente import Cliente

cliente1 = Cliente(123, "Joao", "Rua das Flores, 0123")
cliente2 = Cliente(456, "Maria", "Rua das Palmeiras, 0456")
# criando uma conta com dois clientes, fazendo a agregacao com uma lista
conta1 = Conta([cliente1, cliente2], 1, 0)

conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()
