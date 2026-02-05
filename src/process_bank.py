import re
from collections import Counter
from typing import Any


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


def process_bank_operations(data: list[dict], categories: list) -> Any:
    """Функция, которая подсчитывает количество определенных операций по ключу 'description'"""
    try:
        description_list = [trans.get('description') for trans in data if trans.get('description') in categories]
        counted = Counter(description_list)
        return counted
    except AttributeError:
        return 'Не верные данные транзакций'
    except ValueError:
        return 'Параметр должен быть списком'
    except TypeError:
        return 'Параметр должен быть списком'


data_of = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

# list_of = ''
print(process_bank_search(data_of, search = ''))