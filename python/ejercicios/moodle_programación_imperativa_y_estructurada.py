'''
04/12/2020
# Ejercicios de programación imperativa y estructurada

1.Encontrar el valor de la variable valor después de
la ejecución de las siguientes sentencias:
a)valor = 4.0 * 5
Solución: 20.0

b)	x = 3.0
	y = 2.0
	valor = x ** y - y
 SOlu: 7.0

c)	valor = 5
	x = 3
    valor = valor * x
Solu: 15

2. ¿Cuál es la diferencia entre [1, 2, 3] y [[1, 2, 3]]?
Solu: Que el primero es una lista con 3 elementosy el
segundo es una lista con un elemento, que a su vez es
una lista con 3 elementos.


3. Explicar la diferencia entre el operador ternario:
〈valor〉if〈condición〉else〈valor〉

y la estructura de control:
if〈condición〉:〈sentencia〉

Solu:
Se observa que en la estructura de control se pierde
la transparencia referencial. Es decir, con tan sólo
observar ambas funciones, es mucho mas complicado
determinar el resultado de su evaluación, debido a que
esas sentencias pueden producir efectos laterales

4. Escribir un programa que pida al usuario su edad y que
imprima el mensaje «¡Quéjoven!» si es menor de 25 años.

Extra: decir dias, y tal de tiempo vivido
'''

def piedad():
    edad = int(input('Dime tu edad: '))
    if edad < 25:
        print('¡Que joven!')
    tiempo = edad * (24 * 365)
    print('Llevas ' + str(tiempo) + ' horas vivo.')

# Ejercicios hasta el 7:
def edades():
    edad = int(input('Dime tu edad: '))
    if edad < 25:
        print('¡Que joven!')
    elif edad > 25 and edad < 40:
        print('No esta mal')
    else:
        print('Eres viejo')

'''
8. Escribir un programa que muestre por pantalla la tabla
de multiplicar de un númerocomprendido entre 0 y 10,
introducido por teclado.
'''

def tabla():
    num = int(input('Dime un numero: '))
    exp = 0
    while exp <= 10:
        print(str(num) + ' x ' + str(exp) + ' = ' + str(num * exp))
        exp += 1

# 9.  Dado el siguiente código:
def patata():
    n = int(input('¿Hasta dónde llego?: '))     # 1
    i = 0                                       # 2
    while i < n:                                # 3
        print('Aquí la i vale', i)              # 4
        i += 2                                  # 5
    print('que hermoso dia')                    # 6
'''
se pide:
a)  Contar cuántas sentencias hay.
 - Hay 5 sentencias.
b)  Por cada una de ellas, indicar si son simples o compuestas.
 - Linea 1: sentencia compuesta
 - Linea 2: sentencia simple
 - Linea 3: sentencia compuesta
 - Linea 4: sentencia compuesta
 - Linea 5: sentencia simple
c)  Por cada sentencia compuesta, indicar de qué tipo de estructura se trata.
 - Linea 1: coerción de tipo de dato y proceso de entrada/salida
 - Linea 3: estructura de control
 - Linea 4: es
d)Deducir cuántas veces se ejecuta la sentencia de la línea 4 en función
del valor de la variable n.
 - La mita del valor de n.
e)  ¿Es posible provocar un bucle infinito al ejecutar ese programa?
 - Con esta definición no.

10. Escribir un programa que calcule la media de cinco valores
numéricos reales (tipofloat) introducidos por teclado.
'''

def media5():
    i = 0
    media = 0
    while i < 5:
        media = media + int(input('Dime un numero: '))
        i += 1
    return media / i

'''
11. Escribir un programa que guarde en una lista diez cadenas
introducidas por teclado y luego las muestre en orden inverso
a como se han introducido, desde la última cadena
introducida hasta la primera
'''

def listainversa():
    lista = []
    for i in range(10):
        lista = lista + [input('Dime una palabra: ')]
    return lista[::-1]

'''
Indicación: Usar el método append sobre la lista y luego un
bucle que recorra la lista desde el último elemento
hasta el primero.
'''
def listainversa():
    lista = []
    i = 0
    while i < 10:
        lista.append(input('Dime una palabra: '))
        i += 1

    while i > 0:
        print(lista[i - 1], end=' ')
        i -= 1

