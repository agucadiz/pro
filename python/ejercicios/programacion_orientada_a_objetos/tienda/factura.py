from articulo import Articulo
from linea import Linea

class Factura:
    """
    ## Modulo factura.py
    # Clase Factura
    linea = [Articulo, cantidad]
    """
    __ultimo = 0
    __ultima_linea = 0

    def __init__(self, cliente):
        self.__ultimo += 1
        self.__codigo = self.__ultimo
        self.__cliente= cliente
        self.__lineas = {}  # {num_linea : Linea}

    def __repr__(self):
        return f'Factura Nº{self.__codigo} - {self.__cliente}\n{self.__lineas}\nTotal: {self.importe_total()}€'

    def lineas(self):
        return self.__lineas

    def codigo(self):
        return self.__codigo

    def cliente(self):
        return self.__cliente

    def agregar_linea(self, articulo, cantidad):
        self.__ultima_linea += 1
        linea = Linea(articulo, cantidad)
        self.__lineas[self.__ultima_linea] = linea

    def borrar_linea(self):
        del self.__lineas[self.__ultima_linea]
        self.__ultima_linea -= 1

    # tratando de resolver pensamiento optimista usando diccionario
    def importe_total(self):
        importe = 0
        for linea in self.__lineas.values():
            precio = linea.articulo().precio()
            cantidad = linea.cantidad()
            importe += (precio * cantidad)
        return importe

"""
    def imprimir_factura(self):
        print('Factura Nº' + self.codigo() + ' - Cliente: ' + self.cliente().nombre())
        print('Artículo; Precio; Cantidad; Subtotal')
        for articulo, cantidad in self.lineas().items():
            print (articulo.denom() + '; ' + articulo.precio() + ';' + cantidad + '; ' + (articulo.precio * cantidad))
        print('Total: ' + self.importe_total)
"""
