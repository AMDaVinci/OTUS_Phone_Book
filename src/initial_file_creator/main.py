import json

initial_dict = [{
    "ID": "00001",
    "First Name": "Alex",
    "Last Name": "Smith",
    "Age": 36,
    "Phone Number": {
        "Mobile": "+79172345678",
        "Home": "",
        "Work":""
    },
    "Birthday": "01-Jan-1989"
},
    {
        "ID": "00002",
        "First Name": "John",
        "Last Name": "Smith",
        "Age": 36,
        "Phone Number": {
            "Mobile": "+79172345678",
            "Home": "",
            "Work": ""
        },
        "Birthday": "01-Jan-1989"
    }
]

initial_dict_json = json.dumps(initial_dict)

with open('Contacts.json', 'w', encoding='utf-8') as contacts:
    json.dump(initial_dict, contacts, ensure_ascii=False, indent=4)
    #contacts.write(initial_dict_json)

