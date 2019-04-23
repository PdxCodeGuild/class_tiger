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

#x = input("Is Merrit the best instructor at PDX Code Guild? ")
#if x == "yes":
#    print("Good answer!")
#if x == "no":
#    raise ValueError("Lies!")

#classes

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

    def scale(self, v):
        self.x *= v
        self.y *= v

    @staticmethod
    def from_polar(r, theta): # static methods belong to the type, not the instance
        px = r * math.cos(theta)
        py = r * math.sin(theta)
        return Point(px, py)


polar_point = Point.from_polar(5.0, math.pi/6)
polar_point.scale(2)

p3 = Point()
p1 = Point(5,2)
p2 = Point(8,4)
dist = p1.distance(p2) # or p2.distance(p1), either works
print(dist)
print(p1.x,p1.y)
p1.scale(2)
print(p1.x,p1.y)

class Merritt:
    def __init__(self,x,y):
        self.name="Mary"
        self.point = Point(x,y)
        self.my_stuff = []

    def get_my_point(self):
        return self.point.x, self.point.y

    def scale_my_point(self,v):
        self.point.scale(v)

    def add_stuff(self, stuff):
        self.my_stuff.append(stuff)

me = Merritt(5,6)
me.scale_my_point(2)
print(me.get_my_point())
