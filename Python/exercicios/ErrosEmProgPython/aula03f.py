nr = eval(input("Digite um número: ")) # Erro de sintaxe: falta de parênteses
s = nr * 3 # Erro de tipo: não é possível multiplicar uma string por um número inteiro
print(s) # Erro de nome: a variável 's' não foi definida devido ao erro anterior
q = 12/s # Erro de divisão por zero: se 's' for zero, isso causará um erro
print(q) # Erro de nome: a variável 'q' não foi definida devido ao erro anterior