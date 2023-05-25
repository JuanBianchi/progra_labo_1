import json

# La idea es hacer lo mismo que hicimos con el archivo CSV pero con el archivo JSON
# Poder leer y parsear un archivo de texto en formato JSON y terminar convirtiendo esta informacion en una lista de diccionarios.

with open("DATA.json", "r") as file:
    lista = json.load(file)['personas']       # Usabamos loads para convertir a string. Pero con load (sin la s) yo le paso el file y automaticamente
                                              # si el file esta en formato json me lo va a leer de una.
    print(lista)
    # load() me devuelve un diccionario.
    # En este caso, lista es un diccionario con una única clave ('personas') cuyo valor es una lista de diccionarios con personas.
    # Entonces, yo puedo decirle que me devuelva esa única clave 'personas' para que me traiga solo la lista de diccionarios.
    # Y luego itero esa lista de diccionarios para obtener cada diccionario

for persona in lista:
    print(persona)


# Y asi nos queda igual al csv.



# Ahora queda hacer lo contrario, si tenemos una lista de objetos (diccionarios) hay que guardarlos en formato json.
# Con la funcion dump() manda la lista de una.
# VER MAINCSV_ALTERN LINEA 96
# Lo que hicimos ahi fue guardar los datos (o informacion) que estaban en el CSV en formato JSON, y le dimos el aspecto parecido que tiene un archivo JSON
# Fijemonos que en el DATA.json el primer nombre es Grier y en personas.json es Antonetta (el mismo que DATA.csv)


# GUARDAR DATOS JSON EN FORMATO CSV
#########################################
with open("personas.csv", "w") as file:
    pass

#########################################