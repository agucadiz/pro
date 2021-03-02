from datetime import datetime
from lector import Lector
from libro import Libro
from prestamo import Prestamo

def principal():

    # Lectores
    ana = Lector('Ana', 'García')
    roberto = Lector('Roberto', 'Sánchez')

    # Libros
    camino = Libro('El camino', 'Miguel Delibes', 'Mis huevos al viento')
    soledad = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Mis huevos al viento')
    rayuela = Libro('Rayuela', 'Julio Cortázar', 'Mis huevos al viento')

    # Prestamos
    prestamo1 = Prestamo(ana, camino)

    print(prestamo1)

    prestamo2 = Prestamo(ana, soledad)
    prestamo3 = Prestamo(roberto, rayuela)

    prestamo_imposible = Prestamo(roberto, soledad)  # Actividad 6.f

    prestamo1.devolver_libro(datetime(2021,4,2))  # Devuelto después de 15 días

    print(prestamo1.libro()) # Prestado debería ser False

    print(prestamo1.lector()) # Moroso debería ser True

if __name__ == "__main__":
    principal()
