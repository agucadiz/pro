def invierte(numeros):
    """
    invierte un numero a base de repetir la func 'pasa_pasa'
    Args: numeros -> List()
    La lista trae el segundo elemento vacio.
    """
    def pasa_pasa(numeros):
        """
        Suprime la ult. cifra del primer num y lo añade al final del segundo
        Args: numeros -> List()
        """
        a, b = numeros
        b = int( str(b) + str(a % 10) )
        a = a // 10
        return [a, b]
    print(numeros)
    for i in range(len(str(numeros[0]))):
        print(pasa_pasa(numeros))
        numeros = pasa_pasa(numeros)

invierte([12345, 0])
