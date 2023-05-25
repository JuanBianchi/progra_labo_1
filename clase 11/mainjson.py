import json

# Algo de formato json es un string

mascota_str = '{"id": 1, "nombre": "otto", "tipo": "perro", "edad": 2}'

#Tengo un objeto de tipo str que es muy parecido a un archivo json
# TODOS los lenguajes de programacion me ofrecen una funcion que me permite convertir un string en formato json a un objeto en memoria
# y un objeto en memoria a un string en formato json.
# En python el objeto que calza con un string en formato json es el diccionario.

print(type(mascota_str))
print(mascota_str)

mascota_dict = json.loads(mascota_str)      # Este metodo lo que hace es transformar un json (un string) en un objeto diccionario.

# Aca vamos a usar el metodo dump y dumps, junto con el load y loads. (Para acceder a estos metodos tengo que importar el modulo json)
# dump y load se utilizan cuando estoy leyendo desde un archivo en formato json.
# dumps y loads los uso cuando no lo estoy leyendo o trabajando desde un archivo, si no desde una cadena (como ahora).

print(type(mascota_dict))
print(mascota_dict)

print(mascota_dict["tipo"])
# La diferencia es que con un diccionario puedo usar cualquier metodo de diccionarios.
# Y como es diccionario, puedo agregarle mas campos, por ejemplo:
mascota_dict["vacunado"] = True
mascota_dict["duenio"] = None

# Ahora vamos a pasar mascota_dict a json con el metodo dumps()

mascota_cadena = json.dumps(mascota_dict, indent=2, separators=(","," : "))
print(type(mascota_cadena))
print(mascota_cadena)

# Ahora el string lo tengo de tipo json (string).
# Y como json es formato JavaScript Object Notation, el True sigue como booleano.
# Es un True pero esta vez en minuscula (en python se escribe la T en mayuscula y js no), porque es un objeto tipo JS.

# Pero si lo vuelvo a leer y lo vuelvo a convertir:
objeto_mascota = json.loads(mascota_cadena)
print(objeto_mascota) 
# El True vuelve a tener la T mayuscula, porque el metodo loads es de python.
# Por lo tanto, sabe transformar un string en formato json a un diccionario en lenguaje python.
# Entonces sabe que en json es true (en minuscula) y en python es True (maysucula) .

# Vamos a suponer que le agrego otro campo, en la linea 28
# Supongamos que yo quiero mostrar si esa mascota tiene dueño o aun no, con el None aclaro que no tiene.
# Cuando pase a formato json el diccionario, va a aparecer como null.

# Y todavia le puedo dar un formato mas "lindo", mas parecido a un archivo json. 
# Esto lo hago con la funcion dumps, que me da la posibilidad de pasarle una indentacion (el estandar en json es 2)
# Y puedo poner una bandera con separators=. Ya que el formato json tiene los : espaciados entre el la clave y el valor


# Este ejemplo nos muestra como podemos leer desde un string en formato json a objeto (diccionario) y de objeto de vuelta a string en formato json.
# con json loads y json dumps