from cliente import Cliente
from cuenta import Cuenta

jorge = Cliente('111222333A', 'Jorge', 'López')

cuenta1 = Cuenta(jorge)

cuenta1.realizar_movimiento('Depósito inicial', 1000)

cuenta1.realizar_movimiento('gasolinera', -20)

cuenta1.realizar_movimiento('Ingreso Nómina', 895.67)

cuenta1.movimientos()
