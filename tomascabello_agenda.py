agenda = {}
def mostrarmenu():
    print("|-----------------------------------------|")
    print("|   :: AGENDA TOMÁS CABELLO FERNÁNDEZ ::  |")
    print("|-----------------------------------------|")
    print("|                                         |")
    print("|  1. Añadir/modificar                    |")
    print("|  2. Buscar                              |")
    print("|  3. Borrar                              |")
    print("|  4. Listar                              |")
    print("|  5. Salir                               |")
    print("|_________________________________________|")
    print("")
    x = input ("Dime la función a realizar: ")
    opc = int (x)
    return (opc)
#Función añadir o modificar.
#Se pide un nombre y un número.
#Se comprueba si está en la agenda, si es así se le da la opción a modificarlo.
#Sino está en la agenda se le pide un número de teléfono y un nombre para añadir el nuevo contacto a la agenda.
#Este es el código de Chema de la función de añadir modificar# 
def anhadirModificarJcaballero(nombre, agenda):
    if nombre in agenda:
        print("%s es un contacto que ya existe, su número de teléfono es %s" % (nombre,agenda[nombre]))
        selec = input("Pulsa la tecla 's' si quiere modificarlo. Cualquier otra tecla para continuar.")
        if selec == "s":
            telefono = input("Dime el nuevo número de teléfono: ")
            agenda[nombre]=telefono
    else:
        telefono = input("Dime el número de teléfono: ")
        agenda[nombre]=telefono

#Este es el código de la búsqueda de Andrés Serrano Rodríguez, sirve para realizar búsquedas en la agenda a partir de nombres de usuarios.
def buscar_ASerrano(nombre, agenda):
        for cadena,numero in agenda.items():
                if cadena.startswith(nombre):
                        print("El número de teléfono de %s es el %s " % (nombre,agenda[cadena]))   
                        
###Parte de agenda Tomás Cabello Fernández,10/03/2022###
###Función borrar###
###Está función te pide un nombre, si le das un contacto existente,###
###te responde pidiendote el pulsado de la tecla s para confirmar el borrado###
###Si no existe el contacto simplemente el programa responde diciendo que no existe.###
def borrarTcabello(nombre, agenda):
    if nombre in agenda:
        opcion = input("Pulsa 's' si quieres borrarlo. Otra tecla para continuar.")
        if opcion == "s":
            del agenda[nombre]
    else:
        print("No existe el contacto.")

#Este codigo esta hecho por Carlos el dia 08/03/2022
#Esta opción lista todos los nombres y numeros que has añadido a la agenda 
def listar_CValverde(agenda):
    for nombre, numero in agenda.items():
                print("----------------------")
                print("|        Listado      |")  
                print("----------------------")
                print("|",nombre,"->",numero,"|")
                print("----------------------")

###Programa###
seleccion = mostrarmenu()
if (seleccion<0 or seleccion>5):
    print("La opción es incorrecta.")

while (seleccion>0 and seleccion<6):
    if (seleccion==1):
        nombre = input ("Escribe el nombre del contacto:")
        anhadirModificarJcaballero(nombre,agenda)

    elif (seleccion==2):   
        nombre = input ("Elige el contacto a buscar: ")
        buscar_ASerrano(nombre, agenda)

    elif (seleccion==3):
        nombre = input ("Nombre del contacto a borrar: ")
        borrarTcabello(nombre, agenda)

    elif (seleccion==4):
        listar_CValverde (agenda)
    
    elif (seleccion==5):
        print("¡Nos vemos!")
        break

    seleccion = mostrarmenu()


