
nombre = "Juan"
edad = 24
altura = 1.78

print(nombre, edad, altura)
print("Nombre: " + nombre + " Edad " + str(edad) + " Altura " + str(altura))
print("Nombre: %s Edad: %d Altura: %.2f" %(nombre, edad, altura)) # Esto lo puedo hacer como en C, es interpolacion de strings PERO NO SE USA
print("Nombre: {} Edad: {} Altura: {}".format(nombre, edad, altura)) # Si yo dejo las llaves vacias, va a respetar el orden del parentesis y format
print(f"Nombre: {nombre} Edad: {edad} Altura: {altura}") # Esto es template string, es otro tipo de interpolacion
