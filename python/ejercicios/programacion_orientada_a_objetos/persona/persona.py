class Persona:
    """
    Clase Persona
    ---
    La clase persona representa a una persona, la cual se \
    idenfitica por su nombre y su edad.
    """
    def __init__(self, nombre, edad):
        """Constructor de la clase Persona."""
        self.__nombre = nombre
        self.__edad = edad

    def __eq__(self, otro):
        """
        Devuelve True si otra persona tienen el \
        mismo nombre y apellido, False en caso contrario y \
        NotImplemented si no comparten el mismo tipo.
        """
        if not isinstance(otro, type(self)):
            return NotImplemented
        return (self.__nombre, self.__edad) == (otro.__nombre, otro.__edad)

    def __hash__(self):
        """Devuelve el hash de una persona."""
        return hash((self.__nombre, self.__edad))

    def __repr__(self):
        """Devuelve la forma normal de una persona."""
        return f"Persona('{self.__nombre}', {self.__edad})"

    def nombre(self):
        """Devuelve el nombre de una persona."""
        return self.__nombre

    def edad(self):
        """Devuelve la edad de una persona."""
        return self.__edad

    def comparar_edad(self, otra):
        """
        Compara su edad con otra persona, e imprime por \
        la salida estándar el resultado.
        """
        if self.__edad > otra.edad():
            print (f'{otra.nombre()} es más viejo que yo')
        elif self.__edad == otra.edad():
            print (f'{otra.nombre()} tiene la misma edad que yo')
        else: print (f'{otra.nombre()} es más joven que yo')

# if __name__ == '__main__':
p1 = Persona('Paula', 21)
p2 = Persona('Emilio', 34)
p3 = Persona('Paula', 21)

print('\n|          Repaso de los métodos mágicos           |\n')
print('----------<<<El método mágico __init__>>>----------')
print('Vamos a comenzar creando tres instancias de la clase Persona.\n'\
    'Ésto se produce gracias al método init que,como su nombre indica,\n'\
    'inicializa los atributos de una clase que se pretende instanciar.\n'\
    'Por lo tanto, habrá que pasarle tantos parámetros como precise.\n'\
    '\n'
    'Ejemplo de signaruta de un método init:\n'\
        '     >>> def __init__(self, nombre, edad)\n'\
    '\n'
    'En este caso, requerimos de los parámetros "nombre" y "edad".\n'\
    'Al método init ambién se le denomina "constructor de la clase".\n'\
        f'     >>> p1 = {p1}\n     >>> p2 = {p2}\n     >>> p3 = {p3}')
print()

print('----------<<<El método mágico __eq__>>>----------')
print('Hemos definido un metodo eq que reconoce que dos personas\n'\
    'son lo mismo, si su nombre y edad son iguales. Por eso:\n')
print(f'     >>> p1 is p3\n     {p1 is p3}')
print(f'     >>> p1 == p3           | En realidad sucede -> '\
    'Persona.__eq__(p1, p2)\n     {p1 == p3}')
print()

print('----------<<<El método mágico __hash__>>>----------')
print('Definimos un método hash que es elquivalente al hash de una \n'\
    'lista que contiene el nombre y la edad de la instancia:\n')
print(f'     >>> hash(p1)\n     {hash(p1)}   | Equivale a -> '\
    'hash((p1.__nombre, p1.__edad))')
print(f'     >>> hash(p3)\n     {hash(p3)}')
print(f'     >>>hash(p1) == hash(p3)\n     {hash(p1) == hash(p3)}')
print()

print('----------<<<El método mágico __repr__>>>----------')
print('Este método define la forma normal de una instancia de clase, \n'
    'devolviendo una expresión que contiene el estado interno de \n'\
    'dicha instancia. De este modo, podriamos reconstruir dicho objeto.\n')

print('  - Sin método repr definido:')
print(f'     >>> p1\n     __main__.Persona object at 0x00000257876D1CD0\n')
print('  - Con método repr definido:')
print(f'     >>> p1\n     {p1}')
print('\nRecuerda que el método se define en la clase, no en la instancia:\n')
print(f'     >>> Persona.__repr__(p1)\n     {Persona.__repr__(p1)}')
input('Pulse cualquier tecla para finalizar...')
