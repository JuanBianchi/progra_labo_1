
# Para definir una clase usamos la palabra reservada class y despues el nombre de la clase.
# El nombre de la clase generalmente es un sustantivo
# Se escribe usando la nomenclatura de PascalCase

# Dentro de las clases vamos a poder definir variables y funciones.
# Cuando una variable esta declarada dentro de una clase se llama ATRIBUTO de una instancia (objeto)
# Se lo llama asi para diferenciarlo de las variables que estan en el scope global

# La clase es la plantilla o molde y las instancias son las variables 
# Cuando reservo espacio en memoria para los atributos y los metodos, esos son objetos.
# Yo puedo tener la clase persona e instanciar (construir, pedir espacio en memoria para esos objetos).
# Una clase tiene un metodo constructor, un metodo es cuando defino una funcion dentro de una clase.
# Existen metodos que podemos definir nosotrosm y otros que existen para todos los objetos.

# El metodo constructor en python se escribe __init__ y el nombre del metodo
# Entonces, cuando creo el metodo, tengo que pensar cuales son los datos que quiero que mi programa recuerde.
# Los escribo entre parentesis de la funcion para que lleguen como parametro

# El self en python es como el this en otros lenguajes. Self es una direccion de memoria.
# Cuando creo un objeto en python, se almacena en una direccion de memoria, que por lo general guardo en una variable.
# Self es el objeto que me permite saber la direccion de memoria dentro de mi clase y fuera.
# Si a mi clase se la asigno a una variable global, esa variable va a guardar self.
# Es decir, self se apunta a el mismo, y se puede guardar en otras variables.
# init es mi funcion constructora, donde la va a construir? En self, y donde se van a guardar los atributos de mi funcion? En self

# Entonces, lo que vamos a hacer a continuacion es crear las variables para guardar lo que recibe por parametro mi funcion constructora.
# usamos self.nombre_variable, y esa variable la estamos declarando en la memoria dinamica, en self.
# Hago lo mismo para todos los parametros y ahi ya tengo una funcion constructora que me permite recordar los atributos.

# Como llamo a la funcion? Con el nombre de la clase y los parentesis, donde le voy a pasar los datos que se necesitan para crear a la persona.
# sin tener en cuenta a self.

# VER DESPUES EXPLICACION DE PORQUE USAMOS ESTO, DESDE QUE SE FUE EL PROFE HASTA MINUTO 57

# Tambien a una clase puedo agregarle funciones (o sea metodos) que no sean la de init o funcion constructora, puedo hacerlo para que mi clase sea especial para algo
# Es importante que cada metodo que le agregue a mi clase le pase como parametro self, porque asi puedo trabajar con los campos que estan en mi funcion constructora, ya que de otra manera tendria que pasarle por parametro
# todos los campos y no se deberia hacer asi.
# Es lo mismo que hago desde afuera para acceder a la variable dentro de un campo.

class Persona:

    def __init__(self, id, nombre, apellido, edad, email) -> None:
        self.id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self._email = email

    # EJEMPLO DE SETER (PROTECCION)
    def set_edad(self, value):
        if value > 0 and value < 100:
            self.__edad = value
    
    # EJEMPLO DE GETER
    def get_edad(self):
        return self.__edad

    def set_nombre(self, value: str):
        # Aca se valida que value sea str, que no tenga caracteres numericos con regex, etc.
        self.__nombre = value.capitalize()

    def set_apellido(self, value: str):
        self.__apellido = value.capitalize()

    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    def presentarse(self):
        print(f"hola, me llamo {self.__nombre} y tengo {self.__edad} años")

per1 = Persona(10, "jose", "lopez", 50, "joselopez43@hotmail.com")

print(per1)     # Me devuelve la direccion de la la clase (self)

print(type(per1))   # Me devuelve que la variable per1 es de tipo Persona


# Si quiero acceder a un campo dentro de mi funcion constructora, lo hago con el operador .
# Con eso accedo a los atributos de la instancia con el operador .
#print(per1.nombre)

# Y ahora que tengo mi funcion constructora, puedo crear las instancias que quiera
per2 = Persona(20, "Mariana", "Suarez", 21, "marian@gmail.com")
#per3 = Persona(26, "Pablo", "Echeverri", 23)
#per4 = Persona(32, "Lionel", "Perez", 22)

# print(per2.nombre)
# print(per3.nombre)
# print(per4.nombre)

# Por que con el . accedo a los campos? Porque es como escribir self.campo
# Como per1/2/3/4 guardan self, es como escribir self.

