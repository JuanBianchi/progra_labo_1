
print("Hola mundo")

# los comentarios en python se usan asi
# en python se usa la nomenclatura SNAKECASE

#sueldoBruto # camelCase

#SueldoBruto # PascalCase

sueldo_bruto = None # snake_case

# en python SI O SI tengo que asignarle un valor a la variable. Si quiero que una variable no tenga valor, le pongo None.

# tanto JS como PY son interpretados (Un lenguaje interpretado es un lenguaje de programación para el que la mayoría de sus implementaciones ejecuta las instrucciones directamente, sin una previa compilación del programa a instrucciones en lenguaje máquina. El código se lee linea por linea y se ejecuta linea por linea, a diferencia de los lenguajes compilados.), debilmente tipados (es decir, tienen tipos pero no hay que especificarlos como C por ejemplo).
# tambien tienen tipado dinámico (quiere decir que primero puedo declarar una variable y asignarle un numero y despues cambiarle el valor a "juan", por ejemplo. Se pueden guardar datos de distinto tipo en una variable).

#si yo quiero saber de que tipo es una variable en python uso la funcion type()

variable = 4

print(type(variable))

while(variable > 4):
    print("Estoy dentro del while")
     # En Pyhton, el while, if, for, etc. No llevan llaves de apertura y cierre. Le agrego al final del parentesis : y al apretar enter me deja escribir todo el codigo del bucle.
     # Para "cerrar" el if o while, etc. Simplemente escribo sin sangría.
print("Estoy fuera del while")

#Python no usa {} para designar bloques de código como otros lenguajes de programación, sino que
# usa bloques identados para indicar que un
# determinado bloque de código pertenece a por ejemplo un if.


if(variable > 5):
    print("Es mayor")
else:
    if(variable == 5):
        print("Es igual")
    else:
        print("Es menor")

# Otra forma de escribirlo usando else if seria asi

if(variable > 5):
    print("Es mayor")
elif(variable == 5):    # En python, else if se abrevia elif
    print("Es igual")
else:
    print("Es menor")


#En python, existen ciertas reglas "gramaticales" o formas de codear. El PEP (Python Enhancement Proposal)
#Este es un documento que proporciona informacion a la comunidad de Python, o que describe una nueva caracteristica

#El PEP8 Es un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible.
#desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener.

#Se recomienda limitar el tamaño de cada línea a 79 caracteres, para evitar tener que hacer scroll a
# la derecha.




#CLASE 2

#acumulador = 0

#while( acumulador <= 1000):
    #numero = input("Ingrese un numero.") #

    #numero = int(numero) #int es una función (igual al parseInt en JS) que convierte una cadena de caracteres a un entero.


#i = 10

#while( i < 20 ):

 #   i += 1
  #  print( i - 10)

#print("fin")

i = 1

while( i <= 10):

    print(i)
    i += 1

print("fin")

#Lo importante a saber de esta explicación es que en una variable de contro (bucle) necesito saber
#SI O SI
# -> variable de inicializacion y cuanto vale
# -> condicion
# -> el incremento de la variable de inicializacion

#El problema con el while, es que si quiero saber las 3 condiciones en un bloque de codigo de un while muy grande
# Tendria que scrollear para arriba y abajo para buscar todos los "elementos" del while

# Para esto existe el for 



#En python no existe el FOR como tal, si no que se llama FOR IN.
#
# Una coleccion de datos que tome los valores del 1 al 10
# Esto lo puedo hacer con la funcion range()

for i in range(10): 
    print(i)            #La palabra reservada pass sirve para rellenar el for, ya que si el for esta vacio me tira error. Es para que el interprete del lenguaje no proteste
                    # 

print("fin")
# De lo que le paso a range toma como limite inferior 0.

#Esta variable de contro for in, lo que hace es darle el valor a la variable, en este caso i, los valores del rango que me devuelve la funcion rango
#En este caso le pase 10, por lo que i va a tomar valores del 0 al 9.

#Entonces, lo que puedo hacer es ponerle, si quiero que me muestre una lista del 1 al 10, poner el valor inicial la izquierda del rango como 1
#Y el rango de la derecha lo aclaro como 11.

for numeros in range(1, 11):
    print(numeros)

print("fin")

#Tambien se puede usar el range para cadena de caracteres.

for nombres in range("Pedro", "Juan", "Martin"):
    print(nombres)

print("fin")


#Ahora vamos al caso del switch. En python no existia el switch como tal hasta una de las nuevas versiones
#Se escribe asi:

valor = 7

match valor:            #Se le llama match, ya que esta pensado de tal manera para que la variable, en este caso "valor", sea igual igual a alguno de los cases. 
    case 3:
        print("Tres")
    case 5:
        print("Cinco")
    case 7:
        print("Siete")
    case _:             #No existe el default, por convencion se usa _ . Pero puede ser cualquier nombre 
        print("Default")