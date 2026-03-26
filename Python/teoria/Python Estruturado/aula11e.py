import numpy as np

def calcular_raizes(a, b, c):
    # O numpy.roots espera os coeficientes em ordem: ax^2 + bx + c
    coeficientes = [a, b, c]
    return np.roots(coeficientes)

# Entrada de dados
try:
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    if a == 0:
        print("Se 'a' é zero, a equação não é de segundo grau!")
    else:
        raizes = calcular_raizes(a, b, c)

        print("\n--- Resultados ---")
        # Itera sobre as raízes encontradas, não importa quantas sejam
        for i, r in enumerate(raizes, 1):
            print(f"Raiz {i}: {r}")

except ValueError:
    print("Erro: Por favor, digite apenas números.")