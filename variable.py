_mile = "Great Distance"
print(_mile)
mile23 = "Alaska"
print(mile23)
# 23mile = "India"
# print(23mile)
# mile23@ = "Cricket"
# print(mile23@)
#camel case
anudipFoundation = "Python is a good language"
#pascal case
AnudipFoundation = "Python is a good competitor of java"
#snake case
anudip_foundation = "Python is a easy language"
print(anudipFoundation)
print(AnudipFoundation)
print(anudip_foundation)
#multiple variable assign
x,y,z = ["momos","pizza","burger"]
print(z)
x = y = z = "3i"
print(z)
#output variable
x = 23
y = 10
z = "Nandini"
print(y,z)
val = 20
def fun1():  
    return val+20
val = fun1()
print(val)
x = "dirty"
def fun2():
    global x
    x = "fantastic"
    return x
print(fun2())
print(x)