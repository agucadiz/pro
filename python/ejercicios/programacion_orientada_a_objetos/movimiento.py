"""
Clase estática basada en la de interacción entre cuentas
Los movimientos son INMUTABLES, por lo que cada movimiento estará dentro de una tupla.
Los movimientos pertenecen a una sola cuenta
"""

class Movimiento:

    @staticmethod
    def generar_movimiento(concepto, cantidad):
        """Devuelve una tupla con la estructura (concepto, cantidad)"""
        __concepto = concepto
        __cantidad = cantidad
        return (__concepto, __cantidad)

    @staticmethod
    def cantidad(movimiento):
        return movimiento[1]



""" Sample code:
> >> mov1 = Movimiento.generar_movmiento('dietas', -20)
> >> mov1
('dietas', -20)
> >> Movimiento.cantidad(mov1)
-20
"""
