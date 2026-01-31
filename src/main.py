print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n')
dict_questions = {1: 'JSON', 2: 'CSV', 3: 'XLSX'}
print('Выберите необходимый пункт меню: ')
for key, item in dict_questions.items():
    print(f'{key}. Получить информацию о транзакциях из {item}-файла')
choise_user = int(input('\nПользователь: '))
while choise_user not in [1, 2, 3]:
    choise_user = int(input('Не верный выбор, попробуй еще раз!: '))

print(f'\nДля обработки выбран {dict_questions[choise_user]}-файл.')
list_operations = ['EXECUTED', 'CANCELED', 'PENDING']
choise_user_operation = input(
        f'Введите статус, по которому необходимо выполнить фильтрацию.\n'
        f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\nПользователь: '
    ).upper()
while choise_user_operation not in list_operations:
    print(f'\nСтатус операции {choise_user_operation} недоступен.\n')
    choise_user_operation = input(
        f'Введите статус, по которому необходимо выполнить фильтрацию.\n'
        f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\nПользователь: '
    ).upper()
print(f'\nОперации отфильтрованы по статусу {choise_user_operation}.')
date_sort_user = input('Отсортировать операции по дате? Да/Нет\nПользователь: ')
