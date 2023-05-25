from alumno import lista_alumnos            # esta es otra forma


notas_primer_parcial = []
notas_segundo_parcial = []
promedios_parciales = []

for i in lista_alumnos: # Este for lo uso para la carga de datos
    # alumno = {}

    # nombre = input("Ingrese el nombre del alumno.")
    # alumno["nombre"] = nombre

    # while True:
    #     try:
    #         nota_primer_parcial = int(input("Ingrese la nota del primer parcial.\n"))
    #         alumno["nota_1"] = nota_primer_parcial
    #         while nota_primer_parcial < 1 or nota_primer_parcial > 10:
    #             nota_primer_parcial = int(input("La nota del primer parcial tiene que ser entre 1 y 10"))
    #             alumno["nota_1"] = nota_primer_parcial
    #         break
    #     except ValueError:
    #         print("ERROR. No es un numero")
    # notas_primer_parcial.append(nota_primer_parcial)

    # while True:
    #     try:
    #         nota_segundo_parcial = int(input("Ingrese la nota del segundo parcial.\n"))
    #         alumno["nota_2"] = nota_segundo_parcial
    #         while nota_segundo_parcial < 1 or nota_segundo_parcial > 10:
    #             nota_segundo_parcial = int(input("La nota del segundo parcial tiene que ser entre 1 y 10"))
    #             alumno["nota_2"] = nota_segundo_parcial
    #         break
    #     except ValueError:
    #         print("ERROR. No es un numero")
    # notas_segundo_parcial.append(nota_segundo_parcial)


    # promedio = (notas_primer_parcial[i] + notas_segundo_parcial[i]) / 2
    # promedios_parciales.append(promedio)
    # alumno["promedio"] = promedio
    lista_alumnos["promedio"] = lista_alumnos["nota_1"] + lista_alumnos["nota_2"] / 2
    
    # # Como en la variable promedio estoy trabajando ya con datos validados, puedo hacer la operacion dentro del append.
    # # y asi me ahorro la variable. Pero cualquiera de las dos estan bien.

    # lista.append(alumno)    # Lo ultimo que faltaria es agregarle el diccionario a la lista



# for alumno in lista:
#     print(alumno)




# print(" *** Listado de notas ***")
# print("------------------------------")
# print("NotaP1    NotaP2     Promedio")
# for i in range(len(notas_primer_parcial)):      # Puedo elegir la lista que sea, porque total, lo que yo quiero es tener una iteracion de la misma cantidad de veces que los elementos de la lista.
#     print(f" {notas_primer_parcial[i]:2d}           {notas_segundo_parcial[i]:2d}        {promedios_parciales[i]:5.2f}")


print(""" *** Listado de notas ***
-----------------------------------------
     Nombre     NotaP1      NotaP2      Promedio""")
for alumno in lista_alumnos:
    print(f" {alumno['nombre']:>10}         {alumno['nota_1']:2d}        {alumno['nota_2']:2d}       {alumno['promedio']:5.2f}")