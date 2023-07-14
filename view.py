import text

def print_msg(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n') 


def show_menu(menu: list[str])-> int:
    for i, item in enumerate(menu):
        if i != 0:
            print(f'\t{i}. {item}')
        else:
            print(item)
    input_select = input('Выберете пункт меню: ')
    while True:
        if input_select.isdigit() and 0 < int(input_select) < len(menu):
            return int(input_select)
        input_select = input(text.menu_error)

def show_contacts(book: dict[int, [list[str]]], msg: str):
    max_count = [0,0,0]
    if book:        
        for contact in book.values():
            for i in range(len(contact)):
                if max_count[i] < len(contact[i]):
                   max_count[i] = len(contact[i]) 
        
        print('\n' + '=' * (sum(max_count) + 10))
        print(f'{"ID": >3}. {"Фамилия и имя": <{max_count[0]}} '
                  f'{"Телефон": <{max_count[1]}} '
                  f'{"Комментарий": <{max_count[2]}}')
        for i, contact in book.items() :
            print(f'{i: >3}. {contact[0]: <{max_count[0]}} '
                  f'{contact[1]: <{max_count[1]}} '
                  f'{contact[2]: <{max_count[2]}}')
        print('=' * (sum(max_count) + 10) + '\n')
    else:
        print_msg(msg)

def contact_input(input_fields: list[str]) -> list[str]:
    contact = []
    for field in input_fields:
        contact.append(input(field))
    return contact

def input_data(msg: str) -> str:
    return input(msg)

def input_number(msg:str) -> int:
    while True:
        number = input(msg)
        if number.isdigit():
            return int(number)
        print(text.number_error)