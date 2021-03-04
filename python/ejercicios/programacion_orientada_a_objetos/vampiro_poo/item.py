from coleccion import Coleccion
import vocabulario as voc

class Item:
    __items = {}

    def __init__(self, corta: str, larga: str, nombre: voc.Nombre):
        self.__corta = corta
        self.__larga = larga
        self.__nombre = nombre
        Item.__items[nombre] = self

    def corta(self):
        return self.__corta

    def larga(self):
        return self.__larga

    def nombre(self):
        return self.__nombre

    @staticmethod
    def get_item(token):
        return Item.__items.get(token)

class Contenedor(Item):
    def __init__(self, corta, larga, nombre):
        super().__init__(corta, larga, nombre)
        self.__contenido = Coleccion()

    def meter_item(self, item):
        self.__contenido.set_elemento(item.nombre(), item)

    def sacar_item(self, nombre):
        self.__contenido.del_elemento(nombre)

cuchillo = Item('un cuchillo', 'Tiene la hoja muy afilada.', voc.CUCHILLO)
crucifijo = Item('un crucifijo', 'Es muy brillante', voc.CRUCIFIJO)
