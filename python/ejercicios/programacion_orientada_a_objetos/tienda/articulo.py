class Articulo:
    """
    # Clase Articulo
    ---
    La clase Articulo representa artículos de una tienda. Estos poseen los campos
    """
    __ultimo = 0
    articulos = {}

    # Métodos mágicos
    def __init__(self, denom, precio) :
        """Constructor de la clase Articulo"""
        Articulo.__ultimo += 1
        self.__codigo = Articulo.__ultimo
        self.__denominacion = denom
        self.__precio = precio
        Articulo.articulos[self.__codigo] = self

    def __repr__(self):
        return f'Art. {self.__codigo}: {self.__denominacion} - Precio: {self.__precio}€'

    # Accesores
    def codigo(self):
        """Devuelve el código correspondiente al artículo."""
        return self.__codigo

    def denom(self):
        return self.__denominacion

    def precio(self):
        return self.__precio

    # ActiveRecord
    @staticmethod
    def get_articulo(numero):
        return Articulo.clientes.get(numero)
