def pasa_pasa(numeros):
    """
    Suprime la ult. cifra del primer num y lo añade al final del segundo
    Args: numeros -> List()
    """
    a, b = numeros
    b = int( str(b) + str(a % 10) )
    a = a // 10
    numeros = [a, b]

    print(numeros)

pasa_pasa([54321, 0])
