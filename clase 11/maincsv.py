
# Aca voy a levantar el archivo csv y procesarlo de alguna manera.
# Lo que quiero hacer es pasar toda la informacion del csv a una lista (igual que en el stark)
# Como en el csv todos los elementos terminan con \n, tengo que sacarselos, como habiamos hecho antes.

# personas = []
# with open("DATA.csv", "r") as file:
#     for linea in file:
#         linea = linea.replace("\n", "").split(",")
#         print(linea)

# for persona in personas:
#     print(persona)


# Cuando hablamos de archivos, usamos los formatos de archivo para guardar texto, usamos los estandares CSV y JSON

#CSV
# Viene de un formato de tabla relacional.
# Donde en cada fila de la tabla tenemos los datos de una entidad. En este caso, en nuestro archivo DATA.csv en cada linea tenemos los valores de una persona
# Y despues en cada columna tenemos el valor de un atributo de esa entidad. Y a cada atributo los tendriamos separados por coma.

#JSON
# Es un estandar que es nacido de javascrpit y adoptado por otros lenguajes de programacion para la transferencia de datos. Por ejemplo para transferir informacion
# de un cliente a un servidor y viceversa.
# Un JSON es un string. Un dato de un objeto JSON es de tipo string.

# VER EXPLICACION DE LA DIRECCION DE MEMORIA

# La idea seria:
# No hay que confundir estos archivos con un archivo.py que es con lo que estuvimos trabajando hasta ahora. El archivo .py lo modularizabamos al importarlo
# al main. La principal diferencia es que un archivo .py, el interprete de python lo lee como código, lo lee como algo ejecutable.
# Lo que queremos hacer con los archivos csv y json (o archivos de texto plano), es tratar de hacer que el interprete de python los lea y podamos manipularlos a través del manejo de funciones de archivos.
# Es decir, abrimos un archivo con la funcion open, cargamos el archivo desde el disco rígido a la memoria, ese objeto archivo a traves de sus métodos (read, readlines, write, writelines) me permita leer el archivo en txt y me permita
# Usar esos string para armar diccionarios, listas de diccionarios o cualquier estructura de datos en memoria y poder trabajar con esa información.

# Entonces, habiamos dicho que tenemos la memoria RAM, donde tenemos la parte estática y dinámica. Y tambien el disco rígido donde está almacenado el archivo DATA.csv
# Lo que tengo que hacer es leer esa informacion contenida en el archivo .csv y llevarla a la memoria dinámica. 
# Con la funcion open yo le voy a decir que archivo tiene que ir a levantar, le paso el directorio donde esta el archivo y por segundo parametro el modo de apertura del archivo
# RECORDAR QUE POR DEFAULT (si no le paso nada) EL MODO ES r de read.
# Entonces, lo que hace la funcion open() es ir a buscar el archivo al disco rígido, lo "mide" y reserva espacio en la memoria dinámica donde va a copiar lo contenido en el archivo.
# Crea un objeto de tipo TextiOwrapper que sabe toda la informacion del archivo (como se llama, donde esta, que modo de apertura, etc.) y ademas tiene un conjunto de métodos que me permite trabajar con ese archivo en memoria.
# Entonces, la funcion open() me devuelve una direccion de memoria de ese objeto y yo la estoy guardando en la variable que se llama file.
# 
# Una vez que el archivo esta abierto, lo que tenemos que hacer es leerlo. Ya que es un archivo de texto, lo que yo leo es un string. 
# Entonces, con el metodo read() yo hago que me lea todo lo que esta contenido en el archivo, el metodo me reserva una direccion de memoria donde almacena todo lo contenido en el archivo, en tipo str
# y me devuelve la direccion de memoria donde esta esa "copia" del texto del archivo y la guardo en una variable.
# Y cuando se cierra el archivo, la direccion de memoria donde estaba abierto el archivo se borra (se lo lleva el garbage collector) y me queda la variable guardada que use con el metodo read()

# PERO, hay que tener claro que eso ya no tiene nada que ver con el archivo, el archivo era mas bien como un contenedor. Ej. botella de coca cola.

with open("DATA.csv", "r") as file:
    contenido = file.read()


