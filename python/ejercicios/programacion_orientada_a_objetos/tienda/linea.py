class Linea():

    def __init__(self, articulo, cantidad):
        self.__articulo = articulo
        self.__cantidad = cantidad

    def articulo(self):
        return self.__articulo

    def cantidad(self):
        return self.__cantidad

    def __repr__(self):
        return f'{self.__articulo.denom()}; Precio: {self.__articulo.precio()}€; Cantidad: {self.__cantidad}'
