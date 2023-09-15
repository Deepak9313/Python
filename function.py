def fun1(name,age,*item): #parameters
    print(f"{name} and {age} color is {item[0]} dog's name is {item[1]} and lucky number is {item[2]}")
    # return print(type(item))
fun1("amiliy",23,"red","tomy",3) #arguments
def fun2(name,**item):
    print(f"the => {name}")
    return print(type(item))
fun2(name = "nandini",child = 23,truth = False)
name = input("Enter your name : ")
age = int(input("Enter your age : "))
contact = int(input("Enter your contact : "))
def output(**values):
    return print(values)
output(name1 = name,age1 = age,contact1 = contact)