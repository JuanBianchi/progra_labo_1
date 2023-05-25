
acumulador = 0
lista = []
bandera = True
mas_alto = None

for i in range(5):
    numero = int(input("Ingrese un numero: "))
    #validamos el dato
    lista.append(numero)

#-------------------------------------------------

for numero in lista:    # Me permite iterar por todos los elementos de la lista
    acumulador += numero
                                # El error aca es que el calculo del promedio se va a hacer x cantidad de veces.
                                # En la ultima iteracion, el resultado del promedio va a ser correcto y va a ser lo que estoy mostrando afuera del for.
                                # Pero antes de la ultima iteracion se calcularon igual, y dieron resultados incorrectos, solo que no los vemos.

promedio = acumulador / len(lista)      # En el momento del programa que necesito conocer la cantidad de elementos de una lista, en este caso para el calculo del promedio
                                        # tengo la funcion len, que me evita hardcodear el total de elementos de la lista y me permite conseguir el dato de forma dinamica.

print(f"El promedio es {promedio}")

#---------------------------------------------------------

for numero in lista: 
    if bandera or numero > mas_alto:            # Aca, uso el or para poner la condicion de bandera se haga primero. Por lo tanto, no importa lo que tenga a la derecha.
        mas_alto = numero                       # En el or, con que uno de los operando sea true, ya se entra al if.
        bandera = False                                  

print("El mayor valor ingresado es: ", mas_alto)

#Sin bandera

mayor = lista[0]        # Esto es para empezar a comparar en cada iteracion desde el primer indice ingresado de la lista.
for numero in lista:
    if numero > mayor:
        mayor = numero


# Otra froma de sacar el numero mas alto es usar la funcion max en el print. Pero la idea es iterar los elementos
# y buscarlo.

# La opcion del metodo .sort, lo que haria es ordenar la lista de mayor a menor, y podria mostrar el primer elemento de la lista
# ya que el numero mas grande va a estar en el primer indice. 
# Pero la desventaja es que me desordena o cambia toda la lista.
# 
 