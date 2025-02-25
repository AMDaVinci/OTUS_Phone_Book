import json, time
from pprint import pprint
from pathlib import Path



#C:\Users\AMakarov5.000\Desktop\Phone_Book\src\initial_file_creator\Contacts.json

menu_list = [
        'Open File',
        'Show All Contacts',
        'Create Contact',
        'Search Contact',
        'Edit Contact',
        'Delete Contact',
        'Save Changes',
        'Exit'
    ]



def phone_book_menu():
    print('-'*(max([len(i) for i in menu_list])+5))
    for i, item in enumerate(menu_list,1):
        print(f'{i}. {item}')
    print('-'*(max([len(i) for i in menu_list])+5))

def menu_selection():
    user_selection = input('Please select action number from menu list: ')
    while user_selection.isdigit() == False or int(user_selection) not in range(1,len(menu_list)+1):
        user_selection = input('Please enter correct menu point: ')
    print(f'\nYou selected \033[91m\033[1m {menu_list[int(user_selection) - 1]} \033[0m\n',)
    return int(user_selection)

def open_file():
    print('\033[1m Please note that only JSON file is allowed for input \033[0m\n')
    file_path = input('Please provide full file path to your json:')
    while not Path(file_path).exists() and str(file_path)[-5:-1] != 'json':
        file_path = input('Please provide CORRECT file path to your json:')
    with open(file_path, 'r', encoding='UTF-8') as contacts_file:
        file_data_list = json.load(contacts_file)
    print('\n Phone Book is opened successfully\n')
    return file_data_list

def show_all_contacts():
    for item in buffer_list:
        for i in item:
            if isinstance(item[i], dict):
                print(f'{i}:')
                for key, value in item[i].items():
                    print(f'    {key}: {value}')
                    time.sleep(0.15)
            else:
                print(f'{i}: {item[i]}')
            time.sleep(0.4)
        print('\n')
    while input('Press "P" to continue...').lower() != 'p':
        pass #Review of Phone Book, required due to visual size

def create_new_contact():
    print('Creating new contact...')
    # print(buffer_list[0])
    new_contact_dict = {}
    for key, value in buffer_list[0].items():
        # print(type(value))
        if key == 'ID':
            new_contact_dict[key] = f'{int(max([_['ID'] for _ in buffer_list])) + 1:0>5}'
            print(f'ID: {new_contact_dict['ID']}')
        elif isinstance(value, dict):
            nc_phone_dict = {}
            for k in value.keys():
                nc_phone_dict[k] = input(f'Enter {k} {key}: ')
            new_contact_dict[key] = nc_phone_dict
        else:
            new_contact_dict[key] = input(f'Enter {key}: ')
    buffer_list.append(new_contact_dict)
    print('New contact has been created successfully\n')

phone_book_menu()
menu_selected  = menu_selection()


while menu_selected != len(menu_list):
    if menu_selected == 1:
        buffer_list = open_file()
        phone_book_menu()
        menu_selected = menu_selection()
    elif  menu_selected == 2:
        show_all_contacts()
        phone_book_menu()
        menu_selected = menu_selection()
    elif menu_selected == 3:
        create_new_contact()
        phone_book_menu()
        menu_selected = menu_selection()