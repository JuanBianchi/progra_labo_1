# VER CLASE GRABADA DESPUES. ME VOY A HACER EL TP xd

# Los objetos son formas de representar etidades.
# Un ejemplo de objeto que usamos para representar entidades eran los diccionarios, que eran
# un tipo de coleccion donde abriamos distintas llaves y definiamos distintas caracteristicas en el diccionario
# que correspondian a distintas entidades de un mismo grupo.
# Pero eso se hacia a nivel de representacion

# No es la manera correcta de trabajar con programacion orientada a objetos
# Nosotros podemos usar las listas de diccionarios, ya que el diccionario es una coleccion de elementos clave-valor 

# Un objeto tambien lo es, pero podemos verlo mas parecido a una "variable" compuesta
# En C, lo mas parecido a un objeto es una estructura de set, que era una variable contenedora de variables llamadas campo a los cuales les guardabamos alguna caracteristica y leugo accediamos a esos campos.

# Vamos a aprender a hacer nuestros propios objetos.

# Un objeto es una variable inventada por el programador, y va a tener que ver con las entidades que interactuan en el programa.
# Asi como existe el tipo de dato list, que tiene metodos, tiene una organizacion de los datos, los diccionarios, las tuplas y los sets son
# objetos que fueron inventados por un programador, haciendo la misma analogia a la coleccion de elementos usadas en los otros lenguajes (lo mismo que haciamos en el primer cuatri de C).

# Cuando vimos las funciones, filter, map, reduce, etc. Estabamos hablando del paradigma de la programación funcional.
# VER DE NUEVO ESA CLASE ALGUN DIA (LA 13)
# En los lenguajes con paradigma de orientacion a objetos, este paradigma trata de simular como interactuan las cosas en el mundo real.
# Por ejemplo, en la facultad o en un curso va a haber una lista de alumnos. En cada alumno va a haber una caracteristica que yo voy a querer recordar (atributos)
# Los atributos son los datos que yo quiero que mi programa recuerde. Y no todas las caracteriticas de los alumnos van a ser de interes para recordar en el contexto del programa que estemos realizando.
# Por ejemplo, si una caracteristica es el cuadro de futbol, al programa de la facultad no le va a interesar ese atributo.
# Todo lo que vamos a guardar en esa variable customizada va a tener que ver con el contexto del programa que estamos creando.

# Entonces, la idea va a ser que las caracteristicas que tienen los objetos en la vida real, nosotros vamos a realizar una tarea que se llama abstracción
# Nos tenemos que abstraer de la entidad como tal y tratar de generalizar cuales son las caracteristicas de todos los alumnos.
# Entonces como vamos a tener muchas entidades, la idea no va a ser escribir un diccionario a mano cargandolo con los datos de cada una. La idea es automatizar esa tarea.
# y usarla a través de lo que se llama una función constructora.

# La manera en la que se construye un objeto varía de lenguaje a lenguaje.
# Todos los objetos se crean en la memoria dinámica, el interprete analiza el espacio que ocupa el objeto, reserva espacio en la memoria dinámica, le asigna un espacio en memoria y nosotros al asignarle un = lo asignamos a una variable
# que nosotros la nombramos y ahi dentro se guarda la direccion de memoria del objeto que se construyo
# Y asi con las listas tambien, cuando creamos un literal de lista con los corchetes, el interprete reserva espacio para todo lo que contiene la lista y nos devuelve la direccion de memoria donde se construyo en la memoria dinamica

# La idea es crear una funcion que reciba los datos que queremos recordar en el programa y que la funcion reserve espacio en memoria para almacenar esos datos y que me devuelva la direccion de memoria donde estan almacenados.
# Y la definicion  de la variable donde vamos a guardar la direccion de memoria se llama "clase"
# Y su responsabilidad va a ser conseguir espacio en memoria para acomodar un conjunto de valores, de datos de una entidad.

# A las clases (que son definiciones de variables) las definimos una vez y la vamos a llamar como si fuera una funcion.
# Las clases tienen una funcion asociada que se ejecuta cada vez que queremos crear una variable de esa clase y una variable creada por una clase se conoce como objeto.
# Es decir, la "clase" seria como el molde, y todas las variables que creo con ese molde se conocen como objetos de esa clase.


