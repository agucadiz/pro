class Empleado:

    def __init__(self, nombre, apellidos, salario = 0):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__salario = salario

    @staticmethod
    def desde_cadena(cadena):
        nombre, apellidos, salario =cadena.split(sep='-')
        return Empleado(nombre, apellidos, salario)

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def salario(self):
        return self.__salario

    def nombre_completo(self):
        apellidos = []
        for i in self.apellidos().split():
            apellidos.append(i.capitalize())
        return f'{self.nombre()} {" ".join(apellidos)}'

    def email(self):
        apellidos = []
        for i in self.apellidos().split():
            apellidos.append(i.lower())
        direccion = f'{self.nombre().lower()}.{".".join(apellidos)}@company.com'
        return f'{direccion.lower()}'

if __name__ == '__main__':
    emp1 = Empleado('Juan', 'Pérez')
    emp2 = Empleado('María', 'García')
    emp3 = Empleado('Antonio', 'González')
    emp1.nombre_completo()
    emp2.email()
    emp3.nombre()
    emp4 = Empleado.desde_cadena('Celia-Atienza Román-55000')
    emp4.nombre_completo
    emp4.salario()
