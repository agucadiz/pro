"""
Función suma_o_resta recibe una cadena y devuelve una función que suma si
la cadena es 'suma'; en caso contrario, devuelve una función que resta:
"""

suma_resta = lambda s: lambda x, y: x + y if s == 'suma' else \
                        lambda x, y: x - y
