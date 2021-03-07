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
        Carta.__baraja[self.__numero] = self

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
    def mostrar_cartas_():
        """Devuelve de todas las cartas de la baraja."""
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


class Naipe(Carta):

    # Crear una especie de parser que nos describa la carta en un lenguaje natural, a partir del palo y el valor
    def __init__(self, palo, valor):
        super().__init__(Naipe.generar_corta(palo, valor), Naipe.generar_larga(palo, valor))
        self.__palo = palo
        self.__valor = valor
        # self.

    def __repr__(self):
        return f"Naipe('{self.valor()}', '{self.palo()}')"

    def palo(self):
        """"Devuelve el palo de un naipe."""
        return self.__palo

    def valor(self):
        """Devuelve el valor de un naipe."""
        return self.__valor

    def calcular_valor(naipe1, naipe2):
        """Compara dos cartas y devuelve la de valor superior."""
        if naipe1.valor() > naipe2.valor():
            return naipe1
        else: return naipe2

    @staticmethod
    def generar_baraja():
        """Genera una baraja de naipes española de 40 cartas."""
        palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
        valores = list(range(1, 11))
        for palo in palos:
            for valor in valores:
                Naipe(palo, valor)

    @staticmethod
    def generar_corta(palo, valor):
        """
        Genera una decripción corta de un naipe, a partir de su palo y valor.
        La descripción corta de un naipe tiene esta composición:
            - El primer caracter del palo : 'Bastos'[0] -> 'B'
            - El literal del valor : 7 -> '7'
        Ejemplo: 'Rey de Bastos' -> 'B10'
        """
        palo = palo[0]
        valor = str(valor)
        return palo + valor

    @staticmethod
    def generar_larga(palo, valor):
        """Genera una decripción larga de un naipe, a partir de su palo y valor."""
        literales = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete','Sota', 'Caballero', 'Rey']
        return f'{literales[valor-1]} de {palo}'

    @staticmethod
    def mostrar_naipes():
        """Descubre todas las naipes de de la baraja, devolviendo su descripción."""
        resultado = ' - '
        for naipe in Naipe.baraja().values():
            resultado += (f'{naipe.larga()},  ')

        return resultado

'''
class Yugi(Carta):
    def __init__(self, corta, larga, ataque, defensa):
        super().__init__(corta, larga)
        self.__ataque = ataque
        self.__defensa = defensa

    def __repr__(self):
        return f'Tugi({self.__corta}, {self.__larga}, {self.__ataque}, {self.__defensa})'

    def ataque(self):
        """Devuelve el ataque de la carta."""
        return self.__ataque

    def defensa(self):
        """Devuelve el defensa de la carta."""
        return self.__defensa

    def calcular_danyo(carta1, carta2):
        diferencia = carta2.defensa() - carta1.ataque()

Código para pruebas:
carta1 = Carta('GE', 'Gran exito')
carta2 = Carta('E', 'Exito')
carta3 = Carta('F', 'Fracaso')
carta4 = Carta('GF', 'Gran Fracaso')

print(Carta.mostrar_cartas())

--BASURA--
if self.corta(0) = 'O':
            return 'Oros'
        if self.corta(0) = 'C':
            return 'Copas'
        if self.corta(0) = 'E':
            return 'Espadas'
        if self.corta(0) = 'B':
            return 'Bastos'
'''
