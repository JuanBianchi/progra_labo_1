
variable = "123"

print(variable.isdigit())   #Es igual al otro ejemplo pero con isdigit, sin exception
                            #

while True:
    edad = input("Ingrese una edad, 18-65: ")
    if edad.isdigit():
        edad = int(edad)
        if edad >= 18 and edad <= 65:
            break
        else:
            print("Edad invalida")
    else:
        print("Eso no es un numero")

