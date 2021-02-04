# Python 3.8.5
# Practicas con funciones de orden superior

"""
suma_enteros(a: int, b: int) -> int
Suma los enteros comprendidos entre a y b.

Pre:    a < b
        suma_enteros(a: int, b: int) -> int
Post:   suma_enteros(a, b) = la suma de enteros
                            entre a y b
"""

suma_enteros = lambda a, b: 0 if a > b else \
                            a + suma_enteros(a + 1, b)

"""
suma_cubos(a: int, b: int) -> int
Suma los cubos de los enteros comprendidos entre a y b

Pre:    a < b
        suma_cubos(a: int, b: int) -> int
Post:   suma_cubos(a, b) = La suma de los cubos
                            entre a y b
"""

cubo = lambda x: x ** 3

suma_cubos = lambda a, b: 0 if a > b else \
                            a ** 3 + suma_enteros(a + 1, b)

la_suma = lambda s, a, b: suma_enteros(a, b) if s == 'enteros' else \
                    cubo(a) + suma_cubos(a, b)
