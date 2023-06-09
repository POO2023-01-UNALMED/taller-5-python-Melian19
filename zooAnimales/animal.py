import zooAnimales

class Animal:
    __totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__genero = genero
        Animal.__totalAnimales += 1
        self.__zona = None

    #metodos get 

    @classmethod
    def getTotalAnimales(cls):
        return Animal.__totalAnimales
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getHabitat(self):
        return self.__habitat
    
    def getGenero(self):
        return self.__genero
    
    def getZona(self):
        return self.__zona
    
    #metodos set

    @classmethod
    def setTotalAnimales(cls, total):
        Animal.__totalAnimales = total

    def setNombre(self, name):
        self.__nombre = name

    def setEdad(self,age):
        self.__edad = age
    
    def setHabitat(self, lugar):
        self.__habitat = lugar

    def setGenero(self, gen):
        self.__genero = gen

    def setZona(self, zone):
        self.__zona = zone

    #metodos

    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\nAves : " + str(zooAnimales.ave.Ave.cantidadAves()) + "\nReptiles : " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces : " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\nAnfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
    
    def __str__(self):
        if (self.__zona == None):
            return "Mi nombre es " + self.__nombre + ", tengo una edad de " + self.__edad + ", habito en " + self.__habitat + " y mi genero es " + self.__genero
        else:
            return "Mi nombre es " + self.__nombre + ", tengo una edad de " + self.__edad + ", habito en " + self.__habitat + " y mi genero es " + self.__genero + ", la zona en la que me ubico es " + self.__zona.getNombre() + ", en el " + self.__zona.getZoo().getNombre()
        
    def toString(self):
        if (self.__zona == None):
            return "Mi nombre es " + str(self.__nombre) + ", tengo una edad de " + str(self.__edad) + ", habito en " + str(self.__habitat) + " y mi genero es " + str(self.__genero)
        else:
            return "Mi nombre es " + str(self.__nombre) + ", tengo una edad de " + str(self.__edad) + ", habito en " + str(self.__habitat) + " y mi genero es " + str(self.__genero) + ", la zona en la que me ubico es " + str(self.__zona.getNombre()) + ", en el " + str(self.__zona.getZoo().getNombre())
        
    def movimiento(self):
        return "desplazaese"