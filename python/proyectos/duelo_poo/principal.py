from carta import  Naipe
from jugador import Jugador

def principal():
    Naipe.generar_baraja()
    Jugador.asignar_bots(4)
    Naipe.barajar()

    for jugador in Jugador.jugadores():
        jugador.recibir_mano(Naipe.repartir(3))
        print(jugador)

    print(f'Baraja descubierta:\n{Naipe.mostrar_baraja()}')

if __name__ == "__main__":
    principal()
