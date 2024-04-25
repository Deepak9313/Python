x = [10,51,2,18,4,31,13,5,23,64,25]
print(x)
for i in range(len(x)-1):
    for j in range(len(x)-i-1):
        if x[j] > x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]
            j +=1
print("Sorted array is : ",x)