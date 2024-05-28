import pandas as pd
# Series
list1 = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m"]
lent = len(list1)
index1 = []
for i in range(1,lent+1):
    index1.append(i)
data = pd.Series(list1,index=index1)
print(data)
dicti = {
    "data1":200,
    "data2":400,
    "data3":4000,
}
data2 = pd.Series(dicti)
print(data2)
file = pd.read_csv("data.csv")
index2 = []
for i in range(0,len(file)+1):
    index2.append(i)
data = pd.DataFrame(file,index=index2)
print(data.loc[4])
# read json data
json_data = pd.read_json("data.json")
data4 = pd.DataFrame(json_data)
print(data4)