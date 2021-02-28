class Cliente:
    """
    Clase Cliente
    ---
    La clase Cliente representa y almacena los clientes de una tienda, compuestos por su DNI, nombre y apellidos.
    """
    __clientes = {}   # Patrón Active record

    def __init__(self, dni, nombre, apellidos):
        """Constructor de la clase Cliente"""
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        Cliente.__clientes[dni] = self

    def __repr__(self):
        return f'Cliente: {self.__nombre} {self.__apellidos}, DNI: {self.__dni}'

    @staticmethod
    def get_cliente(dni):
        """
        Devuelve un cliente existente en el registro a partir de su DNI.

        Parámetros:
        dni: str -> el DNI del cliente a buscar
        """
        return Cliente.__clientes.get(dni)

    def dni(self):
        """Devuelve el DNI del cliente."""
        return self.__dni

    def nombre(self):
        """Devuelve el nombre del cliente."""
        return self.__nombre

    def apellidos(self):
        """Devuelve los apellidos del cliente."""
        return self.__apellidos


"""class Alumno(Cliente):
    def __init__(self, dni, nombre, apellidos, curso):
        super().__init__(dni, nombre, apellidos)
        self.__curso = curso

    def descripcion(self):
        return super().descripcion() + f' y estoy cursando {self.__curso}'

lucia = Alumno ('98765432T', 'Lucía', 'Terraria', 'Prevencion de riesgos laborales')"""
