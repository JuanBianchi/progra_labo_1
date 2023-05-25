import re

# La funcion open me permite abrir archivos, y el nombre del archivo lo paso por parametro.
# Pero tambien tengo que pasarle la direccion, si no esta en la misma carpeta. Para eso uso el path
# El path puede ser relativo o absoluto.
# Un path absoluto es todo el camino que tengo que hacer desde 0, desde el nivel inicial, que seria C: (o la unidad de almacenamiento)
# Por eso si le doy clic derecho al archivo que quiero traer, me muestra para copiar la ruta de acceso tanto absoluta como relativa.


file = open("C:\\Users\\juamp\\OneDrive\\Escritorio\\Clases 1G cuatri 2023\\Clases\\clase 11\\prueba.txt", "r")
print(file)
# C:\Users\juamp\OneDrive\Escritorio\Clases 1G cuatri 2023\Clases\clase 11\prueba.txt

# prueba.txt # Esta es la ruta relativa, y en este caso me copia solo el nombre y extension del archivo ya que la raiz de este llamado es el mismo de donde esta el archivo.
# Por eso es relativo, relativo a donde estoy.


# Al igual que en C, a la funcion open le pasamos el nombre del archivo y el modo de apertura.
# En python, si no lo especifico, el modo de apertura por defecto es R. 
# Modo R es de read(lectura). Pero es mejor escribirlo.

# De todos los que hay, vamos a darle bola a 3:
# Modo r, lectura de texto
# Modo w, escritrura de texto   (esto es una operacion destructiva, lo empieza desde 0)
# Modo rb, lectura de archivo binario
# Modo wb, escritura de archivo binario
# Modo a (viene de append), escritura pero para agregar contenido al archivo.


# Si yo abro un archivo en modo lectura (r), me devuelve una direccion de memoria.
# Porque abrir un archivo en modo lectura (que existe), es decirle al sistema operativo que agarre el archivo en el disco rigido y lo cargue en memoria (en la RAM).
#  Entonces, en C cuando abrimos un archivo y lo leemos, el interprete lee lo que esta en el disco, lo carga en memoria.

# Si ejecuto el codigo, y no tira error, ya lo tenemos abierto (guardado en file).
# Ahora puedo hacer diferentes cosas con el archivo.
# La manera mas "inteligente" de trabajar con un archivo es:
# Lo abro.
# Lo leo / Lo escribo.
# Lo cierro.

# Ya que hay riesgos de que el archivo se corrompa y no sirva despues.
# Entonces, en el momento que le hago el open, de una le clavo el close() y escribo en el medio

# contenido = file.readlines() # Lo que hace read es devolverme un string, ese string va a ser todo lo que tenga en el archivo.
                        # Si yo a read no le pongo nada, lee todo el contenido. Si le pongo un numero, lee esa cantidad de caracteres.

print(file.readline())          # Si al archivo le agrego mas lineas de texo, me lo muestra literlamente con los \n.
                                # Con el readline, me muestra hasta el primer \n
# file.close()

                        # Tambien existe readline, que solo lee la primera linea, es decir, hasta el primer \n
                        # Cada vez que llamo a readline, lee una nueva linea, la siguiente.

# print(contenido)      # El print por defecto finaliza con un salto de linea, entonces, con el segundo parametro le digo como quiero que termine, con un espacio en blanco.
                        # Ya que en el archivo ya hay un salto de linea. 

                        
                        # Existe la funcion readlines. Que me devuelve una lista con los strings como elementos de ella.
                        # Pero tambien me guarda y muestra los \n que representarian los saltos de linea


# Hay una forma mas facil de abrir un archivo sin la necesidad de cerrarlo explicitamente con el close.
# Esto se hace de la siguiente manera:

with open("C:\\Users\\juamp\\OneDrive\\Escritorio\\Clases 1G cuatri 2023\\Clases\\clase 11\\prueba.txt", "r") as file:
    contenido = file.readlines()

# Es exactamente lo mismo a como lo hicimos antes pero mas corto.

