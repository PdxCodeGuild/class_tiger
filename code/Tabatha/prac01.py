# x = int(input('Enter a number > '))

def even_num(x):
    test = x % 2
    if test == 0:
        return True
    else:
        return False
# print(even_num(x))
# even_num(x)

def opposite(a,b):
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return False
    else:
        return True
# opposite(3, 4)
# print(opposite(3,-4))

def near_100(x):
    test2 = abs(x - 100)
    if test2 > 10:
        return False
    else:
        return True
# print(near_100(98))
# even_num(x)

def the_max(a,b,c):
    max_list = [a,b,c]
    sorted_list = sorted(max_list)
    return sorted_list[2]
# print(the_max(8, 6, 5))
# the_max(8, 6, 5)

def exponent(a,x):
    if x <= 20:
        x += 1
        start = a ** x
        print(start, sep=",", end=" ") 
        return exponent(a,x)   
exponent(2,0)