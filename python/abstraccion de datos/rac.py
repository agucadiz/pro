from math import gcd


def racional(x, y):
    return pareja(x, y)

def pareja(x, y):
    """Devuelve una función que representa una pareja."""
    def get(indice):
        if indice == 0:
            return x
        elif indice == 1:
            return y
    return get

"""
Selectores
"""
def select(p, i):
    """Devuelve el elemento situado en el índice i de la pareja p."""
    return p(i)

def numer(r):
    """El numerador es el primer elemento de la lista."""
    return select(r, 0)

def denom(r):
    """El denominador es el segundo elemento de la lista."""
    return select(r, 1)

def set_numer(r, v):
    """El numerador es el primer elemento de la lista."""
    return select(r, 0, v)

def set_denom(r, v):
    """El denominador es el segundo elemento de la lista."""
    return select(r, 1, v)

'''
def set_numer(r, v):
    """El numerador es el primer elemento de la lista."""
    r[0] = v

def set_denom(r, v):
    """El denominador es el segundo elemento de la lista."""
    r[1] = v
'''

"""
Ecuaciones
"""
def suma(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return racional(nx * dy + ny * dx, dx * dy)

def mult(x, y):
    return racional(numer(x) * numer(y), denom(x) * denom(y))

def iguales(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def imprimir(x):
    print(numer(x), '/', denom(x), sep='')


"""
Pruebas
"""

rac1 = racional(2, 3)
print(numer(rac1))
imprimir(rac1)
