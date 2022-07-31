import naves as nav
#vista
navesLanzaderas = []
navesNotripuladas = []
navesTripuladas = []

def menu():
    print("\t\t MENU PRINCIPAL\t\t")
    print("1 -> Creacion de naves.")
    print("2 -> Listado de naves.")
    print("3 -> Inventario de naves.") # sin implementar
    print("0 -> Salir")



def mencreacionNaves():
    print("\t\t CREACION DE NAVES\t\t")
    nombreNave = input("Ingrese el nombre de la nave: ")
    pesoNave = input("Ingrese el peso de la nave: ")
    combustible = input("Ingrese el tipo de combustible de la nave: ")
    print("1. Nave tipo lanzadera.")
    print("2. Nave no tripulada.")
    print("3. Nave tripulada.")
    tipoNave = int(input("Seleccione el tipo de nave: "))
    if tipoNave == 1:
        print("Seleccione el tipo de carga que llevará la nave: ")
        print("1. Nave no tripulada.")
        print("2. Nave tripulada.")
        print("3. Deshecho de elementos.")
        tipoCarga = int(input("Opción: "))
        lanzadera = nav.Navelanzadera(nombreNave, pesoNave, tipoCarga, combustible)
        navesLanzaderas.append(lanzadera)
        
    if tipoNave == 2: 
        print("Seleccione el tipo de nave no tripulada: ")
        print("1. Satelite de comunicaciones.")
        print("2. Satelite de investigacion cientifica.")
        print("3. Satelite metereológico.")
        print("4. Otros.")
        tipoSatelite = input("Opción:  ")
        noTripulada = nav.Navenotripulada(nombreNave, pesoNave, tipoSatelite, combustible)
        navesNotripuladas.append(noTripulada)

    if tipoNave == 3: 
        integrantes = input("Ingrese el numero de integrantes de la nave: ")
        tripulada = nav.Navetripulada(nombreNave, pesoNave, integrantes, combustible)
        navesTripuladas.append(tripulada)

def listaNaves ():
    for nave in navesLanzaderas:
        print("\t\tNave tipo lanzadera.")
        print(nave.getNombre(), nave.getPeso(), nave.getCarga(), nave.getCombustible())

    for nave in navesNotripuladas:
        print("\t\tNave no tripulada.")
        print(nave.getNombre(), nave.getPeso(), nave.gettipoNave(), nave.tipoCombustible())

    for nave in navesTripuladas:
        print("\t\tNave tripulada.")        
        print(nave.getNombre(), nave.getPeso(), nave.getIntegrantes(), nave.getCombustible())



    




    
