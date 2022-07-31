#importacion de archivos construidos
import vista as vis
import naves as nav

#ciclo fundamental para la ejecución del programa
salir = False


while salir != True:
    menu = vis.menu()
    opcion = int(input("Ingrese una opcion: ")) 
    if opcion == 0: 
        salir == True
        print("Vuelva pronto.")
        break
    if opcion == 1:     
        vis.mencreacionNaves()
        
    if opcion == 2: 
        vis.listaNaves()


