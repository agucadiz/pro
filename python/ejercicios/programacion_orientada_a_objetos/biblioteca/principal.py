from datetime import datetime
from lector import Lector
from libro import Libro
from prestamo import Prestamo

def principal():
    # Lectores
    ana = Lector('Ana', 'García')
    roberto = Lector('Roberto', 'Sánchez')

    # Libros
    camino = Libro('El camino', 'Miguel Delibes', 'Austral')
    soledad = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Sagitario')
    rayuela = Libro('Rayuela', 'Julio Cortázar', 'Plutón')

    # Prestamos
    prestamo1 = Prestamo(ana, camino)
    prestamo2 = Prestamo(ana, soledad)
    prestamo3 = Prestamo(roberto, rayuela)

    prestamo_imposible = Prestamo(roberto, soledad)  # 6.f

    prestamo1.devolver_libro(datetime(2021,4,2))  # Devuelto después de 15 días

    print(prestamo1.libro()) # Prestado = False

    print(prestamo1.lector()) # Moroso = True

if __name__ == "__main__":
    principal()
