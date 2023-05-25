# Ya vimos como levantar un archivo.
# Si yo quisiera escribir en un archivo, la operatoria es casi siempre la misma.

lista = ["esto es un archivo de texto plano\n",
"esto es otra linea\n",
"alcoyana alcoyana\n",
"no me pidan imaginacion un viernes a esta hora\n",
"estoy quemado\n"]

file = open("probando.txt", "w") # La w es modo escritura

file.writelines(lista)

file.close()


# Pero que pasa si yo abro de nuevo el archivo? Ya sea para hacer otra escritura distinta o para ver que pasa si lo abro en modo escritura.
# Lo que estaba escrito antes se destruyó, quedo el archivo pero sin contenido.
# El modo escritura (w) destruye el contenido del archivo.

# Puedo saber si un archivo existe abriendolo sin que se destruya con el modo "a".
# El modo a tambien lo que tiene es que si no existe el archivo y quiero abrir un archivo con ese modo, lo crea y lo escribe.
# Pero si el archivo ya existe, va a escribir a continuacion de donde quedo el cursor, y a veces no queremos eso.

# Lo que se suele hacer para saber si un archivo ya existe sin destruir su contenido es abrirlo primero en modo lectura.
# Entonces, si al ejecutar en modo lectura me devuelve algo, el archivo existe, si me tira error no.

# Y asi como tenemos el write, tambien esta el writelines, que es lo opuesto a readlines.
# Si yo tuviera una lista de strings, asi como el readlines me lee todas las lineas y me las agrega a una lista de strings
# si yo ya tengo hecha una lista de strings y la quiero escribir, puedo usar writelines.

# Entonces paso de la lista  un string completo, si no le pongo los \n o saltos de espacio

# Con readlines leo todas las lineas y las devuelve en una lista donde cada elemento es una cadena, 
# Si yo ya tengo esa lista y la quiero guardar en archivo, en lugar de hacer write write write uso writelines.