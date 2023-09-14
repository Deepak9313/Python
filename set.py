set = {"apple","cheery","banana","grapes","apple","apple"}
print(set)
# print(set[0])
for x in set:
    print(x)
set.add("watermelon")
print(set)
set.add("papaya")
print(set)
set2 = {1,2,3}
print(set)
set.update(set2)
print(set)
set.remove("cheery")
print(set)
set.discard("blackberry")
print(set)
set = {"str","str1",1}
for x in set:
    print(x)
set3 = set.union(set2)
print(set3)
# set.intersection_update(set2)
# # doesn't return a value
set5 = set.intersection(set2)
print(set5)
set = {"str","str1",1}
print(set.symmetric_difference(set2))