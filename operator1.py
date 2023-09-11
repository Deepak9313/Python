'''
Arithmetic operators => +,-,*,/,**,%
Assignment operators => += ,-=,*=,/=,**=,%=
Comparison operators => ==,!=,!=,<,>,<=,>=
Logical operators => and,or,not
Identity operators => is ,isnot
Membership operators => in,not in
Bitwise operators
'''
a = int(10)
b = 2
print( a + b)
print( a - b)
print( a * b)
print( int(a / b))
print( a % b)
print( a ** b)
#----------
a+=30
print(a)
a-=30
print(a)
a*=30
print(a) # 300
a/=30 # 10
print(a)
a%=30 # 10%30 => always give us remainder of 10
print(a)
a**=2
print(a)
a = int(10)
print(a)
#---------- a = 10 and b = 2
print(a == b)
print(a <= b)
print(a >= b)
print(a != b)
if ( a >= 0 and b >= 0):
    print("Both values are greater than zero")
if( a == 0 or b >=0):
    print("successfull")
if(not(a >= 100)):
    print("not running")
str = [1,3]
str2 = [3,4]
str3 = [1,3] # x = 2, x =y , y? 
str4 = str
st5 = "sakshi"
print(str4 is str) # this comparison between memory location
print(str3 is not str)
print("z" in st5)
print(id(str))
print(id(str2))