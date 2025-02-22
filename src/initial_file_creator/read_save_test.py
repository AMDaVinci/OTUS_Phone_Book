#C:\Users\AMakarov5\Desktop\Phone_Book\src\initial_file_creator\Contacts.json

import csv, json
from pprint import pprint

file_path = input('Please provide path to your file:')


with open(file_path, 'r', encoding='UTF-8') as contacts_file:
    file_dict = json.load(contacts_file)

buffer_dict1 = file_dict
pprint(buffer_dict, sort_dicts=False)

for item in buffer_dict[0]:
    print(type(buffer_dict[0][item]))
print(buffer_dict[0]['Phone Number'].keys())