import json
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
        file_dict = json.load(contacts_file)
    print('\n Phone Book is opened successfully\n')
    return file_dict


phone_book_menu()
menu_selected  = menu_selection()


while menu_selected != len(menu_list):
    if menu_selected == 1:
        buffer_dict = open_file()
        phone_book_menu()
        menu_selected = menu_selection()
    elif  menu_selected == 2:
        for item in buffer_dict:
            pprint(item, sort_dicts=False, compact=True)
        while input('Press any key to continue...') == '':
            pass #Review of Phone Book, required due to visual size
        phone_book_menu()
        menu_selected = menu_selection()