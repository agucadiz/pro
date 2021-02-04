'''
vamos a intentar hacer de golpe algunas funciones segun el paradigma declarativo
'''

# De este modo podemos evaluar una función anónima sin asignarle una variable:
(lambda x: 'Hola ' + x)('Paco')

# La fomra más cómoda sin embargo es ligando la función a un identificador:
saluda = lambda x: 'Hola ' + x
saluda('Miguel')

# Las funciones anónimas no siempre deben requerir argumentos(?)
(lambda : 'Hola a todo el mundo!')()

saludos = lambda: 'Hola a todo el mundo'
# Aunque no lleve argumentos, para llamar a la función se le acompaña con argumento vacío '()'
# De lo contrario sólo nos devolverá la dirección en la memoria de la función:
saludos     # devuelve "<function <lambda> at 0x7f9018f1e670>"
saludos()   # devuelve la evaluación del cuerpo de la función: 'Hola a todo el mundo'

'''
La clave de este tipo de funciones es que cumplen la transparencia
referencial, por lo que sus expresiones pueden cambiarse en cualquier
momento por su resultado.
Estas funciones siempre van a devolver el mismo resultado,
independientemente del momento en el que se invoquen para ser evaluadas.
'''

suma = lambda x, y: x + y
suma(5, 4)  # devuelve la suma de los dos operandos

# A partir de esta función, podemos crear una nueva que resuelva el mismo
# problema pero de un modo más general, sumando 3 operandos en lugar de 2:
sumas = lambda x, y, z: x + y + z
sumas(5, 4, 0)  # sabiendo que la función suma tres operandos, pasándole uno
                # como 0, cumplimos el mismo requisito que la función anterior
# tambien podemos incluir operaciones aritméticas para resolver distintos casos:
suma(5, 4 + 3)  # 12
sumas(5, 4, 3)

# Las funciones anónimas tambien pueden contener operadores ternarios, con los
# que se puede determinar una selección, a partir de dos posibilidades:

mayorque = lambda a, b: a if a > b else b
mayorque(62, 26)

mayorquecero = lambda x: True if x > 0 else False
mayorquecero(-23)

'''
Una función puede llamarse a sí misma, lo que produce una función recursiva.
Para ello es imprescindible localizar un caso base para nuestra función,
es decir, una evaluación en la que nuestra función se detenga
'''
factorial = lambda x: 1 if x == 1 else x * factorial(x - 1)
factorial(4)     # Devuelve 24
'''
En el caso anterior, el caso base es que si 'x' vale 1, devovlerá 1.
Gracias a la transparencia referencia, podemos entender que:
    1. Al evaluar el ternario, seleccionará una de las opcines.
    2. Al evaluar la expresión tras el 'else', observamos que
    multiplica el valor de 'x' (4) por 'factorial(n - 1)' (3)
    3. Podemos saber que la función se ejecutará hasta llegar al caso base
    4. Una vez llegado a él, comenzará a evaluar las expresiones hasta
    devolver su resultado (24)

Es importante tener en cuenta que, a cada recursión, se va almacenando
en la pila cada una de las funciones:

|  REPRESENTACIÓN DE LA PILA  |
-------------------------------
factorial(1) = 1
factorial(2) = 2 * factorial(1)
factorial(3) = 3 * factorial(2)
factorial(4) = 4 * factorial(3)

Por lo que hasta que no se alcance el caso base, se irán
acumulando en la pila para luego ser evaluadas de arriba a abajo

Otra forma de representarlo es:

factorial(4) = (4 * factorial(3))
factorial(4) = (4 * (3 * factorial(2))
factorial(4) = (4 * (3 * (2 * factorial(1)))
factorial(4) = (4 * (3 * (2 * 1)))
factorial(4) = (4 * (3 * 2))
factorial(4) = (4 * 6)
factorial(4) = 24
'''

'''
Ejercicios de prog. funcional, usando recursividad
--------------------------------------------------

Dada una función matemática:
calcula el valor de f(3)

Voy a tratar de realizar su especificación:

Pre:    True
        funcion(n: int) -> int
Post:   funcion(n) = (2 ** n) - 1
'''

funcion = lambda n: 0 if n == 0 else \
            1 + 2 * funcion(n - 1)
funcion(2)      # devuelve 7

'''
funcion(3) = (1 + 2 * funcion(2))
funcion(3) = (1 + 2 * (1 + 2 * funcion(1)))
funcion(3) = (1 + 2 * (1 + 2 * (1 + 2 * funcion(0))))
funcion(3) = (1 + 2 * (1 + 2 * (1 + 2 * 0)))
funcion(3) = (1 + 2 * (1 + 2 * 1))
funcion(3) = (1 + 2 * 3)
funcion(3) = 7
'''

'''
2. La funcin potencia tiene la sig especificación:

Pre:    b >= 0
        potencia(a: int, b: int) -> int
Post:   potencia(a, b) = a**b
'''

# a. implementar de forma no recursiva
potencia = lambda a, b: a ** b
potencia(2, 5)  # 32

# b. Implementar de forma recursiva
potencia_recur = lambda a, b: 1 if b == 0 else \
                    a * potencia_recur(a, b - 1)
potencia_recur(2, 5)    # 32

'''
3. La funcion repite tiene la siguiente especificación:

Pre:    n >= 0
        repite(s: str, n: int) -> str
Post:   repite(s, n) = s * n

Implementar la función de forma recursiva.
'''

repite = lambda s, n: '' if n == 0 else \
            s + repite(s, n - 1)
repite('Paco', 3)   # devuelve 'PacoPacoPaco'

'''
Suma lenta
a) escribir su especificacion
Pre:    True
        suma_lenta(ant(a): int, sig(b): int) -> int
Post:   suma_lenta(ant(a), sig(b)) = (a - 1) + (b + 1)
'''

# b) implementar de forma recursiva
ant = lambda n: n - 1
sig = lambda n: n + 1

suma_lenta = lambda a, b: b if a == 0 else \
    ant(suma_lenta(0, a)) + sig(suma_lenta(0, b))
suma_lenta(4, 6)    # 10

'''
La funcion suma_digitos calcula la suma de los digitos de un numero entero:

Pre:    True
        suma_digitos(n: int) -> int
Post:   suma_digitos(n) = La suma de los digitos de n
'''
suma_digitos = lambda n: n if n == n // 10 == 0 else \
                n % 10 + suma_digitos(n // 10)
suma_digitos(423)   # 9

'''
La funcion voltea le da la vuelta a un número entero

a) Escribir su especificación

Pre:    True
        voltea(n: int) -> int
Post:   voltea(n) = Un número formado por los digitos de n volteados
'''

digitos = lambda n: 1 if n < 10 else \
            1 + digitos(n // 10)
digitos(423)    # 3

voltea = lambda n: n if n < 10 else \
            (n % 10) * (10 ** digitos(n // 10)) + voltea(n // 10)
voltea(423)     # 324
