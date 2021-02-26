from cliente import Cliente
from cuenta import Cuenta

antonio = Cliente ('111222333F', 'Antonio', 'Martínez')
cuenta_antonio1 = Cuenta(antonio)
cuenta_antonio2 = Cuenta(antonio)

cuenta_antonio1.realizar_movimiento('Depósito inicial', 1000)
cuenta_antonio1.realizar_movimiento('gasolinera', -20)
cuenta_antonio1.realizar_movimiento('Ingreso Nómina', 895.67)
cuenta_antonio1.movimientos()

cuenta_antonio2.realizar_movimiento('Depósito inicial', 9000)
cuenta_antonio2.realizar_movimiento('Compra ordenador', -789.99)
cuenta_antonio2.realizar_movimiento('Netflix', 12.67)
cuenta_antonio2.movimientos()
