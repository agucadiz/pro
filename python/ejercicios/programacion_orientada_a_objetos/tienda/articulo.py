class Articulo:
    """
    Clase Articulo
    ---
    La clase Articulo representa y almacena los artículos de una tienda, compuestos por su código, denominacion y precio.
    """
    __ultimo = 0    # Control de cod. de artículo.
    __articulos = {}  # Registro de artículos.

    def __init__(self, denom, precio) :
        """Constructor de la clase Articulo"""
        Articulo.__ultimo += 1
        self.__codigo = Articulo.__ultimo
        self.__denominacion = denom
        self.__precio = precio
        Articulo.__articulos[self.__codigo] = self

    def __repr__(self):
        return f'Art. {self.__codigo}: {self.__denominacion} - Precio: {self.__precio}€'

    # ActiveRecord
    @staticmethod
    def get_articulo(codigo):
        """
        Devuelve un artículo existente en el registro a partir de su código.

        Parámetros:
        codigo: int -> el código del articulo a buscar
        """
        return Articulo.__articulos.get(codigo)

    def codigo(self):
        """Devuelve el código del artículo."""
        return self.__codigo

    def denom(self):
        """Devuelve la denominación del artículo."""
        return self.__denominacion

    def precio(self):
        """Devuelve el precio del artículo."""
        return self.__precio
