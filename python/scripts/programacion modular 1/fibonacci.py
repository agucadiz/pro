'''
# Ejercicio 4
Escribe un módulo llamado fibonacci.py que contenga las siguientes funciones:
'''
# Una función fib que calcule el n-ésimo término de la sucesión de Fibonacci de forma recursiva.

'''
Una función fib_iter que calcule lo mismo pero de forma iterativa llamando a
otra función_fib_aux(ojo, que empieza por ‘_), que es la que realmente lleva
a cabo el proceso iterativo.
'''

fib = lambda n: 0 if n == 0 else 1 if n == 1 else \
                fib(n - 1) + fib(n - 2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def _fib_aux(cont, a, b):
    if cont == 0:
        return a
    else:
        return _fib_aux(cont - 1, b, a + b)

def fib_iter(n):
    return _fib_aux(n, 0, 1)

if __name__ == "__main__":
    import sys
    print(fib(int(sys.argv[1])))
