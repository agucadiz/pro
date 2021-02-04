# se encargara de barajar las cartas y comprobarlas
import cartas
from random import shuffle as mezclar

def barajar():
    # Baraja las cartas de forma aleatoria.
    mezclar(cartas.baraja)
    print('(El repartidor mezcla las cartas cuidadosamente.)')

def mostrar():
    # Crea una copia de la baraja identificandola con sus siglas.
    mano = []
    for carta in cartas.baraja:
        if carta == cartas.GE:
            mano.append('[GE]')
        elif carta == cartas.E:
            mano.append('[E]')
        elif carta == cartas.F:
            mano.append('[F]')
        elif carta == cartas.GF:
            mano.append('[GF]')
    print('(El repartidor voltea tu carta y...)')
    print('\n', mano, '\n')

def comprobar(carta, jugador):
    # Comprueba y anuncia la carta elegida por el jugador.
    if carta == cartas.GE:
        print('Repartidor.- ¡La fortuna te sonríe, gran éxito!.')
        jugador['vida'] = jugador['vida'] + 2
    elif carta == cartas.E:
        print('Repartidor.- No está mal ¡Es un éxito!.')
        jugador['vida'] = jugador['vida'] + 1
    elif carta == cartas.F:
        print('Repartidor.- Mas suerte la proxima vez, es un fracaso.')
        jugador['vida'] = jugador['vida'] - 1
    elif carta == cartas.GF:
        print('Repartidor.- La desgracia se cierne sobre tí, es un gran fracaso.')
        jugador['vida'] = jugador['vida'] - 2

    print('La vida de', jugador['nombre'], 'es de:', jugador['vida'])
def repartir():
    # Reparte las cartas al jugador y le de la opción de elegir una de ellas.
    correcto = False    # Auxiliar para controlar la ejecución de la sentencia while
    seleccion = None
    print()
    print ('[XX] [XX] [XX] [XX]')
    print()
    while not correcto:
        try:
            seleccion = int(input('Elige una carta([1 - 4]): ')) - 1
            if seleccion < 4:
                correcto = True
            else:
                print('Repartidor.- Por favor, elige una opción válida ([1 - 4]).')
        except ValueError:
            print('Repartidor.- Por favor, elige una opción válida ([1 - 4]).')
    return seleccion

def repetir():
    # Pregunta al jugador si quiere comenzar una nueva partida.
    correcto = False    # Auxiliar para controlar la ejecución de la sentencia while.
    respuesta = None
    while not correcto:
        try:
            respuesta = input('¿Te gustaría probar suerte de nuevo (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                print('Repartidor.- Muy bien, volvamos a empezar entonces')
                return True
            else :
                print('Repartidor.- De acuerdo. ¡Vuelve cuando quieras!')
                break
        except ValueError:
            print('Por favor, elige una opción válida.')

def explicar():
    # Explica al jugador las reglas del juego.
    correcto = False    # Auxiliar para controlar la ejecución de la sentencia while.
    respuesta = ''
    print('\nRepartidor.- Bien, presta atención, seré breve:')
    print('\nVoy a barajar 4 cartas y tu tendrás que seleccionar una de ellas.')
    print('Las cartas pueden presentar los siguientes valores:')
    print('\n[Gran Éxito] | [Éxito] | [Fracaso] | [Gran Fracaso]')
    print('\nTendrás que elegir una al azar, y así descubriremos tu destino')
    while not correcto:
        try:
            respuesta = input('¿Quieres que te lo repita (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                explicar()
                correcto = True
            elif respuesta == 'N':
                correcto = True
        except ValueError:
            print('Por favor, elige una opción válida.')
