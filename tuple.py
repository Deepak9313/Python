a = ("apple","banana","cherry")
print(a)
b = list(a)
b[0] = "pineapple"
a = tuple(b)
print(a)
print(a[1])
print(a[-1])
print(a[0:2])
print(type(a))
print("pineapple" in a)
# remove function
b = list(a)
b.remove("pineapple")
print(b)
b.append("guava")
print(b)
val1    = b[0]
val2   = b[1]
val3 = b[2]
(x,*z) = b
print(x,z)
#----------------
a = ("a","b","c","a","k","a")
b = (1,True,2,3)
join = a + b
print(join*3)
print(a.count("b"))
print(b.index(2)+1)