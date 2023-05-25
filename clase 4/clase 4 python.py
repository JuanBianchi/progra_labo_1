# El concepto de MUTABILIDAD.
# Algo mutable es algo que CAMBIA, y algo INMUTABLE no cambia, se mantiene constante

# Nosotros vamos a crear una variable o una estructura de datos, y en el momento de la creacion, las cosas mutables no cambian, conserva los valores
# al momento de la creacion. Una vez creado no lo puedo modificar (en principio)
# Lo mutable puedo modificar sus valores.

# Por ejemplo, X = 20, declaro una variable entero y le doy un valor. Pero si supuestamente los enteros son inmutables, por que despues puedo cambiarle el valor a la variable?
# En la memoria (vagamente explicado) existe una parte conocida como memoria dinamica y memoria estatica.
# Cuando yo cree la variable X, se guardo en una parte de la memoria estatica, y el valor de esa variable se guarda en la memoria dinamica, en otra "cajita".
# Lo que esta guardado en la "cajita" de la variable X en la memoria estatica es la DIRECCION de MEMORIA de donde esta almacenado el valor de la variable X.
# que podemos verla con la funcion id()
# Esto pasa en los lenguajes orientados a objetos, se tienen que guardar asi

# Una variable tenia:
# Un id (una direccion de memoria)
# un tipo (a que clase pertenece)
# Un valor (lo que estoy guardando) 

x = 20
print(id(x))
print(type(x))
print(x)

# Es importante saber el tipo de la variable por los metodos que trae asociados.

# Entonces, como los valores enteros no son mutables (es decir, que cambian) en python, cuando yo a X le cambio el valor que tenia por uno nuevo lo que pasa es 
# que se crea otra "cajita" en otra parte de la memoria dinamica, se borra la anterior, y la variable X tiene una nueva direccion de memoria, donde esta almacenado el nuevo valor.

x = 30
print(id(x))

# Los tipos de datos INMUTABLES: Son los enteros, float, string, booleanos.
# En los valores tipo enteros, lo que no muta es lugar o ubicacion donde se guarda el valor, la direccion de memoria.

# Lo que hay que entender ademas es que en python la variable no guarda el valor, si no la direccion de memoria donde esta almacenado el valor.
# Todas las variables guardan direcicon de memoria. 
# Todas las variables son "punteros".

# Entonces, lo que es INMUTABLE es el tipo de dato. Las variables SI son mutables, porque cada vez que yo le cambio el valor a una variable, esta variable cambia a la nueva direccion
# de memoria. Es decir, muta, se muda de direccion.



# Pero tambien existen los tipos de datos MUTABLES, el primer ejemplo son las LISTAS.
# Ya que una lista siempre va a tener la MISMA direccion de memoria, es inmutable, guarda la misma direccion de memoria siempre.
# Lo que va a cambiar es lo que yo guarde en ese dato o lista.

# En C, las cadenas eran un vector de caracteres y yo podia cambiarle el valor de una letra usando vectores.
# Aca no se puede, si yo quiero escribir una cadena diferente, sea minimo el cambio, tengo que destruir la que tengo y construirla de nuevo, porque es inmutable
# No podemos modificar un string.

# Hay dos formas de crear una lista, una con la funcion constructora list() y con corchetes.

lista1 = list()

lista2 = []

lista3 = [2, 42, 63, 10]

print(lista1)
print(lista2)
print(lista3)

print(type(lista1))
print(type(lista2))
print(type(lista3))

print(id(lista1))
print(id(lista2))
print(id(lista3))

# Ambas listas van a guardar una direccion de memoria, cada una la suya. 
# En lista3 lo importante a saber es que todos los elementos tienen la misma direccion de memoria. Y para identificar los elementos, en una lista se utilizan indices.
# El indice indica la posicion que ocupa el elemento en la lista y arranca desde el 0. Si la lista tiene 55 elementos, el indice del ultimo elemento sera el 54. Si tiene 100 elementos, el ultimo sera el 99
# Si una lista tiene N elementos, el indice sera N - 1.

# Si alguien nos pregunta el TAMAÑO o el LARGO de una lista, se esta refiriendo a la cantidad total de elementos de la lista.
# Para eso esta la funcion len()

