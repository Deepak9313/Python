set1 = {1,2,12,1,1,12,11,12,12,1,44,4,4,4,4,4,"apple","apple","apple","banana"}
# 1 2 4 banana 11 12 44 apple 
set2 = {"apple","banana","litchi"}
# 1 2 4 11 12 44
# intersection
print(set1.intersection(set2))
cpy1 = set1.copy()
cpy2 = set1.copy()
cpy3 = set1.copy()
cpy1.intersection_update(set2)
print(cpy1)
# union
print(set1.union(set2))
cpy2.difference_update(set2)
print(cpy2)
print(cpy3.symmetric_difference(set2))
fruit = input("Enter the values : \n")
set1.add(fruit)
print(set1)
# set clear
cpy2.clear()
#remove command
set1.remove("apple")
print(set1)
print(set1.discard("apple"))
print(set1)
# update command
set3 = {"paneer","tomato","potato"}
l1 = ["shinchan","dora","chotta bheem"]
set1.update(l1)
print(set1)
# pop method
set1.pop()
set1.pop()
set1.pop()
print(set1)
print(cpy1)
set4 = {1,2,3,4,5,6,7,8,9,10,11,12}
set5 = {4,5,6}
print(set5.issubset(set4))
print(set4.issuperset(set5))