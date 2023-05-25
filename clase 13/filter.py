# Filter recibe una lista de algo 
# y devuelve otra lista pero filtrada

numeros = [4,3,7,6,8,2,3]


pares = list(filter(lambda num : not (num % 2), numeros))


# pares = []
# for item in numeros:
#     if item % 2 == 0:
#         pares.append(item)

# Esto es lo que tendria que hacer sin filter.

print(pares)