#test.py
def addition(num1, num2, *args, **kwargs):
    num = num1 + num2
    for arg_num in args:
        num += arg_num
    if "should_I_print":
        print(num)
    return num
my_num = 5
my_other_num = 7
value = "stuff"

num1 = 1
num2 = 2

my_addition_number = addition(my_num, my_other_num, 1, 34, 3)
#print(my_addition_number)

def my_func():
    #print("function!")
    return 3

#separate

def get_dimensions():
    return 500, 200

#print(get_dimensions())

width, height = get_dimensions()
#print(width)
#print(height)



#def print_movie_ratings(username, *args, **kwargs):
#    print(args)
#    print(kwargs)
#    for arg in args:
#        if arg in kwargs:
#            print(arg, kwargs[arg])





def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


def a(x, y):
    return x + y

a = lambda x,y: x+y

x = input("Is Merrit the best instructor at PDX Code Guild? ")
if x == "yes":
    print("Good answer!")
if x == "no":
    raise ValueError("Lies!")
