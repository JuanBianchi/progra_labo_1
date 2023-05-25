import os 

def menu_personas() -> str:
    """ muestra menu de opciones para personas
    
    
    Returns:
        str: opcion seleccionada
    """
    print("----------------------------")
    print("| *** Gestion Personas *** |")
    print("----------------------------\n")
    print("1- Cargar Lista.")
    print("2- Mostrar Lista")
    print("3- en construccion")
    print("4- Salir")
    opcion = input("Elija una opcion: ")
    return opcion


def cargar_lista(lista_destino: list, datos: list)-> None:      # Por ahora vamos a poner que devuelve None. Despues cuando validemos, ahi ponemos que la funcion devuelve algo
    for dato in datos:
        lista_destino.append(dato)

# Esta funcion lo que va a hacer es cargar la lista de personas de main. 
# Lo que va a recibir por parametro es la lista a cargar (la destino) y la lista con datos (origen) que contiene toda la informacion.
# Por ahora lo vamos a hacer asi, despues vamos a cargar la lista desde un archivo.

# Entonces, por ahora, para pasarle los datos de la lista de origen a la lista destino, recorro la lista origen con un for in
# Y con un append le voy agregando diccionario por diccionario mientras va iterando a la lista destino.

# Y como habiamos visto, si a una funcion le paso un objeto mutable, la funcion puede modificar ese objeto sin que tenga que retornar nada y sin pisar la lista original.


def mostrar_ordenar_persona(persona: dict) -> None:
    print(f"{persona['id']:3d} {persona['nombre'] + ' ' + persona['apellido']:<40} {persona['email']:<45}    {persona['genero']:<10}          {persona['edad']:2d}")

# Como explicamos en la funcion listar_personas (abajo), esta funcion recibe el diccionario dentro de la lista personas, por eso la notation tiene que ser de tipo diccionario.
# Luego, solo queda imprimir y ordenar la informacion dentro del diccionario usando los corchetes con la key donde esta contenido el value.


def listar_personas(lista_personas: list) -> None:
    print("                          *** Lista de Personas ***")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print(" Id  Nombre y apellido                       Email                                       Genero                      Edad  ")
    print("----------------------------------------------------------------------------------------------------------------------------------")
    for persona in lista_personas:
        mostrar_ordenar_persona(persona)

# Esta funcion recibe la lista de personas ya cargada. Entonces lo que hace es mostrar todo el menu armado, pero en vez de iterar
# la lista de diccionarios (que cada diccionario contiene la informacion de una persona) lo que quiero hacer es dentro de la funcion listar_persona
# llamar a otra funcion que me muestre y ordene la persona. 
# Esa funcion llamada mostrar_ordenar_persona la voy a iterar con un for in en la lista cargada de personas, por lo tanto va a mostrar persona por persona

# Lo que hace el for in es iterar en la lista ya cargada (o no) de personas e ir diccionario por diccionario. Solo que en vez de imprimir la informacion de la persona ahi,
# hago e invoco otra funcion y le tiro el diccionario de persona a la funcion mostrar_ordenar_persona

