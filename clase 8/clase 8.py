# Hoy vemos TUPLAS y SETS.
# y algunos metodos que tienen

# vimos que las listas y los diccionarios eran mutables, podiamos modificarlos cambiando los elemento.
#Las tuplas son INMUTABLES, una vez creada no se puede modificar.

# En C, lo mas parecido a una lista era el linkedlist.

# VER EN VIDEO EXPLICACION MALLOC
# Python usa malloc internamente, ya que esta programado en C
# Si queres guardar un numero gigante, python calcula el tamaño que va a ocupar ese numero y reserva bits en la memoria
#
# Una tupla es un elemento INMUTABLE, una vez creado es inmodificable, no puedo ni agregar ni quitar elementos
# Viene fija de fabrica,
# Una tupla vendria a ser lo que es un vector o array en C
# 
# Cuando voy a hacer una tupla, en lugar de usar corchetes para definirlo, uso PARENTESIS

lista = [20, 45, 30, 48, 34]


# Esa tupla en memoria, es como que pida en la memoria dinamica un array
# Un array son celdas de memoria contiguas.
# Entonces, lo que va a hacer es fijarse cuanto pesan todos los numeros en la tupla
# Y en memoria ocupan una misma direccion de memoria.
# Los vectores o arrays son estaticos, no lo puedo mover, solo puedo moverlos con malloc.

# Para que sirven las tuplas? Para recorrerlo mas rapido.
# Si yo tengo una lista de datos, y lo unico que quiero hacer es recorrerla, solo recorrela, es mejor tener una tupla.
# No tengo que dar vueltas a comparacion de una lista, que sus datos e indices estan guardados en cualquier lado.

# Tengo la posibilidad de pasarle una lista a una tupla, es decir, convertir la lista en tupla.
# con la funcion tuple

tupla = tuple(lista)

print(lista)
print(type(lista))
print(tupla)
print(type(tupla))

print(id(tupla[0]))
print(id(tupla[1]))
print(id(tupla[2]))
print(id(tupla[3]))
print(id(tupla[4]))

for i in tupla:
    print(i)

for i in range(len(tupla)):
    print(tupla[i])

# El metodo

# El metodo INDEX me devuelve el indice de donde se encuentra el elemento en la tupla
# Si no esta, me tira una excepcion

# Puedo utilizar el operador in para saber si el elemento esta dentro de la tupla
print(45 in tupla)
# y  me devuelve un booleano

if(45 in tupla):
    indice = tupla.index(45)


# Hay algo que se puede hacer con las tuplas.

tupla = ([20, 45, 30, 48, 34])

# Es estructuracion.
# Si quiero guardar el 20 y el 45 en una variable hago lo siguiente.

a = tupla[0]
b = tupla[1]

# Ahora, yo podria hacer lo mismo pero asi

a, b, c, d, e = tupla

print(a)
print(b)

# Si o si tengo que asignarle a variables todos los elementos de la tupla, si le asigno menos me tira error. No importa si despues no las uso.


# En una funcion, yo puedo hacer que una funcion devuelva dos objetos.
# Entonces, la funcion devuelve esos objetos como tupla, es como si los empaquetara y me los devuelve juntos.
# Despues, cuando hago la desestructuracion, es como si desarmara la caja y atrapo los valores en variables separadas.

# Tambien puedo hacer esto:

valores = 34, 56, 78
print(type(valores)) # Esto me va a devolver que es una tupla.

