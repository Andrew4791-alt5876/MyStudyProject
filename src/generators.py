from typing import Any, Generator


def filter_by_currency(transactions: list, code_money: str) -> Generator[list[Any] | Any, Any, None]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code_money and transaction.get("id", 0) != 0:
            yield transaction
        elif transaction.get("id", 0) == 0:
            yield []
        else:
            yield []


def transaction_descriptions(transactions: list) -> Generator[Any, Any, None]:
    for transaction in transactions:
        yield transaction["description"]
