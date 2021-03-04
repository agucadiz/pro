class Jugador:
    def __init__(self, localidad_actual):
        self.__localidad_actual = localidad_actual

    def localidad_actual(self):               # getter, selectora
        return self.__localidad_actual

    def set_localidad_actual(self, localidad_actual):
        self.__localidad_actual = localidad_actual

    def mover_jugador(self, destino):
        self.set_localidad_actual(destino)
        self.describe_localidad_actual()

    def describe_localidad_actual(self):
        self.localidad_actual().describir()

    def intentar_mover(self, verbo):
        destino = self.localidad_actual().salida_hacia(verbo)
        if destino is not None:
            self.mover_jugador(destino)
            return True
        return False
