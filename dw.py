
'''
result = []
list1  = 'alisa18 in list course4 an learn python'
temp = list1.split(' ')
for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        result.append(item)
print(result)
for r in result:
    print(r)

import string
for char in string.punctuation:
    str3 = str3.replace(char, "#")

new_dict = {
    "name": "Alisa",
    "age": 22,
    "position": "dev",
    "salary": 1000
    }
keys_extract = ["name", "salary"]
result_dict = {}
for k in keys_extract:
    result_dict.update({k: new_dict[k]})
print(result_dict)
'''     
new_dict = {
    "name": "Alisa",
    "age": 22,
    "position": "dev",
    "salary": 1000
    }
keys_extract = ["name", "salary"]
result_dictionary = {k: new_dict[k] for k in keys_extract}
print(result_dictionary)

