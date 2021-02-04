# Módulo principal del programa "cartas". Por Eduardo Martínez Romero. 2021
import cartas, repartidor
_tuto = False    # Auxiliar para controlar la disponibilidad del tutorial.

def comenzar(): # Da comienzo la partida
    print('\nRepartidor.-¡Bienvenido de nuevo!')
    tutorial()  # El juego propone un tutorial que el jugador puede aceptar o no.
    jugar()


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

def jugar():
    # A traves del módulo repartidor realizaremos una partida.
    print('Repartidor.- Comienza una nueva partida. Ponte cómodo mientras barajo.')
    repartidor.barajar()    # El repartidor baraja las cartas.
    print('\nRepartidor.- Bueno, ahora te toca tí.')
    seleccion = repartidor.repartir()   # El jugador selecciona una carta del reparto.
    print('\nRepartidor.- Vamos a ver que terrible destino te espera...')
    repartidor.mostrar()    # El repartidor muestra las cartas [...]
    repartidor.comprobar(cartas.baraja[seleccion])  # [...] Y comprueba tu elección.
    print('\nRepartidor.- Bueno, esto ha sido todo por ahora.')
    finalizar()             # Esperamos a la decisión del jugador.

def finalizar():
    # El repartidor pregunta al jugador si quiere volver a jugar.
    decision = repartidor.repetir()
    if decision == True:
        comenzar()
    else:
        print('(El repartidor se desvanece en la oscuridad.)')

if __name__ == "__main__":
    comenzar()
