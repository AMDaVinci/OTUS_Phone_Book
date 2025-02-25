#C:\Users\AMakarov5.000\Desktop\Phone_Book\src\initial_file_creator\Contacts.json

import csv, json, time
from pprint import pprint

file_path = input('Please provide path to your file:')


with open(file_path, 'r', encoding='UTF-8') as contacts_file:
    file_dict = json.load(contacts_file)

buffer_dict1 = file_dict
pprint(buffer_dict1, sort_dicts=False)

for item in buffer_dict1[0]:
    print(type(buffer_dict1[0][item]))
print(buffer_dict1[0]['Phone Number'].keys())

for item in buffer_dict1:
    for i in item:
        if isinstance(item[i], dict):
            print(f'{i}:')
            for key, value in item[i].items():
                print(f'    {key}: {value}')
                time.sleep(0.4)
        else:
            print(f'{i}: {item[i]}')
        time.sleep(0.4)



def id_generator():
    curr_id = int(max([_['ID'] for _ in buffer_dict1]))+1
    while True:
        yield curr_id
        curr_id += 1

curr_id = id_generator()
print(next(curr_id))
print(next(curr_id))