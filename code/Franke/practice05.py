#Problem 1
#Write a comprehension to
# generate the first 10 powers of two.
def ten_first_power():
    return [2**i for i in range(10)]

#Problem 2
#Write a comprehension to
# generate the first 10 even numbers.
def ten_first_even():
    return [i for i in range(1,21) if i%2 == 0]

print(ten_first_even())

#Problem 3
#Write a dictionary comprehension to swap keys and values
# of a given dictionary. So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.
#.items turns a dict in to a list of tuples easier to switch vales
def dict_swap(dictio):
    return {value : key for key, value in dictio.items()}

dict = {1: 'a', 2: 'b'}

print(dict_swap(dict))

#Problem 4
#Write a dictionary comprehension to print each
# letter of the alphabet and its corresponding ASCII code (check out ord)
import string as s
def alphabet_and_code():
    return {value : ord(value) for value in s.ascii_letters}

print(alphabet_and_code())
