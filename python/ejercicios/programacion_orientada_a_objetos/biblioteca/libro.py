class Libro:

    __ultimo = 0
    # __ultimo_lector - último Lector que retiró el libro?

    def __init__(self, titulo, autor, editorial):
        self.__ultimo +=1
        self.__codigo = self.__ultimo
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__prestado = False

    def __repr__(self):
        return f'ISBN: {self.__codigo}, "{self.__titulo}", por {self.__autor}. Editorial: {self.__editorial}. En prestamo?: {self.__prestado}'

    def codigo(self):
        return self.__codigo

    def titulo(self):
        return self.__titulo

    def autor(self):
        return self.__autor

    def editorial(self):
        return self.__editorial

    def prestado(self):
        return self.__prestado

    def set_prestado(self, valor):
        self.__prestado = valor
