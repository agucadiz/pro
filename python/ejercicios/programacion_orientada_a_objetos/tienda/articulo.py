class Articulo:
    """
     __codigo, __denominacion y __precio
    """
    __ultimo = 0
    articulos = {}

    def __init__(self, denom, precio) :
        Articulo.__ultimo += 1
        self.__codigo = Articulo.__ultimo
        self.__denominacion = denom
        self.__precio = precio
        Articulo.articulos[self.__codigo] = self

    # Métodos mágicos
    def __repr__(self):
        return f'Articulo (# {self.__codigo}: {self.__denominacion}, {self.__precio} €)'

    def codigo(self):
        return self.__codigo

    def denom(self):
        return self.__denominacion

    def precio(self):
        return self.__precio
