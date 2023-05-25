# Esto va a ordenar una lista de elementos sencillos, no de diccionarios.

lista = [
    {
        "id": 1, 
        "nombre": "Dean",
        "apellido": "Winchester", 
        "edad": 32, 
        "genero" : "M"
    },
    {
        "id": 2, 
        "nombre": "Sam", 
        "apellido": "Winchester",
        "edad": 29,
        "genero" : "M"
    },
    {
        "id": 3, 
        "nombre": "Castiel",
        "apellido": "Lopez",
        "edad": 1000,
        "genero" : "M"
    },
    {
        "id": 4, 
        "nombre": "Ruby",
        "apellido": "Ciani",
        "edad": 27,
        "genero" : "F"
    },
    {
        "id": 5, 
        "nombre": "Jo", 
        "apellido": "Claus",
        "edad": 25,
        "genero" : "F"
    },
    {
        "id": 6, 
        "nombre": "Delfi", 
        "apellido": "Farrace",
        "edad": 24,
        "genero" : "F"
    },
    {
        "id": 7, 
        "nombre": "Juan", 
        "apellido": "Bianchi",
        "edad": 24,
        "genero" : "M"
    },
    {
        "id": 8, 
        "nombre": "Susana",
        "apellido": "Gimenez",
        "edad": 70,
        "genero" : "F"
    },
    {
        "id": 9, 
        "nombre": "Dennis", 
        "apellido": "Rodman",
        "edad": 49,
        "genero" : "M"
    }
]

def ordenar_lista(lista: list, asc = True):
    tam = len(lista)
    for i in range(0, tam - 1):    
        for j in range(i + 1, tam):
            if (asc and lista[i] > lista[j]) or (not asc and lista[i] < lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def ordenar_lista_diccionario(lista: list, clave: str, asc = True):
    tam = len(lista)
    for i in range(0, tam - 1):    
        for j in range(i + 1, tam):
            if (asc and lista[i][clave] > lista[j][clave]) or (not asc and lista[i][clave] < lista[j][clave]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def ordenar_lista_diccionario_doble_crit(lista: list, grupo: str, clave: str, asc = True):
    tam = len(lista)
    for i in range(0, tam - 1):    
        for j in range(i + 1, tam):
            if ((lista[i][grupo] == lista[j][grupo]) 
                and (((lista[i][clave] > lista[j][clave]) and asc) or ((lista[i][clave] < lista[j][clave]) and not asc)) 
                or (lista[i][grupo] > lista[j][grupo])):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                



numeros = [2,5,4,8,9,1,3,2,5,7]

# print(numeros)

# ordenar_lista(numeros)

# print(numeros)

# print("--------------------------------------------------------")

# print(lista)

# ordenar_lista_diccionario(lista, "edad", False)

# print(lista)

print("--------------------------------------------------------")

ordenar_lista_diccionario_doble_crit(lista, "genero", "edad")

for persona in lista:
    print(persona)


# Que pasa si quiero agrupar por doble criterio?
# Es decir, si quiero que el criterio sea agrupar a quienes tengan datos en comun y tenerlos todos juntos.
# Dentro de un mismo criterio, ahi ordeno por el segundo.

# Por ejemplo, quiero agrupar por genero y despues ordenarlos por edad.

# En este caso, se utilizan dos condiciones separadas con and y se combinan con el operador or. 
# La primera condición verifica si los elementos tienen el mismo valor de grupo, y luego tiene dos subcondiciones:

# ((lista[i][clave] > lista[j][clave]) and asc): 
# Esta subcondición se evalúa como verdadera si asc es True y el valor de clave en lista[i] es mayor que el valor de clave en lista[j]. 
# Esto asegura el orden ascendente.

# ((lista[i][clave] < lista[j][clave]) and not asc): 
# Esta subcondición se evalúa como verdadera si asc es False y el valor de clave en lista[i] es menor que el valor de clave en lista[j]. 
# Esto asegura el orden descendente.

# Si ninguna de las subcondiciones anteriores es verdadera, la segunda parte de la condición:
# (lista[i][grupo] > lista[j][grupo]) se evalúa para manejar el ordenamiento cuando los valores de grupo son diferentes.



# Formas de copiar listas

# Copia shallow:
# lista2 = lista.copy()     copia toda la lista
# lista 2 = lista[ : ]      copia desde tal elemento de la lista hasta el elemento end -1. Es decir, si le paso del 0 al 2, el elemento 2 esta excluido. ( me copiaria el elemento 0 y 1)

# Deep Copia:
#from copy import deepcopy

#lista2 = deepcopy()