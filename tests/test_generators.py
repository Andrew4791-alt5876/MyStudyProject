from src.generators import filter_by_currency


def test_filter_by_currency_usd(info_transactions, info_transactions_usd):
    test_generators = filter_by_currency(info_transactions, "USD")
    for i in range(5):
        assert next(test_generators) == info_transactions_usd[i]


def test_filter_by_currency_not_money(info_transactions, info_transactions_empty):
    test_generators = filter_by_currency(info_transactions, "")
    for i in range(5):
        assert next(test_generators) == info_transactions_empty


def test_filter_by_currency_empty_list(info_transactions_empty_list, info_transactions_empty):
    test_generators = filter_by_currency(info_transactions_empty_list, "USD")
    for i in range(5):
        assert list(test_generators) == info_transactions_empty
