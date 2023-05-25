import os
from data_spark import *

# lista = lista_personajes. Esto esta mal, porque si yo despues quiero cambiarle el valor a un elemento de mi lista, no puedo hacer sin modificar la lista original.

def esta (lista:list, item:any)->bool:
    rta = False
    for elemento in lista:
        if elemento == item:
            rta = True
            break
    return rta

def filtrar_por(lista:list, key:str, value:any)->None:
    for item in lista:
        if(item[key] == value):
            print(item)

def filtro(lista:list, key:str, value:any)->list:
    lista_filtrada = []
    for item in lista:
        if item[key] == value:
            lista_filtrada.append(item)
    return lista_filtrada

lista = []         # Lo que quiero hacer es no trabajar con la lista de datos original, si no procersarla y trabajar con los mismos datos pero en esa lista creada por mi.
colores = []
colores_filtrados = []

for heroe in lista_personajes:
    lista.append(heroe.copy())

print(lista)
os.system("pause")

for heroe in lista:
    colores.append(heroe['color_ojos'])

print(colores)
os.system("pause")

for color in colores:
    if not esta(colores_filtrados, color):
        colores_filtrados.append(color)

print(colores_filtrados)
os.system("pause")

for color in colores:
    print("\n------------------")
    print(color)
    print("------------------")
    for heroe in lista:
        if heroe['color_ojos'] == color:
            print(heroe['nombre'])
print("-----------------------------------")



print("-----------------------------------------------")


# for heroe in lista_personajes:
#     print(heroe)

## print(lista_personajes[0])
# o tambien
## print(lista[0])

## lista[0]['empresa'] = 'dc comics'
# Con esto cambio una clave del diccionario
# Se lee como 'del campo empresa, en el elemento 0'
# Del personaje que esta en el indice 0, quiero cambiarle la empresa

