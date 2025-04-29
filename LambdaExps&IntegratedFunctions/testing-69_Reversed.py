"""
    Note: Don't mix up "reverse" function present in the lists with "reversed".
"""

# "Reverse" function (only works with lists):
l1 = [1, 2, 3, 4, 5]
print(l1)

l1.reverse() # doesn't return anything
print(l1)

# -- Reversed Function --------------------------------
# * The function "reversed" works with whatever iterable you wish 

res = reversed(l1)
print(res) # returns an iterable object called "list_reverseiterator"
print(type(res))

# Nonetheless, we can cast the "list reverse iterators" to tuples, lists or sets
print(tuple(reversed(l1)))
print(list(reversed(l1)))
print(set(reversed(l1)))

# We can also iterate over the reversed object

for letter in reversed('A man, a plan, a canal, Panama!'):
    print(letter, end='') # "end" argument used for avoiding line break

print('\n')

# "reversed" + join (now we don't need a for loop)
print(''.join(list(reversed('Was it a car or a cat I saw?'))))

# reversed with string slicing
print('No lemon, no melon.'[::-1])

# "reversed" in a reversed for loop
for n in reversed(range(1, 11)):
    print(n)

# It is also possible to do this using the range function
for n in range(10, 0, -1): # o "-1" define o sentido
    print(n)

