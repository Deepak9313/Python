import numpy as np
arr1 = np.array([2+8j,8+2j,9+1j,6+3j],dtype=complex)
arr2 = np.asarray([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# range function
arr3 = np.arange(1,100,2)
arr4 = np.asarray([[1,2],[3,4]],dtype=int)
arr5 = np.empty((3,4),dtype=int)
print(arr5)
arr6 = np.ones(shape=(3,4),dtype=int)
print(arr6)
arr7 = np.zeros(shape=(3,4),dtype=int)
print(arr7)
# Question : take five values from user and make a numpy array 
list1 = [10,20,30,40,50]
# for i in range(0,5):
#     inp = input("Enter the value\n: ")
#     list1.append(inp)
arr8 = np.array(list1,ndmin=7)
print(arr1.ndim)
arr9 = np.full(shape=(4,4),dtype=int,fill_value=66)
arr10 = np.eye(10,10,k=2,dtype=int)
print(arr10)
print(arr10.ndim)