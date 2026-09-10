new_dictionary = {} # diff between set and dictionary
new_set = set() # хранит уникальыне значения, несортирован

new_set.add("banana")
new_set.add("apple")

print(new_set)

new_set.add("banana")
print(new_set)

new_set.add("orange")
print(new_set)

new_set.update('apple') #делит на буквы и пихает уникальные буквы в SET
print(new_set)
# new_set.remove('banana')
# print(new_set)