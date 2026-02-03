import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, возвращающая список словарей, у которых в описании есть необходимая строка."""
    if not isinstance(data, list):
        raise ValueError("Параметр 'data' должен быть списком")
    if not isinstance(search, str):
        raise ValueError("Параметр 'search' должен быть строкой")
    if not search.strip():
        return data
    try:
        pattern = re.compile(search, re.IGNORECASE | re.UNICODE)
    except re.error as e:
        raise ValueError(f"Некорректное регулярное выражение в параметре 'search': {e}")
    result = []
    for operation in data:
        if not isinstance(operation, dict):
            continue
        description = operation.get('description')
        if not isinstance(description, str):
            continue
        if pattern.search(description):
            result.append(operation)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    for t in data:
        counted = Counter(t)
        print(counted)


data_of_operations = [
    {
        'id': 650703.0,
        'state': 'EXECUTED',
        'date': '2023-09-05',
        'amount': 16210.0,
        'currency_name': 'Sol',
        'currency_code': 'PEN',
        'from': 'Счет 58803664561298323391',
        'to': 'Счет 39745660563456619397',
        'description': 'Перевод организации'
    },
    {
        'id': 3598919.0,
        'state': 'EXECUTED',
        'date': '2020-12-06',
        'amount': 29740.0,
        'currency_name': 'Peso',
        'currency_code': 'COP',
        'from': 'Discover 3172601889670065',
        'to': 'Discover 0720428384694643',
        'description': 'Перевод с карты на карту'
    },
    {
        'id': 3107343.0,
        'state': 'EXECUTED',
        'date': '2023-01-25',
        'amount': 33639.0,
        'currency_name': 'Krona',
        'currency_code': 'SEK',
        'from': 'nan',
        'to': 'Счет 35662766798195077538',
        'description': 'Открытие вклада'
    },
    {
        'id': 4813301.0,
        'state': 'EXECUTED',
        'date': '2021-11-02',
        'amount': 15080.0,
        'currency_name': 'Euro',
        'currency_code': 'EUR',
        'from': 'Счет 65547878890984510340',
        'to': 'Счет 91457207307678002163',
        'description': 'Перевод со счета на счет'
    },
    {
        'id': 593027.0,
        'state': 'CANCELED',
        'date': '2023-07-22',
        'amount': 30368.0,
        'currency_name': 'Shilling',
        'currency_code': 'TZS',
        'from': 'Visa 1959232722494097',
        'to': 'Visa 6804119550473710',
        'description': 'Перевод с карты на карту'
    },
    {
        'id': 5380041.0,
        'state': 'CANCELED',
        'date': '2021-02-01',
        'amount': 23789.0,
        'currency_name': 'Peso',
        'currency_code': 'UYU',
        'from': 'nan',
        'to': 'Счет 23294994494356835683',
        'description': 'Открытие вклада'
    },
    {
        'id': 3176764.0,
        'state': 'CANCELED',
        'date': '2022-08-24',
        'amount': 16652.0,
        'currency_name': 'Euro',
        'currency_code': 'EUR',
        'from': 'Mastercard 8387037425051294',
        'to': 'American Express 5556525473658852',
        'description': 'Перевод с карты на карту'
    },
    {
        'id': 1449073.0,
        'state': 'CANCELED',
        'date': '2021-05-11',
        'amount': 11834.0,
        'currency_name': 'Rupiah',
        'currency_code': 'IDR',
        'from': 'Счет 17847122626293622323',
        'to': 'Счет 68570011224094542755',
        'description': 'Перевод со счета на счет'
    },
    {
        'id': 2130098.0,
        'state': 'PENDING',
        'date': '2020-06-07',
        'amount': 30731.0,
        'currency_name': 'Euro',
        'currency_code': 'EUR',
        'from': 'Visa 5749750597771353',
        'to': 'American Express 9106381490184499',
        'description': 'Перевод с карты на карту'
    },
    {
        'id': 1068715.0,
        'state': 'PENDING',
        'date': '2023-08-03',
        'amount': 18891.0,
        'currency_name': 'Yuan Renminbi',
        'currency_code': 'CNY',
        'from': 'nan',
        'to': 'Счет 04362233061130879079',
        'description': 'Открытие вклада'
    }
]


list_categories = [
    'Перевод с карты на карту',
    'Перевод организации',
    'Перевод со счета на счет',
    'Открытие вклада',
    'Перевод с карты на счет'
]


print(process_bank_operations(data_of_operations, list_categories))
