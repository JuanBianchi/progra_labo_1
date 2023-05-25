# diccionarios
# Para generar un diccionario hago lo mismo que con una lista pero con llaves en vez de corchetes
# Los nombres de los datos se escriben entre comillas como string y el dato se guarda
# con DOS PUNTOS y se separan con COMA

alumno = {
    "nota_1": 10,           
    "nota_2": 9,
    "promedio": 9.0,
    "nombre": "Juan",
}

#print(alumno["nombre"])

# El diccionario no es ordenado como una lista. Aca yo accedo por el nombre del dato. 
# Entonces no importa de la posicion en la que se encuentre
# Al igual que las listas, los diccionarios son mutables.
# Significa que lo puedo modificar una vez creado, se queda en la misma posicion de memoria y es dinamico
# Entonces, si quiero recorrer un diccionario, lo hago igual que una lista.

for elemento in alumno:
    print(elemento) #Esto me devuelve el nombre de las claves

for elemento in alumno:
    print(alumno[elemento]) #Esta manera me devuelve el VALOR del nombre de las claves

for elemento in alumno:
    print(elemento, alumno[elemento]) #Esta manera me devuelve tanto el nombre de las claves y el valor.


# Esto me permite preguntar el campo que quiera y acceder a ese campo y con el print, mostrar lo que vale la clave.
clave = input("Ingrese clave: ")

print(alumno[clave])


# alumno["nombre"] = "Juancito" # Con esto puedo sobreescribir el valor de una clave

alumno["email"] = "juampibianchi@hotmail.com"  # Puedo agregar elementos tambien asi.

print(alumno)


del alumno["promedio"]      # Con esto puedo eliminar un elemento o clave.