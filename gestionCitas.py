import os
import core
import calendar
import  random
from datetime import datetime

cal = calendar.TextCalendar()

registroCitas={}
calendario = {"2023":
              {
                  "1":{},"2":{},"3":{},"4":{},"5":{},"6":{},"7":{},"8":{},"9":{},"10":{},"11":{},"12":{}
              }}


def generadorHoras():
        global año
        año = 2023

        for mes in calendario["2023"]:
            numdays=calendar.monthrange(año,int(mes))[1]
            for i in range (1,numdays+1):
                calendario["2023"][mes][str(i)]={"10":"LIBRE","11":"LIBRE","12":"LIBRE"}



   
        core.EditarData("calendario.json",calendario)

def LoadInfoCItas():
    global registroCitas
    global calendario
    if (core.checkFile("citas.json")) and (core.checkFile("calendario.json")):
        registroCitas = core.LoadInfo("citas.json")
        calendario = core.LoadInfo("calendario.json")
    else:
        core.crearInfo("citas.json", registroCitas)
        core.crearInfo("calendario.json", calendario)
        generadorHoras()

def MainMenu():
    isAddDate = True
    opcion = 0

    while (isAddDate):
        print("""Menú de citas
              Las acciones que puede realizar son:

              1. Agregar cita
              2. Buscar cita
              3. Modificar cita
              4. Cancelar cita
              5. Regresar al menú principal""")
        
        opcion = int(input(":)_ "))

        if (opcion==1):
            os.system('clear')
            agendarCita()
        elif (opcion==2):
            os.system('clear')
            buscarCita()
        elif (opcion==3):
            os.system('clear')
            modificarCita()
        elif (opcion==4):
            os.system('clear')
            cancelarCita()
        else:
            print("Opción no válida")
            isAddDate = False
            if (isAddDate):
                MainMenu()            

    
        
        

def agendarCita():
    global mes, dia, hora
    cal = calendar.TextCalendar()
    calendarioACtual = ""

    #Escoger mes
    
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio",
            "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    mesActual=(datetime.now().month)

    print("Escoja el mes en el que desea agendar su cita")
    for i in range (mesActual-1,12):
            print(f'{i+1}. {meses[i]}')

    mes = input(":)_ ")
    
    #"Escoger día"
    os.system('clear')
    print("Seleccione el día: ")
    calendarioACtual = cal.formatmonth(2023, int(mes))
    print(calendarioACtual)

    dia = input(":)_ ")

    
    
    #Mostrar horarios y Validar disponibilidad
    isHoraOk=False
    
    while (isHoraOk==False):
        print("Horarios disponibles, seleccione la hora que desea para su cita: ")
        print(calendario["2023"][mes][str(dia)])
        hora = input(":)_ ")

        if ((calendario["2023"][mes][str(dia)][hora])=="OCUPADO"):
            print("Horario ocupado")
            isHoraOk=False
        else:
            (calendario["2023"][mes][str(dia)][hora])="OCUPADO"
            core.EditarData("calendario.json",calendario)
            isHoraOk=True
            registrarCita()

def liberarCita():
    global mes, dia, hora
    cal = calendar.TextCalendar()
    calendarioACtual = ""

    #Escoger mes
    
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio",
            "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    mesActual=(datetime.now().month)

    print("Escoja el mes de su cita anterior: ")
    for i in range (mesActual-1,12):
            print(f'{i+1}. {meses[i]}')

    mes = input(":)_ ")
    
    #"Escoger día"
    print("Seleccione el día de su cita anterior: ")
    calendarioACtual = cal.formatmonth(2023, int(mes))
    print(calendarioACtual)

    dia = input(":)_ ")

    
    
    #Mostrar horarios y cambiar disponibilidad
    isHoraOk=False
    
    while (isHoraOk==False):
        print("Escriba la hora de la cita anterior")
        hora = input(":)_ ")

        if ((calendario["2023"][mes][str(dia)][hora])=="OCUPADO"):
            (calendario["2023"][mes][str(dia)][hora])="LIBRE"
            print("Horario de cita liberado")
            core.EditarData("calendario.json",calendario)
            break
        else:
            print("EL espacio ya está libre")
            break


def registrarCita():
    id = random.randint(0,100)
    if (id in registroCitas):
        id = random.randint(0,100)
    os.system('clear')
    print("Cita agendada, ingrese los datos de la consulta")
    fecha=str(dia)+str(mes)+"2023"
    nombre = input("Nombre del paciente: ")
    motivo = input("Motivo del la cosulta: ")

    datos = {
        id:{
            "paciente":nombre,
            "motivoConsulta":motivo,
            "fecha":fecha,
            "hora":hora
        }
        
    }
    registroCitas.update(datos)
    core.EditarData("citas.json", registroCitas)

    os.system('clear')
    print("Cita agendada")
    
    print(f"""CITA REGISTRADA CORRECTAMENTE:
          NÚMERO DE CITA: {id} 
          GUARDE SU NÚMERO DE CITA PARA PRÓXIMAS CONSULTAS""")
    
    core.EditarData("citas.json", registroCitas)

def buscarCita():
    registroCitas = core.LoadInfo("citas.json")
    isSearchActive = True
    while (isSearchActive):
        print("Escriba el Número de su cita para buscar: ")
        idCita = input(":)_ ")
        if (idCita in registroCitas):
            print("Se encontró una cita: ")
            print(registroCitas[idCita])
            isSearchActive = False
        else:
            print("Cita no encontrada")


def modificarCita():
    registroCitas = core.LoadInfo("citas.json")
    isModifyActive = True
    while (isModifyActive):
        print("Escriba el Número de su cita para buscar: ")
        idCita = input(":)_ ")
        if (idCita in registroCitas):
            os.system('clear')
            print("Se encontró una cita: ")
            print(registroCitas[idCita])

            #Liberar espacio de cita anterior
            liberarCita()
            registroCitas.pop(idCita)
            core.EditarData("citas.json",registroCitas)


            #Programar nueva cita
            print("Programe su nueva cita: ")
            agendarCita()
            isModifyActive = False
            

            
        else:
            print("Cita no encontrada")
            isModifyActive = False

def cancelarCita():
    registroCitas = core.LoadInfo("citas.json")
    isCancelActive = True
    while (isCancelActive):
        print("Escriba el Número de su cita para cancelar: ")
        idCita = input(":)_ ")
        if (idCita in registroCitas):
            os.system('clear')
            print("Se encontró una cita: ")
            print(registroCitas[idCita])

            decision=input("Está seguro que desea cancelar la cita: S para Sí o N para No ::: ").upper()

            if (decision == "S"):
                #Liberar espacio de cita anterior
                liberarCita()

                #Eliminar registro de la cita
                registroCitas.pop(idCita)
                core.EditarData("citas.json",registroCitas)
                print("Cita cancelada")
                isCancelActive = False


            elif (decision=="N"):
                isCancelActive = False
            
            else:
                print("Opción no válida")
            
        else:
            print("Cita no encontrada")
            isCancelActive = False
 
    