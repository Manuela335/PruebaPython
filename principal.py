import os
import gestionCitas

if __name__ == "__main__":
    isActive = True
    opcion = 0
    while (isActive):
        print("""----Bienvenido al módulo de gestión de citas----
              
              Las opciones que puede realizar son:

              1. Gestionar citas
              2. Salir
              
              """)
        
        opcion = int(input(":)_ "))

        if (opcion == 1):
            gestionCitas.LoadInfoCItas()
            gestionCitas.MainMenu()
        elif (opcion == 2):
            print("Adios")
            isActive = False
        else:
            pass

