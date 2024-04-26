def greet(): # function declaration
    print("Good Evening") # function definition
    print("Good Morning")
    print("Good Afternoon")
greet() # function calling
'''
two types of function are there
1) inbuild function :- python consists some inbuild functions : print()
2) Userdefined function :- these functions are created by user for their own purpose
'''
# syntax for parameterized functions
def greet1(name):
    print("Good Evening",name)
greet1("shadiya")
greet1("paras")
# Question : Write a function to print user name age and salary
def person(name,age,salary): # (name,age,salary)parameter 
    print(f"My name is {name} , my age is {age} and my salary is {salary}")
person("xyz",34,70000) # ("xyz",34,70000) argument
person("abc",45,100000) 
# indefinite arguments
def student(name,rollno,*odata):
    print(name,rollno,*odata)
    print(type(name))
    print(type(rollno))
    print(type(odata))
    print(f"student name :-{name} \nfather name :- {odata[1]}")
student("arpit",38,"red","rajat sharma",44,"shruti")
# Question : Write a function which take indefinte argument and print the top 1 meal all details of the day
# Definite : dish name and price
# indefinite : rating , customer order , amount ( 1 kg), total_profit
# Ans : ................
# **args
def fruit(name,**fdata):
    print("fruit name :-{} and color is {},weight is {}".format(name,fdata["color"],fdata["weight"]))
    print(type(fdata))
fruit("apple",color="red",weight="250g")
# pass function
def duck_typing():
    pass