print(file.closed)  # La propiedad closed me informa si el archivo sigue abierto (con False) o si ya esta cerrado (con True)
print(contenido)

# La diferencia del read() con el write() (o writelines()), es que el write hace lo opuesto a lo que hace el read.
# Reserva espacio en memoria para lo que querramos escribir o agregar, y cuando se cierra el archivo lo vuelca en el archivo contenido en el disco rígido.

# Volviendo a la explicacion principal, entonces, cuando guardamos el contenido del archivo en una variable, ahora lo tenemos en tipo str. Lo que hay guardado es un gran string.
# Si imprimimos en la consola el contenido de la variable, nos lo va a mostrar, pero aunque no lo veamos tiene el \n y todo. 
# Entonces con los metodos de strings o las expresiones regulares ( que son los metodos de strings pero en esteroides ) hay que formatearlos y sacarselos.
# Como lo vamos a hacer? A traves de parseos.
# Un parseo es un analisis semantico de una cadena de caracteres. Recorrer una cadena de caracteres haciendo una conversion de eso.
# 
# La idea es que un archivo de texto CSV se convierta en memoria en una lista de diccionarios. Es decir, que el DATA.csv sea una lista y que cada linea sea un diccionario.
# Lo unico que vamos a tener que hacer a mano son las claves.

# Esto se puede hacer de dos maneras.
# Una es cuando ya tengo todo ese gran string en una variable (en este caso contenido, ya que el metodo read() me lee de una todo el archivo y me devuelve un string)
# Como la variable contenido guarda un objeto de tipo string, puedo acceder a los metodos de tipo string.


lista = contenido.split("\n")   # El metodo split me devuelve una lista de strings, por lo que no necesito declarar una lista vacia. 
                                # Simplemente lo guardo en una variable llamada lista
                                # Lo que va a hacer split es va a agarrar ese gran string que tengo en contenido y cada vez que encuentra un \n, todo lo que este a la izquierda del \n lo guarda como elemento de la lista.
                                # Le paso el caracter que separa los renglones, que es el \n

print(lista)
# Si nos fijamos, ahora cada elemento esta como una cadena (en comillas simples) y cada elemento esta separado por una coma, pero no hay que confundirla con
# la coma que sirve como separador de datos dentro de la cadena.
# Al final de todo hay un elemento que es una cadena vacía. Por qué? Porque al final del ultimo elemento quedó como que hay un \n que salta a la linea de abajo que no hay nada.
# Si yo la borro y dejo el cursor adelante del ultimo caracter de la ultima linea, desaparece.
# Esto pasa porque cuando generamos automaticamente un archivo, la maquina no lo hace para que sea manipulado por una persona, lo hace
# para que pueda ser abierto, leido y cerrado, no es para que se ande modificando.

# Ya tenemos nuestra cadena parseada y en una lista, donde cada elemento de esa lista es una linea del archivo.
# Puedo iterar la lista, donde en cada iteracion, el valor que toma el objeto, en este caso persona, es un string:

lista_personas = []

for persona in lista:
    p = persona.split(",")      # Aca, p seria una lista retornada por la funcion split, que en este caso me separa los valores.
    dic_persona = {}
    dic_persona['id'] = int(p[0])   # Ya que voy a tratar al id como entero, lo parseo.
    dic_persona['nombre'] = p[1]
    dic_persona['apellido'] = p[2]
    dic_persona['email'] = p[3]
    dic_persona['genero'] = p[4]
    dic_persona['edad'] = int(p[5])
    lista_personas.append(dic_persona)    
    
for elemento in lista_personas:
    print(elemento)

# Ahora cada elemento de la lista es una lista que contiene los valores separador por elemento.
# Y ahora se en que indice esta cada campo. En el 0 esta el 'id', en el 1 esta el 'nombre', en el '2' el apellido, en el 3 el 'email', etc.
# Entonces, puedo crear un diccionario adentro del for para que en cada iteracion me lo genere de nuevo, y dentro del diccionario voy generando las claves y guardandole los valores.
# Ahora, puedo crear una lista nueva donde voy a guardarle todos los diccionarios con las claves generadas y sus valores
