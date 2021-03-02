class Lector:

    __ultimo = 0

    def __init__(self, nombre, apellidos):
        self.__ultimo += 1
        self.__numero = self.__ultimo
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__moroso = False

    def __repr__(self):
        return f'nº lector: {self.__numero}, {self.__nombre} {self.__apellidos} (Moroso?: {self.__moroso})'

    def numero(self):
        return self.__numero

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def moroso(self):
        return self.__moroso

    def set_moroso(self, valor):
        self.__moroso = valor
