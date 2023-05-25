

resultado = 123

try:
    print("El resultado es " + str(resultado))
except TypeError:
    print("No puedo concatenar un entero con un string")

#Una de las tantas soluciones, seria usar la funcion str(), que convierte a string cualquier otro tipo de dato