'''
Funcion imperativa que recibe una cadena y comprueba si es un isograma.
(Palabra que no repite ninguna de sus letras)
'''
palabra = 'poleando'

def isograma(cadena):
    letras = list(cadena)
    for i in letras:
        contador = 0
        for j in letras:
            if j == i:
                contador += 1
        if contador >= 2:
            return False
    return True

# isograma(palabra)
