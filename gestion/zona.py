from zooAnimales import animal

class Zona:
    def __init__(self, nombre, zoo = None):
        self.__nombre = nombre
        if zoo == None:
            self.__zoo = None
        else:
            self.__zoo = zoo
        self.__animales = []

    #metodos get y set

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, name):
        self.__nombre = name
    
    def getZoo(self):
        return self.__zoo
    
    def setZoo(self, zoologico):
        self.__zoo = zoologico
    
    def getAnimales(self):
        return self.__animales
    
    def setAnimales(self, animal):
        self.__animales = animal

    #metodos

    def agregarAnimales(self, nuevo):
        self.__animales.append(nuevo)

    def cantidadAnimales(self):
        return len(self.__animales)