from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(info_transactions: list, info_transactions_usd: list) -> None:
    """Тест для транзакций в USD."""
    test_generator = filter_by_currency(info_transactions, "USD")
    for i in range(5):
        assert next(test_generator) == info_transactions_usd[i]


def test_filter_by_currency_rub(info_transactions: list, info_transactions_rub: list) -> None:
    """Тест для транзакций в RUB."""
    test_generator = filter_by_currency(info_transactions, "RUB")
    for i in range(5):
        assert next(test_generator) == info_transactions_rub[i]


def test_filter_by_currency_not_money(info_transactions: list, info_transactions_empty: list) -> None:
    """Тест для пустой строки валюты."""
    test_generator = filter_by_currency(info_transactions, "")
    for i in range(5):
        assert next(test_generator) == info_transactions_empty


def test_filter_by_currency_empty_list(info_transactions_empty_list: list, info_transactions_empty: list) -> None:
    """Тест для пустого списка транзакций."""
    test_generators = filter_by_currency(info_transactions_empty_list, "USD")
    assert next(test_generators) == info_transactions_empty


def test_transaction_descriptions_with_data(info_transactions: list, descriptions_exit: str) -> None:
    """Тест для описания транзакций при наличии данных."""
    test_gen = transaction_descriptions(info_transactions)
    for i in range(5):
        assert next(test_gen) == descriptions_exit[i]


def test_descriptions_empty_list(info_transactions_empty_list: list, info_transactions_empty: list) -> None:
    """Тест для пустого списка транзакций."""
    test_generators = transaction_descriptions(info_transactions_empty_list)
    assert next(test_generators) == info_transactions_empty


def test_card_number_generator(card_number_generator_exit_15: list) -> None:
    """Тест генератора номера карты в диапазоне от 16 до 20."""
    generator_card = card_number_generator(16, 20)
    for i in range(5):
        assert next(generator_card) == card_number_generator_exit_15[i]


def test_card_number_generator_big(card_number_generator_exit_999: list) -> None:
    """Тест генератора номера карты в диапазоне от 9000800070006000 до 9000800070006020."""
    generator_card = card_number_generator(9000800070006000, 9000800070006020)
    for i in range(5):
        assert next(generator_card) == card_number_generator_exit_999[i]


def test_card_number_generator_no_data() -> None:
    """Тест генератора номера карты при отсутствии данных ввода."""
    generator_card = card_number_generator()
    assert next(generator_card) == "Не верные данные."


def test_card_number_generator_not_right_data() -> None:
    """Тест генератора номера карты при не верном вводе данных."""
    generator_card = card_number_generator(567, 7)
    assert next(generator_card) == "Не верные данные."


def test_card_number_generator_not_typeerror() -> None:
    """Тест генератора номера карты при не верном вводе данных."""
    generator_card = card_number_generator("567", 7)
    assert next(generator_card) == "Не верные данные."
