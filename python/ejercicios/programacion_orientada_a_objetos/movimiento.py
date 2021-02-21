# Clase basada en la de interacción entre cuentas
# Los movimientos son INMUTABLES
# Los movimientos pertenecen a una sola cuenta
class Movimiento():

    def __init__(self, concepto, cantidad):
        __concepto = concepto
        __cantidad = cantidad
