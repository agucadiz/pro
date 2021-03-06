# ¿Traerme funciones del repartidor aquí?
from random import shuffle as mezclar

class Carta:
    """
    Cartas
    ---
    La clase Carta representa y almacena las cartas en una baraja.
    La carta está compuesta por:
        - corta: str -> Descripción corta de la carta (ej: 'RC')
        - larga: str -> Descripción larga de la carta (ej: 'Rey de copas')

    Ea la baraja, las cartas se identifican por:
        - int numero; Numero que define en que posición se encuentra la carta dentro de la baraja.
        - Su valor, compuesto por una carta.

    """
    __baraja = {}
    __ultima = 0

    def __init__(self, corta, larga):
        """Constructor de la clase Carta"""
        Carta.__ultima += 1
        self.__numero = Carta.__ultima
        self.__corta = corta
        self.__larga = larga
        Carta.__baraja [self.__numero] = self

    def __repr__(self):
        return f"Carta('{self.corta()}', '{self.larga()}')"

    @staticmethod
    def get_carta(seleccion):
        """
        Devuelve una carta existente en la baraja a partir de su número.

        Parámetros:
            - seleccion: int -> La n-ésima carta de la baraja.
        """
        return Carta.baraja().get(seleccion)

    def numero(self):
        """Devuelve el numero de la carta."""
        return self.__numero

    def corta(self):
        """Devuelve una descripción (o denominación) de la carta."""
        return self.__corta

    def larga(self):
        """Devuelve una descripción larga de la carta."""
        return self.__larga

    @staticmethod
    def baraja():
        """Devuelve la baraja."""
        return Carta.__baraja

    @staticmethod
    def mostrar_cartas():
        """Devuelve las denominaciones de todas las cartas."""
        resultado = ' - '
        for carta in Carta.baraja():
            resultado += (f'{Carta.describir(carta)} - ')
        return resultado

    @staticmethod
    def barajar():
        """Mezcla las cartas de la baraja de forma aleatoria."""
        temp = list(Carta.baraja().values())
        mezclar(temp)
        Carta.__baraja = dict(zip(Carta.baraja(), temp))

    @staticmethod
    def describir(seleccion):
        """
        Devuelve una descripción completa de una carta de la baraja.
        Parámetros:
            - seleccion: int -> La n-ésima carta de la baraja.
        """
        seleccion = Carta.get_carta(seleccion)
        return f'{seleccion.corta()}: {seleccion.larga()}'

"""Código para pruebas:
carta1 = Carta('GE', 'Gran exito')
carta2 = Carta('E', 'Exito')
carta3 = Carta('F', 'Fracaso')
carta4 = Carta('GF', 'Gran Fracaso')

print(Carta.mostrar_cartas())
"""
