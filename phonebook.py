
def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()

    return f'{surname} {name} {patronymic}  {phone}\n{address}\n\n'

def add_contact(contact):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)
def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        print(file.read().rstrip())
def search_contact():
    var_search = input('Выберите вариант поиска:\n'
                       '1. По фамилии\n'
                       '2. По имени\n'
                       '3. По отчеству\n'
                       '4. По номеру телефона\n'
                       '5. По адресу\n'
                       'Ввод: ')

    while var_search not in ('1', '2', '3', '4', '5'):
        print('Неккоректные данные')
        var_search = input('Введите вариант поиска: ')

    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)

def copy_contact(source_file, destination_file):
    try:
        line_number = int(input('Введите номер строки для копирования: '))
        with open(source_file, 'r', encoding='UTF-8') as source:
            contacts_list = source.read().rstrip().split('\n\n')
            if 1 <= line_number <= len(contacts_list):
                contact_to_copy = contacts_list[line_number - 1]
                with open(destination_file, 'a', encoding='UTF-8') as destination:
                    destination.write(contact_to_copy + '\n\n')
                print('Контакт успешно скопирован.')
            else:
                print('Некорректный номер строки.')
    except ValueError:
        print('Некорректный ввод. Введите целое число.')


def interface():
    source_file = 'phonebook.txt'
    destination_file = 'phonebook_copy.txt'

    with open(source_file, 'a', encoding='UTF-8'):
        pass

    command = '-1'
    while command != '5':
        print('Возможные варианты меню: \n'
              '1. Добавить контакт\n'
              '2. Вывести на экран\n'
              '3. Поиск контакта\n'
              '4. Копировать контакт\n'
              '5. Выход из программы')

        command = input('Введите номер команды: ')

        while command not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные')
            command = input('Введите номер команды: ')

        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                copy_contact(source_file, destination_file)
            case '5':
                print('Всего хорошего')

interface()