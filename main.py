from typing import Any
from src.read_file import read_csv_file, read_excel_file
from src.utils import read_json_file


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


def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('#'*80)
    dict_questions = {1: 'JSON', 2: 'CSV', 3: 'XLSX'}
    print('\nВыберите необходимый пункт меню: ')
    for key, item in dict_questions.items():
        print(f'{key}. Получить информацию о транзакциях из {item}-файла')
    choose_user = input('\nПользователь: ')
    data_operations_select = load_data_operations(choose_user)
    print(f'Получено {len(data_operations_select)} транзакций.')
    print('#'*80)
    # print(data_operations_select)

    list_type_operations = ['EXECUTED', 'CANCELED', 'PENDING']
    choose_user_type = input(
        f'\nВведите статус, по которому необходимо выполнить фильтрацию.\n'
        f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\nПользователь: '
    ).upper()
    while choose_user_type not in list_type_operations:
        print(f'\nСтатус операции {choose_user_type} недоступен.\n')
        choose_user_type = input(
            f'Введите статус, по которому необходимо выполнить фильтрацию.\n'
            f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\nПользователь: '
        ).upper()
    print(f'\nОперации отфильтрованы по статусу {choose_user_type}.')
    # # date_sort_user = input('Отсортировать операции по дате? Да/Нет\nПользователь: ')



main()