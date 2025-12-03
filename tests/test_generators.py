from src.generators import filter_by_currency

def test_filter_by_currency(info_transactions, info_transactions_usd):
    test_generators = filter_by_currency(info_transactions, "USD")
    for i in range(2):
        assert next(test_generators) == info_transactions_usd