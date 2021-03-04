from interprete import Interprete
from mapeado import *
from jugador import Jugador
import vocabulario as voc

jugador = Jugador(pasillo)
jugador.describe_localidad_actual()

while True:
    orden = input('> ')
    Interprete.interpretar(orden)
    if Interprete.hay_error_sintactico():
        print('No entiendo lo que quieres decirme.')
    elif Interprete.verbo_es_direccion():
        if not jugador.intentar_mover(Interprete.verbo()):
            print('No hay salida en esa dirección.')
    elif Interprete.verbo() == voc.ACABAR:
        if Interprete.nombre() is None:
            print('Hasta luego, Lucas.')
            break
        else:
            print('No entiendo lo que quieres decirme')
    else:
        print('Verbo:', Interprete.verbo())
        print('Nombre:', Interprete.nombre())
