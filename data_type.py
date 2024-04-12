# Data type is a type of data which stored in the variables
'''
integer :-  ex : -20,100 range = -infinte to infinte
float :- ex : 20.122 or 20.00
complex : ex : 2 + 6j
string : "Python is a easy language"
list : ["python", "java", "ruby", "c++","php"] [] = braod brackets
tuple : ("python","java","ruby","c")            () = curved brackets
set : {1,2,1,1,10,2}                             {} = curly brackets
dictionary : {
            "name" : "xyz,
            "age" : 23,
            "gender" : "male"
        }
frozenset : forzenset((1,2,3,4,5,6,7,8,9,10,1))
memoryview : memoryview(b'hello) => it is used to see the data location
'''
comp = 2 + 6j
print(comp.real)
print(comp.imag)
str1 = "Python is a simple language "
print(type(str1))
print(str1)
lang = ["python", "java", "ruby", "c++","php"]
print(type(lang))
print(lang)
tup = ("python","java","ruby","c")
print(type(tup))
print(tup)
list2 = [1,2,1,1,3,4,5,6,7,8,9,10,1]
set1 = {1,2,1,1,3,4,5,6,7,8,9,10,1}
print(list2)
print(set1) # set print repeated values only once
dict1 = {
    "name":"abc",
    "age" : 20,
    "description" : "software developer"
}
print(type(dict1))
print(dict1)
froze = frozenset([1,2,3,4,5,6,7,8,1,1,1,1]) # you can't add or change value after intialization
print(froze)
print(memoryview(b'Hello'))