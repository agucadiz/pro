from articulo import Articulo
from cliente import Cliente
from factura import Factura

def principal():
    lucia = Cliente('111222333A', 'Rosa', 'González')

    tele = Articulo('Televisor', 399)

    grafica = Articulo('Tarjeta Gráfica', 239)

    factura1 = Factura(lucia)

    factura1.agregar_linea(tele, 2)
    factura1.agregar_linea(grafica, 1)

    print(factura1)

if __name__ == "__main__":
    principal()
