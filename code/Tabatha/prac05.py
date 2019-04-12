

def powers_of_2(x):
    return [2 ** x for x in range(1, x)]
    
# print(powers_of_2(10))

def even_numbers(x):
    even_numbers = [x for x in range(2, (x * 2) + 1)  if x % 2 == 0]
    return even_numbers

# print (even_numbers(10))
d = {'a': 1, 'b': 2}
def swap(dictionary):
    return {value:key for key, value in dictionary.items()}
# print(swap(d))

import string

def unicode_dict(string):
    letters = [char for char in string.ascii_lowercase]
    numbers = [x+1 for x in range(len(letters))]

    return dict(zip(letters, numbers))

print(unicode_dict(string))