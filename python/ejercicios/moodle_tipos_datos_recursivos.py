"""
# Ejercicio 1
La función elem tiene la siguiente especificación:

Pre:    True
        elem(e, t: tuple)-> bool
Post:   elem(e, t)= {True si e está en t}
                    {False en caso contrario}

Escribir una función recursiva que satisfaga dicha especificación.
"""

elem = lambda e, t: False if t == () else \
                    True if t[0] == e else \
                        elem(e, t[1:])

"""
# Ejercicio 2
La función cuantos tiene la siguiente especificación:

Pre:    True
        cuantos(e, t: tuple) -> int
Pos:    cuantos(e, t) = el numero de veces que aparece e en t

Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
"""

# a. recursivo
cuantos_recur = lambda e, t: 0 if t == () else \
                    1 + cuantos_recur(e, t[1:]) if t[0] == e else \
                        0 + cuantos_recur(e, t[1:])

# b. iterativo
iter_cuantos = lambda e, t, i: i if t == () else \
                    i + 1 + iter_cuantos(e, t[1:], i) if t[0] == e else \
                        iter_cuantos(e, t[1:], i)
cuantos_iter = lambda e, t: iter_cuantos (e, t, 0)

"""
La función quita tiene la siguiente especificación:

Pre:    True
        quita(e, t: tuple) -> tuple
Post:   quita(e, t) = una tupla igual que t pero sin los e
"""


quita = lambda e, t: () if t == () else \
                    (t[0],) + quita(e, t[1:]) if t[0] != e else \
                        () + quita(e, t[1:])

"""
#Ejercicio 4
La función sustituye tiene la siguiente especificación:

Pre:    True
        sustituye(a, b, t: tuple) -> tuple
Pos:    sustituye(a, b, t) = una tupla igual que t pero sustituyendi los a por b

Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
"""

# a. recursivo

sustituye_recur = lambda a, b, t: () if t == () else \
                            (b,) + sustituye_recur(a, b, t[1:]) if t[0] == a else \
                                (t[0],) + sustituye_recur(a, b, t[1:])
# sustituye_recur(6, 5, tupla) - > (1, 4, 5, 4, 1)

# b. iterativo

iter_sus = lambda a, b, t, i: () if t == () else \
                                    (b,) + iter_sus(a, b, t[i + 1:], i) if t[i] == a else \
                                        (t[0],) + iter_sus(a, b, t[i + 1:], i)
sustituye_iter = lambda a, b, t: iter_sus(a, b, t, 0)
# sustituye_iter(1, 'paco', tupla) -> ('paco', 4, 6, 4, 'paco')

"""
# Ejercicio 5
La función ultimo tiene la siguiente especificación:

Pre:    t != ()
        ultimo(t: tuple)
Post:   ultimo(t) = el último elemento de t

Escribir una función recursiva que satisfaga dicha especificación.
"""

ultimo = lambda  t: () if t == () else \
                    t[0] if ultimo(t[1:]) == () else \
                        ultimo(t[1:])
# ultimo((1, 4, 6, 4, 7)) -> 7

"""
# Ejercicio 6
La función enesimo tiene la siguiente especificación:

Pre:    t != () ^ 0 <= n < len(t)
        enesimo(n: int, t: tuple)
Post:   enesimo(n, t) = el n-ésimo elemento de t

Escribir una función recursiva que satisfaga dicha especificación.
"""
# Solución sin recursividad
enesimo = lambda n, t: () if n == len(t) else \
                        () if t == () else t[n]

# Solución recursiva (no lo hice yo, lo hizo la ciencia)
enesimo = lambda n, t: t[0] if n == 0 else \
                        enesimo(n - 1, t[1:])

# Solución iterativa
enesimo = lambda n, t, i: () if t == () else \
                            t[i] if i == n else \
                                enesimo(n, t, i + 1)
