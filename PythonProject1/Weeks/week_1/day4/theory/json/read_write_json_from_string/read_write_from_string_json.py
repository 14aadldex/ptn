example = '{"nae":"bal"}'

with open('my_json.json', 'w', encoding='utf-8') as file:
    file.write(example)

with open('my_json.json', 'r', encoding='utf-8') as file:
    print(file.read())