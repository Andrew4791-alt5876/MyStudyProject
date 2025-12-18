from typing import Any, Generator


def filter_by_currency(transactions: list, code_money: str) -> Generator[list[Any] | Any, Any, None]:
    """Функция, которая поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
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
    """Функция, которая принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    if not transactions:
        return
    for transaction in transactions:
        try:
            yield transaction["description"]
        except (StopIteration, AttributeError, KeyError):
            continue


def card_number_generator(start_number: Any ="", finish_number: Any ="") -> Generator[str | type[Exception], Any, None]:
    """Генератор, который выдает номера банковских карт в заданном диапазоне."""
    if (
        isinstance(start_number, int)
        and isinstance(finish_number, int)
        and start_number >= 0
        and finish_number >= 0
        and start_number <= finish_number
    ):
        for number in range(start_number, finish_number + 1):
            zero_str = "".join(["0" for z in range(16 - len(str(number))) if len(str(number)) <= 16])
            card_number_str = zero_str + str(number)
            card_number_exit = (
                f"{card_number_str[:4]} {card_number_str[4:8]} " f"{card_number_str[8:12]} {card_number_str[12:]}"
            )
            yield card_number_exit
    else:
        yield "Не верные данные."
