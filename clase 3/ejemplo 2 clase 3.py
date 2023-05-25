


a = 20
b = 0

try:
    rta = a / b
    print(rta)
except ZeroDivisionError:
    print("No esta definido la division por cero")




print(rta)

#Como no se puede dividir por 0, lo que haciamos en el ingreso era proteger la opreacion con un if else. 
#Pero ahora puedo usar el manejo de excepciones