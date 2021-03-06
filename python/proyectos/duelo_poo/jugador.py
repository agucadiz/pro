from random import randint as aleatorio

VIDA_INICIAL = 4

class Jugador:

    __ultimo = 0
    __jugadores = {}

    def __init__(self, nombre, vida, bot):
        Jugador.__ultimo += 1
        if Jugador.comprobar_nombre(nombre) is True:
            self.__numero = self.__ultimo
            self.__nombre = nombre
            self.__vida = vida
            self.__bot = bot
            Jugador.__jugadores[self.__numero] = self
        else:
            print('Lo sentimos, pero ya existe un jugador con el nombre "'+ nombre +'".')

    def __repr__(self):
        return f'Jugador({self.__nombre}, {self.__vida}, {self.__bot})'

    def __str__(self):
        return f'{self.nombre()} | Salud: {self.vida()}'

    def numero(self):
        return self.__numero

    def nombre(self):
        return self.__nombre

    def vida(self):
        return self.__vida

    def bot(self):
        return self.__bot

    @staticmethod
    def jugadores():
        return Jugador.__jugadores

    @staticmethod
    def nombre_aleatorio():
        nombres = ('Lucía', 'Roberto', 'Belén', 'Alicia',
            'Juan', 'Paloma', 'Natalia', 'Josemi','Andrés', 'Isabel', 'Pablo','Álex',
            'Vicenta', 'Marisa', 'Concha', 'Mauri', 'Fernando',
            'Emilio', 'Mariano', 'Paco'
            )
        return nombres[aleatorio(0, (len(nombres) - 1))]

    @staticmethod
    def comprobar_nombre(nombre):
        resultado = True
        for i in Jugador.jugadores().values():
            if nombre == i.nombre():
                resultado = False
        return resultado

    @staticmethod
    def asignar_humanos(num_jugadores):
        """Creador interactivo de humanos. Solicita por entrada el nombre del jugador."""
        for i in range(num_jugadores):
            try:
                nombre_jugador = str(input('¿Nombre del jugador?: '))
            except ValueError:
                print('Por favor, elige una opción válida.')
            Humano(nombre_jugador)

    @staticmethod
    def asignar_bots(num_bots):
        """Creador interactivo de bots. Asigna nombres de forma automática."""
        for i in range(num_bots):
            Bot()

class Humano(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre, VIDA_INICIAL, False)

    def __str__(self):
        return f'Humano: {super().__str__()}'

class Bot(Jugador):
    def __init__(self):
        super().__init__(self.nombre_aleatorio(), VIDA_INICIAL, True)

    def __str__(self):
        return f'BOT: {super().__str__()}'