'''
Escribir un programa que calcule el máximo común divisor de dos
números enteros introducidos por teclado, usando:
'''
# a)  La función math.gcd.
import math
def mcd():
    return math.gcd(int(input('Primer numero: ')), int(input('Segundo numero: ')))

# b)  Bucles

def mcd():
    nums = []
    i = 1
    resultado = 0
    for j in range(2):
        nums = nums + [float(input('Dime un numero: '))]
    while i <= nums[0] and i <= nums[1]:
        if nums[0] % i == 0 and nums[1] % i == 0:
            resultado = i
        i += 1
    return resultado

'''Escribir un programa que determine si un número entero introducido
por teclado es primo o compuesto.
'''
def esprimo():
    num = int(input('Dime un numero: '))
    i = 1
    resultado = 0
    while i <= num:
        if num % i == 0:
            resultado += 1
        i += 1
    if resultado <= 2:
        print(num, ' es un numero primo')
    else:
        print(num, ' es un numero compuesto')

esprimo()

# variable con break

def esprimo():
    num = int(input('Dime un numero: '))
    i = 1
    resultado = 0
    while i <= num:
        if num % i == 0:
            resultado += 1
            if resultado > 2:
                print(num, ' es un numero compuesto')
                break
        i += 1
    if resultado == 2:
        print(num, ' es un numero primo')

esprimo()
'''
14. Escribir un programa que gestione datos almacenados en una lista,
de forma que muestre un menú con las siguientes opciones:
    1. Añadir un elemento a la lista.
    2. Cambiar el valor de un elemento de la lista.
    3. Eliminar un elemento de la lista.
    4. Eliminar todos los elementos de la lista.
    5. Mostrar los elementos de la lista.
    0. Salir del programa.

El programa deberá pedir la información necesaria para
cada opción elegida por elusuario.
'''
def anadir(l):
    e = input('Introduce un elemento: ')
    l.append(e)
def cambiar(l):
    print()
    pos = int(input('Introduce posición (max ' + str((len(l) - 1)) + '): '))
    e = input('Introduce nuevo elemento: ')
    l[pos] = e
def eliminar(l):
    e = input('Introduce elemento a eliminar: ')
    l.remove(e)
def borrar(l):
    l.clear()
def mostrar(l):
    print(l)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def gestionaLista(lista):
    print('Menu:')
    print('1. Añadir un elemento a la lista.')
    print('2. Cambiar el valor de un elemento de la lista.')
    print('3. Eliminar un elemento de la lista.')
    print('4. Eliminar todos los elementos de la lista.')
    print('5. Mostrar los elementos de la lista.')
    print('0. Salir del programa.')
    s = int(input('Selecciones una opsion: '))
    if s == 1:
        anadir(lista)
    elif s == 2:
        cambiar(lista)
    elif s == 3:
        eliminar(lista)
    elif s == 4:
        borrar(lista)
        print('La lista ha sido borrada')
    elif s == 5:
        mostrar(lista)
    elif s == 0:
        print('Nos vemos!')
    else:
        print('Opción incorrecta')
        gestionaLista(lista)

gestionaLista(lista)

'''
Se pide escribir un programa que modifique la lista de empleados
incrementando en un 10 % el salario de cada empleado y muestre
por pantalla el salario total de los empleados de la empresa.
'''

empleados = [('María', 'González', 1800.23),
             ('Javier', 'Ruiz', 1630.50),
             ('Jesús', 'Pérez', 2100.42),
             ('Rosa', 'Muñoz', 2240.78)]
def modificaSalarios(lista):
    lista_empleados = []
    salario_total = 0.0
    for i in range(len(lista)):
            lista_empleados = lista_empleados + [list(lista[i])]

    for i in range(len(lista_empleados)):
        lista_empleados[i][2] = lista_empleados[i][2] + ((lista_empleados[i][2] * 10) / 100)
        salario_total = salario_total + lista_empleados[i][2]

    print('Salario total: ', salario_total)

modificaSalarios(empleados)
