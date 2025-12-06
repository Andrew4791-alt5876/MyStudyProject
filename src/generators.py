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


def card_number_generator(start_number: int, finish_number: int) -> Generator[str, Any, None]:
    for number in range(start_number, finish_number + 1):
        if len(str(number)) <= 16:
            zero_str = ""
            for z in range(17 - len(str(number))):
                zero_str += "0"
            card_number_str = zero_str + str(number)
            card_number_exit = f"{card_number_str[:4]} {card_number_str[4:9]} {card_number_str[9:13]} {card_number_str[13:]}"
        yield card_number_exit
