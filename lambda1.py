a = lambda num1,num2 = 0,num3 = 0: num1+num2+num3
print(a(10,20,30))
print(10)
# scope 
# global scope
x = "Daredevil" # => global scope
def display():
    return x
print(display())
print(x)
# local scope
def display():
    y = "Mat Mardock" # => local scope
    return y
print(display())
# not possible print(y)
# local to global scope
def display():
    global z
    z = "Friday"
    return z
print(display())
print(z)
# nonlocal keyword
def fun1():
    car = "Tata"
    def fun2():
        nonlocal car
        car = "Fortuner"
    fun2()
    return car
print(fun1())