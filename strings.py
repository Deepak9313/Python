'''
Q : What is a string?
Ans : A string which enclose in double and single quotes . The string contains alphanumeric and number values.
Use Case :- String is used to create patterns
'''
str1 = "      The python consist of many useful libraries for Data Science"
# to find the length of the string
print(len(str1))
# to find the word in sentence
# Difference find vs index
# Ans :- find will give -1 if not found but index give an error message
print(str1.find("python",20)) # taking a offest as a second argument
print(str1.index("python"))
# to check the characters
print(str1[len(str1)-2])
# to remove whitespace
print("The length with whitespace is : {}".format(len(str1)))
newstr = str1.strip()
print("The length without whitespace is : {}".format(len(newstr)))
# format function
a = "watermelon"
b = "mango"
c = "litchi"
# format is used to print the variable in the string
res = "{} , {} and {} are summer fruits".format(a,b,c)
#Q : Print Mango and Watermelon in terminal
res1 = "{1} and {0}".format(a,b)
print(res1)
# fstring
res2 = f"{b} and {c} are my favorite fruits"
print(res2)
# slicing ? = it is used to cut a part of the string
sl_str = res2[0:10]
print(sl_str)
# lowercase and uppercase
print(res2.capitalize() + " = Captilize")
print(res2.lower() + " = lower")
print(res2.upper() + " = upper")
print(res2.title() + " = title")
print(res2.center(130))
# Split function : it will break the string into array or list
city = "Delhi|Mumbai|Agra|chennai|Punjab|Haryana"
spl = res2.split(" ")
spl2 = city.split("|")
print(spl2)
str2 = "Good Evening"
str2 = str2.replace("Evening","morning")
print(str2)
print(str2.startswith("Good"))
print(str2.endswith("Evening"))