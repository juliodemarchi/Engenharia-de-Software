# Função recursiva fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)
vfat = fatorial(5)
print(f'resultado recursiva: {vfat}')

# Função fatorial não recursiva
def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
            fat = fat*x
        return fat
    vfat = fatorial(5)
    print(f'resultado iterativa: {vfat} ')