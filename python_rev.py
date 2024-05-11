import json as js
import math as m
print("This is a Python print statement")
# single line comment
'''
Multiline comment
'''
'''
Data types in python
1) String
2) Integer
3) Float
4) Boolean
5) complex
6) list
7) tuple
8) set
9) frozenset
10) dictionary
11) bytes
12) bytesarray
13) memoryview
14) None
'''
_a = "String variable"
a = 23
b = 12.1
c = True
d = 1+10j
e = []
f = ()
g = {}
h = frozenset({})
i = {}
j = b'Hello'
k = memoryview(j)
l = None
#------------------------------ String Manipulation ------------------------------
str1 = "        This is a test string                  "
length = len(str1)
trim = str1.strip()
array = str1.split()
lower1 = str1.lower()
upper1 = str1.upper()
center1 = str1.center(50)
titles = str1.title()
sw = str1.startswith("This") # returns in boolean format
ew = str1.endswith('string') # returns in boolean format
repl = str1.replace("is","Is")
# searching the string value
ind = str1.index("test")
fin = str1.find("test")
slic = str1[0:15]
join = str1 + upper1
# ------------------------------ List Manipulation ------------------------------
l1 = ["pineapple","apple","orange","guava","mango","litchi","banana"]
l2 = list(('a','b'))
search = l1.index("banana")
add = l1.append("watermelon")
count = l1.count("apple")
copy = l1.copy()
copy.clear()
del copy
length = len(l1)
insert = l1.insert(2,"kiwi")
l1.sort()
des_sort = l1.reverse() # or l1.sort(reverse=True)
l2 = ["tomato","grapes","plum"]
l1.extend(l2)
l1.remove("guava")
l1.pop()
print(l1)
# -------------------------------- tuple maipulation --------------------------------
t1 = tuple(("apple","banana","litchi"))
listt = list(t1)
listt[0] = "red"
t1 = tuple(listt)
print(t1)
# -------------------------------- set manipulations --------------------------------
s1 = {1,10,16,12,13,1,1,1,1,1,1,1,1,12,2,22,2,2,2,2,2,2,4}
s2 = {"apple","banana","grapes",1,2,4}
intersect = s1.intersection(s2)
union = s1.union(s2)
s1.add(1000)
diff = s1.difference(s2)
subset = s1.issubset(s2)
supset = s1.issuperset(s2)
s1.add(2000)
rem = s1.pop() # remove the item from last
s1.remove(2000)
s1.discard(2000) # doesn't show error if item is not present
s1.update(s2)
c1 = s1.copy()
cl = c1.clear()
# frozenset is a type of set you cannot change the value after intialization
# --------------------------------- Dictionary Manipulation --------------------------------
di = {
    "name":"abc",
    "city":"delhi",
    "age" : 23,
    7 : "favorite Number",
    "married" : True,
}
di.get("name")
di["desingation"] = "Software Engineer"
d2 = {
    "wife" : "xyz",
    "age" : 20,
    "height" : 150
}
di.update(d2)
json1 = js.dumps(di)
load1 = js.loads(json1)
print(type(json1))
print(type(load1))
key = di.keys()
val = di.values()
pair = di.items()
# pop vs popitem
di.pop("age") # remove specified key
di.popitem() # remove last item
d1 = di.copy()
cl = di.clear()
# -------------------------------------- Loops --------------------------------
for i in range(0,10):
    if ( i == 5):
        continue
    print(i)
j = 1
while j < 20:
    print(j)
    if( j == 14):
        break
    j = j + 1
# -------------------------------------- control flow --------------------------------
age = 12
if age < 18:
    print("You are not eligible for vote")
elif( age > 200):
    print("type correct age")
else:
    print("eligible")
val = 1
match(val):
    case 0 :
        print("case 0")
    case 1 :
        print("case 1")
# -------------------------------------- function --------------------------------------
def greet(name):
    print("Hello Good morning!"+name)
greet("Anand")
def fruits(*val):
    print(val)
fruits("apple")
fruits("orange","litchi")
# postion argument
# -------------------------------------- Operator --------------------------------
# Assignment Operator
# arithmetic operator
# comparison operator
# logical operator and , or and not
# ternary operator ?:
# identity operator : is , is not
# membership operator : in , not in
# -------------------------------------- lamba ------------------------------------
a = lambda val : val * 20
print(a(10))
print(a(20))
# -------------------------------------- Scope --------------------------------
age = 90
def show_age():
    a = 12
    global value
    value = 100
    print(age) # global scope
    print(a) # local scope
show_age()
print(value)
# ------------------------------------- Math Module --------------------------------
pow1 = m.pow(2,3)
sqe = m.sqrt(12)
# ------------------------------------- file handling --------------------------------
f1 = open("test.txt","at")
f1.write("File is open now")
f1.close()
f1 = open("test.txt","rt")
print(f1.readlines())
f1.close()
# ------------------------------------- User Input --------------------------------
inp = input("Enter the value you want to insert :\n")
# ------------------------------------- OOPS Concepts -------------------------------
class Person:
    def __init__(self,name,age,country="india"):
        self.name = name
        self.age = age
        self.country = country
    def __str__(self) -> str:
        return f"The name is {self.name} and the age is {self.age} and the country is {self.country}"
obj = Person("abc",23)
print(obj)
# inheritance
class Student(Person):
    def __init__(self,n,a,c,color):
        self.color = color
        super().__init__(n,a,c)
        self.color = color
    def __str__(self):
        return f"{self.name},{self.age},{self.country},{self.color}"
obj2 = Student("a",11,"brazil","red")
print(obj2)
# function overloading
class Shape:
    def __init__(self,a,b = None,c = None):
        if a != None and b == None and c == None:
            print("one side")
        elif a != None and b != None and c ==None:
            print("two sides")
        elif a != None and b != None and c != None:
            print("three sides")
        else:
            print("unknown")
obj3 = Shape(12)
obj4 = Shape(14,12)