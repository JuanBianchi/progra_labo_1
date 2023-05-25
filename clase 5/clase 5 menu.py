# Es conveniente hacer un menu de opciones para que el usuario elija lo que el quiera en lugar de mostarle todas
# las opciones de una.

# La operatoria normalmente es:
# - MOSTRAR MENU
# - PEDIMOS OPCIONES    -----> SALIR DEL MENU (tiene que ser una de las opciones)
# - REALIZAR LAS TAREAS QYE CORRESPONDAN A LA OPCION SELECCIONADA
# - MOSTAR MENU DE NUEVO (para que el usuario elija otra opcion)

# Una manera de resolver esto es:

import os       # Es importante importar el modulo os para 

bandera_saludo = False
bandera_brindis = False

while True: 

    os.system("cls")    # Para limpiar la pantalla de la consola
                       # Pero como pasa muy rapido, no llego a ver la opcion que elegi. Para eso esta la funcion pause, asi como la cls

    print(" *** MENU DE OPCIONES ***")
    print("------------------------------")
    print("1- Saludar")
    print("2- Brindar")
    print("3- Despedir")
    print("4- Salir")
    opcion = input("Seleccione una opcion: ")

    if (opcion == "1"):
        print("Hola.")
        bandera_saludo = True
    elif (opcion == "2"):
        if (bandera_saludo):
            print("Chin chin...")
            bandera_brindis = True
        else:
            print("No podemos brindar si primero no me saludas...")
    elif (opcion == "3"):
        if(bandera_brindis):
            print("Chau.")
            bandera_saludo = False          # Pongo las banderas en false de nuevo para "resetar" el menu.
            bandera_brindis = False
        elif(bandera_saludo):
            print("Antes de despedirnos, primero brindemos.")
        else:
            print("No podemos despedirnos si no nos saludamos primero.")
    elif (opcion == "4"):
        confirma = input("Confima salida? s/n")     # Esto lo hago por si el usuario se llega a equivocar en la opcion o se arrepiente de salir.
        if confirma == "s":
            break 

    os.system("pause")


    # TAREA para viernes 15/04:

    # Refactorizar con match los elif.

    # Hacer un programa con menu que cumpla estas opciones:
    #-----------------------------------------
    # Opcion 1 sea cargar lista con 5 numeros 
    # Opcion 2 mostrar el total de los numeros ingresados
    # Opcion 3 mostrar el mayor numero
    # Opcion 4 mostrar el menor numero
    # Opcion 5 pedir un numero y decir si esta en la lista
    # Opcion 6 pedir numeros e informar todos los indices donde aparece 
    # Opcion 7 vaciar la lista (una vez que vacie la lista, tengo que resetear todo. O sea, empezar desde la opcion 1.)
                # No puedo acceder a la opcion a todas las demas opciones si no pase por la opcion 1 primero.
