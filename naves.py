from abc import ABCMeta, abstractmethod
import random
#Controlador

#--------------------------------------------------
class Nave (metaclass=ABCMeta):

    def comunicacionTierra(self):
        print("Comunicando con control en tierra.")
    
    def calcularVelocidad(self):
        x = random.randint(1,1000)
        t = random.randint(1,100)
        print("Distancia recorrida: ",x,"m")
        print("Tiempo transcurrido: ",t,"s")
        print("Velocidad media: ", (x/t), "m/s")
        print("Velocidad instantanea: f'(x(t))" )

    def calcularPosicion(self):
        x = random.randint(1,1000)
        print("La posicion de la nave es: ", x)

    @abstractmethod #Metodos abstracto
    def despegar(self):
        pass
        
    @abstractmethod #Metodo abstracto
    def tipoCombustible(self):
        pass

    @abstractmethod #Metodo abstracto
    def envioDatos(self):
        pass

class Navelanzadera(Nave):
    #tipoCarga es un parametro que indica si la nave lleva una nave no tripulada o tripulada
    def __init__(self, nombreNave, pesoNave, tipoCarga, combustible):
        self.__nombreNave = nombreNave
        self.__pesoNave = pesoNave
        self.__tipoCarga = tipoCarga
        self.__combustible = combustible

    #Metodos accesores
    def getNombre(self):
        return self.__nombreNave
        
    def getPeso(self):
        return self.__pesoNave

    def getCarga(self):
        return self.__tipoCarga
    
    def getCombustible(self):
        return self.__combustible

    def despegar(self):
        i=3
        print("Conteo regresivo para el despegue")
        while i >= 0:
            print("T-",i)
            i-=1
        print("Despegue exitoso!.")

    def tipoCombustible(self):
        list=["combustible quimico solido",
        "propelente liquido", "combustible quimico solido y propelente liquido"]
        print(random.choice(list))

    def envioDatos(self):
        print("Envio de informacion de la mision, estado de desacople de la carga y estado de propulsores.")    


class Navenotripulada(Nave):
    #El parametro tipoNave hace referencia al tipo de satelite (comunicaciones, metereologico, etc)
    def __init__(self, nombreNave, pesoNave, tipoNave, combustible):
        self.__nombreNave = nombreNave
        self.__pesoNave = pesoNave
        self.__tipoNave = tipoNave
        self.__combustible = combustible

    #Metodos accesores
    def getNombre(self):
        return self.__nombreNave
        
    def getPeso(self):
        return self.__pesoNave

    def gettipoNave(self):
        return self.__tipoNave
    
    def getCombustible(self):
        return self.__combustible

    def despegar(self):
        print("El despegue lo controla la nave lanzadera que lo transporta.")

    def tipoCombustible(self):
        list=["Orbita geoestacionaria", "Celdas fotovoltaicas", "Combustibles no fosiles"]
        print(random.choice(list))

    def envioDatos(self):
        print("Envio de datos recopilados segun el objetivo de la nave.")
        
        
class Navetripulada(Nave):
    def __init__(self, nombreNave, pesoNave, numeroIntegrantes, combustible):
        self.__nombreNave = nombreNave
        self.__pesoNave = pesoNave
        self.__numeroIntegrantes = numeroIntegrantes
        self.__combustible = combustible

    #Metodos accesores
    def getNombre(self):
        return self.__nombreNave
        
    def getPeso(self):
        return self.__pesoNave

    def getIntegrantes(self):
        return self.__numeroIntegrantes
    
    def getCombustible(self):
        return self.__combustible

    def despegar(self):
        print("El despegue lo controla la nave lanzadera que lo transporta.")

    def tipoCombustible(self):
        list=["Combustible quimico solido", "Propelente liquido"]
        print(random.choice(list))

    def envioDatos(self):
        print("Envio de informacion de la mision. Estado de los tripulantes.")

