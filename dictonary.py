d1 = {
    "name":"abc",
    "age":23,
    "color":"red"
}
d2 = d1.copy()
print(d1)
print(type(d1))
print(d1["name"])
print(d1.keys())
d1["age"] = 55
print(d1.values())
print(d1.items())
# a = input("Enter the Key for assign: ")
# b = input("Enter the value for assign: ")
# d1.update({a:b})
# print(d1)
print(d1)
print(d1.pop("age"))
print(d1)
d1.popitem()
print(d1)
print("*")
print("**")
print("***")
print("****")
print("*****")
print(d2)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child3"]["name"])