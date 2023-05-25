# Supongamos que tenenmos una lista para cada dato, tendriamos los datos de una misma entidad desparramados en un monton de listas
# Y tendriamos que manipular muchas listas.

# Una manera de resolver seria pudiendo meter todos los datos repartidos en los indices en cada una de las listas en una coleccion.
# Es decir, poder hacer una lista que tenga datos de distinto tipo pero de una sola persona
# Por ejemplo una lista que tenga la nota 1er parcial, 2do parcial y el promedio de un alumno. Otra lista para otro alumno y asi.
# Por ejemplo una lista de listas.

notas_alumnos =  [[10, 9, 9.0, "Juan"], [6, 7, 6.5, "Sebastian" ], [4, 5, 4.5, "Carlos"]]

print(notas_alumnos[0])     # Imprime la lista con los datos de Juan, si pongo 1 las de sebastian y asi..
print(notas_alumnos[0][3])  # Esto es si quisiera mostrar el nombre del primer alumno.

# notas_alumnos es una lista de listas.
 
 # Poder trabajar con esto se puede, pero es un quilombo acordarse los indices de cada elemento de las listas.
 # Para resolver este tipo de problemas tenemos otra coleccion de objetos. Que son los DICCIONARIOS.
 # en otros lenguajes se llaman ARRAYS asociativos.

 