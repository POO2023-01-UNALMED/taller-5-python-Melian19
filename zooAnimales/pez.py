from zooAnimales.animal import Animal

class Pez(Animal):
    __listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self,nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorEscamas = colorEscamas
        self.__cantidadAletas = cantidadAletas

    #metodos set y get

    @classmethod
    def getListado(cls):
        return cls.__listado
    
    @classmethod
    def setListado(cls, lista):
        cls.__listado = lista

    def getColorEscamas(self):
        return self.__colorEscamas
    
    def setColorEscamas(self, color):
        self.__colorEscamas = color
    
    def getCantidadAletas(self):
        return self.__cantidadAletas
    
    def setCantidadAletas(self, numero):
        self.__cantidadAletas = numero

    #metodos

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearSalmon(cls, name, age, gen):
        cls.salmones += 1
        return Pez(name, age, "oceano", gen, "rojo", 6)
    
    @classmethod
    def crearBacalao(cls, name, age, gen):
        cls.bacalaos += 1
        return Pez(name, age, "oceano", gen, "gris", 6)