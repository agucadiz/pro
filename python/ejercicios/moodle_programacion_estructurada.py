import re
import unicodedata
'''
Escribir una función palindromo() que determine si una cadena es un palíndromo.

Un palíndromo es una cadena (palabra o expresión) que es igual si se lee de izquierda a derecha que de derecha a izquierda.

Por ejemplo: «Amar da drama».

La función debe ignorar los caracteres no alfabéticos y no debe distinguir las mayúsculas de las minúsculas.

Por ejemplo:
Test 	Resultado
print(palindromo('Amar da drama.')) - True
print(palindromo('Hola, qué tal')) - False
'''

'''
primero quiero crear una funcion que reciba una cadena y devuelva auna lista con todos sus caracteres
'''

import unicodedata
def limpia_frases(cadena):
    # normalize descompone los caracteres compuestos, como vocales con tilde,
    # devolviendo sólo los caracteres.
    # 'Mn' seginifica "Nonspacing_Mark, incluye replace() para quitar espacios
    # y lower()) para dejarlo todo en minúsculas"
    return ''.join(c for c in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(c) != 'Mn').replace(' ', '').lower()

cadena = 'paco pica coca'

def palindromo(s):
   s.split()

    if frase == esarf:
        return True
    else:
        return False

palindromo(cadena)

def palindromo(s):
    limpio = (re.sub('[/W_ ]', '', s))

    frase = limpio[0]

    print(limpio)

palindromo(cadena)

'''
    esarf = frase[::-1]
    if frase == esarf:
        return True
    else:
        return False

palindromo(cadena)

def palindromo(s):


    limpio = (re.sub(r'[^a-zA-Z]', '', s).split())

    frase = limpio[0]
    print(limpio[0])


    frase = limpio[0]
    esarf = frase[::-1]
    if frase == esarf:
        return True
    else:
        return False

palindromo(cadena)
'''



cadena = "àéêö hello"
def palindromo(s):
    u = unicode(s, "utf-8")
    u = unidecode.unidecode(u)
    limpio = (re.sub('[/W_ ]', '', u))

    print(limpio)

palindromo(cadena)
