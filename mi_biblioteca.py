import os
import re


def saludar(nombre):
    print(f"Hola {nombre}")

("----------------------------------- FUNCION GENERAR DICCIONARIO Y PARSEAR CSV -----------------------------------")

("------------------------------------------- NORMALIZAR DATOS ------------------------------------------------")
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


def parsear_csv(nombre_archivo: str)-> list:
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


("------------------------------------------------ STARK PARTE 1 ------------------------------------------------")

def buscar_mostrar_heroe(lista: list, clave: str, valor: any) -> None:
    for item in lista:
        if item[clave] == valor:
            print("-----------------------------------------------------------------------------------------")
            print(item)


def filtro(lista:list, key:str, value:any)->list:
    lista_filtrada = []
    for item in lista:
        if item[key] == value:
            lista_filtrada.append(item)
    return lista_filtrada


def esta (lista:list, item:any)->bool:
    rta = False
    for elemento in lista:
        if elemento == item:
            rta = True
            break
    return rta


def calcular_mas_altos_mas_bajos(lista: list, clave: str, valor: any)-> list:
    lista_mas_altos = []
    lista_mas_bajos = []
    bandera = True
    for heroe in filtro(lista, clave, valor):
        altura = float(heroe['altura'])
        if bandera or altura > altura_maxima:
            altura_maxima = altura
            mas_alta = heroe 
        
        if bandera or altura < altura_minima:
            bandera = False
            altura_minima = altura
            mas_bajo = heroe


    for heroe in filtro(lista, clave, valor):
        if float(heroe['altura']) == altura_maxima:
            lista_mas_altos.append(heroe)
        
        if float(heroe['altura']) == altura_minima:
            lista_mas_bajos.append(heroe)

    return lista_mas_altos, lista_mas_bajos


def calcular_mostrar_promedio_alturas(lista: list, clave: str, valor: any)->None:
    alturas = []
    for item in filtro(lista, clave, valor):
        alturas.append(item['altura'])

    acumulador_alturas = 0
    for altura in alturas:
        acumulador_alturas += float(altura)

    promedio_alturas = acumulador_alturas / len(alturas)
    print(f"El promedio de las alturas es: {promedio_alturas:.2f} centimetros." )


def contar_mostar_cuantos_tienen_cada_tipo_atributo(lista, clave):
    lista_atributo = []
    lista_atributos_filtrada = []
    for elemento in lista:
        if elemento[clave] == "":
            elemento[clave] = "No tiene"
        lista_atributo.append(elemento[clave])

    for atributo in lista_atributo:
        if not esta(lista_atributos_filtrada, atributo):
            lista_atributos_filtrada.append(atributo)

    contador_atributos = 0   # Inicializo

    for atributo in lista_atributos_filtrada:
        print("\n" + atributo)
        print("------------")
        for elemento in lista:
            if atributo == elemento[clave]:
                contador_atributos +=1
        print(contador_atributos)
        contador_atributos = 0   # Reseteo contador a 0


def mostrar_por_atributo(lista, clave):
    lista_atributo = []
    lista_atributos_filtrada = []
    for elemento in lista:
        if elemento[clave] == "":
            elemento[clave] = "No tiene"
        lista_atributo.append(elemento[clave])

    for atributo in lista_atributo:
        if not esta(lista_atributos_filtrada, atributo):
            lista_atributos_filtrada.append(atributo)

    for atributo in lista_atributos_filtrada:
        print(f"\n{atributo}")
        print("-------------------")
        for elemento in lista:
            if atributo == elemento[clave]:
                print(elemento)


(" ---------------------------------------- EJERCICIO STARK PARTE 2 ----------------------------------------------")

def obtener_nombre(diccionario: dict) -> str:
    """_summary_
        busca y retorna el primer valor dentro de un diccionario 
    Args:
        diccionario (dict): diccionario con claves y valores a ser iterado. 

    Returns:
        str: devuelve el primer valor del diccionario que sea de tipo str
    """
    nombre = None
    for clave in diccionario:
        valor = diccionario[clave]
        if type(valor) == str:
            nombre = valor
            break
        else:
            break
    if nombre == None:
        nombre = "Nombre no encontrado."
    else:
        nombre_encontrado = f"Nombre: {nombre}"

    return nombre_encontrado


def imprimir_dato(dato: str):
    """_summary_
        imprime lo que recibe por parametro
    Args:
        dato (str): tipo de dato string a ser impreso
    """
    print(dato)


