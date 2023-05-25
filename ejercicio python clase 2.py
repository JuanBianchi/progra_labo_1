

seguir = "si"

contador_participantes_femeninas = 0
acumulador_edades_femeninas = 0
cantidad_masculinos = 0

bandera_del_primero = True

edad_mas_joven = 0 #Esto de inicializar minimos (y/o maximos) NO SE HACE. En este caso lo hacemos porque python protesta

while seguir != "no":
    nombre_votante = input("Ingrese nombre: ")
    edad_votante = int(input("Ingrese su edad: "))
    while edad_votante < 13:
        edad_votante = int(input("Error. Reingrese su edad: "))
    #
    genero_votante = input("Ingrese su género, 'masculino', 'femenino' u 'otro' ")
    while genero_votante != "masculino" and genero_votante != "femenino" and genero_votante != "otro":
        genero_votante = input("Por favor, ingrese un genero correcto entre las opciones 'masculino', 'femenino' u 'otro'. ") 
        #asdas
    voto_votante = input("Ingrese su voto: 'Nacho', 'Julieta' o 'Marcos' ")
    while voto_votante != "Nacho" and voto_votante != "Julieta" and voto_votante != "Marcos":
        voto_votante = input("Por favor, ingrese a un votante que esté entre las opciones 'Nacho', 'Julieta' u 'Marcos'. ") 

    if genero_votante == "femenino":
        contador_participantes_femeninas += 1
        acumulador_edades_femeninas += edad_votante
    elif genero_votante == "masculino":
        if(edad_votante >= 25 and edad_votante <= 40) and voto_votante != "Marcos": 
            cantidad_masculinos += 1

    if voto_votante == "Nacho":
        if edad_votante < edad_mas_joven or bandera_del_primero:   #Aca, ponemos bandera_del_primero del lado derecho ya que solo va a ser condicion solo una vez en todo el ciclo de vida del programa
            edad_mas_joven = edad_votante
            nombre_mas_joven = nombre_votante
            bandera_del_primero = False


    seguir = input("Desea continuar? si/no")


if contador_participantes_femeninas > 0:
    promedio_edades_femeninas = acumulador_edades_femeninas/contador_participantes_femeninas
    print(f"El promedio de edad de las participantes femeninas es: {promedio_edades_femeninas}") #interpolado de variables. En python se usa f. En JS eñ $
    #print("El promedio de edad de las participantes femeninas es: {0}".format(promedio_edades_femeninas))
else:
    print("No se ingresaron votantes del genero femenino")

print(f"La cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta es: {cantidad_masculinos}")

if not bandera_del_primero:
    print(f"El nombre del mas joven que voto a Nacho es: {nombre_mas_joven}")
else:
    print("Nadie votó a Nacho")