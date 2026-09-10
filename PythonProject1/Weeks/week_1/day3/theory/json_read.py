import json

# read from json to dictionary
with open("data.json", 'r') as file:
    data = json.load(file)
    print(data)

# dictionary
info = {
    "name": "Alex",
    "age": "22",
    "job": "unemployment"
}
# write in json
with open("data.json", 'w') as file:
    json.dump(info, file, ensure_ascii=False, indent=4)

with open("data.json", 'r') as file:
    data = json.load(file)
    print(data)

#from string to json
json_string = '{"name": "Lonny", "age": "55", "job": "Boss"}'
data = json.loads(json_string)
print(data)