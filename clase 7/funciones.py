# normalmente los nombres de las funciones son un verbo en infinitivo, ya que las funciones realizan una tarea.
# Y si bien vamos a documentar nuestras funciones, hay que darle un nombre acorde a la funcion que va a realizar.

# F1  funciones que no reciben nada y no devuelven nada 
# F2  funciones que no no reciben nada y retorna algo
# F3  recibe algo y no devuelve nada. Ej, la funcion print.
# F4  recibe algo y retorna algo

# Estas 4 combinaciones son las 4 posibles formas de funciones.
# Todo va a depender de la tarea que realice la funcion
#

def sumar_f1 ():
    num_1 = int(input("Ingrese un numero."))
    num_2 = int(input("Ingrese otro numero."))
    rta = num_1 + num_2
    print("La suma es " + str(rta))

def sumar_f2 ():
    num_1 = int(input("Ingrese un numero."))
    num_2 = int(input("Ingrese otro numero."))
    rta = num_1 + num_2
    
    return rta

def sumar_f3 (num_1, num_2):  #num_1 y num_2 son los parametros formales. Ya que reciben valores.
    rta = num_1 + num_2     #rta es un parametro local de la funcion.
    print("La suma es " + str(rta))

def sumar (num_1: int, num_2: int) -> int: 
    """suma dos enteros y retorna el resultado
    
    Args:
        a (int): primer numero a sumar
        b (int): segundo numero a sumar
    
    Returns:
        int: suma de los parametros ingresados
    
    """
    rta = num_1 + num_2     
    return rta

# Si yo me fijo, en la funcion, arriba de las "instrucciones", estan las notations.
# Esas notations es lo que vemos al principio que decia Any any any, que seria el tipo de dato que recibe y devuelve la funcion.
# Para arreglar eso, al lado de los parametros formales ponemos dos puntos y el tipo de dato que deberian recibir, y afuera del parentesis
# ponemos una flecha y ponemos el tipo de dato que deberia retornar la funcion
