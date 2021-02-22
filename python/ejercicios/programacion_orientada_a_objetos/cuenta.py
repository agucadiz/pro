from movimiento import Movimiento
"""
Clase que controla las cuentas
Detalles:
1. No se puede cambiar el numero de cuenta
2. Se puede añadir un mov a una cuenta, pero no cambiar ni eliminarlos
3. Tampoco se puede modificar directamente el saldo, sino que se debe
    actualizar a traves de los movs que se realicen en la cuneta.
"""

from movimiento import Movimiento


class Cuenta:
    """
        # Cuenta (Clase)
        Genera instancias de cuentas, asignadas a un cliente (titular)
        ## Atribs:
        - numero -> int (inmutable)
        - titular -> Cliente
        - saldo -> int (incializado a 0€)

    """
    __ultimo = 0
    __cuentas = {}      # Patrón ActiveRecord. La clase almacena las instancias

    def __init__(self, titular):
        Cuenta.__ultimo += 1
        self.__numero = Cuenta.__ultimo      # sin mutador (1)
        self.__titular = titular    # recibe instancia de la clase Cliente
        self.__movimientos = []     # lista vacía
        self.__saldo = 0
        Cuenta.__cuentas[self.__numero] = self

    @staticmethod
    def get_cuenta(numero):
        return Cuenta.__cuentas.get(numero)

    def numero(self):
        return self.__numero

    def titular(self):
        return self.__titular

    def movimientos(self):
        return self.__movimientos

    def saldo(self):
        return self.__saldo

    def __set_saldo(self, saldo):
        self.__saldo = saldo

    def realizar_movimiento(self, concepto, cantidad):
        mov = Movimiento(concepto, cantidad)
        self.__agregar_movimiento(mov)
        self.__set_saldo(self.saldo() + mov.cantidad())

    def __agregar_movimiento(self,movimiento):
        self.__movimientos.append(movimiento)

    def __repr__(self):
        return f'Cuenta (nº cuenta: {self.__numero}, Titular: {self.__titular}, saldo: {self.__saldo}€)'
