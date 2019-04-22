'''
Practice 1 Fundamentals


'''

# Problem 1 : Write a function that tells whether a number is even or odd


def is_even(a):
    if a % 2 == 0:
        print('even')
    else:
        print('odd')

# is_even(4)
# is_even(7)

# Problem 2 : write a function that takes two ints, a and b, and returns Triue if one is positive and the other is negative

def opposite(a,b):
    if a * b < 0:
        return True

# mytest = opposite(-1,-1)
#
# if mytest:
#     print("true")
# else:
#     print('false')

# Problem 3 : write a function that returns True if a number is within 10 of 100

def near_100(num):
    if abs(100 - num) <= 10:
        return True

mytest = near_100(80)
#
# if mytest:
#     print("true")
# else:
#     print('false')


# Problem 4 : Write a function that returns the maximum of 3 parameters

def maximum_of_three(a,b,c):
    my_list = [a,b,c]
    return max(my_list)

# print(maximum_of_three(1,22,3))


# Problem 5 : Print out the powers of 2 from 2 ^ 0 to 2^20

def my_powers():
    for n in range(0,21):
        power_n = 2 ** n
        print(power_n)

# my_powers()












#######
