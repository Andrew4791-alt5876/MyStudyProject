from typing import Any

from src.process_bank import process_bank_operations, process_bank_search


def test_bank_search_with_data_and_search(info_transactions: list, search_with_data_and_search: list) -> None:
    """Тест для функции process_bank_search, которой подается необходимая строка и база данных."""
    assert process_bank_search(info_transactions, search="карт") == search_with_data_and_search


def test_bank_search_with_search_and_empty_data(info_transactions: list, search_with_data_and_search: list) -> None:
    """Тест для функции process_bank_search, которой подается необходимая строка и пустая база данных."""
    assert process_bank_search([], search="карт") == []


def test_bank_search_with_data_and_empty_search(info_transactions: list, search_with_data_and_search: list) -> None:
    """Тест для функции process_bank_search, которой подается пустая строка и база данных."""
    assert process_bank_search(info_transactions, search="") == info_transactions


def test_bank_search_with_search_and_incorrect_data(incorrect_data: Any, search_with_data_and_search: list) -> None:
    """Тест для функции process_bank_search, которой подается необходимая строка и не корректная база данных."""
    assert process_bank_search(incorrect_data, search="карт") == "Ошибка входных данных"


def test_bank_search_with_data_and_incorrect_search(
    info_transactions: list, search_with_data_and_search: list
) -> None:
    """Тест для функции process_bank_search, которой подается база данных и не корректная строка."""
    assert process_bank_search(info_transactions, search="hjkhjkjk") == []


def test_bank_search_with_data_and_incorrect_type_search_1(
    info_transactions: list, search_with_data_and_search: Any
) -> None:
    """Тест для функции process_bank_search, которой подается база данных и не корректный тип строки."""
    assert process_bank_search(info_transactions, search=1) == "Ошибка типа входных данных"


def test_bank_search_with_data_and_incorrect_type_search_2(
    info_transactions: list, search_with_data_and_search: Any
) -> None:
    """Тест для функции process_bank_search, которой подается база данных и не корректный тип строки."""
    assert process_bank_search(info_transactions, search=[1, 2, 3]) == "Ошибка типа входных данных"


def test_process_bank_operations_with_data_and_categories(
    info_transactions: list, results_with_data_and_categories: list
) -> None:
    """Тест для функции process_bank_operations, которой подается база данных и категории."""
    assert process_bank_operations(info_transactions, categories=["орг", "кар"]) == results_with_data_and_categories


def test_process_bank_operations_with_empty_data_and_categories(
    info_transactions: list, results_with_data_and_categories: list
) -> None:
    """Тест для функции process_bank_operations, которой подается категории и пустая база данных."""
    assert process_bank_operations([], categories=["орг", "кар"]) == {}


def test_process_bank_operations_with_data_and_empty_categories(
    info_transactions: list, results_with_data_and_categories: list
) -> None:
    """Тест для функции process_bank_operations, которой подается база данных и пустые категории"""
    assert process_bank_operations(info_transactions, categories=[]) == {}


def test_process_bank_operations_with_categories_and_incorrect_data(
    incorrect_data: list, results_with_data_and_categories: list
) -> None:
    """Тест для функции process_bank_operations, которой подается категории и некорректная база данных"""
    assert process_bank_operations(incorrect_data, categories=["орг", "кар"]) == "Не верные данные транзакций"


def test_process_bank_operations_with_data_and_incorrect_categories(
    info_transactions: list, results_with_data_and_categories: list
) -> None:
    """Тест для функции process_bank_operations, которой подается база данных и некорректные категории"""
    assert process_bank_operations(info_transactions, categories=["dfs", "kl;lk"]) == {}


def test_process_bank_operations_with_data_and_incorrect_type_categories_1(
    info_transactions: list, results_with_data_and_categories: list
) -> None:
    """Тест для функции process_bank_operations, которой подается база данных и категории."""
    assert process_bank_operations(info_transactions, categories=1) == "Параметр должен быть списком"


def test_process_bank_operations_with_data_and_incorrect_type_categories_2(
    info_transactions: list, results_with_data_and_categories: list
) -> None:
    """Тест для функции process_bank_operations, которой подается база данных и категории."""
    assert process_bank_operations(info_transactions, categories=[{1: "tyt"}, {2: "ygg"}]) == {}
