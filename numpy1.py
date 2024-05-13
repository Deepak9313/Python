import numpy as np
# print(dir(np))
a = np.array([2,3,12,13,14,15],dtype=int)
b = np.asarray(['a','b','c','d','e','f'],dtype=str)
l1 = [12.1,11.3,18.9,20.8]
print(type(l1))
c = np.asarray(l1,dtype=float)
d = np.asarray([[1,0],[0,1]],dtype=int)
# shortcut way to create a identity matrix
e =np.identity(3,dtype=int)
print(d)
print(e)