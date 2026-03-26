#docstring
#Determina o n-ésimo termo da sequência de Fibonacci
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
vfibo= fibo(3)
print(vfibo)
print(help(fibo))
