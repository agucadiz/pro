class Token:
    __tokens = {}

    def __init__(self, lexemas):
        self.__ident = lexemas[0]
        for lexema in lexemas:
            Token.__tokens[lexema] = self

    def __str__(self):
        return self.__ident

    @staticmethod
    def get_token(lexema):
        return Token.__tokens.get(lexema)

class Verbo(Token):
    pass

class Direccion(Verbo):
    pass

class Nombre(Token):
    pass

COGER = Verbo(['COGER', 'COGE', 'TOMAR', 'TOMA'])
DEJAR = Verbo(['DEJAR', 'DEJA'])
NORTE = Direccion(['NORTE', 'N'])
SUR = Direccion(['SUR', 'S'])
ESTE = Direccion(['ESTE', 'E'])
OESTE = Direccion(['OESTE', 'O'])
ARRIBA = Direccion(['ARRIBA', 'SUBIR'])
ACABAR = Verbo(['ACABAR', 'TERMINAR', 'FIN'])
TRAJE = Nombre(['TRAJE'])
CUCHILLO = Nombre(['CUCHILLO', 'NAVAJA'])
CRUCIFIJO = Nombre(['CRUCIFIJO', 'CRUZ'])
