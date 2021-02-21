"""
# Ejercicios de tipos de datos estructurados
Última modificación: 04/02/2021
"""
def last_ind(elemento):
    """
    1. Devolver el último elemento
    Crear una función que devuelva el último valor del último elemento de una
    lista o cadena.
    """
    if elemento in [[], '']:
        return
    else:
        return elemento[-1]

lista = ['paco', 'miguel', 'ultimo']
last_ind([0, 4, 2, 1])
last_ind('Mi pare come alcauciles')
last_ind([])
last_ind(lista)

def assign_per_to_job(people, jobs):
    """
    2. Asignar personas a profesiones
    Tienes dos listas. Una muestra los nombres de las personas (names), mientras
    que el otromuestra sus profesiones (jobs). Tu tarea es crear un diccionario
    que muestre a cada persona con su respectiva profesión.
    """
    return dict(zip(people, jobs))

nombres = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
trabajos = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]
assign_per_to_job(nombres, trabajos)

def calcular_perdidas(informe):
    """
    3. Calcular perdidades totales.
    Acabas de regresar a casa y descubres que han robado tu mansión! Dado un
    diccionario de los artículos robados, devolver el monto total del
    robo (número). Si no se robó nada, devolver la cadena "Lucky you!".
    """
    total = 0
    perdidas = informe.values()
    for i in perdidas:
        total = total + i
    if total == 0:
        print('¡Has tenido suerte!')
    else:
        return total

informe_perdidas = {"tv" : 30, "skate" : 20, "stereo" : 50,}
calcular_perdidas(informe_perdidas)
informe_vacio = {}
calcular_perdidas(informe_vacio)

def contar_unicos(a, b):
    """
    4. Cantidad total de caracteres únicos.
    Dadas dos cadenas, crear una función que devuelva el número total de
    caracteres únicos de la cadena combinada.
    """
    return len(set(a + b))

contar_unicos('América', '')
contar_unicos('', 'Gibraltar')
contar_unicos('América', 'Gibraltar')
contar_unicos('', '')


def convertir(data1, data2):
    """
    5. ¿Cuál es tu tipo?.
    Dadas dos estructuras de datos, data1 y data2, devolver data2
    convertido al tipo de data1.
    """
    if str(type(data1)) == "<class 'list'>":
        return list(data2)
    elif str(type(data1)) == "<class 'tuple'>":
        return tuple(data2)
    else:
        return set(data2)

convertir([1, 2, 4, 8], (7, 8, 9)) # == lista
convertir((7, 8, 9), [1, 2, 4, 8]) # == tupla
convertir([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}) # == lista
convertir({2, 3, 5, 7, 11, 13}, [1, 2, 4, 8]) # == conjunto

def anadir_nombre(objeto, nombre, valor):
    """
    6. Añade su nombre.
    Dados tres argumentos (un diccionario obj, una clave name y un
    valor value) devolver un diccionario con ese nombre y valor
    (como pares clave-valor).
    """
    return objeto.update({nombre:valor})

diccionario = {}
anadir_nombre(diccionario, 'piano', 'instrumento')
anadir_nombre(diccionario, 'navaja', 'arma')
print(diccionario)

def ordenar_unicos(lista):
    """
    7. Purgar y organizar.
    Dada una lista de números, escribir una función que devuelva una lista que:
        1. Elimine todos los elementos duplicados. (x in c)
        2. Esté ordenado de menor a mayor valor - (lista.sort())
    """
    return list(set(lista))

lista = [2, 9, 5, 7, 5, 8, 1, 3, 3]
ordenar_unicos(lista)

def entero_booleano(entero):
    """
    8. Unos verdaderos, ceros falsos
    Crear una función que devuelva una lista de valores booleanos, a partir de
    un número dado. Repitiendo el dígito del número uno a la vez, agregar True
    si el dígito es 1 y False si es 0.
    """
    resultado = []
    for d in str(entero):
        if d is '1':
            resultado.append(True)
        else:
            resultado.append(False)
    return resultado

entero_booleano(100100101010)

def obtener_nombres_estudiantes(listado):
    """
    9. Obtener nombres de estudiantes
    Crear una función que tome un diccionario de nombres de estudiantes y
    devuelva una lista de nombres de estudiantes en orden alfabético.
    """
    return sorted(listado.values())

estudiantes = {"Student 1" : "Steve", "Student 2" : "Becky", "Student 3" : "John"}
obtener_nombres_estudiantes(estudiantes)

# EXTRAS

def beneficios(ventas):
    """
    Recibe un diccionario con un informe de ventas y devuelve el beneficio total
    """
    [precio_compra, precio_venta, inventario] = ventas.values()
    return round((precio_venta - precio_compra) * inventario)

informe_ventas ={'precio_compra': 32.67, 'precio_venta': 45.00, 'inventario': 1200}
beneficios(informe_ventas)