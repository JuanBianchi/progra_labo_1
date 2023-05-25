# MUTABILIDAD

# El concepto de punteros no es tan parecido en python como lo era en C.

# En la memoria RAM, existen transistores. Cuando declaramos una variable, lo que pasa en memoria es reservarse transistores.
# Todo lo que funcione en la memoria, se hace en codigo binario.

# A todos los millones de transistores que estan en memorias, que se dividen en octetos, se los reconocen por la direccion de memoria que ocupan
# Entonces, cuando declaramos una variable, esta tiene 3 caracteristicas principales:
# -La direccion de memoria
# -El tipo de dato
# -Y un valor (que es el que se guarda)

x = 20
print(x)
print(id(x))
x = 40
print(x)
print(id(x))

# Si quiero saber el tipo, uso la funcion type
# Si quiero saber la direccion de memoria, uso la funcion id, que me muestra la direccion de memoria.

# Si yo le cambio el valor a la misma variable, muestra otra direccion de memoria.
# Que es lo que hace python? Cada vez que declaramos una variable y le asignamos un valor, y luego se lo cambiamos, se genera una direccion de memoria nueva en la memoria dinamica y 
# Esto se le conoce como INMUTABILIDAD. Se le puede dar un valor en el momento en que se crea la variable.
# Cuando se le pone un valor nuevo a una variable, la direccion de memoria anterior se libera y se ocupa otra.
# Se muda, si pasa eso en un tipo de dato es INMUTABLE
# Esto pasa con los tipos booleanos, strings, enteros, flotantes y los complex

# Pero tambien hay tipos de datos MUTABLES, tambien llamados LISTAS.
# Es un tipo de dato que nos permite guardar otros tipos de datos
# Es el equivalente al array en C. Pero no es un array

lista = []
lista_dos = [1, 4, 5, 6]
lista_tres = ["a", "e", "q", "g", "c", "o"]
lista_cuatro = [True, False, True, False, False]
lista_cinco = [23, "Juan", True, 1.75]
lista_seis = [1, 4, 6, 8, ["a", "b", "c", "d", [23, 45, 65]]]     #Tambien pueden guardarse listas dentro de otra lista. Lo que serian las matrices

print(type(lista))
print(type(lista_dos))
print(type(lista_tres))
print(type(lista_cuatro))


# Puedo tener listas de los tipos de datos que quiera
# Independientemente de lo que tenga guardado una lista, todas son del tipo list.
# En un array, se guardan datos del mismo tipo. En una lista, se pueden guardar datos de distinto tipo. Esto es DINAMICO
# A pesar de que puede hacerse esto, no lo vamos a hacer. Vamos a mantener el tipo 

# Las listas tambien tienen metodos, que se pueden ver usando . al lado del nombre de la lista

lista.append(88) # Con el metodo append, agregamos un elemento nuevo a la lista. Este elemento va al final de la lista

# Una lista es MUTABLE, por mas que yo modifique los elementos de una lista, la lista no se muda de direccion o destruye.
# Ademas es DINAMICA, significa que puedo agregarle o quitarle elementos cuando sea, es decir cambia su tamaño. A diferencia de un string, que no puedo cambiarlo

# Los elementos de una lista estan señalados por un índice. Empieza desde el indice 0, siendo el 0 el primer elemento de la lista.
# Siempre se arranca desde el 0

print(len(lista_dos)) #TAMAÑO. Cuenta los elementos que tiene la lista
print(lista_dos[0]) #Muestra el primer elemento de la lista
print(lista_dos[1]) #Muestra el segundo elemento de la lista
print(lista_dos[2]) #Muestra el tercer elemento de la lista
print(lista_dos[3]) #Muestra el cuarto elemento de la lista



# La cantidad de elementos que tiene una lista se refiere tambien como al LARGO o el TAMAÑO de la lista.
# Y NUNCA va a haber una lista del tamaño de su LARGO, es decir, no puede haber una lista de tamaño 5, con un indice 5. Siempre es indice = largo/tamaño + 1

# Cada elemento de la lista ocupa una direccion de memoria DIFERENTE de las demas.
print(id(lista_dos[0])) #Muestra la direccion de memoria del primer elemento de la lista
print(id(lista_dos[1])) #Muestra la direccion de memoria del segundo elemento de la lista
print(id(lista_dos[2])) #Muestra la direccion de memoria del tercer elemento de la lista
print(id(lista_dos[3])) #Muestra la direccion de memoria del cuarto elemento de la lista

# La caracteristica que tiene python es que puedo poner indices negativos en la lista para mostrarlos.
# Seria como empezar a contarlo al reves, del ultimo elemento hasta el primero
print(lista_dos[-1])
print(lista_dos[-2])
print(lista_dos[-3])
print(lista_dos[-4])

# Lo que podemos hacer tambien, es cambiarle el valor que esta en un indice especifico.
lista_dos[1] = 3 # Aca estoy cambiando el valor que estaba en el elemento 1 (que era un 4) a un 3


# Ahora vamos al caso de las listas dentro de otra lista.
# La lista en total tiene 5 elementos. Por que? Porque las otras listas tambien cuentan como elementos para la lista "principal".

print(len(lista_seis)) #Tiene 5 elementos

# Entonces, el elemento 4 de lista_seis, seria la otra lista (la que tienen a, b y c).
# Y sus elementos, serian como "sub-elementos" de la lista principal, pero son elementos principales de la lista de a, b y c. Es decir, se empiezan contando desde el 0 siempre.

#print(lista_seis[0][1][3]) # Esto es para mostrar los distintos elementos de las diferentes listas. Va un corchete por cada lista.


# Cuando dijimos que cada elemento tiene una direccion de memoria diferente, nosotros podemos cambiarle un elemento a una lista, pero la lista va a tener la misma direccion de memoria.
# Es decir, las listas son MUTABLES.


# Una lista es un elemento iterable, y la forma mas facil de recorrer una lista es con un for in.
for i in lista_dos:
    print(i)


    #TAREA
    # Pedir 5 numeros e ir agregandolos a la lista
    # Mostrar los numeros de la lista
    # Recorrer la lista y sumarlos