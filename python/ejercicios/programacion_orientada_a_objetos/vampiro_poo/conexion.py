from vocabulario import Token

class Conexion:
    def __init__(self, direccion, destino):
        self.__direccion = direccion
        self.__destino = destino

    def direccion(self):
        return self.__direccion

    def destino(self):
        return self.__destino
