'''
Practice 5 : Comprehensions
'''

# Problem 1 : write a comprehension to generate the first 10 powers of list_word

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

# Problem 4 : dictionary comprehension
