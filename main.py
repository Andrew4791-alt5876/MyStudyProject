from datetime import datetime
from typing import Any

from src.process_bank import process_bank_search
from src.read_file import read_csv_file, read_excel_file
from src.utils import read_json_file
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card_fun


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
    if choose_user_type in ['EXECUTED', 'E', 'EX', 'EXE', 'EXEC', 'EXECU', 'EXECUT', 'EXECUTE']:
        status_transactions = list_type_operations[0]
    elif choose_user_type in ['CANCELED', 'C', 'CA', 'CAN', 'CANC','CANCE', 'CANCEL', 'CANCELE']:
        status_transactions = list_type_operations[1]
    elif choose_user_type in ['PENDING', 'P', 'PE', 'PEN', 'PEND', 'PENDI', 'PENDIN']:
        status_transactions = list_type_operations[2]
    return status_transactions


def sort_operations_by_date(select_transactions_by_status, date_sort_user):
    global sort_transactions
    while date_sort_user or date_sort_user == '':
        if date_sort_user.isalpha() and date_sort_user in ['ДА', 'Д']:
            direction_of_sort = input(
                f'Отсортировать по возрастанию или по убыванию?\n'
                f'Пользователь (по возрастанию - Да /по убыванию - Нет)\n'
                f'(можно ввести первую букву): '
            ).upper()
            if direction_of_sort.isalpha() and direction_of_sort in ['ДА', 'Д', 'ПО ВОЗРАСТАНИЮ']:
                for one_transaction in select_transactions_by_status:
                    one_transaction['date'] = one_transaction['date'][:10]
                sort_transactions = sorted(
                    select_transactions_by_status,
                    reverse=False,
                    key=lambda x: datetime.strptime(
                        x["date"],"%Y-%m-%d"
                    )
                )
                return sort_transactions
            elif direction_of_sort.isalpha() and direction_of_sort in ['НЕТ', 'НЕ', 'Н', 'ПО УБЫВАНИЮ']:
                for one_transaction in select_transactions_by_status:
                    one_transaction['date'] = one_transaction['date'][:10]
                sort_transactions = sorted(
                    select_transactions_by_status,
                    reverse=True,
                    key=lambda x: datetime.strptime(
                        x["date"], "%Y-%m-%d"
                    )
                )
                return sort_transactions
        elif date_sort_user.isalpha() and date_sort_user in ['НЕТ', 'НЕ', 'Н']:
            for one_transaction in select_transactions_by_status:
                one_transaction['date'] = one_transaction['date'][:10]
            return select_transactions_by_status
        else:
            date_sort_user = input(
                f'Не верный ответ, нужен ответ Да или Нет,\n'
                f'можно ввести первую букву: '
            ).upper()


def sort_transactions_by_rub(sort_transactions_by_date, user_currency_code):
    while user_currency_code or user_currency_code == '':
        if user_currency_code.isalpha() and user_currency_code in ['ДА', 'Д']:
            list_only_rub = [
                transactions_all_currency for transactions_all_currency
                in sort_transactions_by_date
                if (transactions_all_currency.get('currency_code')
                    and transactions_all_currency['currency_code']== 'RUB')
                   or (transactions_all_currency.get('operationAmount')
                       and transactions_all_currency['operationAmount']['currency']['code'] == 'RUB')]
            return list_only_rub
        elif user_currency_code.isalpha() and user_currency_code in ['НЕТ', 'НЕ', 'Н']:
            return sort_transactions_by_date
        else:
            user_currency_code = input(
                f'Не верный ответ, нужен ответ Да или Нет,\n'
                f'можно ввести первую букву: '
            ).upper()


def sort_by_word_of_description(sort_by_rub, choose_user_word):
    global sort_by_word
    while choose_user_word or choose_user_word == '':
        if choose_user_word.isalpha() and choose_user_word in ['ДА', 'Д']:
            input_word_or_string = input('Введите слово или строку для сортировки: ')
            return process_bank_search(sort_by_rub, input_word_or_string)
        elif choose_user_word.isalpha() and choose_user_word in ['НЕТ', 'НЕ', 'Н']:
            return sort_by_rub
        else:
            choose_user_word = input(
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
    choose_user_file = input('\nПользователь: ')
    data_operations_select = load_data_operations(choose_user_file)
    print('#'*80)

    choose_user_status = input(
        f'\nВведите статус, по которому необходимо выполнить фильтрацию.\n'
        f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n'
        f'Пользователь (можно ввести первую или первые три буквы): '
    ).upper()
    user_choose_status = status_transactions(choose_user_status)
    print(f'\nОперации отфильтрованы по статусу {user_choose_status}.')
    select_transactions_by_status = filter_by_state(data_operations_select, user_choose_status)
    print('#' * 80)

    choose_user_sort_date = input(f'\nОтсортировать операции по дате? Да/Нет\n'
                           f'Пользователь (можно ввести первую букву): '
                           ).upper()
    sort_transactions_by_date = sort_operations_by_date(select_transactions_by_status, choose_user_sort_date)
    print('#' * 80)

    choose_user_sort_rub = input(f'\nВыводить только рублевые транзакции? Да/Нет\n'
                                      f'Пользователь (можно ввести первую букву): ').upper()
    sort_by_rub = sort_transactions_by_rub(sort_transactions_by_date, choose_user_sort_rub)
    print('#' * 80)

    choose_user_word = input(f'\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n'
                             f'Пользователь (можно ввести первую букву): ').upper()
    data_after_choosing = sort_by_word_of_description(sort_by_rub, choose_user_word)
    for k in data_after_choosing:
        print(k['description'])
    print('#' * 80)

    if len(data_after_choosing) == 0:
        print('\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.')
    else:
        print('\nРаспечатываю итоговый список первых десяти транзакций...')
        print(f'Всего банковских операций в выборке: {len(data_after_choosing)}')
        for k in data_after_choosing[:10]:
            if isinstance(k.get('from'), str) and isinstance(k.get('operationAmount'), dict):
                print(
                    f'\n{k['date']} {k['description']}\n'
                    f'{mask_account_card_fun(k['from'])} -> {mask_account_card_fun(k['to'])}\n'
                    f'Сумма: {k['operationAmount']['amount']}'
                )
            elif isinstance(k.get('operationAmount'), dict):
                print(
                    f'\n{k['date']} {k['description']}\n'
                    f'{mask_account_card_fun(k['to'])}\n'
                    f'Сумма: {k['operationAmount']['amount']}'
                )
            elif isinstance(k.get('from'), str):
                print(
                    f'\n{k['date']} {k['description']}\n'
                    f'{mask_account_card_fun(k['from'])} -> {mask_account_card_fun(k['to'])}\n'
                    f'Сумма: {k['amount']}'
                )
            else:
                print(
                    f'\n{k['date']} {k['description']}\n'
                    f'{mask_account_card_fun(k['to'])}\n'
                    f'Сумма: {k['amount']}'
                )
    print('#' * 80)


main()