print(len(lista3))

# Puedo cambiarle el valor de un elemento de la lista, pero la direccion de memoria va a ser la misma, es inmutable.
# Es decir, la lista es mutable porque puedo ir agregandole y cambiandole valores cuando quiera, pero los valores de la lista, los elementos, son INMUTABLES, tengo que crear y destruir cada vez que quiera cambiarlos.

# Entonces, en los tipos de datos inmutables tiene que cambiar la direccion de memoria que guarda la variable
# Y en los tipos de datos mutables la variable no tiene que cambiar la direccion de memoria. Porque como el elemento es mutable, siempre va a estar en la misma direccion dentro de la memoria dinamica. 

# Yo no puedo ir agregando elementos a una lista vacia simplenete asignandoles un valor. Para eso, tengo que usar metodos de la lista, como el append.
# Y el append agrega el elemento al ULTIMO indice de la lista. Si ya tengo una lista con 2 elementos, con el append se agrega uno nuevo en el 2 indice y tendria 3 elementos.



# Para recorrer una lista, podemos hacerlo facil con la estructura de programacion for in que nos permitia recorrer un iterable.
# Para utilizar el for in necesitamos crear un iterador, un elemento que tengas varios elementos, para eso esta la funcion range.
# Range nos devolvia un iterable, entonces con el for in podiamos iterar tantas veces como lo tenga el iterable (la funcion range)
# Y una lista es un elemento iterable

lista = [23, 34, 45, 56, 67]

for numero in lista:     #aca lista tiene 5 elementos, es decir que se va a iterar 5 veces.
    print(numero)

print("----------------------")

# Otra forma en la que puedo iterar es la siguiente:

for indice in range(len(lista)):
    print(lista[indice])

# Aca lo que estoy haciendo es usar la funcion range para iterar una determinada cantidad de veces, solo que puedo pasarle como parametro el tamaño de la lista usando la funcion len()
# Y una vez dentro del for in, la variable indice va a tomar el valor de cada elemento de la lista durante las iteraciones.
# Cuando haga la primera iteracion, como la variable indice va a estar en el indice 0 de la lista, va a tomar el valor 23, que es el primer elemento de la lista.

# Las dos formas de escribir la iteracion son lo mismo, obviamente vamos a preferir la primera porque es mas simple
# PERO, hay mas flexibilidad a la hora de escribir el codigo, y voy a usar la forma que yo crea mas conveniente en el momento.
# Para el usuario, la lista iterada de numeros es la misma, pero el codigo es diferente. 
 


# Ahora, yo tambien puedo hacer esto:

lista4 = [43, "hola", 3.14, True, 34, ["hola", "soy", "juan"]]

# Puedo almacenar en una lista cualquier tipo de datos (ACLARACION, lo que guardan las listas son direcciones de memoria, solo que nosotros no lo vemos).
# Si todas las variables guardan direcciones de memoria, todos los elementos de una lista son direcciones de memoria. Todo lo que tenemos en las listas, separados por comas
# son direcciones de memoria donde se guardan los valores.
# A su vez, la propia lista tiene su propia direccion de memoria.
# Esta lista tendria 6 elementos, la lista de strings dentro de lista4 cuenta como elemento de la lista principal.
# Y pudiendo hacer esto, por ahora no lo vamos a hacer. Porque es mucho mas dificil de manejar.


# Hay una particularidad que tienen las listas con respecto al indice. Y es que yo puedo indicar los indices de las listas con numeros negativos.
# Lo mas importante es saber que si yo indico el -1 como numero de indice, estaria seleccionando el ultimo elemento de la lista.


#METODOS DE LAS LISTAS

# Si yo quiero acceder o iterar sobre la lista de strings de lista4, existe la siguiente manera:

print(lista4[5][2]) # Aclaro entre el primer corchete el indice donde se encuentra la "sub-lista" y con otros corchetes al lado la posicion que quiero imprimir de la "sub-lista"

# Y si quiero iterar sobre la lista con un for in:

for elemento in lista[5]:   #aclaro entre corchetes el elemento donde esta la sublista.
    print(elemento)

# Tambien podriamos hacer: 

lista_rosa = lista4[5]

for elemento in lista_rosa:
    print(elemento)