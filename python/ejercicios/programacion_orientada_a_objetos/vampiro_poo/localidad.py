from coleccion import ColeccionConexiones
from conexion import Conexion

class Localidad:
    def __init__(self, corta, larga):
        self.set_corta(corta)
        self.set_larga(larga)
        self.__conexiones = ColeccionConexiones()

    def corta(self):
        return self.__corta

    def set_corta(self, corta):
        self.__corta = corta

    def larga(self):
        return self.__larga

    def set_larga(self, larga):
        self.__larga = larga

    def conexiones(self):
        return self.__conexiones

    def set_conexiones(self, conexiones):
        for direccion, destino in conexiones.items():
            con = Conexion(direccion, destino)
            self.__conexiones.anyadir_conexion(con)

    def describir(self):
        print(self.corta())
        print(self.larga())
        self.describir_salidas()

    def salida_hacia(self, verbo):
        return self.__conexiones.salida_hacia(verbo)

    def describir_salidas(self):
        print(self.__conexiones.describir_salidas())
