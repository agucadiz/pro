"""
# jaja
numero = int(input('Introduzca un numerio: '))

i = 0
res = 1
while i < numero:
    i += 1
    res *= i

print('El fact de ', numero, 'es: ', res)


1 fact = lambda n: n if n== 0 else n * fact(n - 1)

fact_iter = lambda con, acc: acc if con == 0 else \
                            fact_iter(cont - 1, acc * cont)

cont = numero
acc = 1

while cont > 0:

    acc, cont = acc * cont, cont - 1

print(acc)

a = 0 # fib(0)
b = 1 # fib(1)
"""

n = int(input('Introduzca un numero: '))
if n <= 1:
    a = n
else:
    a = 0 # fib(0)
    b = 1 # fib(1)
    while a < n - 1:
        a, b = b, a + b

print(a)
