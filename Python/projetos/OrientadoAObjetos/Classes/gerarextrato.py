# Classe conta

from Classes.Contadec import Contadec

def main():
    conta = Contadec(1)
    conta.saldo = 1000 #usando o @saldo.setter para atribuir o valor
    print(f'saldo da conta = {conta.saldo}')
                              
if __name__ == "__main__":
    main()