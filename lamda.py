y = lambda a,b : a**b
print(y(2,3))
def fun1(n):
    return lambda a : a * n
mynum = fun1(30)
print(mynum(2))