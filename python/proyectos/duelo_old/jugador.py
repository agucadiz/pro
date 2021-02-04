"""
Se aloja a los jugadores en una lista y sus datos en un diccionario
Tienen esta estructura:

Jugador {'nombre' : 'jugador1', 'vida' : VIDA_INICIAL, 'bot' : True | False}
"""
VIDA_INICIAL = 4
jugadores = []

def crear_jugador(nombre_jugador, es_bot):
        jugadores.append({'nombre' : nombre_jugador, 'vida' : VIDA_INICIAL, 'bot' : es_bot})
