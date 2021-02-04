"""
Diseñar una función recursiva que describa el numero de movimientos necesarios para resolver
un juego de hanoi, dependiendo del numero de discos.

/
|Pre: n >= 0 and (True) ignorar esto
|hanoi(n: int, a: str, b: str, c: str) --> str
|Post: hanoi(n, a, b, c) = una cadena con lso movimientos que hay que ralizar para resolver
|                            el puzzle de mover n discos de "a" a b, con c como pivote de
|                            auxiliar en el puzzle de las torres de Hanoi.
\


hanoi(n, a, b, c) = '' si n == 0 (caso base)
                        hanoi(n - 1, a, c, b) +
                        'mover un disco del ' + a + ' al ' + b + '\n'
                        hanoi(n - 1, c, b, a)
"""

#SOCORRO!
hanoi= lambda n, a, b, c: '' if n == 0 else \
                            hanoi(n - 1, a, c, b) + \
                            'muevo un disco del ' + a + ' al ' + b + '\n' + \
                            hanoi(n - 1, c, b, a)
