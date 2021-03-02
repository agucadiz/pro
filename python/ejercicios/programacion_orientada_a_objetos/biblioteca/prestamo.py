from datetime import datetime

class Prestamo:

    prestamos = []

    def __init__(self, lector, libro):
        self.__lector = lector
        if libro.prestado() is False:   # este modo es mas sencillo, pero desconocemos quien tiene el libro
            self.__libro = libro
            self.__libro.set_prestado(True)
            self.__fecha_prestamo = datetime.today()
            self.__fecha_devolucion = None
            Prestamo.prestamos.append(self)
        else:
            print('Lo sentimos, pero el libro "'+libro.titulo()+'" se encuentra en préstamo.')

    def __repr__(self):
        return f'Prestamo (Lector: {self.__lector}, Libro: {self.__libro}, Fecha préstamo: {self.__fecha_prestamo}, Fecha devolución: {self.__fecha_devolucion})'

    def lector(self):
        return self.__lector

    def libro(self):
        return self.__libro

    def fecha_prestamo(self):
        return self.__fecha_prestamo

    def fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion(self, fecha):
        self.__fecha_devolucion = fecha

    def devolver_libro(self, fecha):
        # self.set_fecha_devolucion(datetime.today()) - solución más elegante
        self.set_fecha_devolucion(fecha)
        self.libro().set_prestado(False)
        diferencia = abs(self.fecha_devolucion() - self.fecha_prestamo()).days
        if diferencia > 15:
            self.lector().set_moroso(True)
