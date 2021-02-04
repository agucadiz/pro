# Ejercicio de práctica con funciones recursivas
from py_toys.suma_rango import *

"""
suma_hasta(n):
Función recursiva que suma todos los numeros existentes hasta un número
concreto

- Especificación
    { Pre: n >= 0
    { suma_hasta(n: int) -- int
    { Post: suma_hasta(n) = la suma de los numeros existentes hasta n

suma_hasta(n) = 0 si n == 0 (caso base)
suma_hasta(n) = suma_hasta(n - 1) + n

- Extras
¿y si usamos abs(), nos permitiría sumar  tambien números negativos?
"""

suma_hasta = lambda n: 0 if n == 0 else \
            suma_hasta(n -1) + n

"""
suma_hasta_alt(n):
Alternativa NO RECURSIVA que suma todos los números existentes hasta un número
concreto
"""

suma_hasta_alt = lambda n:  n * (n + 1) / 2

"""
suma_hasta_dep(n):
Alternativa que usa la función suma_rango definida en otro fichero .py
"""

suma_hasta_dep = lambda n: suma_rango(1, n)
