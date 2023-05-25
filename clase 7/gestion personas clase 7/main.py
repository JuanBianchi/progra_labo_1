import os
from menu import *
from data_personas import *

personas = []       # Esta lista esta vacia porque la idea es ir cargandola cuando querramos desde el menu. Luego sera usada en una funcion para cargar la lista.

while True: 
    os.system("cls") 
    match(menu_personas()):                 # El match recibe un valor que tiene que coincidir con algun case, entonces puedo poner entre parentesis la llamada a la funcion de menu_personas(), que me muestra el menu y me devuelve en string la opcion seleccionada por el usuario y que coincide con el case del match
        case "1":
            cargar_lista(personas, lista)
        case "2":
            listar_personas(personas)
        case "3":
            print("--------.")
        case "4":
            confirma = input("Confima salida? s/n")     # Esto lo hago por si el usuario se llega a equivocar en la opcion o se arrepiente de salir.
            if confirma == "s":
                break 


    os.system("pause") 

# Despues lo que se suele hacer es que en cada case es encapsular la logica en funciones, para que no sea tan engorroso el codigo
# y sea lo mas legible posible