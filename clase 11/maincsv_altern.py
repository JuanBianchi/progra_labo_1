import os
import re
import json

#def crear_csv(lista, nombre_archivo): HACER FUNCION

def normalizar_datos(lista: list) :
    """_summary_
        convierte datos de tipo string al tipo de dato correspondiente.
    Args:
        lista (list): lista de diccionarios con datos a ser normalizados
    """
    bandera_cambios = False
    if len(lista) > 0:
        for dict in lista:
            for clave in dict:
                valor = dict[clave]
                if type(valor) == str:
                    try:
                        if re.search(r"\d+\.", valor):
                            dict[clave] = float(valor)
                            bandera_cambios = True
                        else:
                            dict[clave] = int(valor)
                            bandera_cambios = True
                    except ValueError:
                        pass
                # if re.search(r"\d+\.", valor):
                #     dict[clave] = float(valor)
                # elif re.search(r"\d{1,}", valor):
                #     dict[clave] = int(valor)
                # else:
                #     pass
        if bandera_cambios:        
            os.system("cls")
            print("Datos normalizados.")
            os.system("pause")
    else:
        print("Error, la lista esta vacía.")
        os.system("pause")


def generar_diccionario(valores: list, claves: list)->dict and list:
    """_summary_

    Args:
        valores (list): _description_
        claves (list): _description_

    Returns:
        dict and list: _description_
    """

    print(valores)
    diccionario = {}

    for tamaño in valores:
        campos = len(tamaño)

    if len(claves) == 0:
        for campo in range(campos):
            clave = input(f"Ingrese el nombre de la clave para el campo {campo + 1}: ")
            claves.append(clave)
    
    for persona in valores:
        for indice in range(campos):
            clave = claves[indice]
            valor = persona[indice]
            diccionario[clave] = valor

    return diccionario, claves


def parser_csv(nombre_archivo: str)-> list:
    lista = []
    lista_valores = []
    lista_claves = []
    with open(nombre_archivo, "r") as file:
        for linea in file:         
            linea = linea.strip("\n") 
            p = linea.split(",")  
            lista_valores.append(p)         # Lista de listas, donde cada elemento de lista es una lista con los valores.
            dic_persona, clave = generar_diccionario(lista_valores, lista_claves)
            lista_claves.append(clave)
            lista.append(dic_persona)

    normalizar_datos(lista)

    return lista  


lista_personas = parser_csv("DATA.csv")

for persona in lista_personas:
    print(persona)


print("--------------------------------------------------------------")


# GUARDAR DATOS CSV EN FORMATO JSON
#############################################
personas = {"personas":lista_personas}

with open("personas.json", "w") as file:
    json.dump(personas, file)
##############################################


# for persona in lista:
#     print(persona)



# for linea in lineas:
    # line = linea.strip("\n")    # Me devuelve una copia del string pero sin los espacios en blanco si no le paso nada, pero si le paso el caracter, va a sacar esos caracteres.
    # print(line)


# Aca arrancamos leyendo todo el archivo de una con read(), entonces en la variable contenido teniamos todo el string con toda la informacion de las personas.
# Pero tambien tenemos el metodo readlines() o el objeto file, que es un iterable.
# Con el metodo readlines me traia todas las lineas del archivo y me generaba una lista donde cada elemento de la lista era un string de cada persona (con el \n incluido).

# Pero tambien en vez de usar readlines, puedo iterar sobre file.







lista = []

with open("DATA.csv", "r") as file:
    # lineas = file.readlines()
    for linea in file:         # Esto es lo mismo que usar el writeline o el read o readlines etc. pero sin que me devuelva una lista, me devuelve una linea.
        linea = linea.strip("\n")     # Tambien puedo usar expresiones regulares, usando el metodo sub.
        p = linea.split(",")  
        dic_persona = {}
        dic_persona['id'] = int(p[0])  
        dic_persona['nombre'] = p[1]
        dic_persona['apellido'] = p[2]
        dic_persona['email'] = p[3]
        dic_persona['genero'] = p[4]
        dic_persona['edad'] = int(p[5])
        lista.append(dic_persona)

print(lista)




# lista = contenido.split("\n")

# print(lista)

# lista_personas = []

# for persona in lista:
#     p = persona.split(",")  
#     dic_persona = {}
#     dic_persona['id'] = int(p[0])  
#     dic_persona['nombre'] = p[1]
#     dic_persona['apellido'] = p[2]
#     dic_persona['email'] = p[3]
#     dic_persona['genero'] = p[4]
#     dic_persona['edad'] = int(p[5])
#     lista_personas.append(dic_persona)    
    
