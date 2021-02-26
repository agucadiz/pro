from articulo import Articulo

class Factura:
    """
    # Factura <Clase>
    linea = [Articulo, cantidad]
    """
    __ultimo = 0

    def __init__(self, cliente):
        self.__ultimo += 1
        self.__codigo = self.__ultimo
        self.__cliente= cliente
        self.__lineas = []

    def codigo(self):
        return self.__codigo

    def cliente(self):
        return self.__cliente

    # factura.anyadir_articulo(tele, 2)
    def anyadir_articulo(self, articulo, cantidad):
        self.__lineas.append([articulo, cantidad])

    # tratando de resolver pensamiento optimista
    def importe_total(self):
        importe = 0
        for linea in self.__lineas:
            precio = linea[0].precio()
            cantidad = linea[1]
            importe += (precio * cantidad)
        return importe
