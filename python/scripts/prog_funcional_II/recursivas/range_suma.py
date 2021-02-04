"""
# range_suma(r: range) -> int
función que calcula la suma de los elementos de un rango
"""

range_suma = lambda r: 0 if r == range(0, 0) else \
                        r[0] + range_suma(r[1:])
