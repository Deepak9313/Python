class Shape:
    def __init__(self,a,b = None,c = None,d = None,*e ) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        if(a != None and b == None and c == None and d == None):
                print("Area of square is ",a*a)
        elif (a != None and b != None and c == None and d == None):
             print("Area of Reactangle is ",a*b)
        elif (a != None and b != None and c != None and d == None):
             print("Perimeter of Triangle is ",a+b+c)
        elif (a != None and b != None and c != None and d != None and e == None):
             print("Perimeter of Quadrilateral is ",a+b+c+d)
        elif (e != None):
             print("Sorry you entered incorrect arguments.")
obj = Shape(12)
obj2 = Shape(10,12)
obj3 = Shape(11,11,11)
obj4 = Shape(2,2,2,2)
obj5 = Shape(99,10,20,10,10)
class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
    def __str__(self):
        return f"the x and y coordinates are:- {self.x} and {self.y}"
    def __add__(self,other):
         self.x = self.x + other.x
         self.y = self.y + other.y
         return Point(self.x,self.y)
    def __len__(self,a):
         return len(a)
a = Point(12,2)
b = Point(1,3)
print(a+b)
print(a)
