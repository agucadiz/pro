"""
Vamos primeros cpn factoriales

# Ventajas:
1. Las funciones iterantes ocupan espacio de forma constante.
    se mantiene creciendo de forma lineal en el tiempo

2. Si yo corto el proceso en un determinado punto, por lo que sea ,
    los parámetros contienen la fino necesaria para que el proces
    pueda calcular el valor que habías pedido, cosa que en la
    recursividad no sucedía.

TCO: Tail-Call Optimization

python no optimiza la recursividad final

que hagan esto hay pocos (lenguajes funcionales puros: haskell, lisp)

"""
fac_iter = lambda cont, acc: acc if cont == 0 else \
    fac_iter(cont - 1, cont * acc)

factorial = lambda n: fac_iter(n, 1)


"""
Vamos a probar a hacre de forma recursiva la funcion anteriormente realizada,
suma_rango:

ESPECIFICACIÓN:

{Pre: True
{Signatura: suma_rango(a: int, b: int) --> int
{Post: suma_rango(a, b) = la suma de todos los numeros comprendidos
                        entre a y b.

suma_rango(a, b) = 0 cuando a > b   # caso base

    ## caso base1: suma_rango (a, b) = a cuando a == b
    caso base2: suma_rango (1, b) = 0 si a > b
    caso recursivo: suma_rango(a, b) = a +  suma_rango(a + 1, b)

si yo puedo hacer suma_rango(5, 7), hacer el suma_rango(4, 7) es
lo mismo que: 4 + suma_rango(5, 7)
4 + 5 + 6 + 7 = 4 + suma_rango(5, 7)


suma rango(2, 4) = sabemos que vale 9

a_nuevo = a_viejo + 1
b_nuevo = b_viejo
acc_nuevo= acc_viejo + a_viejo

    a           b           acc
--------    --------    --------
    2           4           0
    3           4           2 + 0 = 2
    4           4           2 + 3 = 5
    5           4           5 + 4 = 9

    Yo me planeto que cuando a sea mayor que b, estamos ante un caso base,
    donde debemos devolverel valor de acc.


"""

sr_iter = lambda a, b, acc: acc if a > b else \
    sr_iter(a + 1, b, acc + a)
suma_rango = lambda a, b: sr_iter(a, b, 0)

# Implementación antigua, la recursiva
suma_rango = lambda a, b: 0 if a > b else \
    a + suma_rango(a + 1, b)

fib_iter = lambda cont, a, b: a if cont == 0 else \
    fib_iter(cont - 1, b, a + b)
fib = lambda n: fib_iter(n, 0, 1)

"""
la recursividad lineal puede producir procesos recusivos lineales o iterativos

la recursivivdad nmutliple genera recursividad en arbol, es un proceso de explosion
combinatoria, de recursividad en arbol

La forma nos dice el tipo de proceso
- proceso recursivo (recursivo lineal)
- proceso iterativo (iterativo lineal)
- proceso en arbol ()

"""