def obtener_nombre_dato(diccionario: dict, clave: str)->str:
    """_summary_
        busca en el diccionario la clave recibida por parametro y la devuelve con su valor formateado.
    Args:
        diccionario (dict): diccionario donde se busca la clave\n
        clave (str): item a ser buscado en el diccionario

    Returns:
        str: retorna un string formateado con la clave y el valor si se encontró o retorna otra cadena informando que no se encontró
    """
    if type(clave) != str:
        print("ERROR. El dato a buscar tiene que estar entre comillas dobles o simples.")
    else:
        for key in diccionario:
            if clave not in diccionario:
                cadena = ("Dato no disponible.")
            else:
                if key == clave:
                    dato = diccionario[key]
                    nombre = diccionario['nombre']
                    cadena = (f"Nombre:{nombre} | {clave}: {dato}")

    return cadena


def calcular_max(lista: list, clave: str)-> dict:
    """_summary_
        encuentra la clave con el valor máximo en una lista de diccionarios y lo retorna 
    Args:
        lista (list): lista de diccionarios donde se busca el dato\n
        clave (str): clave o key del valor a ser buscado

    Returns:
        dict: retorna el elemento de tipo diccionario donde se encuentra el valor máximo de la clave
    """
    maximo = None
    bandera = True
    if len(lista) > 0:
        for diccionario in lista:
            for key in diccionario:
                if key == clave:
                    if type(diccionario[key]) == int or type(diccionario[key]) == float:
                        if bandera or diccionario[key] > valor_mas_alto:
                            bandera = False
                            valor_mas_alto = diccionario[key]
                            maximo = diccionario
                
    # HACERLO CON MAS DE 1 MAXIMO.
    return maximo


def calcular_min(lista: list, clave: str)-> dict:
    """_summary_
        encuentra la clave con el valor minimo en una lista de diccionarios y lo retorna 
    Args:
        lista (list): lista de diccionarios donde se busca el dato\n
        clave (str): atributo por el cual se filtra la busqueda

    Returns:
        dict: retorna el elemento de tipo diccionario donde se encuentra el valor máximo de la clave
    """
    minimo = None
    bandera = True
    if len(lista) > 0:
        for diccionario in lista:
            for key in diccionario:
                if key == clave:
                    if type(diccionario[key]) == int or type(diccionario[key]) == float:
                        if bandera or diccionario[key] < valor_mas_bajo:
                            bandera = False
                            valor_mas_bajo = diccionario[key]
                            minimo = diccionario
        
    # HACERLO CON MAS DE 1 MINIMO.
    return minimo


def calcular_max_min_dato(lista: list, calculo: str, clave: str)-> dict:
    """_summary_
        busca tanto el valor máximo como el mínimo dentro de una lista de diccionarios. El tipo de cálculo es recibido como
        segundo parámetro.
    Args:
        lista (list): lista de diccionarios donde se busca el dato\n
        calculo (str): tipo de cálculo a realizar, máximo o mínimo\n
        clave (str): atributo por el cual se filtra la busqueda

    Returns:
        dict: devuelve el elemento de tipo diccionario donde se encuentra la clave con el valor máximo o mínimo
    """
    if calculo == "maximo":
        retorno = calcular_max(lista, clave)
    elif calculo == "minimo":
        retorno = calcular_min(lista, clave)

    return retorno


def sumar_dato_heroe(lista: list, clave: str)-> float:
    """_summary_
        busca y suma en la lista diccionarios los valores contenidos en las claves que coincidan con el segundo parametro de la funcion   
    Args:
        lista (list): lista de diccionarios donde estan los valores a sumar
        clave (str): clave a buscar en el diccionario

    Returns:
        float: valores encontrados sumados
    """
    total_datos = 0
    for heroe in lista:
        if type(heroe) == dict and len(heroe) > 0:
            for dato in heroe:
                if clave == dato:
                    total_datos += heroe[dato]
        else:
            print("Diccionario vacío")            

    return total_datos


def dividir(dividendo: int, divisor: int)-> float:
    """_summary_
        divide el primer parametro por el segundo parametro y analiza que este ultimo sea distinto de 0.
    Args:
        dividendo (int): valor a ser dividido
        divisor (int): valor que divide

    Returns:
        float: resultado de la division
    """
    if divisor == 0:
        rta = 0
    else:
        rta = dividendo / divisor

    return rta


