x = "Hola mundo"

print(x.lower())

print("Chau mundo".lower())

aux = list(x)

for i in range(len(aux)):
    if (aux[i].islower()):
        aux[i] = aux[i].upper()

print(aux)

# Nosotros creemos que la funcion print recibe una cadena de caracteres.
# Pero no, esta recibiendo una direccion de memoria.

# Es decir, el interprete de python primero analiza lo que esta entre parentesis, reserva el espacio en memoria justo y necesario para almacenarla.
# Y la funcion print devuelve la direccion de memoria donde esta guardado ese string
# Despues la funcion print lee lo que hay en esa direccion de memoria y lo muestra.
# 
# Y asi como se genero una cadena, que es un objeto, tambien tiene metodos.

# La unica diferencia entre un metodo y una funcion es que a diferencia de una funcion, es que puedo acceder a los metodos con el operador .

# Yo puedo acceder al metodo a traves de la variable o a traves del objeto (en este caso "chau mundo", que es un objeto str)

# Las cadenas una vez que las tengo creadas en memoria son iterables.
# Es decir, yo puedo imaginarlas como una lista de strings.
# Pero como un objeto string es inmutable, no puedo cambiarle su valor

print(x[0])

# el metodo join lo que hace es devolver una cadena o una lista de cadenas y los concatena con el string que quiero.

y = "".join(aux)

print(y)