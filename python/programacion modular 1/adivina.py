import random

def adivina():
    op = 0
    intentos = 0
    num = random.randint(1,100)
    print('Estoy pensando en un número del 1 al 100... ¡Adivínalo!')
    while op != num:
        try:
            if intentos == 0:
                op = int(input('Prueba un número: '))
                intentos +=1
            else:
                op = int(input('Prueba otra vez: '))
                intentos +=1

            if op < num:
                print('¡Más!')
            else:
                print('¡Menos!')
        except ValueError:
            op = print('¡Cuidado, sólo números!')
    print('¡Enhorabuena, has acertado en', intentos, 'intentos!')
