class Persona:
    """
    Clase Persona
    ---
    La clase persona representa a una persona, la cual se \
    idenfitica por su nombre y su dni. \n

    Atributos:\n
        - nombre: str -> El nombre de la persona.
        - dni: str -> El DNI de la persona.

    Dos personas son iguales si tienen el mismo nombre y dni.
    """
    def __init__(self, nombre, dni):
        """Constructor de la clase Persona."""
        self.__nombre = nombre
        self.__dni = dni

    def __eq__(self, otro):
        """
        Devuelve True si otra persona tienen el \
        mismo nombre y apellido, False en caso contrario y \
        NotImplemented si no comparten el mismo tipo.
        """
        if not isinstance(otro, type(self)):
            return NotImplemented
        return (self.__nombre, self.__dni) == (otro.__nombre, otro.__dni)

    def __hash__(self):
        """Devuelve el hash de una persona."""
        return hash((self.__nombre, self.__dni))

    def __repr__(self):
        """Devuelve la forma normal de una persona."""
        return f"Persona('{self.__nombre}', '{self.__dni}')"

    def __str__(self):
        return f'Se trata de {self.nombre()}, con DNI {self.dni()}.'

    def nombre(self):
        """Devuelve el nombre de una persona."""
        return self.__nombre

    def dni(self):
        """Devuelve el dni de una persona."""
        return self.__dni

    '''
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
    '''

# if __name__ == '__main__':
p1 = Persona('Paula', '11122233A')
p2 = Persona('Emilio', '22233344B')
p3 = Persona('Paula', '11122233A')

print('\n|          Repaso de los métodos mágicos           |\n')
print('----------<<< El método mágico __init__ >>>----------')
print('Vamos a comenzar creando tres instancias de la clase Persona.\n'\
    'Ésto se produce gracias al método init que,como su nombre indica,\n'\
    'inicializa los atributos de instancia de una clase que se pretende \n'\
    'instanciar. Habrá que pasarle tantos parámetros como precise.\n'\
    '\n'
    '  - Ejemplo de signaruta de un método init:\n'\
        '     >>> def __init__(self, nombre, dni)\n'\
    '\n'
    'En este caso, requerimos de los parámetros "nombre" y "dni".\n'\
    'Al método init también se le denomina "constructor de la clase".\n'\
        f'     >>> p1 = {repr(p1)}\n'\
        f'     >>> p2 = {repr(p2)}\n'\
        f'     >>> p3 = {repr(p3)}')
input('Pulse Intro para continuar...')
print()

print('----------<<< El método mágico __eq__ >>>----------')
print('Por defecto, este método viene predefinido, de manera \n'\
    'que devolvera True si dos objetos son idénticos (usando \n'\
    ' el operador "is".\n'\
    '\n'\
    'Nosotros podriamos considerar que dos objetos son iguales \n'\
    'cuando algunos de sus atributos tienen el mismo valor. \n'\
    'Así que hemos definido un método eq que reconoce que dos personas\n'\
    'son la misma, si su nombre y dni son iguales. Por eso:\n')

print(f'     >>> p1 is p3\n     {p1 is p3}')
print(f'     >>> p1 == p3            | En realidad sucede -> '\
    f'Persona.__eq__(p1, p3)\n     {p1 == p3}')
input('Pulse Intro para continuar...')
print()

print('----------<<< El método mágico __hash__ >>>----------')
print('Recuerda que no todos los tipos de datos son hashables. \n'\
    'En el caso de los objetos, a pesar de que éstos son mutables, \n'\
    'algunos de sus atributos a menudo suelen permanecer intactos.\n'\
    'En esta ocasión definimos un método hash que es elquivalente \n'\
    'a calcular el hash de una lista que contiene el nombre y el \n'\
    'dni de la persona:\n')

print(f'     >>> hash(p1)\n     {hash(p1)}    | Equivale a -> '\
    'hash((p1.__nombre, p1.__dni)) [mirar línea 25]')
print(f'     >>> hash(p3)\n     {hash(p3)}')
print(f'     >>> hash(p1) == hash(p3)\n     {hash(p1) == hash(p3)}')
input('Pulse Intro para continuar...')
print()

print('----------<<< El método mágico __repr__ >>>----------')
print('Este método define la forma normal de una instancia de clase, \n'
    'devolviendo una cadena que contiene el estado interno de \n'\
    'dicha instancia. De este modo, podríamos repliclar dicho objeto \n'\
    'a partir de lo que devuelva este método. De hecho siempre debería \n'\
    'cumplirse esta condición, pero no siempre es posible.')

print('  - Sin método repr definido:')
print(f'     >>> p1                     | Equivale a -> Persona.__repr__(p1)'\
    '\n     __main__.Persona object at 0x00000257876D1CD0\n')
print('  - Con método repr definido:')
print(f'     >>> p1\n     {p1.__repr__()}')
input('Pulse Intro para continuar...')
print()

print('Con la funcion "eval" evaluamos exprexiones contenidas en una cadena.\n'\
    'Significa que podemos evaluar la cadena que devuelve el método repr:\n')

print(f'     >>> eval(repr(p1)) == p1\n     {eval(repr(p1)) == p1}')
print(f'     >>> eval(repr(p1)) == p3\n     {eval(repr(p1)) == p3}    | '\
    'Recuerda que p1 y p3 tenian el mismo estado.')

print('\n¡Recuerda que los métodos se definen en la clase, no en los objetos!\n')
input('Pulse Intro para continuar...')
print()

print('----------<<< El método mágico __str__ >>>----------')
print('Recordar que la función str convierte un valor a cadena. \n'\
    'Algunos métodos usan esta función de forma implícita, como print.\n'\
    'El método "objeto.__str__" equivale a hacer str(objeto).\n'\
    'Este método viene predefinido de manera que __str__ == __repr__, \n'\
    'pero no debemos olvidar que la finalidad de str es ser legible, mientras \n'\
    'que repr busca devolver una expresión no ambigüa, la forma normal \n'\
    'de un objeto. Es por eso que vamos a definir str para que nos devuelva una \n'\
    'cadena que describa al objeto.\n')

print(f'     >>> print(p1)\n     {p1}')
print()
input('Pulse Intro para finalizar.')
