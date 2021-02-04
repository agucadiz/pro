# Módulo principal del programa "cartas". Por Eduardo Martínez Romero. 2021
import cartas
import repartidor
import jugador
from random import randint as aleatorio

_tuto = False    # Auxiliar para controlar la disponibilidad del tutorial.

def comenzar(): # Da comienzo la partida
    print('\nRepartidor.-¡Bienvenido de nuevo!')
    tutorial()  # El juego propone un tutorial que el jugador puede aceptar o no.
    asignar_jugadores()
    ronda()
    finalizar()             # Esperamos a la decisión del jugador.


def tutorial():
    # Pregunta al jugador si quiere que el repartidor le explique las reglas del juego.
    global _tuto # Cambiaremos _tuto para omitir el tutorial.
    if _tuto == True:
        return
    else:
        correcto = False
        while not correcto:
            try:
                respuesta = input('¿Quieres que te explique las reglas del juego (S/N)?: ').upper()
                if respuesta == 'S' or respuesta =='Y':
                    repartidor.explicar()
                    correcto = True
                elif respuesta == 'N':
                    correcto = True
            except TypeError:
                print('Por favor, elige una opción válida.')
        _tuto = True

def ronda():
    for i in jugador.jugadores:
            jugar(i)
            input('Pulsa una tecla para continuar...')

    for i in jugador.jugadores:     #verificamos que no haya perdido ningun jugador
        if i['vida'] <= 0:    # i['bot'] == False and
            finalizar()
        else:
            ronda()

def jugar(jugador):    # A jugar se le puede pasar un jugador como argumento
    # A traves del módulo repartidor realizaremos una partida.
    if jugador['bot'] == True:
        seleccion = aleatorio(0, 3)
        print('Repartidor.- Es el turno de', jugador['nombre'])
        repartidor.barajar()    # El repartidor baraja las cartas.
        seleccion = aleatorio(0, 3)   # El bot selecciona una carta del reparto.
        print('\nRepartidor.- Veamos como escapa nuestro compañero...')
        repartidor.mostrar()    # El repartidor muestra las cartas [...]
        repartidor.comprobar(cartas.baraja[seleccion], jugador)  # [...] Y comprueba su elección.
    else:
        print('Repartidor.- Vuelta al tajo. Ponte cómodo mientras barajo.')
        repartidor.barajar()    # El repartidor baraja las cartas.
        print('\nRepartidor.- Bueno, ahora te toca tí.')
        seleccion = repartidor.repartir()   # El jugador selecciona una carta del reparto.
        print('\nRepartidor.- Vamos a ver que terrible destino te espera...')
        repartidor.mostrar()    # El repartidor muestra las cartas [...]
        repartidor.comprobar(cartas.baraja[seleccion], jugador)  # [...] Y comprueba tu elección.

def finalizar():
    # El repartidor pregunta al jugador si quiere volver a jugar.
    print('\nRepartidor.- Bueno, esto ha sido todo por ahora.')
    decision = repartidor.repetir()
    if decision == True:
        comenzar()
    else:
        print('(El repartidor se desvanece en la oscuridad.)')

def asignar_jugadores():
    num_jugadores = int(input('¿Cuántos van a jugar esta vez?: '))
    for i in range(num_jugadores):
        nombre_jugador = input('¿Nombre del jugador?: ')
        try:
            respuesta = input('¿Es un bot (S/N)?: ').upper()
            if respuesta == 'S' or respuesta =='Y':
                jugador.crear_jugador(nombre_jugador, True)
            elif respuesta == 'N':
                jugador.crear_jugador(nombre_jugador, False)
        except ValueError:
                print('Por favor, elige una opción válida.')

if __name__ == "__main__":
    comenzar()
