idade = int(input("Digite sua idade: "))
if idade < 10:
    print("Voce é uma criança.")
elif idade >= 10 and idade <= 15:
    print("Voce é um adolescente.")
elif idade >= 16 and idade < 18:
    print("Voce é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Voce é adulto.")
else
    print("Voce é um idoso.")