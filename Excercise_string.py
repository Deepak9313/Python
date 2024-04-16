# Q1 : How to convert text in upper case form?
a1 = "this is a cat"
print(a1.upper())
# Q2 : convert this below string into array
a2 = "Apple,Banana,Cherry,Orange,Strawberry,Watermelon"
print(a2.split(","))
# Q3 : Find a particular word in a string
print(a2.find("this"))
print(a2.index(",Strawberry"))
# Q4 : How to find length of a string
print(len(a1))
# Q5 : Convert a string into an array and fill the blank spaces in the string
arr = a2.split(",")
str1 = "I Like {} Fruit but {} is a Summer Fruit".format(arr[3],arr[len(arr)-1])
print(str1)
# Q6 : Covert a whitespace string into an array but we don't want any junk data
str2 = "       Hello Python Good to see you again    " # string cleaning
newstr = str2.strip()
newarr = newstr.split(" ")
# shortcut 
newarr2 = str2.strip().split(" ")
print(newarr2)
# Q7 : Cut the string with a definite range
str2 = "This is a Watermelon"
cutstr = str2[0:4]
cutstr2 = str2[-5:]
print(cutstr2)
# Q8 : Check a Word in a string it exists or not
str2 = "This is a Watermelon"
res = "Watermelon" in str2
print(res)
# Q9 : Check a Word in a string it exists or not but using find function
res2 = bool(str2.find("Watermelon")) # if -1 give false or any value give true
res3 = bool(str2.find("Apple") + 1)
print(res2)
print(res3)
# Q10 : How to replace a string with a upper case but it will replace from the array