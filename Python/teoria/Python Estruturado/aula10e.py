# Utilizando o numpy para calcular as raizes
# importando o numy
import numpy as np

# Criando a função para calcular as raizes da equação de segundo grau

def calcular_raizes(a, b, c):
    # Coeficientes da equação
    coeficientes = [a, b, c]

    # usando numpy.roots para calcular as raizes
    raizes = np.roots(coeficientes)
    return raizes

# Solicitando o coeficientes ao usuário
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

# Calculando as raizes
raizes = calcular_raizes(a, b, c)

# Imprimindo os resultados
print(f"As raizes da equação são: {raizes[0]} e {raizes[1]}")