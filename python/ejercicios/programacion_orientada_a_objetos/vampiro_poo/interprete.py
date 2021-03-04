"""
Se encarga de todo lo relacionado con la interpretación de la
entrada del jugador.

El módulo almacena el último verbo y el último nombre reconocidos.

El análisis de la entrada del jugador se lleva a cabo en la función
interpretar.
"""

import vocabulario as voc

class Interprete:
    __verbo = None
    __nombre = None

    @staticmethod
    def verbo():
        """
        Devuelve el último verbo reconocido.

        Args:
            - No tiene

        Returns:
            - El último verbo reconocido, o None si no se
            ha reconocido ninguno.
        """
        return Interprete.__verbo

    @staticmethod
    def nombre():
        """Devuelve el último nombre reconocido."""
        return Interprete.__nombre

    @staticmethod
    def interpretar(orden):
        """
        Interpreta la orden del jugador.

        Args:
            - orden: str => La orden del jugador.

        Returns:
            - None

        Modifica:
            - Las variables globales _verbo y _nombre.
        """
        Interprete.__verbo, Interprete.__nombre = None, None
        lista = orden.upper().split()
        if len(lista) >= 1:
            Interprete.__buscar_verbo_primera_palabra(lista)
        if len(lista) >= 2:
            Interprete.__buscar_nombre_segunda_palabra(lista)

    @staticmethod
    def marcar_error_sintactico():
        Interprete.__verbo = None

    @staticmethod
    def hay_error_sintactico():
        return Interprete.__verbo is None

    @staticmethod
    def verbo_es_direccion():
        return isinstance(Interprete.__verbo, voc.Direccion)

    @staticmethod
    def __buscar_verbo_primera_palabra(lista):
        token = voc.Token.get_token(lista[0])
        if token is not None:
            if isinstance(token, voc.Verbo):
                Interprete.__verbo = token
                Interprete.__nombre = None
            elif isinstance(token, voc.Nombre):
                Interprete.marcar_error_sintactico()
                Interprete.__nombre = None

    @staticmethod
    def __buscar_nombre_segunda_palabra(lista):
        token = voc.Token.get_token(lista[1])
        if token is not None:
            if isinstance(token, voc.Nombre):
                Interprete.__nombre = token
            else:
                Interprete.marcar_error_sintactico()
