# Hay distintos tipos de ordenamiento.
# Vamos a ver el bubblesort. No es el mas eficiente, pero es el mas clásico

# Que es un ordenamiento?

lista = [3,2,5,8,4,1,7,9,6,2]

# Lo que vamos a hacer es entender el funcionamiento del burbujeo para despues pasarlo a código.
# Tengo que comparar el primer elemento de la lista con el siguiente.

# Me fijo si estan desordenados, y si lo estan, hago un enroque.
# 

print(lista)

tam = len(lista)

for i in range(0, tam - 1):    
    for j in range(i + 1, tam):
            if (lista[i] > lista[j]):         # La condicion del if se llama criterio de ordenamiento
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

print(lista)

# Por cada iteracion del primer for, el segundo itera 3 veces. Cuando el segundo for termina, recien pasa a la segunda iteracion del primer for.