# EJERCICIOS DE FUNCIONES RECURSIVAS, 2 de Noviembre de 2020
"""
# Ejercicio 1

Dada la sig. f- matematica:

        {0                  si n = 0
f(n)n= {
        {1 + 2 · f(n - 1)   si n > 0

calcula el valor de f(3)
"""

funcion = lambda n: 0 if n == 0 else \
    1 + 2 * funcion(n - 1)

"""
*Voy a llamar a f > funcion, porque me resulta más natural*

El valor de funcion(3) es equivalente al numero abstracto 7.

-Por qué? Vamos a descomponer funcion(3) para averiguarlo:
    funcion(3) = 1 + (2 * funcion(2))

    funcion(2) = 1 + (2 * funcion(1))

    funcion(1) = 1 + (2 * funcion(0))

    funcion(0) = 0      # Porque la funcion propone como caso base
                        que se devuelva 0 si n = 0

- Por lo tanto:
    funcion(3) = 1 + (2 * (1 + (2 * (1 + (2 * 0)))))

    Si metemos esta vaina loca en el intérprete:
        1 + (2 * (1 + (2 * (1 + (2 * 0)))))
    Nos devolverá lo mismo que si evaluasemos funcion(3)

# Signatura:
    { Pre: True
    { funcion(n: int) -> int
    { Post: funcion(n) = la suma de n potencias de 2, menos 1

# Fin ejercicio 1
"""

"""
Ejercicio 2
La funcion "potencia"tiene la siguiente especificación:

{ Pre: b >= 0
{ potencia(a: int, b: int) -> int
{ Post: potencia(a, b) = a^b

a)  Implementar la función de forma no recursiva.
b)  Implementar la función de forma recursiva.

===================================================

# Parte a) Implementar la función de forma no recursiva.
BIEN! Saquemos primero la función no recursiva:

Veamos, estamos hablando de una función que pretende evaluar la potencia (b) de un número(a)
FACIL! Si mal no recuerdo, existe una funcion que ya hace  "pre-built" llamada pow. Pues voy a usarla.
Tiene gracia, no me tengo que preocupar de como funciona, o si se pudiera hacer mejor. Sólo
quiero que funcione y, dese luego, yo no estoy usando recursidad. Desconozco si la funcion pow se vale
de la recursividad, pero insisto, YO no me tengo que preocupar de cómo funciona, sólo de que funcione.
Sé que lo hace y estoy convencido (¿Pensamiento optimista?) de que lo hace genial.

De lo unico que me quedan dudas es sobre la pre-condicion. ¡Vamos a leer los apuntes!:
- PUUES  resulta que no importa en el código la precondición, y cito textualmente:
    "Tanto la precondición como la postcondición sonpredicados, es decir, expresiones
    lógicas que seescriben usando el lenguaje de las matemáticas y la lógica."
    [...]
    "La signaturas e escribe usando la sintaxis del lenguaje de programación que se
    vaya a usar paraimplementar la función (Python, en este caso)."

Pues ale, ahi lo tenemos:
"""

potencia = lambda a,b: pow(a, b)

"""
# Parte b) Implementar la función de forma recursiva.
Y ahora vamos a por la recursiva... ¿Cómo se supone que se hace esto de forma recursiva?
PUUES supongo que multiplicando un numero a si mismo, tantas veces nos pida (b)

Veamos... Tendriamos que buscar un caso base. Por lo pronto voy a empezar a estrujarme el cerebro:

¿Es 2^2 = 2 * 2?      # bravo... voy a comer mayonesa

¿Es 2**4 lo mismo que 2**3 * 2?
Dicho de otro modo...
    a**b = a**(b-1) * a

Vamos a decomponer la propuesta:

potencia(2, 4) = 2 * (potencia(2, 3))

potencia(2, 3) = 2 *(potencia(2, 2))

potencia(2, 2) = 2 * (potencia(2, 1))

potencia(2, 1) = 2 * (potencia(2, 0))

potencia(2, 0) = 1      # porque  se devuelve 1 si b <= 0


creo que el caso base es:

devolver 1 si b <= 0 (caso base)

Pues ya lo tenemos
"""

potencia = lambda a, b: 1 if b <= 0 else\
    a * potencia(a, b-1)

"""
Quiero además describirlo en forma de función matemática:

                 { 1                        si b <= 0
potencia(a, b) = {
                 { a * potencia(a, b - 1)   si b > 0

# Fin ejercicio 2
"""

"""
# Ejercicio 3
La función repite tiene la siguiente especificación:

    { Pre: n >= 0
    { repite(s: string, n: int) -> str
    { Post: repite(s, n) = s * n

Implementar la función de forma recursiva.

Bueno, por lo que se ve la funcion repite se trata de repetir una cadena n veces.
Después de lo realizado anteriormente no resultará demasiado difícil.
Además ya tenemos la especificación. Vamos pues a sacar un caso base:

0 si n <= 0 (caso base)

La función matemática tendría esta forma:

                { "s"                         si n <= 1
repite(s, n)  = {
                { "s" · repite("s", n - 1)  si n > 1
"""

