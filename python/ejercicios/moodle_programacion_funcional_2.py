"""
# Ejercicio 1
Escribir una función tomar_mientras que tenga el mismo comportamiento que la
función itertools.takewhile, pero devolviendo una tupla en lugar de un iterador:

from itertools import takewhile
tuple(takewhile(lambda x: x < 5, (1, 4, 6, 5, 4, 1, 5))) => (1, 4)

Naturalmente, no se puede usar la función itertools.takewhile.

tupla = (24, 'hola', False, 'mipare', 27)

Ejemplo de takewhile:
print(tomar_mientras(lambda x: x < 5, (1, 4, 6, 4, 1))) = (1, 4)


Bien, ahora que entendí como funciona itertools.takewhile, vamos a pensar como
recrear este comportamiento.

Especificación
Pre: True
tomar_mientras() --> tuple
"""
tupla = (1, 4, 6, 4, 1)

tomar_mientras = lambda e, t: () if t == () else \
                    (t[0],) + tomar_mientras(e, t[1:]) if t[0] < e else ()

"""
Escribir una función inversa que devuelva la inversa de una tupla, de forma que:

inversa((1, 2, 3, 4)) => (4, 3, 2, 1)

No se puede usar la función predefinida reversed ni ninguna construcción sintáctica que no se haya visto hasta la UD4 (incluyendo slices).

Especificación:
Pre:    True
        inversa(t: tuple) -> tuple
Post:   inversa(t) = una tupla igual que t pero invertida
"""

inversa = lambda t: () if  t == () else \
             (t[-1],) + inversa(t[:-1])

"""
Escribir una función dejar_mientras que tenga el mismo comportamiento
que la función itertools.dropwhile, pero devolviendo
una tupla en lugar de un iterador:

from itertools import dropwhile
tuple(dropwhile(lambda x: x < 5, (1, 4, 6, 4, 1))) => (6, 4, 1)

Naturalmente, no se puede usar la función itertools.dropwhile.

Especificación:
Pre:    True
        dejar_mientras(e, t: tuple) -> tuple
Post:   dejar_mientras(e, t) = los valores de t, a partir de la primera
                                aparición de e.

"""

tupla = (1, 4, 6, 4, 1)

dejar_mientras = lambda e, t: () if t == () else \
                        () + dejar_mientras(e, t[1:]) if t[0] < e else t

"""
Escribir una función quitar_digitos no recursiva usando funciones de orden
superior que, dada una cadena, la devuelva quitando todos los
dígitos que puedan aparecer en ella:

quitar_digitos("hkj23hk234kj1h24kj") => "hkjhkkjhkj"
"""
