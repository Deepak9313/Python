import numpy as np
names_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack']
a = np.array([[names_list]])
sh = a.reshape(-1)
print(sh)
res = np.where(sh == "Ian")
b = np.arange(10)
c = np.where(b == 5,b,b*10 )
print(c)
# filter array
arr1 = np.arange(10)
names_list = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'])
status_list = [True, False, True, True, False, False, True, True, False, False]
result = names_list[status_list]
print(result)
# iteration
multi_array = np.array([[[1,2,3]],[[10,11,12]]])
# for i in range(len(multi_array)):
#     for j in i:
#         for k in j:
#             print(multi_array[i][j][k])
for x in np.nditer(multi_array):
    print(x)
# specific value
ar = np.array([[1,2,3],[10,11,12]])
res = np.where(ar <5,ar,-2)
print(res)
# argsort
rand = np.array([16,  7 ,12 , 5  ,10 ,11, 2])
print(rand)
res1 = np.argsort(rand)
print(res1)
for i in res1:
    print(rand[res1])