repite = lambda s, n: s if n <= 1 else \
    s + repite(s, n - 1)

# Fin Ejercicio 3

"""
# Ejercicio 4
La suma lenta es un algoritmo para sumar dos números para el que sólo necesitamos saber
cuáles son el anterior y el siguiente de un número dado. El algoritmo se basa en la siguiente
recurrencia:

                   { b                             si a = 0
suma_lenta(a, b) = {
                   { suma_lenta(ant(a), sig(b))    si a > 0

Suponiendo que tenemos las siguientes funciones ant y sig:
    ant = lambda n: n - 1
    sig = lambda n: n + 1

Se pide:
    a) Escribir su especificación.
    b) Implementar una función recursiva que satisfaga dicha especificación.

Manos a la obra, señor Freeman:

    { Pre: True
    { suma_lenta(a: int, b: int) -> int
    { Post: suma_lenta(a, b) = a-1 + b+1

Vamos a ver...

b si a = 0 (caso base)

"""
ant = lambda n: n - 1
sig = lambda n: n + 1
suma_lenta = lambda a, b: b if a == 0 else \
    ant(suma_lenta(0, a)) + sig(suma_lenta(0, b))

# Fin Ejercicio 4

"""
# Ejercicio 5
La función suma_digitos calcula la suma de los dígitos de un número entero:
    - suma_digitos(423) = 4 + 2 + 3 = 9
    - suma_digitos(7) = 7

Se pide:
    a) Escribir su especificación.
    b) Implementar una función recursiva que satisfaga dicha especificación.

Indicación: Recordar que n // 10 le quita el último dígito a n. Además, n % 10 devuelve el
último dígito de n.

---

Primero hay que hacer n // 10 y si esto devuelve... pues no! resulta que esto por ahora no
me sirve, prque no se como controlar detectar que la evaluación... se MENOR DE 10! listo!

a) Escribir su especificación:

{ Pre:
{ suma_digitos(n: int) - > int
{ Post: suma_digitos(n) :  La suma de los digitos que componen a n


0 si [...] n // 10 < 10   # caso base que no logro conseguir en los casos que necesito

Mi caso base es:

n    si n // < 10

               { n                                       si n // 10 = 0
suma_digitos = {
               { (n % 10) + (suma_digitos(n // 10))     si n // 10 > 10
}

"""
# b) Implementar una función recursiva que satisfaga dicha especificación.

suma_digitos = lambda n: n if n < 10 else \
    (n % 10) + suma_digitos(n // 10)

# Fin Ejercicio 5

"""
# Ejercicio 6
La función voltea le da la vuelta a un número entero:

    - voltea(423) = 324
    - voltea(7) = 7

Se pide:
    a) Escribir su especificación.
    b) Implementar una función recursiva que satisfaga dicha especificación.

Indicación: Usar la función digitos que devuelve la cantidad de dígitos que
tiene un entero. Usar además la indicación del ejercicio anterior.



"""

digitos = lambda n: 1 if n < 10 else \
    1 + digitos(n // 10)

# versión trampuchera con coerciones de tipo(?)
voltea = lambda n: '' if n <= digitos(n) else \
    int(str(n % 10) + str(voltea(n // 10)))

# versión completa usando sólo matemáticas
voltea = lambda n: n if n <= 10 else \
    (n % 10) * (10 ** digitos(n//10)) + voltea(n // 10)

# Fin ejercicio 6
"""

voltea(752) be like...

2 * (10** digitos(752))

"""

"""
# Ejercicio 7
# La función par_positivo determina si un número entero positivo es par:
par_positivo(0) = True
par_positivo(1) = False
par_positivo(27) = False
par_positivo(82) = True
Se pide:
a) Escribir su especificación.
b) Implementar una función recursiva que satisfaga dicha especificación.

Uf, hace mucho que no estudio programación... vamos  a ponernos al día.

Especificación:


sabemos que % 2 da0 parapares y 1 para impared

"""

par_positivo = lambda n: str(n) + " es par" if n % 2 == 0 else \
                        str(n) + " no es par, pero " + par_positivo(n+1)

"""
Bueno, es recurvia pero no cumple las espectativas. Tiene que devolver False o True
"""

par_positivo = lambda n: True if n % 2 == 0 else False

"""
Especificación:
Pre: n >= 0
par_positivo(n: int) -> bool
Pos: par_positivo(n) = True si es par, False en caso contrario
"""
par_positivo: lambda n: True if n <= 0 else \
                        False if par_positivo(n - 1) else True

"""
# Ejercicio 8.
# La función par determina si un número entero (positivo o negativo) es par:
par(0) = True
par(1) = False
par(-27) = False
Se pide:
a) Escribir su especificación.
b) Implementar una función recursiva que satisfaga dicha especificación.
c) ¿Cómo se podría implementar una función impar a partir de la función par ?

Especificación:
Pre: True
par(n: int) -> Bool
Pos: par(n) = True si es par, False en caso contrario

"""
# a
par = lambda n: True if n == 0 else \
                False if par(abs(n - 1)) else True


print(par(27))
