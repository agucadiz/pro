class Coleccion:
    def __init__(self):
        """Inicializa la colección."""
        self.__coleccion = {}

    def __iter__(self):
        return iter(self.__coleccion)

    def __len__(self):
        return len(self.__coleccion)

    def itera_valores(self):
        return iter(self.__coleccion.values())

    def elemento(self, k):
        """
        Devuelve el elemento cuya clave es k.

        Lanza una excepción KeyError si la clave k no está.
        """
        return self.__coleccion[k]

    def set_elemento(self, k, e):
        """
        Inserta el elemento e con la clave k.
        """
        self.__coleccion[k] = e

    def del_elemento(self, k):
        """
        Quita de la colección elemento con clave k.

        Lanza una excepción KeyError si la clave k no existe.
        """
        del self.__coleccion[k]


class ColeccionConexiones(Coleccion):
    def __iter__(self):
        return self.itera_valores()

    def anyadir_conexion(self, con):
        self.set_elemento(con.direccion(), con)

    def salida_hacia(self, verbo):
        try:
            return self.elemento(verbo)
        except KeyError:
            return None

    def describir_salidas(self):
        ret = []
        for conexion in self:
            ret.append(str(conexion.direccion()))
        return 'Salidas: ' + ', '.join(ret)
