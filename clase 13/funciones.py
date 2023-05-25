# Las funciones son objetos de primera clase
# Esto es:
# - debe poder asignarse a una variable
# - debe poder retornarse por una funcion
# - debe poder pasarse como parametro a una funcion

# Las funciones cumplen esos 3 criterios.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

x = sumar
print(x)
print(type(sumar))

print(x(3,4))
print(sumar(3,4))
# Solamente el nombre de la funcion es una direccion de memoria.
# Si ponemos los parentesis de la llamada, le estamos diciendo: anda a esta direccion de memoria y ejecuta ese codigo que esta ahi.

# Yo puedo invocar a la funcion sumar usando la variable x y pasarle los parametros y va a funcionar.

def calcular(a, b, operacion):
    return operacion(a, b)

print(calcular(3, 4, multiplicar))
print(calcular(3, 4, restar))
print(calcular(3, 4, dividir))
print(calcular(3, 4, sumar))
print("----------------------")

# Para esto me sirve pasarle una funcion como parametro a otra funcion, para cambiarle la funcionalidad.
# Pero tambien tiene infinidad de usos, depende de la funcion que le pase a otra funcion, le cambio completamente la funcionalidad.

# Esto es lo que se conoce como callback en JS, delegado en C++, como funcion lambda en Python, puntero a funcion en C.


duplicar = lambda a, b : a - b * 2
# Ver explicacion funciones anonimas, etc.

# La idea de las funciones lambda serian como para "resumir" una funcion y pasarsela a otra funcion como "callback".
# Pensar a la funcion lambda como un literal de funcion, asi como un literal de cadena que se lo guarda en una variable.

print(duplicar(2, 5))  # le paso la funcion lambda. Que hace la operacion

print(calcular(3, 4, lambda a, b : a - b * 2)) 
print(calcular(3, 4, restar))
print(calcular(3, 4, dividir))
print(calcular(3, 4, sumar))