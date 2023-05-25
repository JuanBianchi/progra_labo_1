# Si quiero consumir ese archivo modular funciones.py
# el archivo funciones.py es un modulo.

# from funciones import sumar_f1, sumar_f2, sumar_f3, sumar_f4
from funciones import *
#1 import modulos.saludos      #
from modulos.saludos import decir_hola
import sys

print(sys.path)  # Esto me muestra donde esta el directorio del modulo que importe (sys).


#sumar_f1()  
# #Llamada o invocacion a la funcion


# if(sumar_f2() > 10):
#     print("Es mayor a 10")
# else:
#     print("Es menor a 10")  

# Si yo invoco a la funcion asi y no hago nada, no
# pasa nada, hace la operacion y el dato del return
# queda en algun lado.
# Lo que puedo hacer es guardarla en una variable
# o customizarla con un if.
# y despues hago lo que quiero

x = 34

# sumar_f3(x, 56)
# En esta ejecucion, lo que le paso en la llamada a la funcion se le llama parametros actuales.

#print(sumar_f4(x, int(input("Ingrese un numero: "))))


#1 modulos.saludos.decir_hola()    # Asi llamo a la funcion. Es seguir el directorio de donde esta guardado
decir_hola()


cadena = "Hola"

# En python las variables guardan direcciones de memoria de objetos.
# Entonces, si a una variable que guarda cualquier tipo (en este caso string) le pongo un punto
# al lado, se muestra un "Menu" con distintos metodos orientados a objetos.

cadena.capitalize()

# Pero no las llamamos funciones. Mas bien, son metodos
# Todo lo que vimos de funciones aplica tambien a objetos
# Por ejemplo, append seria el metodo del objeto lista



#----------------------------------------------------

def duplicar(x):
    # print(f"2- Al comienzo de mi_funcion x vale {x}")
    print("Direccion x = " + str(id(x)))
    x = x * 2
    print("Direccion x = " + str(id(x)))
    print(f"3- Al comienzo de mi_funcion x vale {x}")



numero = 20

# print(f"1- Al comienzo del programa numero vale {numero}")
print("Direccion de numero = " + str(id(numero)))

duplicar(numero)

print(f"4- Al final de mi_funcion valor vale {numero}")

# La direccion de memoria es la misma, ya que en python, todas las variables guardan direccion de memoria
# Entonces, al pasarle la variable "numero" a la funcion duplicar, en realidad le estoy pasando la direccion de memoria 
# de donde estaria guardado el valor. Por eso son las mismas.

# PERO, al entrar a la funcion y pasarle la direccion de memoria del valor 20,
# al hacerse la operacion de duplicar y dar 40, ese 40 se guarda en otra direccion de memoria, ya que el 20 original no puede modificarse ni destruirse
# ya que tambien ese valor existe fuera de la funcion.
# 
# Una vez que se termina la funcion, ese valor de x, que valdria 40, se destruye. 

# Lo que hay que entender es que si a una funcion le pasamos un tipo de dato INMUTABLE, la funcion no lo puede modificar.


# Si yo quisiera guardar el valor 40 de la funcion, primero la funcion me tendria que retornar ese valor.
# Y luego la tendria que O guardar en una nueva variable O sobreescribirla en la misma variable con la que le pasaste el parametro a la funcion (en este caso, numero).


# Si la variable fuera MUTABLE, la funcion puede modificar la variable.
# Por ejemplo.

def agregar_cien(lista):
    lista.append("100")

l = [23, 4, 5, 67]

print(l)

agregar_cien(1)

print(l)

# La lista "l" si es mutable, entonces, la funcion al agregarle el 100 a la lista, nos la modifica.
# l guarda la direccion de memoria de la lista. Y cuando nosotros le pasamos "l" a la funcion, le pasamos la misma direccion de memoria de "l".
# Y como las listas son objetos mutables, y se le agrega el "100", al terminar la funcion, esa variable l va a ser modificada.