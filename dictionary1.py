import json
fam_real = {
    # Key : value
    "name" : ["father", "mother","son","daughter"],
    "age" : (44,40,23,20),
    "gender" : ["male", "female","male","female"],
    "vaccination" : True
}
print(fam_real)
print(type(fam_real))
# JSON
fam = '{ "name" : ["father", "mother","son","daughter"],"age" : (44,40,23,20),"gender" : ["male", "female","male","female"],"vaccination" : True}'
print(type(fam))
# dict to JSON
js = json.dumps(fam)
print(js)
# JSON to dict
dict10 = json.loads(js)
print(dict10)
# get the value
get1 = fam_real.get("name")
print(get1)
print(fam_real.get("age"))
# add new properties
fam_real["country"] = "India"
fam_real["vaccination"] = False
print(fam_real)
# update dictionary
dict2 = {
    "fruits" : "apple",
    "color" : ["red", "green", "orange"]
}
fam_real.update(dict2)
print(fam_real)
# functions of dictionary
print(fam_real.keys())
print(fam_real.values())
print("----------------------------------------------------------")
items = fam_real.items()
print("----------------------------------------------------------")
'''
dict_items (
    [
        ('name', ['father', 'mother', 'son', 'daughter']),
        ('age', (44, 40, 23, 20)), 
        ('gender', ['male', 'female', 'male', 'female']), 
        ('vaccination', False), ('country', 'India'), 
        ('fruits', 'apple'), ('color', ['red', 'green', 'orange'])
     ]
     )

'''
# remove the key and values
fam_real.pop("gender") # remove the definite key
print(fam_real)
fam_real.popitem() # remove the last key value pair
print(fam_real)
dict2.clear()
dict3 = fam_real.copy()
print(dict3)
l1 = [] # 0 1 2 3 
for i in range(0,4):
    l1.append(i)
l2 = []
inp = int(input("Enter the items you want to insert:\n"))
for  j in range(0,inp):
    inp2 = input(f"Enter the value {j+1}:- \n")
    l2.append(inp2)
l3 = {"a","b","c"}
new_dict = dict.fromkeys(l1,l3)
print(new_dict)