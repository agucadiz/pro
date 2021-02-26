from articulo import Articulo
from cliente import Cliente
from factura import Factura


lucia = Cliente('111222333A', 'Lucía', 'Peña')

tele = Articulo('Televisor', 399)

factura1 = Factura(lucia)

factura1.anyadir_articulo(tele, 2)

# factura1.total() = 798 € - Pensamiento optimista
factura1.importe_total()
