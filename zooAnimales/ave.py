from zooAnimales.animal import Animal

class Ave(Animal):
    __listado = []
    halcones = 0
    aguilas = 0

    def __init__(self,nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPlumas = colorPlumas
        Ave.__listado.append(self)

    #metodos get y set

    @classmethod
    def getListado(cls):
        return cls.__listado
    
    @classmethod
    def setListado(cls, lista):
        cls.__listado = lista

    def getColorPlumas(self):
        return self.__colorPlumas
    
    def setColorPlumas(self, color):
        self.__colorPlumas = color

    #metodos

    @classmethod
    def cantidadAves(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearHalcon(cls, name, age, gen):
        cls.halcones += 1
        return Ave(name, age, "montanas", gen, "cafe glorioso")
    
    @classmethod
    def crearAguila(cls, name, age, gen):
        cls.aguilas += 1
        return Ave(name, age, "montanas", gen, "blanco y amarillo")
    
    def movimiento(self):
        return "volar"
    
    def __str__(self):
        super().__str__()