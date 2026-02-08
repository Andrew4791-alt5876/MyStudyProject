import re
from collections import Counter
from typing import Any


def process_bank_search(data: list[dict], search: Any) -> None | str | list[Any]:
    """Функция, возвращающая список словарей, у которых в описании есть необходимая строка."""
    try:
        result = []
        pattern = re.compile(search, re.IGNORECASE | re.UNICODE)
        for operation in data:
            description = operation.get("description")
            if pattern.search(description):
                result.append(operation)
        return result
    except AttributeError:
        return "Ошибка входных данных"
    except TypeError:
        return "Ошибка типа входных данных"


def process_bank_operations(data: Any, categories: Any) -> None | str | dict:
    """Функция, которая подсчитывает количество определенных операций по ключу 'description''"""
    try:
        categories_correct = []
        for no_correct_categories in categories:
            if isinstance(no_correct_categories, str):
                pattern = re.compile(no_correct_categories, re.IGNORECASE | re.UNICODE)
                for operation_of_transactions in data:
                    description = operation_of_transactions.get("description")
                    if pattern.search(description):
                        categories_correct.append(description)
        description_list = [
            trans.get("description") for trans in data if trans.get("description") in categories_correct
        ]
        counted = Counter(description_list)
        if counted:
            return counted
        else:
            return {}
    except AttributeError:
        return "Не верные данные транзакций"
    except ValueError:
        return "Параметр должен быть списком"
    except TypeError:
        return "Параметр должен быть списком"