# Como readlines me devuelve una lista de lineas, la puedo iterar para obtener cada elemento.
for linea in contenido:
    print(linea, end = '')


# Y puedo hacerlo mas corto todavia! 
# file es un objeto iterable, entonces puedo hacer:

patron = re.compile("\n")

with open("C:\\Users\\juamp\\OneDrive\\Escritorio\\Clases 1G cuatri 2023\\Clases\\clase 11\\prueba.txt", "r") as file:
    lista = []
    for linea in file:
        lista.append(linea.replace("\n", ""))

print(lista)

# La diferencia es que aca no tengo una lista de strings con las lineas, si no que tengo las lineas directamente. (sin saltos de linea, etc.)
# Si lo quiero volver a pasar a lista, puedo crear una vacia y usar el metodo append para agregarle las lineas en cada iteracion. (Esto para tener el mismo efecto que el readlines)
# Pero, tengo que sacarles el \n. Hay muchas formas de hacerlo, puedo usar regex con sub, metodos de strings como el strip, el metodo replace, usando split, etc.
# Yo lo voy a hacer con replace pero reemplazandolo con "". 
# Y ahora puedo imprimirlo sin problemas, sin usar el end como segundo parametro.

# Si lo quiero hacer con regex, puedo hacerlo de la manera en la linea 78.
# re.compile. Yo puedo hacer una compilacion de una expresion regular.
# Hay dos maneras de trabajar con expresiones regulares, como ya vimos en la clase de regex a nivel modulo (usando search, findall, match, etc.)
# Y la otra manera es compilando un patron como en la linea 80. Entonces, yo puedo usar la variable patron para llamar al metodo sub y compararlo con el string.
# En este caso, como lo que quiero es comparar el patron compilado con la linea para buscar si hay coincidencias, uso el metodo sub en patron y le paso la linea.
# Pero lo probe y no sirve asi que no le doy bola a eso (?)


# Volviendo a lo de las regex, lo bueno de compilar los patrones es que los puedo tener guardados y reutilizarlos para realizar validaciones y comparaciones, por ejemplo:

patron_patente_nueva = re.compile("[A-Z]{2}\d{3}[A-Z]{2}")

if patron_patente_nueva.search("AS123CV"):
    print("Es valido")
else:
    print("Es invalido")


# Hay otro metodo que puede sernos util, el tell(). Este metodo nos dice en que posicion se encuentra el cursor en el archivo
# Por ejemplo.

with open("prueba.txt", "r") as file:
    posicion = file.tell()
    print(posicion)
    print(file.read(5))
    posicion = file.tell()
    print(posicion)

# El primer posicion (tell) me va a decir que estoy en la posicion 0, ya que no di ninguna orden de lectura ni nada.
# Entonces, si le digo a file que lea 5 caracteres, va a mover el cursor esa cantidad de caracteres.
# Si vuelvo a llamar a tell despues de eso, me va a mostrar la posicion en la que se encuentra el cursor despues de haber leido 

# Existe el metodo seek, que lo que hace es mover el cursor las posiciones que le indique por los parentesis pero sin leer los caracteres.
# Es decir, sirve para posicionar el cursor en algun lugar del archivo.

with open("prueba.txt", "r") as file:
    posicion = file.seek(6)
    print(file.read(3))




# De todos los datos que estan en mockaroo, vamos a usar los datos separados por comas (CSV) y el formato JSON
# JSON es un formato de string, y es lo que normalmente se usa cuando nos conectamos a una API para envio de comunicacion de datos
# de un cliente a un servidor y viceversa.

# El CSV viene del mundo de las tablas, puede tener una analogía con el mundo relacional de las bases de datos relacional.
# en donde si tenemos una cadena de caracteres, le tenemos que poner un caracter separador.

# Si nos fijamos, en el archivo JSON tengo un array de diccionarios (pero no es una lista de diccionarios, es un gran str).
# En el CSV son lineas (strings separados por \n) pero en vez de tener claves, cada informacion se separa en coma.
# Hay que imaginarselo como tabla.