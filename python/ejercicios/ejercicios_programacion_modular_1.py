'''
# Ejercicio 2
Importa el módulo math en un programa que necesite la función math.gcd para calcular
el máximo común divisor de dos números:
a) Usando import math
b) Usando from math import gcd
c) Usando from math import *
'''

# a) usando import math
import math
from random import random
math.gcd(6, 12)


# b) usando from math import gcd
from math import gcd
gcd(6, 12)


# c) usando from math import *
from math import *
gcd(6, 12)

'''
¿Cuál es la diferencia entre las tres opciones? ¿Cuál es más conveniente?
¿Qué inconvenientes presenta la última opción?
- La diferencia reside en que al hacer "import math" estamos creando en el
marco global un objeto que contendra los atributos y funciones del modulo
en cuestión, y su vez una ligadura con su mismo nombre.
"from math import gcd" importa sólo la función gcd definida en el módulo
La ultima opción importa las definiciones del módulo en cuestión, excepto
las que comienzan por "_".
La problematica de este último caso es que al importar tantas definiciones
se corre el riesgo de "machacar" algunas definiciones propias.
'''

'''
# Ejercicio 3
Usa el módulo random para escribir programas que necesiten mostrar un comportamiento aleatorio:
a) La función random.randint(a,b)) devuelve un número entero aleatorio entre a y
b. Úsala para escribir un programa que juegue a que el usuario tenga que adivinar
un número entre 1 y 100.
'''

def adivina():
    import random
    num = random.randint(1,100)
    print('Estoy pensando en un número del 1 al 100...')
    op = int(input('¡Adivínalo!: '))

    while op != num:
        op = int(input('Prueba otra vez: '))

    print('¡Enhorabuena, has acertado!')

'''
b) La función random.shuffle(x) ordena aleatoriamente la secuencia x. Úsala para
escribir un programa que pida al usuario cinco cadenas y que luego las imprima
en un orden aleatorio.
'''

def agita():
    import random
    lista = []
    for i in range(5):
        lista.append(input('Introduce una cadena:'))

    random.shuffle(lista)

    for i in lista:
        print(i)
