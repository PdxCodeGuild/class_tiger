#practice_fundamentals.py
def is_even(a):
    if a/2 == int(a/2):
        return "true"
    else:
        return "false"
#print(is_even(2)) -> true


def opposite(a, b):
    if (a>0 and b<0) or (a<0 and b>0):
        return "true"
    else:
        return "false"


def near_100(c):
    if (c>10 and c<100):
        return "true"
    else:
        return "false"

def maximum_of_three(a, b, c):
    if (a>=c and a >= b):
        return a
    elif (b>=a and b>=c):
        return b
    elif (c>=a and c>=b):
        return c

def powers_2(n):
    return [2**i for i in range(n)]

#practice_strings.py
def double_letters(x):
    my_string == ''
    for char in x:
        my_string += char*2
    return my_string

def missing_char(x):
    x == []
    for i in range
    return x

print(missing_char('hello'))
