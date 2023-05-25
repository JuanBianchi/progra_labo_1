# Expresiones regulares.
# En todos los lenguajes, cuando tenemos que hacer alguna busqueda en algun texto, existen las 
# expresiones regulares.
# como por ejemplo si queremos validar un email, una patente de auto.

# Hay alguna manera de buscar algun patron que me permita validar esa cadena de texto?
# La mas comun es usando expresiones regulares.

# en python hay que importar un modulo llamado re (regular expression)
# 

import re

texto = "Esto es una frase para usar de modelo en la explicacion de expresiones regulares"

retorno = re.search("z", texto, re.IGNORECASE)

print(retorno)
# En principio este metodo necesita un patron a buscar y una cadena de texto.
# patron y cadena son de tipo string.

# Supongamos que donde esta patron, le paso que busque la letra "o", nos retorna un objeto de tipo match.
# en match aparece lo que consiguio, en este caso encontro una "o" (por que lo mande a buscar)
# y el span, el primer numero me indica en que posicion la encontro y el segundo en donde terminó.

# Si le mando a search que busque algo que no esta en el texto, en este ejemplo una z, me va a devolver un None.
# Ese None lo puedo usar como falsy (booleano)

# if (retorno):
#     print("Encontro la letra")
# else:
#     print("No encontro la letra")

if retorno:
    print(retorno.group())

# Con el metodo group tengo que tener cuidado, ya que si no encuentra lo que mando a buscar

# El metodo start y end me dicen la ubicacion de donde empieza y termina el objeto a buscar 

# El metodo span me devuelve una tupla con la ubicacion de donde empieza y donde termina

# El metodo findall me devuelve una lista con todos los objetos que encontro. Si le mando a buscar una 'o', me devuelve una lista con la cantidad de 'o' que 
# hay en la cadena
# si le mando algo que no esta en el texto, me devuelve una lista vacia.


# Tambien le puedo pasar un tercer parametro. Por ejemplo, usando re.IGNORECASE (que hace que no se fije en las mayusculas)


# el search, funciona con estados, un estado inicial y un estado final.
# si hay que buscar dos caracteres, por ejemplo "io", primero busca una i, si no hay, vuelve a empezar. Si la encuentra, pasa al siguiente estado que es una "o".
# Si lo que esta despues de la i no es una o, empieza a buscar de nuevo.
# Es decir, funciona con estados, uno inicial, uno secundario (terciario y asi sucesivamente...) y uno final.
# Cuando llega al estado final, me devuelve el match.


# Con las llaves de apertura y cierre {} puedo especificar cuantas ocurrencias seguidas del elemento a buscar.
# Si le paso para que busque una i{3}, esto significa que me busque 3 i seguidas y me los devuelva.
# Tambien puedo separar por coma dentro de las llaves para armar un "rango" de busqueda, por ejemplo i{1,4}, me dice que busque entre 1 y 4 i.

# Con el operador * que significa "nada" o "todo".
# Esto quiere decir que me va a devolver todo lo que no hay antes del elemento a buscar y todos los elementos a buscar. 

# Con el operador + significa 1 o mas elementos, sin limite.

# Con el acento circunflejo, le indico que me devuelva algo que empiece con el elemento que le pasé.
# Si uso el acento circunflejo dentro de un rango, por ejemplo de numeros, lo uso para "discriminar". Es decir, que me devuelva todo menos lo que hay en ese rango.

# Si yo tengo una cadena de texto multilinea, puedo usar la bandera re.MULTILINE para buscar y analizar linea por linea que este el elemento y me lo devuelva.

# Con el simbolo de pesos, me devuelve lo que termine con el elemento a buscar. Solo que a diferencia de los anteriores, lo especifico al final del elemento. elemento$

# Tambien, como elemento puedo especificar un rango, por ejemplo de la "a" a la "z". Asi: [a-z]

# Si pongo [eo], por ejemplo. No me va a devolver "eo" como antes, sino todas las "e" y todas las "o" que hayan

# Si pongo \s, me devuelve todos los epacios en blanco y saltos de linea.
# Si pongo \S en mayuscula, me devuelve todo lo que NO sea un espacio

# El \d me devuelve todo lo que sea numeros.
# El \D me devuelve todo lo que NO sean numeros.
# Si hago \d{2} le indico que me arme grupos de dos numeros, los primeros que encuentre.

# El \b (limite de palabra)

# Los parentesis significa, de lo que me vas a devolver, filtrame lo que que te paso.

email = "juanperez@hotmail.com otroemail@gmail.com.ar"

retorno2 = re.findall("@[^ ]*", email)
# con esto le estoy dicendo, despues del arroba traeme todo MENOS el espacio.
print(retorno2)



# Existe tambien la funcion split. Le pasamos el patron y el texto y me devuelve lo que le pase pero cortado por el patron que le paso.
# Es decir, devuelve todo menos la ocurrencia del patron.
# Y como tercer parametro, le puedo pasar la cantidad de veces que quiero que use el patron como separador
retorno3 = re.split("mail", email, 2)
print(retorno3)

# Tengo otra funcion que es sub. Donde encuentre una ocurrencia de un patron, lo reemplazo por el elemento o patron que le pase como segundo parametro

retorno4 = re.sub("@", "arroba", email)
print(retorno4) 


# el re.search sirve para buscar si esta el patron o no. Me puede servir para validaciones.
# el findall me devuelve una lista con todas las ocurrencias del patron enviado por parametro.
# el re.split me devuelve una lista con los elementos de la lista sin el separador (el patron que le mando como primer parametro)
# el re.sub me devuelve un string. Reemplaza el patron de una re por otro string.

