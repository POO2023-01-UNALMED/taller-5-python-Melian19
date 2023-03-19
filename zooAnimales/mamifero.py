from zooAnimales.animal import Animal

class Mamifero(Animal):
    __listado = []
    caballos = 0
    leones = 0

    def __init__(self,nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.__pelaje = pelaje
        self.__patas = patas

    #metodos get y set

    @classmethod
    def getListado(cls):
        return cls.__listado
    
    @classmethod
    def setListado(cls, lista):
        cls.__listado = lista
    
    def isPelaje(self):
        return self.__pelaje
    
    def setPelaje(self, pelo):
        self.__pelaje = pelo
    
    def getPatas(self):
        return self.__patas
    
    def setPatas(self, numero):
        self.__patas = numero

    #metodos

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearCaballo(cls, name, age, gen):
        cls.caballos += 1
        return Mamifero(name, age, "pradera", gen, True, 4)
    
    @classmethod
    def crearLeon(cls, name, age, gen):
        cls.leones += 1
        return Mamifero(name, age, "selva", gen, True, 4)