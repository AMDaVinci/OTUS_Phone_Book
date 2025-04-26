import json, time
from pathlib import Path


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

def work_list_printing(item):
    for i in item:
        if isinstance(item[i], dict):
            print(f'{i}:')
            for key, value in item[i].items():
                print(f'    {key}: {value}')
                time.sleep(0.15)
        else:
            print(f'{i}: {item[i]}')
        time.sleep(0.4)
    print('')

def proceed_input():
    while input('Press "P" to continue...').lower() != 'p':
        pass #Review of Phone Book, required due to visual size

def path_request():
    print('\033[1mPlease note that only JSON file is allowed for input \033[0m\n')
    file_path = input('Please provide full file path to your json:')
    while file_path == '' or not Path(file_path).exists() and str(file_path)[-5:-1] != 'json':
        file_path = input('Please provide CORRECT file path to your json:')
    return file_path

def open_file(file_path, menu_choice):
    with open(file_path, 'r', encoding='UTF-8') as contacts_file:
        file_data_list = json.load(contacts_file)
    if menu_choice == 1:
        print('\n Phone Book is opened successfully\n')
    return file_data_list

def show_all_contacts():
    for item in buffer_list:
        work_list_printing(item)
    proceed_input()

def create_new_contact(work_list: list):
    print('Creating new contact...')
    new_contact_dict = {}
    for key, value in work_list[0].items():
        if key == 'ID':
            new_contact_dict[key] = f'{int(max([_['ID'] for _ in work_list])) + 1:0>5}'
            print(f'ID: {new_contact_dict['ID']}')
        elif isinstance(value, dict):
            nc_phone_dict = {}
            for k in value.keys():
                nc_phone_dict[k] = input(f'Enter {k} {key}: ')
            new_contact_dict[key] = nc_phone_dict
        else:
            new_contact_dict[key] = input(f'Enter {key}: ')
    work_list.append(new_contact_dict)
    print('New contact has been created successfully\n')

def search_contact(work_list: list):
    print('Search for Contact...')
    search_input = input('Enter search string: ')
    for item in work_list:
        if search_input.lower() in str(item.values()).lower():
            work_list_printing(item)
    proceed_input()


def edit_contact(work_list: list):
    print('Editing contact...')
    edit_contact_id = input('Enter contact ID to edit: ')
    while not int(edit_contact_id):
        edit_contact_id = input('Please enter correct contact ID: ')
    for item in work_list:
        if int(item.get('ID')) == int(edit_contact_id):
            for key, value in item.items():
                if key == 'ID':
                    print(f'ID: {value}')
                elif isinstance(value, dict):
                    for k, v in value.items():
                        print(f'You want to update \033[91m\033[1m{k}: {v}\033[0m with')
                        record_update = input(f'Enter new {k} {key}: ')
                        if record_update:
                            item[key][k] = record_update
                else:
                    print(f'You want to update \033[91m\033[1m{key}: {value}\033[0m with')
                    record_update = input(f'Enter new {key}: ')
                    if record_update:
                        item[key] = record_update
            return print('\n', 'Contact has been edited successfully\n')

    return print('Contact ID not found\n')


def delete_contact(work_list: list):
    print('Deleting contact...')
    delete_contact_id = input('Enter contact ID (as number) to delete: ')
    while not int(delete_contact_id):
        delete_contact_id = input('Please enter correct contact ID: ')
    for item in work_list:
        if int(item['ID']) == int(delete_contact_id):
            work_list.remove(item)
        return print('Contact has been deleted successfully\n')
    return print('Contact ID not found\n')

def save_changes(work_list: list, initial_list: list ):
    if work_list == initial_list:
        print('Initial file was not changed')
    else:
        print('File will be saved in the project directory\n')
        with open('Contacts.json', 'w', encoding='UTF-8') as contacts_file:
            json.dump(work_list, contacts_file, ensure_ascii=False, indent=4)
        print('Changes saved successfully\n',f'\nPress {len(menu_list)} for exit or choose another option')


if __name__ == '__main__':

    phone_book_menu()
    menu_selected  = menu_selection()

    while menu_selected != len(menu_list):
        if menu_selected == 1:
            path_to_file = path_request()
            buffer_list = open_file(path_to_file, menu_selected)
            phone_book_menu()
            menu_selected = menu_selection()
        elif  menu_selected == 2:
            show_all_contacts()
            phone_book_menu()
            menu_selected = menu_selection()
        elif menu_selected == 3:
            create_new_contact(buffer_list)
            phone_book_menu()
            menu_selected = menu_selection()
        elif menu_selected == 4:
            search_contact(buffer_list)
            phone_book_menu()
            menu_selected = menu_selection()
        elif menu_selected == 5:
            edit_contact(buffer_list)
            phone_book_menu()
            menu_selected = menu_selection()
        elif menu_selected == 6:
            delete_contact(buffer_list)
            phone_book_menu()
            menu_selected = menu_selection()
        elif menu_selected == 7:
            initial_list = open_file(path_to_file, menu_selected)
            save_changes(buffer_list, initial_list)
            phone_book_menu()
            menu_selected = menu_selection()
