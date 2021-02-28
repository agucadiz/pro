from articulo import Articulo
from linea import Linea

class Factura:
    """
    Clase Factura
    ---
    La clase Factura representa una factura de compra, compuesta por un
    código de factura, el cliente al que corresponde, y los artículos que la
    forman.
    """
    __ultimo = 0
    __ultima_linea = 0
    __facturas = {}

    def __init__(self, cliente):
        """Constructor de la clase Factura"""
        self.__ultimo += 1
        self.__codigo = self.__ultimo
        self.__cliente= cliente
        self.__lineas = {}  # {num_linea : Linea}
        self.__facturas[self.__codigo] = self

    def __repr__(self):
        return f'Factura Nº{self.__codigo} - {self.__cliente}\n{self.__lineas}\nTotal: {self.importe_total()}€'

    # ActiveRecord
    @staticmethod
    def get_factura(codigo):
        """
        Devuelve una factura existente en el registro a partir de su código.

        Parámetros:
        codigo: int -> el código de la factura a buscar
        """
        return Factura.__facturas.get(codigo)

    '''
    def lineas(self):
        """Devuelve el registro de líneas pertenecientes a la factura."""
        return self.__lineas
    '''
    def codigo(self):
        """Devuelve el código de la factura."""
        return self.__codigo

    def cliente(self):
        """Devuelve el cliente involucrado en la factura."""
        return self.__cliente

    def agregar_linea(self, articulo, cantidad):
        """
        Incorpora un nuevo artículo y su cantidad a la factura.

        Parámetros:
            articulo: Articulo -> el artículo a incluir en la línea
            cantidad: int -> El número de unidades del artícuo a incluir en la línea
        """
        self.__ultima_linea += 1
        linea = Linea(articulo, cantidad)
        self.__lineas[self.__ultima_linea] = linea

    def borrar_linea(self):
        """Elimina la última línea añadida a la factura."""
        del self.__lineas[self.__ultima_linea]
        self.__ultima_linea -= 1

    def importe_total(self):
        """Calcula y devuelve el importe total de la factura."""
        importe = 0
        for linea in self.__lineas.values():
            importe += linea.subtotal()
        return importe

"""
    # Metodo para imprimir factura?
    def imprimir_factura(self):
        print('Factura Nº' + self.codigo() + ' - Cliente: ' + self.cliente().nombre())
        print('Artículo; Precio; Cantidad; Subtotal')
        for articulo, cantidad in self.lineas().items():
            print (articulo.denom() + '; ' + articulo.precio() + ';' + cantidad + '; ' + (articulo.precio * cantidad))
        print('Total: ' + self.importe_total)
"""
