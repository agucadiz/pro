from cliente import Cliente
from cuenta import Cuenta
import movimiento

"""
Clase principal
"""

jorge = Cliente('22233344A', 'Jorge', 'López')

cuenta1 = Cuenta(1234, jorge, 100)



cuenta1.realizar_movimiento('dietas', -20)

# cuenta1.movimientos()
