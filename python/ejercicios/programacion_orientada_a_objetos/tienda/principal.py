from articulo import Articulo
from cliente import Cliente
from factura import Factura

def principal():
    # Clientes.
    lucia = Cliente('111222333A', 'Rosa', 'González')

    # Artículos.
    tele = Articulo('Televisor', 399)
    grafica = Articulo('Tarjeta Gráfica', 239)
    placa = Articulo('Placa Base', 98)
    cpu = Articulo('Procesador', 122)

    # Facturas
    factura1 = Factura(lucia)

    # Funciones de factura - Añadiendo y eliminando elementos.
    factura1.agregar_linea(tele, 2)
    factura1.agregar_linea(grafica, 1)
    factura1.agregar_linea(placa, 1)

    print(factura1)
    factura1.borrar_linea()
    print(factura1)
    factura1.agregar_linea(cpu, 2)

    # usando la función get_factura.
    print(Factura.get_factura(1))

if __name__ == "__main__":
    principal()
