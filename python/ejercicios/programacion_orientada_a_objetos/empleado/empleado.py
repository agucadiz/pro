import unicodedata
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

        """https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-\
        accents-normalize-in-a-python-unicode-string"""
        def remove_accents(input_str):
            nfkd_form = unicodedata.normalize('NFKD', input_str)
            return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

        apellidos = []
        for i in self.apellidos().split():
            apellidos.append(i.lower())
        direccion = f'{self.nombre().lower()}.{".".join(apellidos)}@company.com'
        return f'{remove_accents(direccion.lower())}'

if __name__ == '__main__':
    emp1 = Empleado('Juan', 'Pérez')
    emp2 = Empleado('María', 'García')
    emp3 = Empleado('Antonio', 'González')
    print(emp1.nombre_completo())
    print(emp2.email())
    print(emp3.nombre())
    emp4 = Empleado.desde_cadena('Celia-Atienza Román-5500')
    print(emp4.nombre_completo())
    print(emp4.email())
    print(emp4.salario())
