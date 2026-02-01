from typing import Any
from src.read_file import read_csv_file, read_excel_file
from src.utils import read_json_file
from src.processing import filter_by_state, sort_by_date


def load_data_operations(choose_user: Any) -> list[dict] | None | str:
    while choose_user or choose_user == '':
        if choose_user.isdigit():
            select_user = int(choose_user)
            if select_user in [1, 2, 3]:
                dict_questions = {1: 'JSON', 2: 'CSV', 3: 'XLSX'}
                print(f'\nДля обработки выбран {dict_questions[select_user]}-файл.')
                if select_user == 1:
                    return read_json_file('data/operations.json')
                elif select_user == 2:
                    return read_csv_file('data/transactions.csv')
                elif select_user == 3:
                    return read_excel_file('data/transactions_excel.xlsx')
            else:
                choose_user = input('Не верный выбор, попробуй еще раз!: ')
        else:
            choose_user = input('Не верный выбор, попробуй еще раз!: ')


def status_transactions(choose_user_type: Any) -> str:
    list_type_operations = ['EXECUTED', 'CANCELED', 'PENDING', 'E', 'C', 'P', 'EXE', 'CAN', 'PEN']
    while choose_user_type not in list_type_operations:
        print(f'\nСтатус операции {choose_user_type} недоступен.\n')
        choose_user_type = input(
            f'Введите статус, по которому необходимо выполнить фильтрацию.\n'
            f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\nПользователь: '
        ).upper()
    if choose_user_type in ['EXECUTED', 'E', 'EXE']:
        status_transactions = list_type_operations[0]
    elif choose_user_type in ['CANCELED', 'C', 'CAN']:
        status_transactions = list_type_operations[1]
    elif choose_user_type in ['PENDING', 'P', 'PEN']:
        status_transactions = list_type_operations[2]
    return status_transactions


def sort_operations_by_date(select_transactions_by_status, date_sort_user):
    while date_sort_user or date_sort_user == '':
        if date_sort_user.isalpha() and date_sort_user in ['ДА', 'Д']:
            return sort_by_date(select_transactions_by_status)
        elif date_sort_user.isalpha() and date_sort_user == ['НЕТ', 'Н']:
            return select_transactions_by_status
        else:
            date_sort_user = input(
                f'Не верный ответ, нужен ответ Да или Нет,\n'
                f'можно ввести первую букву: '
            ).upper()


def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('#'*80)
    dict_questions = {1: 'JSON', 2: 'CSV', 3: 'XLSX'}
    print('\nВыберите необходимый пункт меню: ')
    for key, item in dict_questions.items():
        print(f'{key}. Получить информацию о транзакциях из {item}-файла')
    choose_user = input('\nПользователь: ')
    data_operations_select = load_data_operations(choose_user)
    print(f'Найдено {len(data_operations_select)} транзакций.')
    print('#'*80)

    choose_user_type = input(
        f'\nВведите статус, по которому необходимо выполнить фильтрацию.\n'
        f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n'
        f'Пользователь (можно ввести первую или первые три буквы): '
    ).upper()
    user_choose_status = status_transactions(choose_user_type)
    print(f'\nОперации отфильтрованы по статусу {user_choose_status}.')
    select_transactions_by_status = filter_by_state(data_operations_select, user_choose_status)
    print(f'Найдено {len(select_transactions_by_status)} транзакций.')
    print('#' * 80)

    date_sort_user = input(f'\nОтсортировать операции по дате? Да/Нет\n'
                           f'Пользователь (можно ввести первую букву или + или -): '
                           ).upper()
    sort_transactions_by_date = sort_operations_by_date(select_transactions_by_status, date_sort_user)
    print(f'Обработано {len(sort_transactions_by_date)} транзакций.')


main()