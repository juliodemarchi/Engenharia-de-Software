for num in range (1000, 10000):
    menor = num % 100 #obtem o numero dos algarismos menos significativos
    maior = num // 100 #obtem o numero dos algarismos mais significativos
    raiz = menor + maior #obtem a raiz

    if (raiz * raiz) == num: # valida se a  raiz gera o numero testado
        print(f"Number: {num}")
        print(f"Halves: {maior} and {menor}")
        print(f"Sum: {raiz} -> {raiz}² = {num}")
        print("-" * 10)

print('terminou')
print('saiu', num)