from os import system
system("cls")

concierto=[
        "1","2","3","4","5","6","7","8","9","10",
        "11","12","13","14","15","16","17","18","19","20",
        "21","22","23","24","25","26","27","28","29","30",
        "31","32","33","34","35","36","37","38","39","40",
        "41","42","43","44","45","46","47","48","49","50",
        "51","52","53","54","55","56","57","58","59","60",
        "61","62","63","64","65","66","67","68","69","70",
        "71","72","73","74","75","76","77","78","79","80",
        "81","82","83","84","85","86","87","88","89","90",
        "91","92","93","94","95","96","97","98","99","100"]
personas=[None]*100
recaudacion=[]
asistentes=[]

Pl=120000
Go=80000
Si=50000

def mostrar_con():
    for i in concierto:
        print(" |", end="")
        print(i, end="|")

def limpiar():
    system ("cls")

def pausa():
    input("Presione una tecla paracontinuar")
    limpiar()


def run_personas(run):
    limpiar()
    runn=run.replace(".","").replace("-","")
    personas.append(runn)
    comprar(runn)
    


def comprar(runn):
    mostrar_con()
    op=input("""
    Desea realizar la compra?
    [1]Si
    [2]No
    """)
    match op:
        case "2":
            print("Saliendo..")
            pausa()
            return
        case "1":
            limpiar()
            mostrar_con()
            print()
            asi=input("Introduzca un asiento")
            

            if asi in concierto and len(asi)==1 or 2 or 3 and concierto[int(asi)-1]!="X":
                concierto[(int(asi)-1)]="X"
                run_personas(runn)
                personas[(int(asi)-1)]=runn
                #se me hizo mas facil asi :c
                if asi in range(1,21):
                    recaudacion.append(Pl)
                    print("El costo es de 120000")
                    pausa()
                    return
                if asi in range(22,51):
                    recaudacion.append(Go)
                    print("gold")
                    pausa()
                    return
                if asi in range (52,100):
                    recaudacion.append(Si)
                    print("Silver")
                    pausa()
                    return
                
                
                    
                        
            else:
                print("Numero no valido o asiento ocupado")
                return
def menu():
    print("""
    Bienvenido a Creativos.cl, ¿Que desea realizar?
    **********************************************
    [1]Comprar Entradas
    [2]Mostrar ubicaciones disponibles
    [3]Ver listado
    [4]Mostrar Ganancias Totales
    [5]Salir
    **********************************************
    """)

def Listado_asis():
    for i in concierto:
        if personas[i]!=None:
            print(f"RUN:{[i]} Asiento:{i+1}")

while True:
    menu()
    op=input("Ingrese una opcion en pantalla:")
    match op:
        case "1":
            
            run=input("Ingrese su run sin punto ni guion:")
            run_personas(run)
            pass
        case "2":
            mostrar_con()
            print()
            pausa()
            pass
        case "3":
            Listado_asis()
            pausa()
            pass
        case "4":
            pass
        case "5":
            print("Fin del sistema..")
            break
        case other:
            print("Opcion no valiad, seleccione una en pantalla")
            