# Lo que pasa cada vez que creo per2/3/4, es que se crea un nuevo self que va a contener los campos, y esos campos guardan la direccion de memoria
# de los objetos que fueron creados en otra parte de la direccion de memoria y que contienen los datos de la persona.
# Pensarlo como una cajita feliz de mcdonalds, adentro de la cajita tengo los atributos (hamburguesa, papas, gaseosa) y si quiero otro almuerzo con otras comidas
# pido otra cajita con otros atributos
# Es lo mismo que haciamos con los diccionarios, guardabamos valores de una misma entidad y accediamos a esos valores con las keys.
# Aca lo hacemos con el operador .

# per1.presentarse()
# per2.presentarse()

# Aca es importante saber que la variable donde guardo los datos de un objeto, guarda la direccion de memoria de donde esta construido ese objeto con el dato
# Lo que guardo en per1/2/3 es la ubicacion de ese grupo de direcciones de memoria de los objetos

# Cuando estoy definiendo una clase podria proteger los datos de mis variables.
# Yo podria acceder a un campo a traves de per1 por ejemplo y asignarle un valor al objeto edad.

per1.edad = -23
print(per1.edad)
per1.presentarse()

# La idea es que el programador no pueda acceder a un atributo por fuera de la clase.
# Sino que lo haga atraves de una instancia que se encargue de validar ese dato que ingresa.
# Lo podemos hacer a traves de una funcion (instancia) que setee el valor, lo valida y ella misma hace la asignacion
# y cuando alguien quiera leer el valor, tener una funcion que me de (retorne) ese dato, en lugar de acceder a el con el operador .

# Esto tiene que ver un poco con el paradigma de orientacion a objetos que se llama encapsulamiento.
# Pero si yo lo dejo asi como esta, por mas que tenga un setter o getter, va a pasar el problema igual.

# Igualmente python ya me permite proteger los elementos, usando __ doble guion bajo en el nombre del objeto que quiero proteger.
# Esto lo que hace es que me "establece" el objeto privado. 
# Esto quiere decir que por fuera de la instancia y clase, yo no puedo acceder ni saber que existe ese objeto, es invisible por fuera de la instancia y la clase y no puedo tener acceso.
# Y esto funciona por mas que yo intente acceder por fuera de la clasee haciendo __edad = -42, me va a decir que no existe

# Lo mismo si yo intento asignarle un valor que esta dentro del rango del setter, ya que no me estaría dejando mostrar el valor real porque el objeto sigue protegido.
# Yo no estoy pudiendo acceder de ninguna manera, le asigne un valor correcto o incorrecto, lo puedo acceder si le cambio el parametro cuando llamo a la instancia

# Si yo hago lo mismo que antes pero intentando acceder con per1.__edad, lo que estaria haciendo es crear un atributo nuevo a la clase

# De todas formas, esto no lo vamos a usar el resto de la cursada, solo vemos que asi se trabaja con los setter y los geter.

# Cuando tenemos un atributo en una clase, con el __ lo que hacemos es que sea inaccesible para el exterior.


# Tambien hay atributos que se llaman "protegidos"
# HERENCIA
# Yo tengo una clase padre generica "personas" que tiene un id, nombre, apellido, etc. Y aveces voy a tener otras clases que comparten los mismos atributos.
# Y si despues tengo otras clases como por ejemplo "alumnos" y "profesores". A veces, los atributos de personas se comparten entre alumnos y profesores.
# Pero no significa que van a tener exactamente los mismos atributos, un profesor puede tener atributos como sueldo, un array de materias, etc. que los alumnos no tienen y viceversa.
# Cuando tenemos esa situacion, se genera como una jerarquia de clases, y para no tener que escribir de nuevo los mismos atributos y metodos en cada clase, vamos a tener un concepto de herencia.

# Los atributos y los métodos tienen 3 niveles de visibilidad:
# -pública: se pueden acceder libremente desde el exterior
# -privada: solamente son para usar dentro de esa clase, no se acceden desde ni el exterior ni desde otra clase
# -protegido: puede ser accedido desde otras clases herederas pero no desde el exterior.
                # El atributo protegido en python no funciona como corresponde, se le pone al nombre del atributo _ un solo guion bajo, pero en realidad sigue quedando visible para el exterior.
                # Con getter y setter puede ser modificado desde el exterior, es lo que deberia usar el programador, pero el _ es mas una convencion. Si el programador quiere, puede acceder desde el exterior, solo le avisamos como deberia usarlo.

# La importancia de los seter y los geter radica en que en ellos podemos usarlos para validar y formatear los datos de ser necesario.
per1.presentarse()
per1.set_nombre("mario")
per1.presentarse()
print(per1.get_nombre_completo())

# VER ULTIMA HORA. A PARTIR DE 2:26:30