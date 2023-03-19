from zooAnimales.animal import Animal

class Anfibio(Animal):
    __listado = []
    ranas = 0
    salamandras = 0

    def __init__(self,nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPiel = colorPiel
        self.__venenoso = venenoso

    #metodos get y set

    @classmethod
    def getListado(cls):
        return cls.__listado
    
    @classmethod
    def setListado(cls, lista):
        cls.__listado = lista

    def getColorPiel(self):
        return self.__colorPiel
    
    def SetColorPiel(self, color):
        self.__colorPiel = color
    
    def isVenenoso(self):
        return self.__venenoso
    
    def setVenenoso(self, estado):
        self.__venenoso = estado

    #metodos

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearRana(cls, name, age, gen):
        cls.ranas += 1
        return Anfibio(name, age, "selva", gen, "rojo", True)
    
    @classmethod
    def crearSalamandra(cls, name, age, gen):
        cls.salamandras += 1
        return Anfibio(name, age, "selva", gen, "negro y amarillo", False)