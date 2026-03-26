while True
print('Voce está no primiero laço.')
opcao1 = input('Deseja sair dele? Digite Sim para isso. \n')
if opcao1 == 'SIM':
    break # este break é do primiero laço
else:
    while True:
        print('Voce está no segundo laço.')
        opcao2 = input('Deseja sair dele? Digite Sim para isso. \n')
        if opcao2 == 'SIM':
            break # este break é do segundo laço
        print('Voce saiu do segundo laço.')
        print('Voce saiu do primeiro laço.')