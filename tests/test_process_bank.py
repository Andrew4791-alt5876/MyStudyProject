from src.process_bank import process_bank_search


def bank_search_with_data_and_search (info_transactions: list, search_with_data_and_search: list) -> None:
    """Тест для функции, которой подается необходимая строка и база данных."""
    assert process_bank_search(info_transactions, search = 'карт') == search_with_data_and_search


def bank_search_with_search_and_empty_data (info_transactions: list, search_with_data_and_search: list) -> None:
    """Тест для функции, которой подается необходимая строка и пустая база данных."""
    assert process_bank_search([], search = 'карт') == []


def bank_search_with_data_and_empty_search (info_transactions: list, search_with_data_and_search: list) -> None:
    """Тест для функции, которой подается пустая строка и база данных."""
    assert process_bank_search(info_transactions, search = '') == info_transactions


def bank_search_with_search_and_incorrect_data (incorrect_data, search_with_data_and_search: list) -> None:
    """Тест для функции, которой подается необходимая строка и не корректная база данных."""
    assert process_bank_search(incorrect_data, search = 'карт') == 'Ошибка входных данных'


def bank_search_with_incorrect_search_and_data (info_transactions, search_with_data_and_search: list) -> None:
    """Тест для функции, которой подается необходимая строка и не корректная база данных."""
    assert process_bank_search(info_transactions, search = 'hjkhjkjk') == []
