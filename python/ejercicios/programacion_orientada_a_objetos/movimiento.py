class Movimiento:
    """
        # Movimiento (Clase)
        Los movimientos son INMUTABLES, por lo que no tendrán métodos mutadores
        Los movimientos pertenecen a una sola cuenta
        ## Atribs:
        - concepto -> str (inmutable)
        - cantidad -> int (inmutable, puede ser un valor negativo o positivo)
    """

    def __init__(self, concepto, cantidad):
        self.__concepto = concepto
        self.__cantidad = cantidad

    def concepto(self):
        return self.__concepto

    def cantidad(self):
        return self.__cantidad

    def __repr__(self):
        return f'Movimiento (Concepto: {self.__concepto} , Cantidad: {self.__cantidad})'
