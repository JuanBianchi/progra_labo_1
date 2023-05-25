# Map y filter son dos funciones que vienen nativas. Reduce no, hay que importarla 
from functools import reduce

numeros = [4,3,7,6,8,2,3]

total = reduce(lambda ant, act : ant + act, numeros, 0)     # El 0 lo mando como 3 parametro para indicarle que tome como primer elemento ese numero


# Sin el reduce seria:
# total = 0

# for item in numeros:
#     total += item

# print(total)

# Con el reduce podemos calcular el maximo tambien

total = reduce(lambda ant, act : ant if ant > act else act, numeros)

print(total)