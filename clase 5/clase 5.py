# Ejemplo
lista = []
x = 50
y = 50

print(id(lista))
print(id(x))
print(id(y))

# Lo que pasa aca es que, cuando python detecta que queremos guardar el mismo valor en diferentes variables,
# detecta que ya internamente guardo ese valor en algun lugar en la memoria. Y para ahorrar espacio en memoria
# hace que las variables x e y apunten a la misma direccion de memoria donde esta almacenado el valor 50.
# Reutiliza el espacio guardado en la memoria dinamica. Esto tiene que ver con mutabilidad.

lista.append(id(x))
lista.append(id(y))

print(id(lista[0]))
print(id(lista[1]))



########################

# Que tema nos vienen a resolver las listas?

numero_uno = None
numero_dos = None
numero_tres = None
numero_cuatro = None
numero_cinco = None

numero_uno = int(input("Ingrese un numero: "))
numero_dos = int(input("Ingrese un numero: "))
numero_tres = int(input("Ingrese un numero: "))
numero_cuatro = int(input("Ingrese un numero: "))
numero_cinco = int(input("Ingrese un numero: "))

total = numero_uno + numero_dos + numero_tres + numero_cuatro + numero_cinco

print(f"La suma de los numeros ingresados es: {total}")

# Con estructura repetitiva:
acumulador = 0
lista = []
TAM = 10    # En python no existe el concepto de constante, pero por convencion se puede declarar una variable en mayusculas para usarlo como constante 


for i in range(5):      # Este for lo puedo usar para cargar datos.
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            break
        except ValueError:
            print("ERROR. No ingresaste un numero.")
    
    #acumulador += numero

    lista.append(numero)

for numero in lista:  # numero va a tomar en cada iteracion el valor de cada elemento de la lista. 
    print(numero)       # Este for in lo uso para recorrer la lista.

for i in range(5):
    print(lista[i]) # Esto es una manera alternativa de hacer lo mismo que antes.
                    # Se va a imprimir la lista en el indice que toma i en cada iteracion.

for i in range(TAM):    # Esto esta bien, PERO si y solo si el tamaño de la lista siempre va a ser el mismo. Que pocas veces va a ser el caso.
    pass

for i in range(len(lista)):  # Esto me va a devolver la cantidad de elementos que tiene la lista y puedo usarla como cantidad de veces para iterar toda la lista.
    print(lista[i])           # Pero es mas facil usar la primera opcion (la de for i in lista:)

for numero in lista:        # Este for lo uso para sumar todos los elementos de la lista.
    acumulador += numero


print(f"La suma de los numeros ingresadoes es: {acumulador}")

# Pero esto tiene la limitacion de no poder recordar los numeros ingresados que se fueron acumulando para dar el total.
# Para esto sirven las colecciones (listas).

# Variables (u objetos) escalares son las que guardan un solo tipo de valor.
# Variables (u objetos) compuestas, que son las colecciones, y hasta ahora el tipo de colecciones que conocemos son las listas.

# con ese for in, hago que itere 5 veces, ingresando 5 numeros, y con el append voy agregando el numero a la lista en cada iteracion
# Siempre es recomendable caputar el dato ingresado por el usuario en una variable y luego validarlo, antes de guardarlo en la lista.

# Con el for in, puedo recorrer un elemento iterable, que en este caso es la lista.


# De todas las formas que puedo usar el for in, la mas comoda es la primera de todas. Pero no hay una unica manera
# de escribir el codigo.