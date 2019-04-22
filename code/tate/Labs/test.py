import math

class Point:
    def __init__(self,x=0,y=0): #this is the initializer
        self.x = x
        self.y = y

    def __str__(self): # specify a str conversion
        return '['+str(self.x)+','+str(self.y)+']'

    def __repr__(self):
        return f'Point({self.x},{self.y})'

    def __getitem__(self, index):
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            return None

    def __len__(self):
        return 2

    def __eq__(self, p):
        print('Check equals')
        return self.x == p.x and self.y == p.y

    def __ne__(self, p):
        return self.x != p.x or self.y != p.y

    def distance(self,p):
        dx = self.x-p.x
        dy = self.y-p.y
        return math.sqrt(dx*dx + dy*dy)

    def scale(self,v):
        self.x *= v
        sel.y *= y

p1 = Point(5,2)
p2 = Point(3,4)
dist = p1.distance(p2)
print(p1)
