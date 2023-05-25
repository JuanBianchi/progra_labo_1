cadena = "juan carlos"

print(cadena.capitalize) # el metodo capitalize solo me pasa a mayuscula la primer inicial y el resto me lo pasa a minuscula.

x = "juan carlos alfredo"

def capitalizar_cadena(cadena:str) -> str:
    aux = list(cadena)
    aux[0] = aux[0].upper()
    for i in range(len(aux)):
        if(aux[i].isspace()):
            aux[i + 1] = aux[i + 1].upper()
    return "".join(aux)

x = capitalizar_cadena(x)

print(x)



cadena = input("Ingrese algo: ")

print(cadena)
print(len(cadena))

cadena = cadena.strip() # strip se encarga de quitar los caracteres de espacios en blanco adelante y atras de cada cadena de string
                        # si le paso por parentesis lo que quiero que le saque, se especifica en eso.

print(cadena)
print(len(cadena))

print("------------------------------------------")

# chr(64) # me devuelve el arroba
# ord("@") # me devuelve el 64

cadena_dos = " Esto es una cadena "

print(cadena_dos.find(""))
print(cadena_dos.count(""))
print(cadena_dos.replace("o", "a"))