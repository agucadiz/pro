class Persona:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def nombre(self):
        return self.__nombre

    def edad(self):
        return self.__edad

    def comparar(self, persona):
        if self.__edad > persona.edad():
            print (f'{persona.nombre()} es más viejo que yo')
        elif self.__edad == persona.edad():
            print (f'{persona.nombre()} tiene la misma edad que yo')
        else: print (f'{persona.nombre()} es más joven que yo')
