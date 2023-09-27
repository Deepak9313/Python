fruits = [1,23,343,565,1,1,1,1,1,1,1,1]
for x in fruits:
    print(x)
for x in range(0,11,2):
    print(x)
# for(i=0;i<20;i++){
    #code excecution
# }
a = "ameoba"
for i in a:
    if(i == "b"):
        continue
    print(i)
else:
    print("Loops finished")
def fun1():
    pass
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(len(matrix))
print("\v")
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        print(matrix[i][j])
# *
# **
# ***
# ****
# *****
val = int(input("Enter the number of rows: "))
for i in range(0, val+1):
    for j in range(0, i):
        print("*", end=" ")
    print("")