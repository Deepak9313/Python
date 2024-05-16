import numpy as np
a = np.array([[10,20,30,40],[1,2,3,4]],dtype=int,ndmin=2)
b = np.array([100,200,300],dtype=int,ndmin=2)
c = np.append(a,b)
# random function
d = np.random.randint(0,100)
e = np.array(np.random.randn(10)*100,dtype=int)
print(e)
# indexing in array
print(a[0][2])
print(a[1][1])
# sum function
f = np.sum(a,axis=0)
g = np.sum(a,axis=1)
print(f)
print(g)
# concatenation
arr1 = np.array(["litchi","mango","watermelon"],dtype=str)
arr2 = np.array(["ladyfinger","brinjal","tinda"],dtype=str)
arr3 = np.concatenate((arr1,arr2),axis=None)
print(arr3)
x=np.array([[1,2],[3,4]])  
y=np.array([[12,30],[50,60]])
z = np.concatenate((x,y),axis=0)
print(z)