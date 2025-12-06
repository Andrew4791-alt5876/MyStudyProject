from typing import Any, Generator


def filter_by_currency(transactions: list, code_money: str) -> Generator[list[Any] | Any, Any, None]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    if not transactions:
        return
    for transaction in transactions:
        try:
            if (transaction.get("operationAmount", {}).get("currency", {}).get("code")) == code_money:
                yield transaction
            else:
                yield []
        except (StopIteration, AttributeError, KeyError):
            continue


def transaction_descriptions(transactions: list) -> Generator[Any, Any, None]:
    if not transactions:
        return
    for transaction in transactions:
        try:
            yield transaction["description"]
        except (StopIteration, AttributeError, KeyError):
            continue
