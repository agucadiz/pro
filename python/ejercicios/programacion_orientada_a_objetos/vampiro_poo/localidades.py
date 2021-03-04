import localidad
import coleccion

VESTIBULO = 0
MITAD_PASILLO = 1
COCINA = 2
BIBLIOTECA = 3

_localidades = coleccion.coleccion()

datos_localidad = {
    VESTIBULO: localidad.localidad(
        'VESTÍBULO',
        'Estás en el vestíbulo del castillo.'
    ),
    MITAD_PASILLO: localidad.localidad(
        'Estás en mitad del pasillo.',
        'MITAD PASILLO'
    ),
    COCINA: localidad.localidad(
        'Estás en la cocina.',
        'COCINA'
    ),
    BIBLIOTECA: localidad.localidad(
        'Estás en la biblioteca.',
        'BIBLIOTECA'
    )
}

for clave, loc in datos_localidad.items():
    coleccion.insertar(_localidades, clave, loc)

"""
Cocina --- Mitad pasillo --- Biblioteca
                |
            Vestíbulo
"""

_conexiones = {
    VESTIBULO: {
        'N': MITAD_PASILLO
    },
    MITAD_PASILLO: {
        'S': VESTIBULO,
        'E': BIBLIOTECA,
        'O': COCINA,
    },
    BIBLIOTECA: {
        'O': MITAD_PASILLO,
    },
    COCINA: {
        'E': MITAD_PASILLO,
    },
}

def salida_hacia(localidad_actual, verbo):
    salidas = _conexiones[localidad_actual]
    return salidas.get(verbo)

def localidad(k):
    """
    Devuelve la localidad cuya clave es k en la colección de localidades.

    Lanza una excepción KeyError si la localidad con clave k no existe.
    """
    return coleccion.elemento(_localidades, k)
