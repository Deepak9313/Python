class Mynum:
    def __init__(self,color,number):
        self.color = color
        self.number = number
    def __str__(value):
        return f"The color is {value.color}"
x = Mynum("red",32)
print(x)
class person:
    def __init__(self,name,rollno,age,gender):
        self.anothername = name
        self.rollno = rollno
        self.age = age
        self.gender = gender
y = person("abc",23,13,"male")
print(y.anothername)
class parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def func(self):
        print(f"The name is {self.name} and age is {self.age}")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.name = "api"
z = child("abc",56)
a1 = child("anjali",30)
a1.func()
z.func()



#polymorphism
class vehicle:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def move(self):
        print("roll")
class boat(vehicle):
    def __init__(self,name,color):
        super().__init__(name,color)
    def move(self):
        print("swim")
val = boat("titanic","white")
val = vehicle("ferrai","red")
val.move()