def calcular_promedio(lista: list, clave: str)-> float:
    """_summary_
        calcula el promedio del dato recibido en el segundo parametro que esta almacenado en la lista de diccionarios recibida 
        en el primer parametro
    Args:
        lista (list): lista de diccionarios que es enviada a la funcion sumar_dato_heroe para que sea iterada en ella
        clave (str): parametro que sirve de filtro para la busqueda del dato 

    Returns:
        float: devuelve el promedio de los valores del dato que fueron encontrados en la lista
    """
    acumulador_datos = sumar_dato_heroe(lista, clave)
    promedio = dividir(acumulador_datos, len(lista))

    return promedio


def validar_entero(numero: str)-> bool:
    """_summary_
        evalua y parsea el caracter o string recibido por parametro
    Args:
        numero (str): caracter numerico que sera evaluado y casteado

    Returns:
        bool: devuelve True si el parametro recibido es un caracter numerico o False si no es un caracter numerico 
    """
    if re.search(r"^\d{1,}$", numero):
        rta= True
    else:
        rta = False

    return rta


def imprimir_opciones_menu():
    """_summary_
        imprime las opciones que seran usadas en el menu principal
    """
    imprimir_dato("1) Normalizar datos")
    imprimir_dato("2) Imprimir nombres de los heroes")
    imprimir_dato("3) Imprimir la altura y el nombre de los heroes")
    imprimir_dato("4) Imprimir el maximo o minimo de: fuerza, altura o peso")
    imprimir_dato("5) Mostrar el promedio de las alturas")


(" ----------------------------------------- FUNCIONES STARK -----------------------------------------------------")

def stark_imprimir_nombres_heroes(lista: list)->int:
    """_summary_
        itera la lista para despues buscar e imprimir el primer valor de la lista. 
    Args:
        lista (list): lista a ser iterada

    Returns:
        int: retorna 0 si la lista contiene elementos, retorna -1 si la lista está vacía
    """
    if len(lista) > 0:
        rta = 0
        for heroe in lista:
            nombre = obtener_nombre(heroe)
            imprimir_dato(nombre)
    else:
        rta = -1
    
    return rta


def stark_imprimir_nombres_alturas(lista: list)->int:
    """_summary_
        busca en una lista de diccionarios la altura de los heroes y retorna el valor y el dato formateado
    Args:
        lista (list): lista de diccionarios donde se va a buscar el dato

    Returns:
        int: retorna 0 si la lista tiene al menos un elemento, o retorna -1 si la lista está vacía
    """
    if len(lista) > 0:
        rta = 0
        for elemento in lista:
            nombre = obtener_nombre_dato(elemento, "altura")
            print(nombre)
    else:
        rta = -1
    
    return rta


def stark_calcular_imprimir_heroe(lista: list, calculo: str, clave: str)-> int:
    """_summary_
        busca en una lista de diccionarios el valor máximo o mínimo y lo imprime formateado junto al heroe a quien
        le corresponde ese valor junto a su atributo. El tipo de calculo es recibido como segundo parámetro 
    Args:
        lista (list): lista de diccionarios donde se encuentra el heroe con el valor a ser buscado\n
        calculo (str): tipo de calculo a realizar, máximo o minimo\n
        clave (str): atributo por el cual se filtra la busqueda

    Returns:
        int: retorna 0 si la lista contiene al menos un elemento o -1 si la lista está vacía
    """
    if len(lista) > 0:
        rta = 0
        resultado = calcular_max_min_dato(lista, calculo, clave)
        for elemento in lista:
            nombre = obtener_nombre_dato(resultado, clave)    
    else:
        rta= -1
    imprimir_dato(f"{clave.capitalize()} {calculo.capitalize()}: {nombre}")

    return rta


def stark_calcular_imprimir_promedio_altura(lista: list):
    """_summary_
        busca y suma todas las alturas en la lista de diccionarios y calcula su promedio 
    Args:
        lista (list): lista que sera recorrida para buscar el promedio
    """
    promedio = calcular_promedio(lista, "altura")
    imprimir_dato(f"El promedio de las alturas es {promedio}")


def stark_menu_principal()->int:
    """_summary_
        imprime las opciones del menu principal y pide al usuario un caracter numerico para ser evaluado como opcion
    Returns:
        int: opcion del menu ya evaluada y validada
    """
    imprimir_opciones_menu()
    opcion = input("Ingrese una opcion (en numeros)")
    if validar_entero(opcion):
        numero = int(opcion)
    else:
        numero = -1
    
    return numero