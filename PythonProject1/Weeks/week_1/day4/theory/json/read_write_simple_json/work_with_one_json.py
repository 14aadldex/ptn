import json

with open('work_with_one_json.json', 'w') as file:
    json.dump("{}",file)

with open('work_with_one_json.json', 'r') as file:
    print(file.read())