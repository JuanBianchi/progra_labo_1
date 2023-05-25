
# Supongamos que tengo esta lista y quiero multiplicar todos los numeros por 2, es decir tenerlos duplicados.

numeros = [4,3,2,1,5,3,5,6]

# La funcion map() va a recibir una funcion lambda
# Lo que hace map es recorrer una lista (como un for sobre numeros) y cada uno de los valores se los tira a funcion lambda
# para que haga la operacion.

# A la funcion map le paso la funcion lambda y un iterable, en este caso una lista.

print(numeros)

duplicados = list(map(lambda num : num * 2, numeros))
# map me devuelve un objeto de tipo map que puede ser convertido a lista y su direccion de memoria, no me devuelve la lista duplicada.
# Si yo quiero que me devuelva una lista, lo encierro en la funcion list para que me devuelva una lista con los items duplicados.

# es decir, la funcion lambda hace exactamente esto:
# duplicados = [] (crea una lista vacia)
# for item in numeros:
#     item = item * 2
#     duplicados.append(item)

print(duplicados)


# Ejemplo para usar en el tark
# colores = list(set(map(lambda heroe : heroe["ojos"], lista_heroes)))
