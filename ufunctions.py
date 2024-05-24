import numpy as np
import math as mt
x = np.array([1,2,3,4],dtype=int)
y = np.array([5,6,7,8],dtype=int)
z = []
for i,j in zip(x,y):
    z.append(i+j)
print(z)
# shorcut way to add
print(np.add(x,y))
# create self function
def myfun(x,y):
    return x*y
a = np.frompyfunc(myfun,2,1)
print(a([1,2,3],[3,4,3]))
# broadcasting
print(x+y)
print(np.subtract(x,y))
print(np.power(x,y))
print(np.remainder(x,y))
print(np.divmod(x,y))
# rounding decimal
t1 = np.trunc([-4.23632784,45.37478])
t2 = np.round([-4.23632784,45.37278],1)
t3 = np.floor([-4.23632784,45.37478])
t4 = np.ceil([-4.23632784,45.37478])
print(t3)
print(t4)
print(np.ceil([511/10]))
# summations
cp1 = np.copy(x)
cp2 = np.copy(y)
print(np.add(x,y))
print(np.sum([x,y],axis=0)) # 0 = up to down , 1= left to right
print(np.cumsum([x,y]))
print(np.cumprod([x,y]))
print(mt.factorial(6))
# Finding LCM
x = np.lcm(10,40)
print(x)
y = np.gcd(28,72)
print(y)