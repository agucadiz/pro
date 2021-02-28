class Linea():
    """
    Clase Linea
    ---
    La clase linea representa una linea dentro de una factura, compuesta
    """
    def __init__(self, articulo, cantidad):
        """Constructor de la clase Linea"""
        self.__articulo = articulo
        self.__cantidad = cantidad

    def __repr__(self):
        return f'Artículo: {self.__articulo.denom()}; Precio: {self.__articulo.precio()}€; Cantidad: {self.__cantidad}; Subtotal = {self.subtotal()}€\n'

    def articulo(self):
        """Devuelve el articulo de la línea."""
        return self.__articulo

    def cantidad(self):
        """Devuelve la cantidad de un artículo de la línea."""
        return self.__cantidad

    def subtotal(self):
        """Devuelve el subtotal de la línea, a partir del precio del artículo y la cantidad del mismo."""
        return self.articulo().precio() * self.cantidad()
