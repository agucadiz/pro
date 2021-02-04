"""
04/02/2021
Práctica de clase
"""
class Deposito:
    """
    # Clase para la gestión de cuentas bancarias.
    ## Variables de instancia:
    - saldo -> int
    """
    def __init__(self, saldo):
        """Constructor de la clase"""
        self.saldo = saldo

    def saldo_actual(self):
        return self.saldo

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError('Fondos insuficientes')
        self.saldo -= cantidad

    def transferir(self, destino, cantidad):
        self.retirar(cantidad)
        destino.ingresar(cantidad)
