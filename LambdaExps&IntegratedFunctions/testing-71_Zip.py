"""
    zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entada em pares
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]

zip1 = zip(list1, list2, 'abc')

print(zip1)
print(type(zip1))
# Sempre podemos gerar uma Lista, uma Tupla ou um Dicionários(Set)

print(list(zip1))
print(tuple(zip1))# Não imprime nada pois o zip é executado apenas uma vez  
print(set(zip1))  # Não imprime nada pois o zip é executado apenas uma vez  
print(dict(zip1)) # Não imprime nada pois o zip é executado apenas uma vez 

# O ZIP pode ser usado, por exemplo, para misturar músicas de vários artistas numa playlist do Spotify


# FORMA CORRETA DE SE FAZER:
zip1 = zip(list1, list2, 'abc')
print(tuple(zip1))

zip1 = zip(list1, list2, 'abc')
print(set(zip1))

zip1 = zip(list1, list2) # keys = list1, values = list2
print(dict(zip1))

# O Zip utiliza como parâmetro o comprimento do menor iterável (a menor lista, menor string, etc).
# Isso significa que, trabalhando com iteráveis de tamanhos diferentes, o programa deve parar quando o número de elementos do menor iteráveis acabar. 
list3 = [7, 8, 9, 10, 11, 12, 14, 15, 16]

zip2 = zip(list1, list2, list3)
print(list(zip2))

# Podemos utilizar diferentes iteráveis com zip

tuple1 = 1, 2, 3, 4, 5, 6
list1 = [7, 8, 9, 10, 11, 12]
dict1 = {'a': 11, 'b': 12, 'c': 13}
mixed_zip = zip(tuple1, list1, dict1)
print(list(mixed_zip))

data1 = [(0, 1), (2, 3,), (4, 5), (6, 7), (True, True)]
print(list(zip(*data1))) # upacking (destructuring or something like this)

