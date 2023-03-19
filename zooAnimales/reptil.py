from zooAnimales.animal import Animal

class Reptil(Animal):
    __listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self,nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorEscamas = colorEscamas
        self.__largoCola = largoCola

    #metodos get y set

    @classmethod
    def getListado(cls):
        return cls.__listado
    
    @classmethod
    def setListado(cls, lista):
        cls.__listado = lista

    def getColorEscamas(self):
        return self.__colorEscamas
    
    def setColorEscamas(self,color):
        self.__colorEscamas = color
    
    def getLargoCola(self):
        return self.__largoCola
    
    def setLargoCola(self, largo):
        self.__largoCola = largo

    #metodos

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearIguana(cls, name, age, gen):
        cls.iguanas += 1
        return Reptil(name, age, "humedal", gen, "verde", 3)
    
    @classmethod
    def crearSerpiente(cls, name, age, gen):
        cls.serpientes += 1
        return Reptil(name, age, "jungla", gen, "blanco", 1)