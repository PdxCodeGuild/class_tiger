'''
Practice 5 : Comprehensions
'''
import string
# Problem 1 : write a comprehension to generate the first 10 powers of 2

def powers_two(num):
    nums = [2**x for x in range(num)]
    return nums
# print(powers_two(10))


# Problem 2 : write a comprehension to generate the first 10 even Numbers

def evens():
    nums = [x for x in range(1,21) if x % 2 == 0]
    return nums
# print(evens())

# Problem 3 : dictionary comprehension

def dict_swap(input_dict):
    ouput_dict = { input_dict[key]: key for key in input_dict }
    return ouput_dict

# print(dict_swap({'a':1,'b':2,'c':3}))

# Problem 4 : dictionary comprehension

def alpha_dict():
    my_dict = { letter:ord(letter) for letter in string.ascii_lowercase}
    return my_dict

# print(alpha_dict())
