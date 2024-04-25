l1 = ["apple","orange","pineapple"]
# length of the list
print(len(l1))
l2 = list((1,2,3,4,5,6,7,8,9,10))
l1.append("strawberry")
l1.extend(l2)
l1.index("strawberry")
# now we are doing forward
print(l1)
cpy = l1.copy()
cpy.remove(9) # it takes value for remove
cpy.pop(2) # it take the index value for remove
print(cpy)
cartoon = ["bheem","popie","oggy and cockroaches","jungle book"]
inp = input("Enter your favourate cartoon: \n")
cartoon.append(inp)
print(cartoon)
cartoon.sort()
print(cartoon)
cartoon.reverse() # cartoon.sort(reverse=True)
print(cartoon)
l4 = [1,1,1,1,2,2,2,1,1,3,4,5,6,7]
print(l4.count(7))