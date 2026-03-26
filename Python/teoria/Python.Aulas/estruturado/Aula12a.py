texto = 'Programação'
letra_para_contar = 'r'
contador = 0

for letra in texto:
    if letra == letra_para_contar:
        contador += 1

print(f"A letra '{letra_para_contar}' aparece {contador} vezes na palavra '{texto}'.")
    