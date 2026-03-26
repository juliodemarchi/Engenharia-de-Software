# Exemplo de uso de modulos
# Calcular as raizes de uma equação do segundo grau
# x2 + 5x + 6 = 0
# raizes {-3, -2}

import math
# Função para calcular as raizes da equação de segundo grau

def calcular_raizes(a, b, c):
    # Calcula o discriminante
    delta = b ** 2 - 4 * a * c

    # Verifica se o descriminante é positivo, negativo ou zero
    if delta > 0:
        #Duas raizes reais e distintas
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return (raiz1, raiz2)
    elif delta == 0:
        # Uma raiz real (duas raizes reais e iguais)
        raiz = -b / (2 * a)
        return (raiz,)
    else: 
        # Raizes complexas (discriminante negativo)
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(-delta) / (2 * a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return (raiz1, raiz2)
    

# Solicitando os coeficientes ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calculando as raízes
raizes = calcular_raizes(a, b, c)

# Imprimindo os resultados
if len(raizes) == 2:
    print(f'As raízes da equação são: {raizes[0]} e {raizes[1]}')
else:
    print(f'A raiz da equação é: {raizes[0]}')