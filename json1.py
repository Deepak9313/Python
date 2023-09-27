import json
x = {
    "name":"abc",
    "age":32,
    "color":"lavender"
}
print(x)
print(type(x))
js = json.dumps(x)
print(type(js))
dict = json.loads(js)
print(dict["name"])