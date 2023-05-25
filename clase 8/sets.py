# El set es un elemento INMUTABLE

# Un set es un elemento que fue creado para asemejarse a la teoria de conjuntos.
# para declarar un set, se usan las llaves, igual que los diccionarios. 
# La diferencia es que en los diccionarios tengo que meterle claves y valores. Aca solo agrego valores separados por comas.

s1 = {4, 3, 6, 12,}

s2 = {4, 3, 6, 20, 12, 8}

print(s1)

# Un set no guarda valores repetidos. Primero se fija si ese valor ya esta en la lista y si esta, no lo agrega.
# Los sets, no tienen indices. 
# En el print se muestran como si estuvieran ordenados de menor a mayor, pero en realidad no lo estan.

# Si yo quisiera buscar un elemento dentro del set, no voy a poder, ya que un set no es una estructura ordenada.

s3 = {"Juan", "Pedro", "Lucia", "Amalia", "Pedro", "Alfredo"}

print(s3)

# Si nos fijamos, cada vez que ejecuto el programa, el set ordena de manera diferente cada vez.

# Con un set de numeros no pasa eso. Es mas, tampoco los "ordena" de forma ascendente si probamos metiendole un 1000 o un 100, etc.

# En que ocasiones puedo usar un set? Primero cuando quiero trabajar con conjuntos,
# para saber si hay elementos repetidos.
# Otro uso es para cuando quiero obtener un elemento de cada tipo.
# O cuando quiero buscar un elemento que comparta un dato en comun.

for item in s2:
    print(item)

# Puedo recorrer el set asi, pero no en un orden en especifico, es decir, no puedo buscar indices o un elemento en especifico.
# Podemos buscar un elemento pero hay que recorrerlo en su totalidad.

# El metodo .pop() nos da un elemento aleatorio, a comparacion de las listas que podiamos pedir el elemento.

print(s2.pop())


# Si quiero recorrer el set con un for in, no puedo ni remover ni agregar elementos al set.
# Es decir, no puedo modificar el tamaño del set.
# Cuando recorro el set, su tamaño tiene que ser constante.



# Tambien puedo unir sets usando el operador | (or) o usando el metodo .union()

s4 = s1 | s2

# Tambien puedo usar el metodo .intersection() para saber lo que los dos conjuntos tienen en comun, la interseccion.
# Para que tenga los numeros que estan en ambos sets.

s4 = s1.intersection(s2)
