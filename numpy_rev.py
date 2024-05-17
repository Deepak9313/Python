import numpy as np
# create an array
a = np.array([1, 2, 3,4],dtype=int,ndmin=2)
# Basic Numpy Functions
b = np.ones(shape=(3,4),dtype=int)
c = np.zeros(shape=(3,4),dtype=int)
d = np.identity(3,dtype=int)
e = np.empty(shape=(3,4))
f = np.eye(5,5,2,dtype=int)
g = np.full(shape=(4,4),fill_value=23)
print(d)
# indexing
print(d[1][1])
# slicing
ar = np.array([[10,20,30],[1,2,3],[9,12,34]])
print(ar[0:2,1:])
# copy vs view
ar2 = np.copy(a)
ar3 = a.view()
print(ar2.base) # if a class contain copy things it will print none
print(ar3.base) # if a class contain actual things or data it will give you real data
# append function 
c = np.append(a,b)
print(a)
print(b)
d = np.concatenate((a,b),axis=0)
#e = np.concatenate((a,b),axis=1)
print(d)
# using for loop to create array
list1 = []
for i in range(1,11):
    list1.append(i*2)
newar = np.array(list1)
list2 = []
for i in range(1,11):
    list2.append(i*3)
newar2 = np.array(list2)
if(len(newar) == len(newar2)):
    print("Broadcasting")
    print(newar+newar2)
else:
    print("Not broadcasting")
# shape
# this is used to check the shape of the array
print(d.ndim)
ar2 = d.shape
# reshape
ar3 = d.reshape(-1)
print(d)
print(ar3)
# total elements  16
ar4 = d.reshape(8,2)
print(ar4)