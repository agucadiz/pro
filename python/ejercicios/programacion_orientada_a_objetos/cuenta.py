"""
Clase que controla las cuentas
Detalles:
1. No se puede cambiar el numero de cuenta
2. Se puede añadir un mov a una cuenta, pero no cambiar ni eliminarlos
3. Tampoco se puede modificar directamente el saldo, sino que se debe
    actualizar a traves de los movs que se realicen en la cuneta.
"""

class Cuenta():

    def __init__(self, numero, titular, movimientos, saldo):
        __numero = numero
        __titular = titular
        __movimientos = movimientos
        __saldo = saldo
