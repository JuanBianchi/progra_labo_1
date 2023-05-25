#Es importante probar el programa mientras vamos programando de a poco, y no cuando este todo finalizado o con gran parte hecha


#seguir = "s"

# # print("Hola")


#while seguir == "s":

while True:
    try: 
        edad = int(input("Ingrese edad 18-65: "))
        if edad >= 18 and edad <= 65:           #<--Si no quiero validar una edad, lo que puedo hacer es sacarle el else a ese if, poner un else en el try except y ahi dentro un break para salir del while
            break
        else:
            print("Edad invalida")

    except ValueError:
        print("Eso no es un numero")



    #seguir = input("Desea continuar? s/n")

print(edad)

#En un programa pueden aparecer 3 tipos de errores.
#Errores de LOGICA: 
#Me doy cuenta cuando testeo el programa y este hace lo que quiere o no. El programa no se detiene, pero me muestra algo que no es deseado
#El resultado que me da, no es el resultado real o el que quiero
#La unica manera de corregirlo es con TESTING
#
#
#Errores de SINTAXIS
#Es escribir mal literalmente el codigo, como por ejemplo hacer mal la identacion, o escribir && en lugar de 'and'.
#
#
#Errores en TIEMPO DE EJECUCION
#Son errores en los que el codigo esta bien, pero en el momento en el que se esta ejecutando se detiene. Eso es un error que tiene que manejar si o si el programador 
#Este error es lo que se conoce como una excepcion
#Son errores que un programador no puede preveer que pasen.


#####PONER EN OTRO EJEMPLO
# valor = print("Ingrese un numero: ")

# try :
#     valor = int(valor)
    
# except ValueError: 
#     print("Trataste de convertir algo que no es un numero")

# else:
#     print(valor + 5)

# print = type((valor))


    #
    #
    #Para arreglar esto, nos dan la herramienta que se le conoce como EXCEPCION
    #
    #En programacion orientada a objetos, los objetos pueden lanzar unicamente DOS COSAS: los EVENTOS y las EXCEPCIONES
    #Cuando yo tengo un codigo susceptible de errores, tengo que lanzarlo en un bloque try except (en otros lenguajes se llama try catch)
    #En el except tengo que especificarle que tipo de error es el que va a lanzar el programa. Y con eso vamos haciendo excepciones a los errores que nos pueden surgir
    #
    #
    #
    #
    #
    #
    #
    #