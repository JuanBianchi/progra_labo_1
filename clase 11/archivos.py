# Toda la informacon que usamos hasta ahora esta guardada en memoria.
# Por ejemplo, el archivo stark que tiene una lista de diccionarios. Nosotros lo importamos de un modulo y lo usabamos
# como una variable.
# Pero no lo estamos leyendo como un archivo guardado en el disco rigido.


# Cuando hablamos a nivel de como se guarda la informacion en un archivo
# Tenemos 2 tipos de archivo:

#Archivos de texto 
# Cuando decimos que vamos a guardar un archivo de texto plano (como .txt, .html, .py, .js, etc.), que sea de texto plano significa que es de texto.
# Que si yo lo abro con un editor de textos (ej. bloc de notas) lo que se va a encontrar es con una tira de 0 y 1 del tamaño del archivo.
# 01110111|01110110|00101010|101100
#   H           O       L       A 
# Lo que hace el editor de texto es, como sabe que el tamaño de un caracter es un byte, y 1 byte son 8 bits, lo corta cada byte. 
# Entonces, cada byte es la representacion de un caracter en codigo ascii y lo va traduciendo.

#Archivos binarios
# No se refiere a que esta guardado en 0 y 1 y los de texto no.
# La informacion se guarda exactamente igual a como se guarda en memoria.
# Si yo tengo un numero en complemento A2, en memoria voy a tener esa representacion de 0 y 1.
#
# Si quiero guardar en un archivo binario:
# id: 12345 nombre: juan altura 1.70 edad 24
# De todo lo que es texto, guardo el codigo ascii, y de los numeros guardo la representacion de 0 y 1 en complemento A2 de cada grupo de numeros, y para los flotantes en IEEE754.


# Cuando los ingenieros tuvieron que pensar como guardar los diferentes tipos de datos (texto, numeros enteros, con decimales, colores, imagenes, sonidos, etc.) y todos esos tipos de 
# datos tienen que ser representados en 0 y 1.
# Cuando tenemos que guardar caracteres, a traves del codigo ASCII tenemos la representación numérica de ese caracter
# Por ejemplo, la "a" tiene el 65. Entonces se guardan los 0 y 1 que representan el 65.
# Si tengo un numero con signo, se usa el sistema complemento A2, esa representacion de transistores abiertos y cerrados (0 y 1), en el archivo va a tener esa misma representacion de 0 y 1.
# Es decir, cada vez que se guarda un dato, se guarda en una representacion.
# Si queremos guardar un color, el sistema RGB guarda un byte de rojo, un byte de azul y un byte de verde para que representen ese color.

# Si quiero leer un archivo binario, no lo puedo leer con un programa que solo sirva para leer archivos de texto, tengo que abrirlo con un programa que me permita
# leer el tipo de archivo correspondiente.
# Es por eso que es importante a cada archivo ponerle la extension cuando lo guardamos, para saber que tipo de archivo es y que programa tiene que abrirlo.

# Los archivos de texto plano, en cambio, si puedo leerlos con cualquier programa.

# Es decir, si el archivo no es 100% ascii (todo con caracteres de texto), es binario y no lo puedo leer con cualquier programa.





