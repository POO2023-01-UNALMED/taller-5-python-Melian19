from gestion.zona import Zona

class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__zonas = []

    #metodos get y set

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, name):
        self.__nombre = name

    def getUbicacion(self):
        return self.__ubicacion
    
    def setUbicacion(self, lugar):
        self.__ubicacion = lugar
    
    def getZona(self):
        return self.__zonas
    
    def setZona(self, zone):
        self.__zonas = zone

    #metodos

    def cantidadTotalAnimales(self):
        cantidadAnimales = 0
        for zona in self.__zonas:
            if isinstance(zona, Zona):
                cantidadAnimales += zona.cantidadAnimales()
        return cantidadAnimales
    
    def agregarZonas(self, zona):
        self.__zonas.append(zona)