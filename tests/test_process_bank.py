import pytest
from src.process_bank import process_bank_search


def bank_search_with_data_and_search (info_transactions: list, search_with_data_and_search: list) -> None:
    """Тест для функции, которой подается необходимая строка и база данных."""
    assert process_bank_search(info_transactions, search = 'карт') == search_with_data_and_search


def bank_search_with_search_and_empty_data (info_transactions: list, search_with_data_and_search: list) -> None:
    """Тест для функции, которой подается необходимая строка и база данных."""
    assert process_bank_search([], search = 'карт') == []


def bank_search_with_data_and_empty_search (info_transactions: list, search_with_data_and_search: list) -> None:
    """Тест для функции, которой подается необходимая строка и база данных."""
    assert process_bank_search(info_transactions, search = '') == info_transactions