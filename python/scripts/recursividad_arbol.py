"""
podemos definir una función recursiva que devuelva el n-esimo
término de la sucesion de fibonacci:

        { 0                         si n = 0 (caso base)
fib(n)= { 1                         si n = 1 (caso base)
        { fib(n - 1) + fib(n - 2)   si n > 1

En esta ocasión tenemos dos casos bases, si n vale 0 o si vale 1, a diferencia
de los demás casos anteriores. Además en esta ocasión vamos a llamar dos veces
a la función dentro de si misma, caso que hasta ahora solo se nos ha dado en
el el problema de las torres de hanoi.

- Especificación:
        { Pre:  True
        {       fib(n: int) -> int
        { Post: fib(n) = suceción de fibonacci

La evaluación de este tipo de funciones producen que se conoce como un
proceso recursivo en árbol, donde la longitud que toma desde su rama más
larga corresponde con el espacio máximo que ocupara en memoria, y el ancho
del árbol será el tiempo que tomará en ser evaluado. Al crecer este ancho de
forma exponencial, encontraremos el principal problema de los procesos
recursivos en árbol: El tiempo que toman en ser ejecutados. Esto se produce
porque vamos a ser muy redundantes, llamando en multitud de ocasiones a las
mismas funciones, haciendo a este tipo de funciones tremendamente ineficientes.

Para asegurarnos de que esta funcion es correcta, voy a escribri aquí abajo un
puñado de las cifras que componen a la sucesión de fibonacci:
0 1 2 3 4 5 6  7  8  9 10 11  12
--------------------------------
0 1 1 2 3 5 8 13 21 34 55 89 144
"""

fib = lambda n: 0 if n == 0 else 1 if n == 1 else \
                fib(n - 1) + fib(n - 2)

"""
Una forma extremadamente fácil de observar esta ineficiencia de ejecución
podemos observarla en cuanto empezamos a pedirle que evalue la sucesion de
los primeros 35 números que componen la secuencia. A partir de aquí, con que
solo subamos una cifra más, empezaremos a notar que el tiempo de ejecución se
dispara. Se dice que **crece exponencialmente**. En este caso lo hace en el
tiempo:

- Representación gráfica de lo que sucede con fib(5):

                             fib(5)
                       /               \
                 fib(4)                   fib(3)
               /       \                /        \
          fib(3)       fib(2)        fib(2)      fib(1)
        /     \       /     \        /    \        |
    fib(2)   fib(1) fib(1) fib(0) fib(1) fib(0)    1
    /    \     |      |      |      |      |
fib(1) fib(0)  1      1      0      1      0
  |      |
  1      0

20 5
25 0
30 5
35 0
40 5
45 0
50 5

"""
